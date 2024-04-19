import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

import google.generativeai as genai

def to_markdown(text):
  """Converts plain text to markdown with indented bullet points."""
  text = text.replace('•', '  *')  # Replace bullet point symbol
  return textwrap.indent(text, '> ', predicate=lambda _: True)  # Indent text

genai.configure(api_key="AIzaSyAFYim_VcIHfHCbu6WopL5BeaafGHT7Df4")  # Replace with your actual API key

for model in genai.list_models():
  if 'generateContent' in model.supported_generation_methods:
    print(model.name)

model = genai.GenerativeModel('gemini-pro')

# Generate content
response = model.generate_content("What is the meaning of life?")

# Convert and print the response in markdown format
print(to_markdown(response.text))
