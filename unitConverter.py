from tkinter import * #for GUI
#dictionary to store the conversion factors 
# the dataStructures
# if __name__ == "__main__":  
    # dictionary of conversion factors  
unitDict = {  
        "millimeter" : 0.001,  
        "centimeter" : 0.01,  
        "meter" : 1.0,  
        "kilometer" : 1000.0,  
        "foot" : 0.3048,  
        "mile" : 1609.344,  
        "yard" : 0.9144,  
        "inch" : 0.0254,  
        "square meter" : 1.0,  
        "square kilometer" : 1000000.0,  
        "square centimeter" : 0.0001,  
        "square millimeter" : 0.000001,  
        "are" : 100.0,  
        "hectare" : 10000.0,  
        "acre" : 4046.856,  
        "square mile" : 2590000.0,  
        "square foot" : 0.0929,  
        "cubic meter" : 1000.0,  
        "cubic centimeter" : 0.001,  
        "litre" :  1.0,  
        "millilitre" : 0.001,  
        "gallon" : 3.785,  
        "gram" : 1.0,  
        "kilogram" : 1000.0,  
        "milligram" : 0.001,  
        "quintal" : 100000.0,  
        "ton" : 1000000.0,  
        "pound" : 453.592,  
        "ounce" : 28.3495  
    }  
  
    # charts for units conversion  
length_units = [  
        "millimeter", "centimeter", "meter", "kilometer", "foot", "mile", "yard", "inch"  
        ]  
temperature_units = [  
        "celsius", "fahrenheit"  
    ]  
area_units = [  
        "square meter", "square kilometer", "square centimeter", "square millimeter",  
        "are", "hectare", "acre", "square mile", "square foot"  
        ]  
volume_units = [  
        "cubic meter", "cubic centimeter", "litre", "millilitre", "gallon"     
    ]  
weight_units = [  
        "gram", "kilogram", "milligram", "quintal", "ton", "pound", "ounce"  
    ]  
  
#function to clear input fields
def reset():
    #use delete method to delete entries in entry fields
    input_field.delete(0, END)
    output_field.delete(0, END)
    #setting the value of the option menu
    #to the first index of the list using set()method
    input_value.set(SELECTIONS[0])
    output_value.set(SELECTIONS[0])
    #use focus_set method to set the focus on input field
    input_field.focus_set()
#function to convert the input value into desired one
def convert():
    try:
        inputVal = float(input_field.get())  # This is the numeric value to convert
        input_unit = input_value.get().lower()
        output_unit = output_value.get().lower()

        # Check for valid conversion group
        if input_unit in length_units and output_unit in length_units:
            result = inputVal * unitDict[input_unit] / unitDict[output_unit]

        elif input_unit in weight_units and output_unit in weight_units:
            result = inputVal * unitDict[input_unit] / unitDict[output_unit]

        elif input_unit in volume_units and output_unit in volume_units:
            result = inputVal * unitDict[input_unit] / unitDict[output_unit]

        elif input_unit in area_units and output_unit in area_units:
            result = inputVal * unitDict[input_unit] / unitDict[output_unit]

        elif input_unit == "celsius" and output_unit == "fahrenheit":
            result = (inputVal * 1.8) + 32

        elif input_unit == "fahrenheit" and output_unit == "celsius":
            result = (inputVal - 32) * (5 / 9)

        else:
            output_field.delete(0, END)
            output_field.insert(0, "Error: Incompatible Units")
            return

        output_field.delete(0, END)
        output_field.insert(0, round(result, 5))

    except ValueError:
        output_field.delete(0, END)
        output_field.insert(0, "Error: Invalid Input")


    # creating the list of options for selection menu  
SELECTIONS = [  
        "Select Unit",  
        "millimeter",  
        "centimeter",  
        "meter",  
        "kilometer",  
        "foot",  
        "mile",  
        "yard",  
        "inch",  
        "celsius",  
        "fahrenheit", 
        "square meter",  
        "square kilometer",  
        "square centimeter",  
        "square millimeter",  
        "are",  
        "hectare",  
        "acre",  
        "square mile",  
        "square foot", 
        "cubic meter",  
        "cubic centimeter",  
        "litre",  
        "millilitre",  
        "gallon",     
        "gram",  
        "kilogram",  
        "milligram",  
        "quintal",  
        "ton",  
        "pound",  
        "ounce"  
    ]  
# creating the main window
# using Tk() class from tKinter library
#creating  an object of tk
guiWindow = Tk()
#setting the title of the window
guiWindow.title("standard Unit Converter-Python")
#setting the size of the window
guiWindow.geometry('500x500+500+250')
#disabling the resizing of the window
guiWindow.resizable(0, 0)
#setting background color of the window
guiWindow.configure(bg='light blue')

#adding frames to main window using frame() widget
header_frame =Frame(guiWindow,bg='light blue')
body_frame =Frame(guiWindow,bg='light blue')
#setting postion of frames in the main window
header_frame.pack(expand=True, fill="both")
body_frame.pack(expand=True, fill="both")
#adding label to header frame
header_label = Label(  
    header_frame,  
    text = "STANDARD UNIT CONVERTER",  
    font = ("arial black", 16),  
    bg = "#16a085",  
    fg = "#e8f6f3"  
)
#setting the position of header label
header_label.pack(expand=True, fill="both")
#objects stringvar()class to store the data from input and output selection menus
input_value = StringVar()
output_value = StringVar()
# using the set() method to set the primary  
# value of the objects to index value 0  
# of the SELECTIONS list 
input_value.set(SELECTIONS[0])
output_value.set(SELECTIONS[0])
#displaying info on main window using label() widget
# creating the labels for the body of the main window  
input_label = Label(  
    body_frame,  
    text = "From:",  
    bg = "#16a085",  
    fg = "#d0ece7"  
)  
output_label = Label(  
    body_frame,  
    text = "To:",  
    bg = "#16a085",  
    fg = "#d0ece7"  
)  
#use grid method to set the position of labels
input_label.grid(row =1, column =1, padx =50, pady =20, sticky = W)
output_label.grid(row = 2, column = 1, padx = 50, pady = 20, sticky = W)
#add some entry fields to main window using entry() widget
#input field to enter data
input_field= Entry(
     body_frame,
     bg = '#e8f8f5'
)
#output field to display data result
output_field= Entry(
     body_frame,
     bg = '#e8f8f5'
)
#using grid () method to set position of the above entry fields
input_field.grid(row = 1, column=2)
output_field.grid(row =2, column =2)
#adding option menus to main window
#using OptionMenu() widget
input_menu = OptionMenu(
     body_frame,
     input_value,
     *SELECTIONS
)
output_menu = OptionMenu(
     body_frame,
     output_value,
     *SELECTIONS
)
#using grid () method to set position of the above option menus
input_menu.grid(row = 1, column = 3,padx = 20)
output_menu.grid(row = 2, column = 3, padx = 20)
#add buttons using button() widget
#these buttons call reset() and convert() fns
convert_button = Button(
     body_frame,
     text = 'CONVERT',
     bg = "#0b5345",  
    fg = "#ffffff",  
     command = convert
)
reset_button = Button(  
    body_frame,  
    text = "RESET",  
    bg = "#f7dc6f",  
    fg = "#000000",  
    command = reset  
)  
# using the grid() method to set the position of the above buttons  
convert_button.grid(row = 3, column = 2)  
reset_button.grid(row = 3, column = 3)  
#to run the application
# we have used the mainloop() method 
# with guiWindow, 
# the object of the Tk() class, 
# to run the application.
guiWindow.mainloop()




        

