# Guida Rapida per Eseguire l'Applicazione

### 1. (Opzionale) Crea e attiva un ambiente virtuale
python -m venv env
####  Su Windows:
.\env\Scripts\activate
####  Su MacOS/Linux:
source env/bin/activate

# 3. Installa le dipendenze
pip install -r requirements.txt

# 4. Linked Data Platform
1. **Scarica l'immagine Docker di GraphDB** ontotext/graphdb:10.4.4
2. **Crea un container con l'immagine**
3. **Crea un nuovo repository in GraphDB**
- Apri il tuo browser e vai all'indirizzo `http://localhost:7200`.
- Accedi come amministratore utilizzando le credenziali predefinite.
- Crea un nuovo repository con ID `LOL`.

1. **Importa i dati RDF**
- Nella sezione "Repositories" dell'interfaccia web di GraphDB, seleziona il repository `LOL`.
- Vai su "Import" e seleziona "RDF File Upload".
- Carica il file `Ontology/LOL.ttl`.
- Imposta la "Base IRI" come `http://www.semanticweb.org/gfazor/ontologies/LOL`.
- Conferma l'importazione.

# 5. Esegui l'applicazione
streamlit run .\League.py
#### Su MacOS/Linux:
streamlit run ./League.py
