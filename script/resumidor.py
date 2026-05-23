import urllib.request
import json
import sys

def leer_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return f.read()

def resumir_con_ollama(texto):
    url = "http://localhost:11434/api/generate"
    prompt = f"Resume el siguiente texto en exactamente 3 líneas en español:\n\n{texto[:3000]}"
    
    datos = {
        "model": "qwen2.5:0.5b",
        "prompt": prompt,
        "stream": False
    }
    
    body = json.dumps(datos).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers={'Content-Type': 'application/json'})
    
    with urllib.request.urlopen(req) as respuesta:
        resultado = json.loads(respuesta.read().decode('utf-8'))
        return resultado['response']

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 resumidor.py <archivo.txt>")
        sys.exit(1)
    
    ruta = sys.argv[1]
    texto = leer_archivo(ruta)
    resumen = resumir_con_ollama(texto)
    print("\n=== RESUMEN ===")
    print(resumen)
