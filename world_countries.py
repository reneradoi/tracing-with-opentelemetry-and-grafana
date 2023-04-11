from fastapi import FastAPI
from sqlalchemy import create_engine, text
from requests import request

engine = create_engine('sqlite:///temp.db')

app = FastAPI()


@app.get("/world")
async def get_country(country: str):
    url = f"https://restcountries.com/v3.1/name/{country}"
    querystring = "fields=name,capital,currencies"

    response = request("GET", url, params=querystring)
    result = response.json()

    create_statement = text("CREATE TABLE IF NOT EXISTS countries("
                            "name text, "
                            "capital text)")

    insert_statement = text("INSERT INTO countries "
                            "(name, capital) "
                            "VALUES (:name, :capital)")

    try:
        with engine.connect() as conn:
            conn.execute(create_statement)
            conn.execute(insert_statement,
                         {'name': result[0]['name']['common'], 'capital': result[0]['capital'][0]})
            conn.commit()
    except Exception as err:
        return err

    return {'name': result[0]['name']['common'], 'capital': result[0]['capital'][0]}
