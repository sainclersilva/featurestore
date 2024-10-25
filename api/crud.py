#Funções CRUD -
#Create (Criar), Read (Ler), Update (Atualizar), Delete (Deletar)

from database import get_db_connection
from models import Consumer, Restaurant

# Funções para a tabela consumer_features
def create_consumer(consumer: Consumer):
    with get_db_connection() as conn:
        conn.execute('''INSERT INTO consumer_features (customer_id, language, created_at, active, customer_phone_area, customer_phone_number) 
                        VALUES (?, ?, ?, ?, ?, ?)''',
                     (consumer.customer_id, consumer.language, consumer.created_at, consumer.active, consumer.customer_phone_area, consumer.customer_phone_number))
        conn.commit()

def get_all_consumers():
    with get_db_connection() as conn:
        return conn.execute("SELECT * FROM consumer_features").fetchall()

# Funções para a tabela restaurant_features
def create_restaurant(restaurant: Restaurant):
    with get_db_connection() as conn:
        conn.execute('''INSERT INTO restaurant_features (id, created_at, enabled, price_range, average_ticket, takeout_time, delivery_time, minimum_order_value, 
                                                          merchant_zip_code, merchant_city, merchant_state, merchant_country) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (restaurant.id, restaurant.created_at, restaurant.enabled, restaurant.price_range, restaurant.average_ticket, restaurant.takeout_time,
                      restaurant.delivery_time, restaurant.minimum_order_value, restaurant.merchant_zip_code, restaurant.merchant_city,
                      restaurant.merchant_state, restaurant.merchant_country))
        conn.commit()

def get_all_restaurants():
    with get_db_connection() as conn:
        return conn.execute("SELECT * FROM restaurant_features").fetchall()
