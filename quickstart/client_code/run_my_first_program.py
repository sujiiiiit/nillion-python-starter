class Party:
    def __init__(self, name):
        self.name = name

class Input:
    def __init__(self, name, party):
        self.name = name
        self.party = party

class SecretInteger:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return SecretInteger(self.value + other.value)
    
    def __mul__(self, other):
        return SecretInteger(self.value * other.value)
    
    def __truediv__(self, other):
        return SecretInteger(self.value // other.value)
    
    def __mod__(self, other):
        return SecretInteger(self.value % other.value)
    
    def __floordiv__(self, other):
        return SecretInteger(self.value // other.value)

class Output:
    def __init__(self, value, name, party):
        self.value = value
        self.name = name
        self.party = party

def sum_of_digits(n):
    s = 0
    while n.value > 0:
        s += n.value % 10
        n = SecretInteger(n.value // 10)
    return SecretInteger(s)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def nada_main(secret_number):
    party1 = Party(name="Alice")
    party2 = Party(name="Bob")
    
    secret_number = SecretInteger(secret_number)
    digit_sum = sum_of_digits(secret_number)
    
    factors = prime_factors(secret_number.value)
    prime_factors_sum = sum(sum_of_digits(SecretInteger(pf)).value for pf in factors)
    
    is_boston = (digit_sum.value == prime_factors_sum)
    
    return [
        Output(is_boston, "is_boston_output", party2)
    ]

# Taking input from the user
secret_number = int(input("Enter a number: "))

# Running the nada_main function
result = nada_main(secret_number)

# Printing the output
for output in result:
    print(f"The number is a Boston number: {output.value}")
