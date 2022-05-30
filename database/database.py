
ArrayOfProductsDB = []

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
# ---------------------- Getters And Setters Products ----------------------



