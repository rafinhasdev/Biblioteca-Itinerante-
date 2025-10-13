
# WorkApp

Sistema referente ao projeto de Extensão da Biblioteca Itinerante, no qual percorre escolas cadastrando novos livros de autores locais.

## Instalação

1. **Clone o repositório**

2. **Crie e ative o ambiente virtual**:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

4. **Execute as migrações**:
```bash
python manage.py migrate
```

5. **Crie um superusuário**:
```bash
python manage.py createsuperuser
```

6. **Carregue dados de exemplo** (opcional):
```bash
python manage.py load_data
```

7. **Inicie o servidor**:
```bash
python manage.py runserver
```

8. **Acesse**:
- Sistema: http://localhost:8000/
- Admin: http://localhost:8000/admin/
