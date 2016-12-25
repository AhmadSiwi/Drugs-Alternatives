from tkinter import *
from fromDataBase import *
import tkinter.messagebox


root = Tk()

labelNameToAdd = Label(root, text = "name")
labelNameToAdd.grid(row=0, sticky=E)

NameToAdd = Entry(root)
NameToAdd.grid(row=0, column=1)
#NameToAdd.focus_set()

labelActiveIngredient = Label(root, text = "Active Ingredients")
labelActiveIngredient.grid(row=1, sticky=E)

ActiveIngredients = Entry(root)
ActiveIngredients.grid(row=1, column=1)
#ActiveIngredients.focus_set()

def handleAddNewDrugButton():
    print (NameToAdd.get())
    print (ActiveIngredients.get())
    drug_name = NameToAdd.get()
    ingredients = ActiveIngredients.get()
    ingredients = ingredients.split(',')
    addDrug(drug_name, ingredients)

AddNewDrugButton = Button(root, text="Add New Drug", command=handleAddNewDrugButton)
AddNewDrugButton.grid(columnspan=2)


labelName = Label(root, text = "name")
labelName.grid(row=3, sticky=E)

name = Entry(root)
name.grid(row=3, column=1)
#name.focus_set()

def handleSearchButton():
    drug_name = name.get()
    Alternatives = findAlternatives(drug_name)
    Alters = ""
    for Alternative in Alternatives:
        Alter = Alter + Alternative + "\n"
    tkinter.messagebox.showinfo(Alter)

SearchButton = Button(root, text="Search", command=handleSearchButton)
SearchButton.grid(columnspan=2)


root.mainloop()
