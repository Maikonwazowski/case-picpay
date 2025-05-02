
# Case PicPay - Machine Learning Engineer

Este projeto implementa uma API de escoragem online para predição de atrasos em voos, utilizando FastAPI, Poetry e um modelo de machine learning com enriquecimento externo via APIs públicas.

---

## Funcionalidades

- `/model-airport/health/` — Verifica se a API e o modelo estão disponíveis
- `/model-airport/model/load/` — Carrega um modelo `.pkl` enviado via upload
- `/model-airport/model/predict/` — Faz a predição com base em dados de voo + clima
- `/model-airport/model/history/` — Retorna o histórico de predições realizadas

---

## Stack utilizada

- **Python 3.11**
- **FastAPI** — Framework web assíncrono
- **Poetry** — Gerenciador de dependências
- **Uvicorn** — ASGI server
- **Scikit-learn** — Modelagem
- **Mongomock** — Armazenamento temporário em memória
- **Docker** — Empacotamento e deploy

---

## Como rodar o projeto local

```bash
# Instale o ambiente virtual padrão
poetry install

# Ativa o ambiente virtual
poetry shell

# Instale as dependências de desenvolvimento
poetry install
```
---

---

## Como rodar os testes
```bash
# Execute todos os testes com:
poetry run pytest -v
```

---

## Como rodar com Docker

### Build da imagem:

```bash
docker build -t case-picpay-api .
```

### Rodar o container:

```bash
docker run --name case-picpay-api -p 8000:8000 case-picpay-api
```

Acesse:

- Documentação: http://localhost:8000/docs

---

## Endpoints esperados

### `/model-airport/model/load/` (POST)

Upload de arquivo `.pkl`

### `/model-airport/model/predict/` (POST)

Campos esperados (via `Form`):

- `origin`, `dest`
- `month`, `distance`, `air_time`
- `carrier_code_*` e `route_*`

### `/model-airport/model/history/` (GET)

Retorna histórico de predições

---

## Estrutura de pastas

```
src/
├── app.py               # Entrypoint da API
├── controllers/         # Lógica de predição e enriquecimento
├── routes/              # Definição dos endpoints
├── schemas/             # Pydantic models
├── services/            # Integração com APIs externas
├── storage/             # Store in-memory com MongoMock
tests/                   # Testes automatizados
```

---

## Autor

Maikon Douglas G. dos Santos

---
