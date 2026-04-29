from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# =========================
# CONFIG
# =========================
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ No se encontró la API KEY en .env")

client = OpenAI(api_key=api_key)

print("✅ IA conectada correctamente")


# =========================
# LIMPIAR JSON
# =========================
def limpiar_json(texto):
    try:
        texto = texto.strip()

        if "```" in texto:
            partes = texto.split("```")
            texto = partes[1] if len(partes) > 1 else texto
            texto = texto.replace("json", "").strip()

        texto = texto.replace("True", "true").replace("False", "false")
        texto = texto.replace("'", '"')

        return json.loads(texto)

    except Exception as e:
        print("❌ Error limpiando JSON")
        print(texto)
        return None


# =========================
# ANALIZAR PRODUCTO
# =========================
def analizar_producto(producto, existentes):

    prompt = f"""
Eres experto en productos virales de ecommerce.

Producto:
{producto["producto"]}

Datos:
Views: {producto["views"]}
Likes: {producto["likes"]}

Productos existentes:
{existentes}

Devuelve SOLO JSON válido:

{{
  "producto": "{producto["producto"]}",
  "categoria": "hogar | belleza | fitness | mascotas | gadgets | automotriz",
  "problema": "dolor real",
  "solucion": "cómo lo resuelve",
  "saturado": false,
  "potencial_marca": true
}}
"""

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

        texto = response.output[0].content[0].text

        data = limpiar_json(texto)

        if not data:
            print("❌ JSON inválido")
            return None

        return data

    except Exception as e:
        print("❌ Error IA:", e)
        return None