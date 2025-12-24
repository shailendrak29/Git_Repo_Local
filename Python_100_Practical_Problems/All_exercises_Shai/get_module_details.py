import os
import pydoc
import re

def clean_pydoc(text):
    # Remove overstrike formatting (char + backspace + char)
    text = re.sub(r'.\x08', '', text)
    return text


folder = "os_details"
file_name = "os_modules_1.txt"
file_path = os.path.join(folder, file_name)

if not os.path.exists(folder):
    os.makedirs(folder)

with open(file_path, "w", encoding="utf-8") as f:
    for attr_name in dir(os):
        try:
            attr = getattr(os, attr_name)
            doc = pydoc.render_doc(attr, "Help on %s")
            doc = clean_pydoc(doc)
            f.write(doc)
            f.write("\n" + "="*80 + "\n")
        except Exception as e:
            f.write(f"Could not document {attr_name}: {e}\n")
