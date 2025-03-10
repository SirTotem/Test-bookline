### Test Bookline

# Para instalar:

- Descarregar python

- Preparar entorn
'''
python -m venv venv.
.\venv\Scripts\activate

pip install -r requirements.txt
'''

- Per mantenir en execució:
  '''
uvicorn app.main:app --reload  
'''

- Per executar tests:

'''
    pytest > resultados.txt
'''

