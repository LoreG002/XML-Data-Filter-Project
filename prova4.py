import csv
import os
import xml.etree.ElementTree as ET


# 📌 Cartella dei file XML
directory = "/Users/lorenzogiannetti/Desktop/file"
csv_file_path = "/Users/lorenzogiannetti/Desktop/output4.csv"

# 📌 Parole chiave
parole_chiave = ["stampa 3d", "3d printing", "additive manufacturing", "fabbricazione additiva"]

# 📌 Lista per salvare i risultati
righe_filtrate = []
header = None  # Intestazioni della tabella

# 🔄 Itera su tutti i file XML
xml_files = [f for f in os.listdir(directory) if f.endswith('.xml')]

for xml_file in xml_files:
    file_path = os.path.join(directory, xml_file)
    try:
        for event, elem in ET.iterparse(file_path, events=("end",)):
            if "AIUTO" in elem.tag:  # 🏷 Nodo principale (senza namespace)

                # 📌 Estrai dati senza namespace
                dati_azienda = {child.tag.split("}")[-1]: (child.text.strip() if child.text else "") for child in elem}

                # 📌 Recupera Titolo e Descrizione Progetto
                titolo_progetto = dati_azienda.get("TITOLO_PROGETTO", "")
                descrizione_progetto = dati_azienda.get("DESCRIZIONE_PROGETTO", "")

                # 📌 Controllo parole chiave
                if any(parola.lower() in titolo_progetto.lower() for parola in parole_chiave) or \
                   any(parola.lower() in descrizione_progetto.lower() for parola in parole_chiave):
                    
                    # 📌 Salva i dati estratti
                    if not header:
                        header = ["File"] + list(dati_azienda.keys())  # Intestazione colonne
                    righe_filtrate.append([xml_file] + list(dati_azienda.values()))

                elem.clear()  # 📌 Libera memoria
            
    except Exception as e:
        print(f"❌ Errore nel file {xml_file}: {e}")

# 📌 Scrivi nel CSV
if righe_filtrate:
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)  # Scrive le intestazioni delle colonne
        writer.writerows(righe_filtrate)

    print(f"\n✅ **Dati salvati in:** {csv_file_path}")
else:
    print("\n⚠ **Nessun dato corrispondente trovato.**")
