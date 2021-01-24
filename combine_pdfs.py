''' Written by Zach Lloyd on a whim, because combing PDF's is a pain. 

        Do not copy or redistribute without express, written consent. '''


import os 
import tkinter as tk
from tkinter import Tk, StringVar
from tkinter.filedialog import askdirectory

from PyPDF2 import PdfFileMerger

master = tk.Tk() #Create UI window
master.title('PDF Combiner') #Window title
master.geometry('300x70') #Window size
filePath = StringVar() #This creates a Tkinter object
filePathFull = StringVar() #This creates a Tkinter object
filePath.set("Directory: PLEASE SET") #No filename yet!
shownPath = tk.Label(master, textvariable=filePath).grid(row=0) #The path the user selected, shown
tk.Label(master, text="Result File Name").grid(row=1, column=0) #User directions
entry = tk.Entry(master)
entry.grid(row=1, column=1)  #User file name

def runMerge():

    ''' Merges PDFS, returns nothing '''
    merger = PdfFileMerger() #Resultant PDF object

    for file in os.listdir(filePathFull.get()): #For file in user selected dir
        filename = os.fsdecode(file)
        if filename.endswith('.pdf'): #If it is a pdf
            merger.append(os.path.join(filePathFull.get(), filename)) #Add it to the result

    merger.write(entry.get() + ".pdf") #Write the result
    merger.close() #Close writer
    master.destroy() #Close program

def setPath(): #Choose path
    path = askdirectory(title='Select Folder') # shows dialog box and return the path
    filePath.set("Directory: " + path.split('/')[-1]) #User-shown side
    filePathFull.set(path) #Set path to search

submit = tk.Button(master, text="Run", command=runMerge).grid(row=2, column=0) #Button to run merger

findPath = tk.Button(master, text="Set Directory", command=setPath).grid(row=2, column=1) #Button to open directory searcher

master.mainloop() #Run the program
