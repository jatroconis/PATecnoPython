
ArrayOfProductsDB = []
movementsUser = []

# ---------------------- Getters And Setters Products ----------------------

def GetArrayOfProductsDB() :
    return ArrayOfProductsDB

def AddProduct(product):
    ArrayOfProductsDB.append(product)

def GetProduct(id):
    for product in ArrayOfProductsDB:
        if product.id == id:
            return product
    return None

def GetProductByName(name):
    for product in ArrayOfProductsDB:
        if product.nombre == name:
            return product
    return None

#editar producto por id
def editProduct(id, name, price, cantidad):
    for product in ArrayOfProductsDB:
        if product.id == id:
            product.nombre = name
            product.precio = price
            product.cantidad = cantidad

#editar producto por id
def editProductQuantity(id , cantidad):
    for product in ArrayOfProductsDB:
        if product.id == id:
            product.cantidad = cantidad

#Borrar producto por id 
def deleteProduct(id):
    for product in ArrayOfProductsDB:
        if product.id == id:
            ArrayOfProductsDB.remove(product)

#Borrar producto por nombre
def deleteProductByName(name):
    for product in ArrayOfProductsDB:
        if product.nombre == name:
            ArrayOfProductsDB.remove(product)

# ---------------------- Getters And Setters Products ----------------------

# ---------------------- Getters And Setters Movements ----------------------
def arrayMovementsUser():
    return movementsUser

def addMovementsUser(movement):
    movementsUser.append(movement)



