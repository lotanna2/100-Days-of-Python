import tkinter 

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady= 30)

#Label

my_label = tkinter.Label(text="new label") # Create a label widget with the specified text
my_label.config(font=("Arial", 24, "bold")) # Set the font and size of the label
#my_label.pack(side="left") # Add the label to the window and make it visible and centered
my_label.grid(row=0, column=0)


#second button 
my_second_button = tkinter.Button(text="this is my second label")
my_second_button.grid(row=0, column=2)

#Button

new_button =tkinter.Button(text="Click Me") # Creates a Button widget with the specified text 
new_button.grid(row=1, column=2) # Add the button to the window and make it visible

#Entry
input = tkinter.Entry() # Create an entry widget for user input
print(input.get()) # Print the current text in the entry widget
input.grid(row=3, column=3) # Add the entry widget to the window and make it visible


window.mainloop()