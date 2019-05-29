import tkinter as tk
import json
#Menu Items Dictionary
DrinkDict = {
    "Drink1": 0,
    "Drink2": 0,
    "Drink3": 0,
    "Drink4": 0,
    "Drink5": 0,
    "Drink6": 0,
    "Drink7": 0,
    "Drink8": 0,
    "Drink9": 0,
    "Drink10": 0,
    "Drink11": 0,
    "Drink12": 0
}

#Counter Function for each menu item Sold
def drinkCounter(drinkNum):
    x = DrinkDict.get(drinkNum)
    x += 1
    DrinkDict[drinkNum] = x
    OutPut["text"] = drinkNum + " : " + str(DrinkDict.get(drinkNum))

#Create a Blank Copy of the Dictonary Used to Reset Dictonary
DrinkDictCopy = DrinkDict.copy()
#Function to Clear The Dictionary
def clearDict():
    global DrinkDict
    DrinkDict = DrinkDictCopy
    OutPut["text"] = ""
#Creates a JSON File that exports to test.txt File  and Prints the json to
#The GUI
def sumbit():
    global DrinkDict
    jsonData = json.dumps(DrinkDict, indent=4)
    OutPut["text"] = jsonData
    with open('test.txt', 'w') as outfile:
        json.dump(jsonData, outfile, indent=0)


#Declaring the Area of the GUI
root = tk.Tk()
HEIGHT = 800
WIDTH = 900

MainScreen = tk.Canvas(root, height=HEIGHT, width=WIDTH)
MainScreen.pack()
#Creating the Frame for the GUI
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relwidth=1, relheight=1)

#Header for the Label
Header = tk.Label(frame, text="Menu Items")
Header.place(relx=.1, relwidth=.4, relheight=.15)

#Creating each Button
AddButton = tk.Button(root, text="Clear", command=lambda: clearDict())
AddButton.place(relx=.55, rely=.01, relwidth=.2, relheight=.15)

AddButton = tk.Button(root, text="Submit", command=lambda: sumbit())
AddButton.place(relx=.78, rely=.01, relwidth=.2, relheight=.15)

AddButton = tk.Button(root, text="Beer1", command=lambda: drinkCounter("Drink1"))
AddButton.place(relx=.15, rely=.2, relwidth=.2, relheight=.1)

AddButton = tk.Button(root, text="Beer2", command=lambda: drinkCounter("Drink2"))
AddButton.place(relx=.4, rely=.2, relwidth=.2, relheight=.1)

AddButton = tk.Button(root, text="Beer3", command=lambda: drinkCounter("Drink3"))
AddButton.place(relx=.65, rely=.2, relwidth=.2, relheight=.1)

AddButton = tk.Button(root, text="Beer4", command=lambda: drinkCounter("Drink4"))
AddButton.place(relx=.15, rely=.32, relwidth=.2, relheight=.1)

AddButton = tk.Button(root, text="Beer5", command=lambda: drinkCounter("Drink5"))
AddButton.place(relx=.4, rely=.32, relwidth=.2, relheight=.1)

AddButton = tk.Button(root, text="Beer6", command=lambda: drinkCounter("Drink6"))
AddButton.place(relx=.65, rely=.32, relwidth=.2, relheight=.1)

AddButton = tk.Button(root, text="Beer7", command=lambda: drinkCounter("Drink7"))
AddButton.place(relx=.15, rely=.44, relwidth=.2, relheight=.1)

AddButton = tk.Button(root, text="Beer8", command=lambda: drinkCounter("Drink8"))
AddButton.place(relx=.4, rely=.44, relwidth=.2, relheight=.1)

AddButton = tk.Button(root, text="Beer9", command=lambda: drinkCounter("Drink9"))
AddButton.place(relx=.65, rely=.44, relwidth=.2, relheight=.1)

AddButton = tk.Button(root, text="Beer10", command=lambda: drinkCounter("Drink10"))
AddButton.place(relx=.15, rely=.56, relwidth=.2, relheight=.1)

AddButton = tk.Button(root, text="Beer11", command=lambda: drinkCounter("Drink11"))
AddButton.place(relx=.4, rely=.56, relwidth=.2, relheight=.1)

AddButton = tk.Button(root, text="Beer12", command=lambda: drinkCounter("Drink12"))
AddButton.place(relx=.65, rely=.56, relwidth=.2, relheight=.1)

#Output Label 
OutPut = tk.Label(frame)
OutPut.place(relx=.1, rely=.7, relwidth=.8, relheight=.3)


root.mainloop()