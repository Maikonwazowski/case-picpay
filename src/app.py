from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.routes import router


description = """
`@copyright`  (c) 2025 - Picpay. ALL RIGHTS RESERVED\n
`@brief`      Case técnico - Machine Learning Engineer\n
`@author`     **Maikon Douglas** <maikondouglasgal@gmail.com>\n
`@since`      Abr 28, 2025       

## Introduction 
Essa api é referente ao case tecnico para machine learning enginner do picpay, com objetivo de dispobilizar um modelo em produção seguindo boas práticas.
"""

app = FastAPI(
    title="Case Picpay - Machine learning Engineer",
    description= description,
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods= ["*"],
    allow_headers=["*"]
)


app.include_router(router)