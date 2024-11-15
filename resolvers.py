def resolve_welcome(obj, info):
    return "¡Bienvenido a nuestra librería online!"

# Base de datos simulada de libros
books_db = {
    "1": {"id": "1", "name": "Cien Años de Soledad", "price": 15},
    "2": {"id": "2", "name": "El Principito", "price": 8},
    "3": {"id": "3", "name": "Don Quijote de la Mancha", "price": 12},
    "4": {"id": "4", "name": "Orgullo y Prejuicio", "price": 10},
    "5": {"id": "5", "name": "1984", "price": 14}
}

# Resolver para obtener todos los libros
def resolve_get_all_books(obj, info):
    return list(books_db.values())

# Resolver para obtener un libro específico por ID
def resolve_get_book(obj, info, id):
    return books_db.get(id)
