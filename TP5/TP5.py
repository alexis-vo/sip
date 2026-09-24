from math import pow, log2
from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits

def force(L, N):
    return int(log2(pow(N, L)))

punct = ".:;!?/()&#@&_-*%"

def is_strong_enough(pwd):
    return (any(s.isupper() for s in pwd))\
    and (any(s.islower() for s in pwd))\
    and (any(s.isdigit() for s in pwd))\
    and (s in punct for s in pwd)\
    and (len(pwd) >= 13)

# Random existe en Python de base
# mais pas de bonne qualité en cryptographie.
# C'est ok pour la simulation, mais le module
# secrets de Python est plus robuste.
def generate_password(size=13):
    alphabet = punct + ascii_lowercase + ascii_uppercase + digits
    # j'aurais pu mettre ascii_letters mais je préfère écrire
    # explicitement lowercase + uppercase pour plus de clarté
    
    # V1
    # pwd = ''
    # while True:
    #     pwd += choice(alphabet)
    #     if is_strong_enough(pwd):
    #         return pwd

    # V2
    # while not is_strong_enough(pwd):
    #     pwd = "".join((choice(alphabet) for _ in range (size)))
    # return pwd

    # V3
    while True:
        pwd = "".join(choice(alphabet) for _ in range(size))
        if is_strong_enough(pwd):
            return pwd

def main():
    # test = "abcdABCD1234()@!"
    # print(is_strong_enough(test))
    # print(generate_password())
    return


main()

