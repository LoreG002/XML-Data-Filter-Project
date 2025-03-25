import csv
import os
import xml.etree.ElementTree as ET

# 📌 Cartella dei file XML
directory = "/Users/lorenzogiannetti/Desktop/file"
csv_file_path = "/Users/lorenzogiannetti/Desktop/output.csv"

# 📌 Parole chiave
parole_chiave = ["stampa 3d", "3d printing", "additive manufacturing", "fabbricazione additiva"]

# 📌 Namespace dal tuo file XML (da correggere se cambia)
namespace = "{http://www.rna.it/RNA_aiuto/schema}"

# 📌 Lista per salvare i risultati
righe_filtrate = []

# 🔄 Itera su tutti i file XML
xml_files = [f for f in os.listdir(directory) if f.endswith('.xml')]

for xml_file in xml_files:
    file_path = os.path.join(directory, xml_file)
    try:
        for event, elem in ET.iterparse(file_path, events=("end",)):
            if elem.tag.endswith("AIUTO"):  # 🏷 Nodo principale

                # 📌 Estrai testo gestendo i namespace
                titolo = elem.find(f"{namespace}TITOLO_PROGETTO")
                descrizione = elem.find(f"{namespace}DESCRIZIONE_PROGETTO")

                titolo_text = titolo.text.strip() if titolo is not None and titolo.text else ""
                descrizione_text = descrizione.text.strip() if descrizione is not None and descrizione.text else ""

                # 📌 Controllo parole chiave
                if any(parola.lower() in titolo_text.lower() for parola in parole_chiave) or \
                   any(parola.lower() in descrizione_text.lower() for parola in parole_chiave):
                    righe_filtrate.append([xml_file, titolo_text, descrizione_text])

                elem.clear()  # 📌 Libera memoria
            
    except Exception as e:
        print(f"❌ Errore nel file {xml_file}: {e}")

# 📌 Scrivi nel CSV
if righe_filtrate:
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["File", "Titolo Misura", "Descrizione"])
        writer.writerows(righe_filtrate)

    print(f"✅ Dati salvati in: {csv_file_path}")
else:
    print("⚠ Nessun dato corrispondente trovato.")
