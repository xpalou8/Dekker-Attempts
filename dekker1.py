import random
from threading import Thread

# Constants
MAX_TO_COUNT = 10000000
COUNT_LOOPS = 100
NTHREADS = 2
MAX = (MAX_TO_COUNT // NTHREADS) // COUNT_LOOPS

PROBLEM = False

# Variable global que indica el torn
turn = 1

# Variable compartida a manipular
counter = 0

# Classe que hereta de threading.Thread. Defineix el comportament dels fils
class MyThread(Thread):

    def __init__(self, id):
        super().__init__()
        self.id = id
    
    # Mètode que executen els fils
    def run(self):

        global turn
        global counter

        for i in range(COUNT_LOOPS):

            ### REGIÓ NO CRÍTICA ###
            # En un moment donat un procés es queda en un bucle infinit
            number = random.randint(15, COUNT_LOOPS - 10)
            while PROBLEM and i > number:
                pass

            ### PREPROTOCOL ###
            # Espera activa mentres no tengui el torn
            while turn != self.id:
                pass

            ### REGIÓ CRÍTICA ###
            for i in range(MAX):
                counter += 1

            ### POSTPROTOCOL ###
            print(f"El procés {self.id} ha trobat fins {counter}")
            turn = (self.id % 2) + 1



# Programa principal
def main():
    processes = [MyThread(1), MyThread(2)]

    p, q = processes

    p.start()
    q.start()

    p.join()
    q.join()

    print(f"Valor real_{counter}\nValor esperat: {MAX_TO_COUNT}")

if __name__ == "__main__":
    main()