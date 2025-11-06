# Plugin para resaltar términos clave
def highlight_terms(text):
    keywords = ["ventas", "retail", "clientes"]  # Ejemplo
    for word in keywords:
        text = text.replace(word, f"**{word}**")
    return text

# Integrar en app.py si activado