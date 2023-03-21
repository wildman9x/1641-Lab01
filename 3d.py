import os
import math
import time
import curses

def main(stdscr):
    A, B = 0, 0
    K1, K2 = 20, 30
    A_delta, B_delta = 0.04, 0.08

    while True:
        stdscr.clear()
        zbuffer = [0] * (80 * 22)

        for j in range(0, 628, 31):
            cj, sj = math.cos(j / 100), math.sin(j / 100)
            for i in range(0, 628, 31):
                ci, si = math.cos(i / 100), math.sin(i / 100)

                x = 1 + ci * (1 + cj)
                y = 1 + si * (1 + cj)
                z = K2 + K1 * cj
                ooz = 1 / z

                xp, yp = int(40 + 30 * ooz * x), int(11 + 15 * ooz * y)
                L = cj * si * 0.5 + 0.5
                if L > zbuffer[xp + 80 * yp]:
                    zbuffer[xp + 80 * yp] = L
                    stdscr.addch(yp, xp, ".,-~:;=!*#$@"[int(L * 11)])

        stdscr.refresh()
        A += A_delta
        B += B_delta
        time.sleep(0.03)

if __name__ == "__main__":
    os.system("resize -s 22 80")
    curses.wrapper(main)