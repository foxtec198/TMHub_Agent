from time import sleep
import pyautogui as pg
from subprocess import run
from sys import platform

c = 25

def main():
    run(["cls" if platform == "win32" else "clear"], shell=True)

    print("="*c, " Localizador de Posição ", "="*c)
    print("Posicione seu mouse em cima da ferramenta deseja e clique em espaço para para o loop")
    print()
    
    pos = pg.position()
    print("Original: ", pos)
    print("Formatdo: ", f"({pos.x}, {pos.y})")
    sleep(2)

while True: main()