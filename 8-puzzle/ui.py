import copy
import os
import sys
import tkinter as tk
from PIL import ImageTk, Image
from game import Pad
from solver import GeneticsSolver
MUTATION_CHANCE = 0.9
CROSS_OVER_RATE = 0.4
POPULATION_LEN = 1000
MAX_ITERATION = 1000


def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_board():
    global txt, lbl, insert_window, img, p, lbl_reslt
    p = Pad()
    k = 0
    img = []
    for i in range(3):
        for j in range(3):
            img.append(ImageTk.PhotoImage(Image.open(resource_path(
                txt[k].get(1.0)+'.png')).resize(size=(100, 100))))
            lbl[k].config(image=img[k])
            lbl[k].image = img[k]
            p.board[i][j] = float(txt[k].get(1.0))
            # print(txt[k].get(1.0))

            k = k+1
    obj = copy.deepcopy(p)

    p.pad.append(obj.board)
    insert_window.destroy()


def open():
    global txt, img_dm, insert_window, lbl_reslt
    insert_window = tk.Toplevel()
    insert_window.geometry('300x400')
    k = 0
    txt = []
    for i in range(3):
        for j in range(3):

            txt.append(tk.Text(insert_window, height=3,
                       width=7, font=('Arial bold', 18)))
            txt[k].grid(row=i, column=j)
            k = k+1
            # print(k)
    img_dm = ImageTk.PhotoImage(Image.open(resource_path(
        'insert.png')).resize(size=(100, 100)))
    # btn_insert = tk.Button(insert_window, text='stop', image=img_dm,
    #                        command=insert_window.destroy)
    btn_insert = tk.Button(insert_window, text='stop', image=img_dm,
                           command=get_board)
    btn_insert.grid(row=4, column=1)


def solve():
    global lbl, p, gSolver, lbl_reslt, lbl_CROSS_OVER_RATE, lbl_MAX_ITERATION, index_show,lbl_POPULATION_LEN, lbl_MUTATION_CHANCE
    index_show=0
    POPULATION_LEN = int(lbl_POPULATION_LEN.get('1.0', 'end-1c'))
    MUTATION_CHANCE = float(lbl_MUTATION_CHANCE.get('1.0', 'end-1c'))
    CROSS_OVER_RATE = float(lbl_CROSS_OVER_RATE.get('1.0', 'end-1c'))
    MAX_ITERATION = int(lbl_MAX_ITERATION.get('1.0', 'end-1c'))
    print('ACTUAL PAEAMS', POPULATION_LEN,
          MUTATION_CHANCE, CROSS_OVER_RATE, MAX_ITERATION)
    # p = Pad()
    # p.shuffle()
    gSolver = GeneticsSolver(
        p, POPULATION_LEN, MUTATION_CHANCE, CROSS_OVER_RATE)
    gSolver.solve(max_iter=MAX_ITERATION)
    img = list()

    print('\n\n====================================================')
    print('Original:')
    print(p)
    print('Found Solution:')
    print(gSolver.best.gene)
    k = 0
    for i in range(3):
        for j in range(3):
            img.append(ImageTk.PhotoImage(Image.open(resource_path(
                str(int(p.board[i, j]))+'.png')).resize(size=(100, 100))))
            lbl[k].config(image=img[k])
            lbl[k].image = img[k]

            k = k+1


def show_sloution():
    global lbl, p, gSolver, index_show, h, lbl_reslt,index_show
    if(index_show == 0):
        h = p.apply_chain(gSolver.best.gene, with_display=True)
        lbl_reslt.config(text='La Solution Est :\n ' +
                         '('+str(len(gSolver.best_solution().gene))+')' +
                         ' -> '.join(gSolver.best_solution().gene))
    if index_show <= len(h):
        if(index_show == len(h)):
            index_show = 0
        k = 0
        img_temp = []
        for l in range(3):
            for m in range(3):
                #  time.sleep(2)
                img_temp.append(ImageTk.PhotoImage(Image.open(resource_path(
                    str(int(h[index_show][l, m]))+'.png')).resize(size=(100, 100))))
                lbl[k].config(image=img_temp[k])
                lbl[k].image = img_temp[k]
                k = k+1
    index_show = index_show+1

    print('Result:')
    print(p)
    print("la solution est : ", gSolver.best_solution().gene)


window = tk.Tk()
window.geometry('1050x500')
txt = []
p = Pad()
index_show = 0
gSolver = GeneticsSolver(
    p, POPULATION_LEN, MUTATION_CHANCE, CROSS_OVER_RATE)

# window.iconbitmap('img.ico')
lbl_reslt = tk.Label(window, text=str('La Solution Est :'), background='#986B41', height=4, font=(
    'Calibri bold', 11), fg='#FBEC5D')
lbl_reslt.grid(row=1, column=4, padx=(0, 0), pady=(0, 0))
titre = tk.Label(window, text=str('ALGORITHME GENETIQUE'), background='#986B41', height=4, font=(
    'Calibri italic', 11), fg='#FBEC5D')
titre.grid(row=0, column=4, padx=(0, 0), pady=(0, 0))
lbl_MUTATION_CHANCE_title = tk.Label(window, text='MUTATE CHANCE', height=1,
                                     width=20, font=('Arial bold', 10))
lbl_MUTATION_CHANCE_title.grid(row=4, column=3,  padx=(15, 0))
lbl_MUTATION_CHANCE = tk.Text(window, height=1,
                              width=20, font=('Arial bold', 10))
lbl_MUTATION_CHANCE.grid(row=4, column=3, pady=(50, 0), padx=(15, 0))
lbl_CROSS_OVER_RATE_title = tk.Label(window, text='CROSSOVER RATE', height=1,
                                     width=20, font=('Arial bold', 10))
lbl_CROSS_OVER_RATE_title.grid(row=4, column=4,  padx=(15, 0))
lbl_CROSS_OVER_RATE = tk.Text(window, height=1,
                              width=20, font=('Arial bold', 10))
lbl_CROSS_OVER_RATE.grid(row=4, column=4, pady=(50, 0), padx=(15, 0))
lbl_POPULATION_LEN_title = tk.Label(window, text='LEN POPULATION', height=1,
                                    width=20, font=('Arial bold', 10))
lbl_POPULATION_LEN_title.grid(row=4, column=5,  padx=(15, 0))
lbl_POPULATION_LEN = tk.Text(window, height=1,
                             width=20, font=('Arial bold', 10))
lbl_POPULATION_LEN.grid(row=4, column=5, pady=(50, 0), padx=(15, 0))
lbl_MAX_ITERATION_title = tk.Label(window, text='MAX ITERATION', height=1,
                                   width=20, font=('Arial bold', 10))
lbl_MAX_ITERATION_title.grid(row=4, column=6,  padx=(15, 0))
lbl_MAX_ITERATION = tk.Text(window, height=1,
                            width=20, font=('Arial bold', 10))
lbl_MAX_ITERATION.grid(row=4, column=6, pady=(50, 0), padx=(15, 0))
lbl_CROSS_OVER_RATE.insert(1.0, str(CROSS_OVER_RATE))
lbl_MUTATION_CHANCE.insert(1.0, str(MUTATION_CHANCE))
lbl_MAX_ITERATION.insert(1.0, str(MAX_ITERATION))
lbl_POPULATION_LEN.insert(1.0, str(POPULATION_LEN))
img2 = ImageTk.PhotoImage(Image.open(
    resource_path('0.png')).resize(size=(100, 100)))
print(resource_path('0.png'))

img_demarrer = ImageTk.PhotoImage(Image.open(resource_path(
    'select.png')).resize(size=(100, 80)))
img_solve = ImageTk.PhotoImage(Image.open(resource_path(
    'solve.png')).resize(size=(100, 80)))
img_step = ImageTk.PhotoImage(Image.open(resource_path(
    'step.png')).resize(size=(100, 80)))
lbl = list()
k = 0
for i in range(3):
    for j in range(3):

        lbl.append(tk.Label(image=img2))
        lbl[k].grid(row=i, column=j)
        k = k+1


btn_select = tk.Button(image=img_demarrer, command=open)
btn_select.grid(row=4, column=2, pady=(50, 0))
btn_solve = tk.Button(image=img_solve, command=solve)
btn_solve.grid(row=4, column=1, pady=(50, 0))
btn_step = tk.Button(image=img_step, command=show_sloution)
btn_step.grid(row=4, column=0, pady=(50, 0))
window.mainloop()
