from sympy import randprime
from random import randint



def createKey():
    USER_ONE_PRIVATE_KEY = 5
    USER_TWO_PRIVATE_KEY = 3

    Prime = randprime(75, 200)
    Base = randint(3, 50)
    
    userOneProduct = Base**USER_ONE_PRIVATE_KEY%Prime
    userTwoProduct = Base**USER_TWO_PRIVATE_KEY%Prime
    userOneFinal = userTwoProduct**USER_ONE_PRIVATE_KEY%Prime
    userTwoFinal = userOneProduct**USER_TWO_PRIVATE_KEY%Prime
    if userOneFinal == userTwoFinal:
        secretKey = userOneFinal
    else:
        raise Exception
    return secretKey

