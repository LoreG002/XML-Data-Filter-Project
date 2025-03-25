import os
import xml.etree.ElementTree as ET
import csv

# 📂 Percorso alla cartella con i file XML
directory = "/Users/lorenzogiannetti/Desktop/file"

# 📌 File CSV di output
csv_file_path = "/Users/lorenzogiannetti/Desktop/output.csv"

# 📂 Elenco di tutti i file .xml nella cartella
xml_files = [f for f in os.listdir(directory) if f.endswith('.xml')]
print("Il numero dei file trovati è:", len(xml_files))

# 🔍 Parole chiave da cercare
parole_chiave = ["stampa 3d", "3d printing", "additive manufacturing", "fabbricazione additiva"]
righe_filtrate = []

# 🔄 Analizza ogni file XML nella cartella
for xml_file in xml_files:
    file_path = os.path.join(directory, xml_file)
    try:
        # 🏗️ Parsing XML
        tree = ET.parse(file_path)
        root = tree.getroot()

        # 📌 Controllo dello spazio dei nomi (se presente)
        ns = ""
        if "}" in root.tag:
            ns = root.tag.split("}")[0] + "}"  # Estrai il namespace

        # 🔄 Scansiona ogni elemento <AIUTO>
        for aiuto in root.findall(f".//{ns}AIUTO"):  
            titolo = aiuto.find(f"{ns}TITOLO_PROGETTO").text if aiuto.find(f"{ns}TITOLO_PROGETTO") is not None else ""
            descrizione = aiuto.find(f"{ns}DESCRIZIONE_PROGETTO").text if aiuto.find(f"{ns}TITOLO_PROGETTO") is not None else ""

            # 🔍 Controlla se una delle parole chiave è presente
            if any(parola.lower() in titolo.lower() for parola in parole_chiave) or \
               any(parola.lower() in descrizione.lower() for parola in parole_chiave):
                righe_filtrate.append(aiuto)

    except ET.ParseError:
        print(f"❌ Errore nel parsing di {xml_file} (file corrotto o caratteri non validi).")
    except Exception as e:
        print(f"❌ Errore nel file {xml_file}: {e}")

# 📌 Stampa i risultati
print("\n🔹 RISULTATI FILTRATI 🔹")
#for riga in righe_filtrate:
#    print(ET.tostring(riga, encoding="utf-8").decode("utf-8"))
#    print("\n")

if righe_filtrate:
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["File", "Titolo Progetto", "Descrizione Progetto"])  # 📌 Intestazione colonne
        writer.writerows(righe_filtrate)  # 📌 Scrive le righe trovate

    print(f"✅ Dati salvati in: {csv_file_path}")
else:
    print("⚠ Nessun dato corrispondente trovato.")