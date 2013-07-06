#from www.pythonware.com/library/tkinter/introduction/hello-tkinter.htm
#it's all given in 2.7 so some of my conversions might be flawnky
#hella, hella adapted & slammed into place from my random hw generator.
#make it work, shoooooooot.

from tkinter import *

class App:

	def __init__(self, master):

		frame = Frame(master)
		frame.pack()

		self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
		self.button.pack(side=LEFT)

		self.randotron = Button(frame, text="randomize?", fg="blue", bg="gray", command=self.randotron)
		self.randotron.pack(side=LEFT)
		self.grab_set()

		#let's see if this works at all
		ent = Entry(mmaster)
		ent.pack()
		ent.focus_set()

		butt = Button(mmaster, text="fwomp", width=10, command=callback)
		butt.pack()
		mainloop()


	def randotron(self):
## this is where the cool stuff goes!!
## I'm gonna put the random module here instead
		import random
		problems = []
		i = 0

		section = input("what section is today's homework? ")
		amount = int(input("\nhow many problems today? "))
		while i < amount:
			problem = int(input("what is the problem number? "))
			problems.append(problem)
			i += 1

		print("From section",section,"there are",amount,"problems, which are the following\n")
		print(problems)

		problemChoice = random.choice(problems)
		#whoa, random.choice might work!  thanks steve from pyladies!
		print("The problem to grade is",problemChoice)
		print("(_|_)")

root = Tk()

app = App(root)

root.mainloop()
root.destroy()
