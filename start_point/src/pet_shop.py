# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, cash_1):
    cc_pet_shop["admin"]["total_cash"] = cc_pet_shop["admin"]["total_cash"] + cash_1
    return get_total_cash

def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, pets_1):
    cc_pet_shop["admin"]["pets_sold"] = cc_pet_shop["admin"]["pets_sold"] + pets_1
    return get_pets_sold

def get_stock_count(cc_pet_shop):
    count =0
    for pet in cc_pet_shop["pets"]:
        count = count +1
    return count

def get_pets_by_breed (cc_pet_shop, breed):
    pet_breed = []
    for pet in cc_pet_shop["pets"]:
        if pet ["breed"] == breed:
            pet_breed.append(pet)
    return pet_breed

def find_pet_by_name (cc_pet_shop, pet_name):
    for pet in cc_pet_shop["pets"]:
        if pet ["name"] == pet_name:
            return pet

def remove_pet_by_name (cc_pet_shop, pet_name):
    for pet in cc_pet_shop["pets"]:
        if pet ["name"] == pet_name:
            cc_pet_shop["pets"].remove(pet)
    return find_pet_by_name

# def add_pet_to_stock (cc_pet_shop, new_pets):
#     for new_pet in new_pets:
#         if new_pet == True:
#             cc_pet_shop["pets"].append(new_pet)
#     return get_stock_count

def get_customer_cash (customers):
    return customers["cash"]

def remove_customer_cash (customers, cash_1):
    customers["cash"] = customers["cash"] - cash_1

def get_customer_pet_count (customers):
    cust_pets = 0    
    for pet in customers["pets"]:
        cust_pets = cust_pets + 1
    return cust_pets

# def add_pet_to_customer (customer, new_pet):
#     for newpet in new_pet:
#         if newpet == True:
#             customer["pets"].append(newpet)
#     return get_customer_pet_count