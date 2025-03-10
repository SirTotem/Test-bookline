### Test Bookline

# Para instalar:

- Descarregar python

- Preparar entorn
```bash
python -m venv venv.
.\venv\Scripts\activate

pip install -r requirements.txt
```

- Per mantenir en execució:
``` bash
uvicorn app.main:app --reload  
```

- Per executar tests:

```bash
pytest > results.txt
```

