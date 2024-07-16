from nada_dsl import *

def nada_main():
    party1 = Party(name="Alice")
    party2 = Party(name="Bob")
    party3 = Party(name="Charlie")
    
    x = SecretInteger(Input(name="X", party=party1))
    y = SecretInteger(Input(name="Y", party=party2))
    
    sum_result = x + y
    product_result = x * y
    
    return [
        Output(sum_result, "sum_output", party3),
        Output(product_result, "product_output", party3)
    ]
