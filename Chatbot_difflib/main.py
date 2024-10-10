import pandas as pd

# Cargar el dataset
dataset = pd.read_csv('Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv')

# Mostrar las primeras filas del dataset para entender su estructura
print(dataset.head())

# extraer las columnas de interés
faq_data = dataset[['instruction', 'response']]

print(faq_data.head())

from difflib import SequenceMatcher

# Función para buscar la mejor respuesta basándose en la similitud del texto
def buscar_respuesta(pregunta_usuario):
  mejor_puntaje = 0
  mejor_respuesta = "Sorry, i don't have information about that."
  for index, row in faq_data.iterrows():
    puntaje = SequenceMatcher(None, pregunta_usuario.lower(), row['instruction'].lower()).ratio()
    if puntaje > mejor_puntaje:
      mejor_puntaje = puntaje
      mejor_respuesta = row['response']
  return mejor_respuesta

  #Ejemplo de interacción con el chatbot
pregunta_usuario = "quiero cancelar una orden"
print(buscar_respuesta(pregunta_usuario))

import gradio as gr

#Crear una interfaz del chatbot con Gradio
def chatbot_respuesta(input_text):
  return buscar_respuesta(input_text)

# Interfaz Gradio
interfaz = gr.Interface(fn=chatbot_respuesta,
                        inputs="text",
                        outputs="text",
                        title = "Chatbot de Soporte de Productos",
                        description="Ingresa una pregunta sobre los productos y el chatbot te responderá.")
#Ejecutar la interfaz
interfaz.launch()
