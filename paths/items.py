from fastapi import APIRouter
from schema.items import Item
from configuration.database import con
from modele.items import items

RouterItem = APIRouter()


@RouterItem.get("/items")
async def index():
    data = con.execute(items.select()).fetchall()
    result = [dict(row._mapping) for row in data]
    return {"success": True, "data": result}


@RouterItem.get("/items/{id}")
async def get_item(id: int):
    result = con.execute(items.select().where(items.c.id == id)).fetchone()
    if result:
        return {"success": True, "data": dict(result._mapping)}
    else:
        return {"success": False, "message": "Item pas trouve"}


@RouterItem.post("/items")
async def store(item: Item):
    result = con.execute(
        items.insert().values(
            name=item.name,
            price=item.price,
            in_stock=item.in_stock
        )
    )
    con.commit()
    if result.rowcount > 0:
        return {"success": True, "message": "Item enrregistre"}
    else:
        return {"success": False, "message": "Probleme survenu"}


@RouterItem.put("/items/{id}")
async def edit_data(id: int, item: Item):
    result = con.execute(
        items.update()
        .values(name=item.name, price=item.price, in_stock=item.in_stock)
        .where(items.c.id == id)
    )
    con.commit()
    if result.rowcount > 0:
        return {"success": True, "message": "Item mis à jour avec succès"}
    else:
        return {"success": False, "message": "Item pas trouve"}


@RouterItem.delete("/items/{id}")
async def delete_data(id: int):
    result = con.execute(items.delete().where(items.c.id == id))
    con.commit()
    if result.rowcount > 0:
        return {"success": True, "message": "Item supprimé avec succès"}
    else:
        return {"success": False, "message": "Item pas trouve"}
