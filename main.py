def is_prime(number: int) -> bool:
     if number <= 1:
        return False
     for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
     return True


def list_prime_factors(number: int) -> list[int]:
    lista_primo = []

    while number != 1:
        i = 2
        looper = False
        while not looper:
         if is_prime(i):
             if number % i == 0:
                number = number / i
                lista_primo.append(i)
                looper = True
             else:
               i+=1
         else:
           i += 1    

    return lista_primo
