import random
import time
from threading import Thread

# Constants
MAX_TO_COUNT = 10000000
COUNT_LOOPS = 100
NTHREADS = 2
PROBLEM = True

# Variable global que indica el dedig d'entrar a la regió crítica de cada procés
want = [False, False]

# Variable compartida a manipular
counter = 0

# Classe que hereta de threading.Thread. Defineix el comportament dels fils
class MyThread(Thread):

    def __init__(self, id):
        super().__init__()
        self.id = id

    # Mètode que executin els fils
    def run(self):

        global want
        global counter
        max = (MAX_TO_COUNT // NTHREADS) // COUNT_LOOPS

        other = (self.id % 2)

        for i in range(COUNT_LOOPS):

            ### REGIÓ NO CRÍTICA ###

            ### PREPROTOCOL ###
            want[self.id - 1] = True
            # Espera activa mentre no tengui el torn
            while want[other]:
                if PROBLEM:
                    time.sleep(0.0000001)
                want[self.id -1] = False
                if PROBLEM:
                    time.sleep(0.0000001)
                want[self.id -1] = True
                if PROBLEM:
                    time.sleep(0.0000001)
            
            ### REGIÓ CRÍTICA ###
            for i in range(max):
                counter += 1

            ### POSTPROTOCOL ###
            print(f"El procés {self.id} ha comptat fins {counter}")
            want[self.id - 1] = False



# Programa principal
def main():
    processes = [MyThread(1), MyThread(2)]

    p, q = processes

    p.start()
    q.start()

    p.join()
    q.join()

    print(f"Valor real: {counter}\nValor esperat: {MAX_TO_COUNT}")

if __name__ == "__main__":
    main()