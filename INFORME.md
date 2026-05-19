# Informe - Laboratorio IA Soberana y Vibe Coding

## Arquitectura e Infraestructura (SysAdmin - Maxi Maidana)

### Modelo elegido
Se utilizó **qwen2.5:0.5b** (500MB aprox). Se eligió este modelo por su tamaño
reducido, optimizado para correr en CPU con poca RAM, ideal para hardware limitado.

### Descubrimiento
Ollama ya se encontraba instalado previamente en el sistema. Se utilizó directamente
la instalación nativa sin necesidad de contenedor.

### Comandos utilizados

#### Intento con Podman:
```bash
podman run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama docker.io/ollama/ollama
```

#### Descarga del modelo:
```bash
ollama run qwen2.5:0.5b
```

#### Verificación de la API:
```bash
curl http://localhost:11434/api/generate \
  -d '{
    "model": "qwen2.5:0.5b",
    "prompt": "Respondé en una sola línea: ¿qué es Ollama?",
    "stream": false
  }'
```

### Evidencia
Ver carpeta `evidencias/evidencia-curl-ollama-api.png`
