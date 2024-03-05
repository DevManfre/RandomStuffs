# automatic_shipment_database
Script creato per [italiangres](www.italiangres.com).

1. [Requirements](#requirements)
2. [How it works](#how-it-works)
    - [source_lambda_aws](#source_lambda_awspy)
    - [source_client](#source_clientpy)
3. [How to create executable](#how-to-create-executable)

## Requirements
Tutte le librerie necessarie sono state installate grazie a pipenv, quindi il virtual environment per avere tutte le dipendenze installate.
```bash
pipenv shell
```
Tutte le librerie necessarie si trovano all'interno di `Pipfile` e `Pipfile.lock`.

Per far funzionare i vari script bisogna inserire tutti i dati sensibili per il funzionamento:
- `source_client`:
    * lambda_aws_api_gateway, ovvero URL
    * api_key
    * query da effettuare all'interno di files
- `source_lambda_aws`:
    * host
    * user
    * password
    * database

## How it works
Lo script si compone di due file:
1. il primo gira lato host ed è il sorgente dell'eseguibile;
2. il secondo gira su una lambda function di AWS lambda.

### source_lambda_aws.py
Questo script crea una connessione al server per poi effettuare le query che vengono passate in metodo POST dall'eseguibile.
Viene utilizzata la lambda perchè si trova in locale rispetto al db e questo permette l'esecuzione delle query, dato che molto spesso i database sono irraggiungibili dall'esterno.

### source_client.py
Questo script si connette tramite API RESTfull alla lambda function, passando una query in post e ne ottiene i risultati, per poi salvarli in un file _.csv_.
Questa operazione viene effettuata per ogni dict all'interno della lista files: questo permette la creazione di più csv file tramite un unico eseguibile.

Per crearne di nuovi basta aggiungere un dict all'interno della lista con le seguenti proprietà:
- `name`: **REQUIRED**, il nome del file _.csv_.
- `query`: **REQUIRED**, la query che verrà eseguita e di cui si salveranno i risultati.
- `dataFunction`: **OPTIONAL**, se c'è bisogno di fare delle modifiche o manipolazioni sui record della query si può passare una funzione prima del salvataggio su disco modifichi i dati. Se non specificata non verrà eseguita alcuna modifica.

## How to create executable
Per creare l'eseguibile si utilizza la libreria python pyinstaller, già presente nel Pipfile.
Il comando da lanciare è il seguente:
```bash
pyinstaller <FILE_NAME> --onefile
```
Ed il file _.exe_ sarà all'interno della cartella `dist`.