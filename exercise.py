up_to_number = int(input("Up to which number do you want all prime numbers: "))
list_of_prime = []
def is_prime(number):
    count = 1
    while count < number:
        if (number % count) == 0 and (count != 1) and (count != number) :
            return False
        count += 1
    return True

def prime_list(up_to_number):
    count = 2
    while count <= up_to_number:
        if is_prime(count):
            list_of_prime.append(count)
        count += 1
    return(list_of_prime)

print(prime_list(up_to_number))