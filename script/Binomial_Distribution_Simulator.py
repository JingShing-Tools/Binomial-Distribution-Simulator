# tkinter toolkit
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom
from math import floor
import os

# plt.show()

def value_around(value=1, min_value=0, max_value=1):
    value = min(max_value, value)
    value = max(min_value, value)
    return value

class Gui_helper_main:
    def __init__(self):
        self.root = Tk()
        self.frame = None
        self.frame_index = 0
        self.root.geometry('300x200')
        self.root.title('Binomial Distribution Simulator')
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        # maker info
        self.maker_name = Label(self.root, text="Maker: JingShing")
        self.maker_name.grid(column=0, row=3, sticky=N+W)
        
        self.frames = [page_module(self)]
        self.switch_frame(0)
        
    def switch_frame(self, index):
        if self.frame is not None:
            self.frame.grid_forget()
        self.frame_index = index
        self.frame = self.frames[self.frame_index]
        self.frame.grid(column=0, row=0, sticky=N+W)

    def run(self):
        # from threading import Thread
        # thread1 = Thread(target=self.frames[0].order_bot)
        # thread1.setDaemon(True)
        # thread1.start()
        self.root.mainloop()

    def quit(self):
        if messagebox.askyesno('Confirm','Are you sure you want to quit?'):
            self.root.quit()

class page_module(Frame):
    def __init__(self, master):
        Frame.__init__(self, master = master.root)
        self.main = master
        self.master = master.root
        self.last_file_path = None

        # display last order
        self.last_order = StringVar()
        self.last_order.set('Binomial Distribution Simulator')
        self.last_order = Label(self, textvariable=self.last_order)
        self.last_order.grid(column=0, row=0, sticky=N+W)
        
        # input box
        self.n_label = Label(self, text='n(int):')
        self.n_label.grid(column=0, row=1)
        self.n_entry = Entry(self)
        self.n_entry.grid(column=1, row=1)
        self.p_label = Label(self, text='p(float):')
        self.p_label.grid(column=0, row=3)
        self.p_entry = Entry(self)
        self.p_entry.grid(column=1, row=3)
        self.size_label = Label(self, text='size(int):')
        self.size_label.grid(column=0, row=5)
        self.size_entry = Entry(self)
        self.size_entry.grid(column=1, row=5)
        self.target_label = Label(self, text='target(int):')
        self.target_label.grid(column=0, row=7)
        self.target_entry = Entry(self)
        self.target_entry.grid(column=1, row=7)
        
        # Button
        self.order_button = Button(self, text='save png', command=self.save_png)
        self.order_button.grid(column=0, row=9)
        self.order_button = Button(self, text='show table', command=self.show_table)
        self.order_button.grid(column=1, row=9)

    def update_string_var(self):
        self.last_order.set(self.order_bot.last_order)

    def save_png(self):
        n = int(self.n_entry.get())
        p = value_around(value = float(self.p_entry.get()), min_value=0, max_value=1)
        size = int(self.size_entry.get())
        target = int(self.target_entry.get())
        # mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
        mean = binom.stats(n, p, moments='m')
        fixed_mean = floor((n+1)*p)
        print("Mean(np):", mean)
        print("fixed mean(floor((n+1)*p)):", fixed_mean)
        print("Original Probability of "+str(target)+":", binom.pmf(target, n, p))
        print("% Probability of "+str(target)+":" + str(binom.pmf(target, n, p)*100) + '%')
        # binom.pmf(k, n, p)
        # binom.pmf(k) = choose(n, k) p**k (1-p)**(n-k)
        sns.displot(random.binomial(n=n, p=p, size=size))
        plt.title("Binomial Simulation w/ n = "+str(n)+", p = "+str(p))
        plt.tight_layout()

        output_dir = 'output'
        output_file_name = 'n_' + str(n) + '_' + 'p_' + str(p).replace('.', '') + '_' + 'plot.png'
        # output_file_name = 'plot.png'
        output_path = os.path.join(output_dir, output_file_name)

        # output_path = output_file_name
        plt.savefig(output_path, dpi=300)

    def show_table(self):
        n = int(self.n_entry.get())
        p = value_around(value = float(self.p_entry.get()), min_value=0, max_value=1)
        size = int(self.size_entry.get())
        target = int(self.target_entry.get())
        # mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
        mean = binom.stats(n, p, moments='m')
        fixed_mean = floor((n+1)*p)
        print("Mean(np):", mean)
        print("fixed mean(floor((n+1)*p)):", fixed_mean)
        print("Original Probability of "+str(target)+":", binom.pmf(target, n, p))
        print("% Probability of "+str(target)+":" + str(binom.pmf(target, n, p)*100) + '%')
        # binom.pmf(k, n, p)
        # binom.pmf(k) = choose(n, k) p**k (1-p)**(n-k)
        sns.displot(random.binomial(n=n, p=p, size=size))
        plt.title("Binomial Simulation w/ n = "+str(n)+", p = "+str(p))
        plt.tight_layout()
        plt.show()
        
if __name__ == '__main__':
    main = Gui_helper_main()
    main.run()