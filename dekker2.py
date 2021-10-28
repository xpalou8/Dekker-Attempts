import random
import time
from threading import Thread

# Constants
MAX_TO_COUNT = 10000000
COUNT_LOOPS = 100
NTHREADS = 2
PROBLEM = True

# Variable global que indica el desig de cada procés d'entrar a la regió crítica
want = [False, False]

# Varibale compartida a manipular
counter = 0

# Classe que hereta de threading.Trhead. Defineix el comportament dels fils
class MyThread(Thread):

    def __init__(self, id):
        super().__init__()
        self.id = id

    # Mètode que executen els fils
    def run(self):

        global want
        global counter
        max = (MAX_TO_COUNT // NTHREADS) // COUNT_LOOPS

        other = (self.id % 2)

        for i in range(COUNT_LOOPS):

            ### REGIÓ NO CRÍTICA ###

            ### PREPROTOCOL ###
            # Espera activa mentre no tengui el torn
            while want[other]:
                pass

            if PROBLEM and self.id == 1:
                time.sleep(0.00000000001)

            want[self.id - 1] = True

            ### REGIÓ CRÍTICA ###
            for i in range(max):
                counter += 1

            ### POSTPROTOCOL ###
            print(f"El procés {self.id} ha comptat fins a {counter}")
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