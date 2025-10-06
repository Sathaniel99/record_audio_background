# Grabador de Audio con PyAudio

Un script en Python para grabar audio desde el micrófono usando PyAudio, con soporte para grabación indefinida o por tiempo definido, selección de dispositivo de entrada, y visualización del tiempo transcurrido en la consola.

---

## 📋 Características

- Graba audio en formato WAV (mono, 48 kHz, 16-32 bits).
- Grabación indefinida (hasta que el usuario detenga con `Ctrl+C`).
- Opción para grabar por un tiempo específico.
- Muestra el tiempo transcurrido y el tiempo total o estimado en la consola.
- Permite seleccionar el dispositivo de entrada de audio.
- Lista los dispositivos de audio disponibles.
- Guarda los archivos de audio en la carpeta `records`.

---

## 📦 Requisitos

- Python 3.6 o superior.
- Librerías requeridas:
  - `pyaudio`
  - `numpy` (opcional, solo si se usa visualización en tiempo real)

Puedes instalar las dependencias con:

```bash
pip install -r requirements.txt
```

Argumentos:
--t       Duración de la grabación en segundos (opcional, por defecto es indefinida)(--t [tiempo en segundos])
```bash
python record.py --t 
```
--d       Índice del dispositivo de entrada
```bash
python record.py --d
```
--ld        Listar dispositivos de audio disponibles
```bash
python record.py --ld
```