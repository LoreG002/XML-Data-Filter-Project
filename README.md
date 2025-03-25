# 📂 XML-Data-Filter-Project
Questo progetto si occupa di estrarre e filtrare informazioni specifiche dai file XML relativi ai progetti di un’impresa, per creare un file CSV contenente solo i dati rilevanti. L’obiettivo è facilitare l’analisi e l’organizzazione di progetti che contengono parole chiave specifiche come “stampa 3D”, “3D printing”, “additive manufacturing” e “fabbricazione additiva”.

🚀 Funzionalità
	•	Lettura e parsing di file XML da una directory specificata.
	•	Estrazione di informazioni rilevanti come titolo e descrizione del progetto.
	•	Filtraggio dei progetti in base a parole chiave.
	•	Esportazione dei dati filtrati in un file CSV per ulteriori analisi.

📋 Requisiti
	•	Python 3.x
	•	Librerie Python:
	•	csv: Per gestire l’output CSV.
	•	os: Per l’accesso ai file di sistema.
	•	xml.etree.ElementTree: Per il parsing dei file XML.

👀 Esempio di utilizzo

Supponendo che ci siano 3 file XML nella directory di input, lo script verificherà se i progetti contengono una delle parole chiave indicate nel titolo o nella descrizione. Se trovato, le informazioni verranno salvate nel file CSV.

⚠️ Errori e gestione delle eccezioni

Lo script è dotato di gestione delle eccezioni per evitare il crash in caso di errori durante l’elaborazione di un file XML.

except Exception as e:
    print(f"❌ Errore nel file {xml_file}: {e}")
