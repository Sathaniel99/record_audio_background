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

## 🛠 Instalación

1. Clona este repositorio o descarga el script.
2. Instala las dependencias mencionadas arriba.
3. Ejecuta el script según las instrucciones de uso.


## 🚀 Uso
### 📝 Argumentos del script:
| Argumento | Descripción                                                                    | Ejemplo |
|:----------|:-------------------------------------------------------------------------------|:--------|
|`--t`      |Duración de la grabación en segundos (opcional, por defecto es indefinida).     |`--t 15` |
|`--d`      |Índice del dispositivo de entrada (opcional, por defecto usa el predeterminado).|`--d 2`  |
|`--l`      |dLista los dispositivos de audio disponibles.                                   |`--ld`   |

## 🎤 Ejemplos de uso

1. Grabación indefinida (por defecto):
```bash
python audio_recorder.py
```
- La grabación se detiene al presionar Ctrl+C.
- Muestra el tiempo transcurrido y el tiempo máximo estimado basado en el espacio libre en el disco.

2. Grabación por 15 segundos:
```bash
python audio_recorder.py --t 15
```
- Graba por 15 segundos y muestra el tiempo transcurrido.

3. Listar dispositivos de audio disponibles:
```bash
python audio_recorder.py --ld
```
- Muestra una lista de los dispositivos de audio disponibles y sus índices.

4. Grabación indefinida con dispositivo específico:
```bash
python audio_recorder.py --d 2
```
- Usa el dispositivo de entrada con índice 2 para grabar.

## 📂 Estructura del proyecto
```bash
audio_recorder/
│── audio_recorder.py  # Script principal
│── records/           # Carpeta donde se guardan las grabaciones
```

## ⚙ Configuración
- Tasa de muestreo (RATE): 48000 Hz (puedes modificarla en el código si es necesario).
- Canales (CHANNELS): 1 (mono).
- Formato (FORMAT): pyaudio.paInt32 (32 bits por muestra).
- Tamaño del buffer (CHUNK): 2048 (puedes ajustarlo si experimentas problemas de latencia).

## 🔧 Solución de problemas

- Error: "No Default Input Device": Asegúrate de que tienes un micrófono conectado y seleccionado correctamente. Usa --ld para listar los dispositivos disponibles.
- Audio distorsionado: Prueba ajustando la tasa de muestreo (RATE) o el tamaño del buffer (CHUNK).
- Problemas de permisos: Asegúrate de que el script tenga permisos para acceder al micrófono y escribir en la carpeta records.