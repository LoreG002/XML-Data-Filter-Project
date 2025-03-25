import pandas as pd
import os

# Cartella con i file XML
cartella_xml = "/Users/lorenzogiannetti/Library/CloudStorage/OneDrive-UniversitàPolitecnicadelleMarche/File di FRANCESCO PERUGINI - Progetti_OI"

# Parole chiave da cercare
parole_chiave = ["stampa 3d", "3d printing", "additive manufacturing", "fabbricazione additiva"]

# Lista per salvare i risultati di tutti i file
df_totale = pd.DataFrame()

# Scansiona tutti i file XML nella cartella
for filename in os.listdir(cartella_xml):
    if filename.endswith(".xml"):  # Filtra solo i file XML
        file_xml = os.path.join(cartella_xml, filename)
        
        # Legge il file XML in un DataFrame
        df = pd.read_xml(file_xml, xpath=".//AIUTO")  # Estrae tutti i nodi <AIUTO>
        
        # Controlla se le colonne necessarie esistono
        if "TITOLO_MISURA" in df.columns and "DES_TIPO_MISURA" in df.columns:
            # Filtra solo le righe che contengono almeno una parola chiave
            df_filtrato = df[df["TITOLO_MISURA"].str.contains('|'.join(parole_chiave), na=False, case=False) |
                             df["DES_TIPO_MISURA"].str.contains('|'.join(parole_chiave), na=False, case=False)]
            
            # Aggiunge i risultati al DataFrame totale
            df_totale = pd.concat([df_totale, df_filtrato], ignore_index=True)

# Stampa i risultati finali
print(df_totale)

# Salva i dati filtrati in un file CSV (facoltativo)
#df_totale.to_csv("risultati_filtrati.csv", index=False, encoding="utf-8")
