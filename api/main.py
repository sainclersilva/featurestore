#Definicao de Endpoints FastAPI

from fastapi import FastAPI, HTTPException
from models import Consumer, Restaurant
from crud import create_consumer, get_all_consumers, create_restaurant, get_all_restaurants

app = FastAPI()

#teste
@app.get("/testeapi/")
def get_root():
    return {"Bem vindo": "API Feature Store está ONLINE!!!"}

# Endpoint para criar um novo consumidor
@app.post("/consumers/")
def add_consumer(consumer: Consumer):
    try:
        create_consumer(consumer)
        return {"message": "Consumer added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint para obter todos os consumidores
@app.get("/consumers/")
def read_consumers():
    consumers = get_all_consumers()
    return {"consumers": [dict(consumer) for consumer in consumers]}

# Endpoint para criar um novo restaurante
@app.post("/restaurants/")
def add_restaurant(restaurant: Restaurant):
    try:
        create_restaurant(restaurant)
        return {"message": "Restaurant added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint para obter todos os restaurantes
@app.get("/restaurants/")
def read_restaurants():
    restaurants = get_all_restaurants()
    return {"restaurants": [dict(restaurant) for restaurant in restaurants]}
