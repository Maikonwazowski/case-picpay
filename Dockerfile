# Etapa 1 - build com Poetry
FROM python:3.11-slim AS builder

WORKDIR /app

# Instala dependências básicas e o Poetry
RUN apt-get update && apt-get install -y curl build-essential

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copia o projeto
COPY pyproject.toml poetry.lock ./

# Instala as dependências no ambiente virtual do poetry (sem criar venv externa)
RUN poetry config virtualenvs.create false \
  && poetry install --only=main --no-root
# Etapa 2 - imagem final
FROM python:3.11-slim

WORKDIR /app

# Copia as dependências já instaladas
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia o código da aplicação
COPY . .

EXPOSE 8000

# Comando para rodar a API
#CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
ENV PYTHONPATH=/app/src

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
