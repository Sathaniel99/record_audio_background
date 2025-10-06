import pyaudio
import wave
import os
import time
import shutil
from datetime import timedelta
import argparse

def filename_():
    if not os.path.exists("records"):
        os.makedirs("records")
    archivos = [archivo for archivo in os.listdir("records") if archivo.endswith(".wav")]
    return len(archivos) + 1

def list_audio_devices():
    p = pyaudio.PyAudio()
    print("Dispositivos de audio disponibles:")
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        print(f"{i}: {dev['name']} (Entrada: {dev['maxInputChannels'] > 0})")
    p.terminate()

def get_free_space():
    # Obtener espacio libre en el disco (en bytes)
    total, used, free = shutil.disk_usage(".")
    return free

def estimate_max_duration(free_space_bytes, rate=48000, channels=1, sample_width=2):
    # Tasa de bits: rate * channels * sample_width (bytes por segundo)
    bit_rate = rate * channels * sample_width
    # Tiempo máximo en segundos
    max_seconds = free_space_bytes / bit_rate
    return int(max_seconds)

def format_time(seconds):
    return str(timedelta(seconds=seconds))

def record_audio_pyaudio(duration=None, device_index=None):
    CHUNK = 2048
    FORMAT = pyaudio.paInt32
    CHANNELS = 1  # Mono
    RATE = 48000
    filename = os.path.join("records", f"sample_{filename_()}.wav")
    p = pyaudio.PyAudio()
    if device_index is None:
        device_index = p.get_default_input_device_info()['index']
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        input_device_index=device_index,
        frames_per_buffer=CHUNK
    )

    # Calcular tiempo máximo estimado si la grabación es indefinida
    free_space = get_free_space()
    max_duration = estimate_max_duration(free_space, RATE, CHANNELS, p.get_sample_size(FORMAT))
    max_time_str = format_time(max_duration)

    print("Grabando audio... (Presiona Ctrl+C para detener)")
    frames = []
    start_time = time.time()
    try:
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)
            elapsed_time = int(time.time() - start_time)
            time_str = format_time(elapsed_time)
            if duration is not None:
                if elapsed_time >= duration:
                    break
                print(f"\r{time_str}/{format_time(duration)}", end="", flush=True)
            else:
                print(f"\r{time_str}/{max_time_str}", end="", flush=True)
    except KeyboardInterrupt:
        print("\nGrabación detenida por el usuario.")
    except Exception as e:
        print(f"\nError durante la grabación: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        if frames:
            wf = wave.open(filename, "wb")
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            print(f"\nAudio guardado como {filename}")
            return filename
        else:
            print("\nNo se guardó ningún archivo, no hay datos de audio.")
            return None

def main():
    parser = argparse.ArgumentParser(description="Grabador de audio con PyAudio.")
    parser.add_argument("--t", type=int, default=None, help="Duración de la grabación en segundos (opcional, por defecto es indefinida)")
    parser.add_argument("--d", type=int, default=None, help="Índice del dispositivo de entrada")
    parser.add_argument("--ld", action="store_true", help="Listar dispositivos de audio disponibles")
    args = parser.parse_args()
    
    if args.ld:
        list_audio_devices()
        return
    
    record_audio_pyaudio(duration=args.t, device_index=args.d)

if __name__ == "__main__":
    main()
