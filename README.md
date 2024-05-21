# speech-to-text

Este proyecto proporciona una solución para transcribir audio a texto utilizando modelos de reconocimiento de voz avanzados de la biblioteca `transformers`. La solución permite transcribir archivos de audio descargados desde YouTube. 

## Características

- Transcripción de archivos de audio desde URLs.
- Utilización de modelos de reconocimiento de voz de última generación.
- Compatibilidad con múltiples dispositivos (CPU, GPU).
- Soporte para diferentes idiomas (actualmente español e inglés).

## Instalación

Para ejecutar este proyecto, necesitas tener `Python` instalado junto con las siguientes dependencias:

```bash
pip install -r requirements.txt
```

Además, necesitas tener ffmpeg instalado en tu sistema. Consulta las instrucciones de instalación de ffmpeg para tu sistema operativo específico:

### Windows:

Descargar: (https://ffmpeg.org/download.html)

### macOS:

Usando Homebrew:

```bash
brew install ffmpeg
```

### Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

## Uso

El script puede transcribir audio desde una URL especificada. Solo necesitas proporcionar la URL del archivo de audio que deseas transcribir.

Para el ejemplo el vídeo de YouTube seleccionado ha sido: (https://www.youtube.com/watch?v=81VnO4puNkg)

Lo primero es necesario modificar en transcriptor.py la url del vídeo que deseas utilizar:

```python
YT_VIDEO = 'https://www.youtube.com/watch?v=81VnO4puNkg"'
```

También se puede configurar para usar GPU o CPU y el idioma:

```python
USE_GPU = True # or False
```

```python
LANGUAGES = [
    "spanish",
    "english"
]
SELECTED_LANG = 0
```

Para ejecutar el código y comenzar con la transcripción, es necesario ejecutar el siguiente comando:

```python
python transcriptor.py
```

## Ejemplo

Se ha probado con el vídeo que se indica más arriba pero se ha editado para obtener solo los dos primeros minutos de vídeos, y a continuación, se muestra el resultado:

Transcripción IA: "Otra cosita que está muy chula, que me parece bastante interesante, este salseo que han soltado por aquí sobre el mundo del desarrollo. Lo ha dicho Carla y vamos primero con la raíz. Decían aquí en Reddit, hoy he visto cuánto dinero gana mi jefe, cuánto dinero le cobra al cliente. Estaba trabajando en una compañía de servicios y soy el único desarrollador en uno de los proyectos en los que estoy trabajando. Y me pagan bien, o sea, no me puedo quejar. Pero mi jefe no hace absolutamente nada más allá que hablar con el cliente y entender los requerimientos. Pero ayer pude ver cuánto es lo que le cobra el cliente y me explotó la cabeza. Son más de cinco veces lo que me pagan a mí, así que le escribí al cliente directamente para ver si me quería a mí contratar, pero lo que hizo en realidad fue enviarle ese correo a mi jefe y entonces mi jefe me ha preguntado que por qué he hecho eso. ¿Es que los clientes no saben cuánto cuesta contratar a sus propios desarrolladores? ¿Qué pasa si soy freelance, tengo trabajo de freelance y puedo conseguir clientes como este? Esta ha sido la historia, ¿no? Entonces, claro, lo interesante de esto es que hay gente que está a favor, gente en contra, lo típico, ¿no? Eso no se hace, se llama plusvalía, eso es horriblemente rata, qué estupidez como llegó, debió ser más inteligente. Si tiene nada, un NDA le mete una demanda que le quitan la casa. Nunca hay que mandar un correo así a un cliente. Lo difícil es conseguir clientes. Mal el jefe, peor el programador. ¿Qué botón el cliente? Malditos intermediarios. Claro, intermediarios. Tan fácil es el trabajo del jefe que le salió mal. Solo por hablar con el cliente y entender los requerimientos. Ya, ahí eso la verdad es que eso te he dicho. Solo. Solo por hablar con el cliente y entender los requerimientos. Solo. Obviamente, claro, cobrar cinco veces lo que cobra el desarrollador. Es mucho, es poco. A ver, os voy a explicar yo una historia. Os voy a explicar yo una historia. Yo cuando empecé en el mundo de la programación, en el primer salario, que además lo podéis ver, el salario que cobré, que lo estuvimos comentando el otro día. Pues, ¿qué pasó? En mi primer trabajo yo cobraba limpios, si no me equivoco, unos 1.200 euros. Netos, ¿vale? Limpios. Mira, en este, en Ascencia. 2010. Limpios..."

