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