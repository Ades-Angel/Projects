# My Glossary Project
import tkinter as tk


# Key down function
def click():
    entered_text = textentry.get()
    output.delete(0.0, tk.END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = 'This word is not in the dictionary. Please try again'
    output.insert(tk.END, definition)


# main:
window = tk.Tk()
window.title('My Tinker Glossary')
window.configure(background='black')

# My photo
# photo1 = tk.PhotoImage(file='cslogo')
# tk.Label(window, image=photo1, bg='black').grid(row=0, column=1, sticky=5)

# Create label
tk.Label(window, text='Enter the word you would like a definition for: ',
         bg='black', fg='white',
         font='none 12 bold').grid(row=1, column=0, sticky=tk.W)

# Create a text entry box
textentry = tk.Entry(window, width=20, bg='White')
textentry.grid(row=2, column=0, sticky=tk.W)

# add a submit button
tk.Button(window, text='SUBMIT', width=6,
          command=click).grid(row=3, column=0, sticky=tk.W)

# create another label
tk.Label(window, text='\nDefinition: ', bg='black', fg='white',
         font='none 12 bold').grid(row=4, column=0, sticky=tk.W)

# Create a text box
output = tk.Text(window, width=75, height=6, wrap=tk.WORD, background='white')
output.grid(row=5, column=0, columnspan=2, sticky=tk.W)

# The dictionary
my_compdictionary = {
    'algorithm': 'Step by step instructions to complete a task',
    'bug': 'piece of code that causes a program to fail'
}

# Run the main loop
window.mainloop()
