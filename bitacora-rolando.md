
## Bitácora de Vibe Coding (Integrante 3 - Rolando Cobis)

### Prompt inicial
Necesito un script en Python que lea un archivo de texto desde la línea 
de comandos y lo envíe a la API local de Ollama para obtener un resumen 
de 3 líneas en español. El script debe usar solo librerías estándar de 
Python y apuntar a http://localhost:11434 con el modelo qwen2.5:0.5b.

### Errores y correcciones
El script generado funcionó correctamente en el primer intento sin necesidad 
de correcciones. Se probó con un archivo de texto sobre la licencia GPL y 
devolvió el resumen esperado.

### Reflexión Soberana
Procesar información localmente con Ollama garantiza que los datos nunca 
abandonan nuestra computadora, lo que representa una ventaja significativa 
en términos de privacidad y soberanía tecnológica frente a servicios como 
ChatGPT o Gemini. Sin embargo, la principal desventaja es la limitación de 
hardware: los modelos locales disponibles para CPU con poca RAM, como 
qwen2.5:0.5b, son considerablemente menos capaces que los modelos en la nube, 
lo que se reflejó en la calidad del resumen generado.

