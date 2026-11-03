## Clone o repositório

```bash
git clone https://github.com/FernandoTinno/AtividadeBackend-2.git
```

**Mude para a pasta do projeto**

```bash
cd AtividadeBackend-2
```

**Acesse o diretório**

```bash
code . -r
```

**Crie um ambiente virtual**

```bash
py -m venv venv
```

**Crie um ambiente virtual**

```bash
venv\Scripts\Activate.ps1
```

**Instale as dependências necessárias**

```bash
pip install -r requirements.txt
```

**Crie o Banco de dados**

```bash
alembic upgrade head
```

**Execute a aplicação**

```bash
py -m uvicorn main:app --reload
```

**Abra o link no navegador**

```bash
http://127.0.0.1:8000/docs
```