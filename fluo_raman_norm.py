import numpy as np    
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import io
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import re


def read_eem():
    """
    Opens a Tkinter window for selecting an Excel file, displays its contents, 
    and asks the user for confirmation on the data display.

    Returns:
        str or None: The path of the selected Excel file, or None if no file is selected.
    """
    # Initialize the main Tkinter window
    root = tk.Tk()
    root.title("Excel File Uploader and Converter")

    # Initialize variables to hold file contents and path
    file_contents = None
    file_path = None

    def _handle_upload():
        """
        Handles the file upload process and displays the contents if it's an Excel file.

        Returns:
            str or None: The path of the selected Excel file, or None if no file is selected.
        """
        nonlocal file_contents, file_path
        # Open file dialog to select a file
        path = filedialog.askopenfilename()
        if path:
            if path.endswith(('.xls', '.xlsx')):
                try:
                    # Read the selected Excel file
                    file_contents = pd.read_excel(path)
                    file_path = path
                    _process_excel_file()  # Display the contents
                    _display_success_message()  # Show success message
                except Exception as e:
                    _display_error_message()  # Show error message if there's an issue
                    output_text.insert(tk.END, f"An error occurred during uploading: {str(e)}\n")
            else:
                # Handle non-Excel file uploads
                file_path = path
                _display_success_message_no_conversion()
        else:
            output_text.insert(tk.END, "Please select a file.\n")
        
        return file_path

    def _process_excel_file():
        """
        Displays the contents of the uploaded Excel file in the GUI and 
        asks the user for confirmation on the data display.
        """
        output_text.delete("1.0", tk.END)  # Clear the text widget
        output_text.insert(tk.END, str(file_contents))  # Insert the contents of the file
        root.update()  # Update the GUI

        # Ask the user if the data was displayed correctly
        user_response = messagebox.askyesno("Confirmation", "Was the data correctly displayed?")
        if not user_response:
            raise ValueError("The code cannot continue due to incorrect data. Please upload a new file.")

    def _display_success_message():
        """
        Displays a success message in the GUI upon successful upload.
        """
        success_message_label.config(text="Upload successful.", fg="green")
        error_message_label.config(text="")
        print_file_path()
        close_window_label.config(text="Please close the window to continue the code")

    def _display_success_message_no_conversion():
        """
        Displays a success message for non-Excel files in the GUI.
        """
        success_message_label.config(text="File uploaded successfully (not an Excel file).", fg="green")
        error_message_label.config(text="")
        print_file_path()
        close_window_label.config(text="Please close the window to continue the code")

    def _display_error_message():
        """
        Displays an error message in the GUI if the upload fails.
        """
        error_message_label.config(text="Upload unsuccessful, please try again.", fg="red")
        success_message_label.config(text="")

    def print_file_path():
        """
        Prints the file path to the console.
        """
        if file_path:
            print("File Path:", file_path)
        else:
            print("No file has been uploaded yet.")

    # GUI components for file upload and messages
    file_label = tk.Label(root, text="Select an Excel file:")  # Label to instruct the user
    file_label.pack()

    upload_button = tk.Button(root, text="Upload", command=_handle_upload)  # Upload button
    upload_button.pack()

    output_text = tk.Text(root)  # Text widget to display file contents
    output_text.pack()

    success_message_label = tk.Label(root, text="")  # Label for success messages
    success_message_label.pack()

    error_message_label = tk.Label(root, text="")  # Label for error messages
    error_message_label.pack()

    close_window_label = tk.Label(root, text="")  # Label to instruct closing the window
    close_window_label.pack()

    root.mainloop()  # Start the Tkinter main loop

    return file_path

def read_excel():
    """
    Uploads and reads an Excel file, then modifies column names.

    Returns:
        pandas.DataFrame or None: The DataFrame containing the Excel file data, or None if no file is selected.
    """
    file_path = read_eem()  # Call read_eem to upload and read the file
    if file_path:
        eem = pd.read_excel(file_path)  # Read the Excel file into a DataFrame
        # Modify column names: keep the first column as is, and extract numbers from other columns
        new_columns = [col if i == 0 else int(re.search(r'\d+', col).group()) for i, col in enumerate(eem.columns)]
        eem.columns = new_columns  # Set the new column names
        return eem
    else:
        print("No file selected.")

# Call read_excel function to upload and read Excel file
eem_data = read_excel()
print(eem_data)  # Print the DataFrame to console



def Area(eem):
    '''
    Calculate the Area of the water Raman peak computed for 350 nm exitation waveleght and emission from 371 nm to 428 nm according to the following paper:
    Lawaetz, A. J., & Stedmon, C. A. (2009). Fluorescence Intensity Calibration Using the Raman Scatter Peak of Water. Applied Spectroscopy, 63(8), 936-940.
    https://journals.sagepub.com/doi/10.1366/000370209788964548

    Args: 
        - eem: dataframe containing the eem matrice created with de read_eem function

    Returns: Arp the Area of the water Raman peak calculated using the trapezoidal rule
    '''
    raman = eem.loc[(eem['EmWl [nm]'] >= 371) & (eem['EmWl [nm]'] <= 428)]
    dif = np.diff(raman['EmWl [nm]'])
    fluo_avg = (raman[350][:-1] + raman[350][1:]) / 2
    A = np.sum(dif[0] * fluo_avg)
    return A

def Raman_normalisation(eem, Area):
    '''
    Normalise all the fluorecence values in each exitation waveleght with the area of the Raman peak computed in the Area function and create a new files with the normalised values
    
    Args:  
    - eem: dataframe containing the eem matrice created with de read_eem function
    - Area: a dataframe containing the wavelenght exitation in each collumn and the associaced Raman Area
    
    Returns: A dataframe containing the normalised matrice
    '''
 
    columns_of_interest = eem.columns[1:] 
    normalised = eem.copy()
    normalised[columns_of_interest] = eem[columns_of_interest].div(Area)
    normalised.to_excel('normalised_Raman.xlsx', index=False)
    return normalised



def fluo_raman_norm(eem):
    A = Area(eem)
    return Raman_normalisation(eem, A)


def remove_rayleigh_scattering(eem, order=1, width=10):
    '''
    Allow to remove the first and second order Rayleigh scattering. It is recommanded to use this function before plotting the graph in order to have a better visualisation.
    The Rayleigh scatteing are removed according the following paper:	Anal. Methods, 2013,5, 6557-6566, https://pubs.rsc.org/en/content/articlelanding/2013/ay/c3ay41160e

    Args:
        - eem: dataframe containing the eem matrice created with de read_eem function
        - order: The order of the Rayleigh scattering that need to be remover. Allow the values 1 or 2. Default is set to 1
        - width: The width of the cut. A higher cut could supress data of interest. Default set to 10 nm

    Return: A copy of the eem DataFrame with the removed value set to NaN
    '''
    df = eem.copy()
    if order not in [1, 2]:
         raise ValueError("The value of 'order' must be either 1 or 2. This function removes Rayleigh scattering peaks of either first or second order.")
    for col in df.columns[1:]:
        df.loc[(df['EmWl [nm]'] >= order * float(col) - width) & (df['EmWl [nm]'] <= order * float(col) + width), col] = np.nan

    return df





def plot_fluorescence_graph():
    """
    Function to plot fluorescence data on a standard graph and/or an interactive graph.

    This function prompts the user to provide the file location, the sheet name, 
    the names of the excitation and emission wavelength columns in an Excel file, 
    and the wavelength of interest in nanometers (nm). It then plots the fluorescence 
    data on a standard graph and an interactive graph using Plotly.

    Returns:
    None
    """
    # Wavelenth of interest

    wavelength = int(input("What is the excitation wavelength of interest in nm : "))
    EmWl = eem["EmWl [nm]"]
    Int = eem[wavelength]

    # Ask the user if he wants to display the standard graph
    while True:
        choice1 = input("Would you like to plot a standard graph ? (yes/no) : ").lower()
        if choice1 == "yes":
            # Size of the graph
            plt.figure(figsize=(40,30))

            # Plotting of the point cloud
            plt.plot(EmWl, Int, label=f'λ = {wavelength}', color='black')
            plt.legend(fontsize=30)

            # Formating of the axis and title of the graph
            plt.title("Raman spectrum", fontsize=70)
            plt.xlabel(r'Excitation wavelength [nm]', fontsize=50)
            plt.ylabel(r'Fluorescence', fontsize=50)

            # Graduation of the axis
            plt.xticks(fontsize=30)
            plt.yticks(fontsize=30)
            plt.show()
            plt.savefig('Raman_spectrum.svg')
            break
        elif choice1 == "no":
            break
        elif choice1 != "no":
            print("Please answer by 'yes' or 'no'.")

    # Creation of an interactive graphic with zoom
    fig = go.Figure()

    # Adding of a scatter plot to the interactive graphic
    fig.add_trace(go.Scatter(x=EmWl, y=Int, marker=dict(color='black'), mode='lines', name='Data'))

    # Configuration of the layout of the interactive graphic
    fig.update_layout(
        title='Interactive graphics with zoom',
        xaxis_title='Fluorescence', 
        yaxis_title='Excitation wavelength [nm]',
        title_font=dict(size=25),  # Size of the title 
        title_x=0.5,  # To center the title
        xaxis=dict(
            title='Fluorescence',
            title_font=dict(size=20),  # Size of the label of the x axis
            rangeselector=dict(
                buttons=list([
                    dict(step="all") ])),
            rangeslider=dict(visible=True), 
            type="linear"),
        yaxis=dict(title='Excitation wavelength [nm]', 
                   title_font=dict(size=20)),  # Size of the label of the y axis
        hovermode='closest',
        height=700,  # Height in pixels
        width=900 )   # Width in pixels

    # Ask the user if he wants to display the interactive graph
    while True:
        choice2 = input("Would you like to plot an interactive graph ? (yes/no) : ").lower()
        if choice2 == "yes":
            fig.show()
            break
        elif choice2 == "no":
            break
        elif choice2 != "no":
            print("Please answer by 'yes' or 'no'.")
            

def plot_superimposed_graphs():
    """
    Function to plot a superposition of graphs on a standard graph and, if wanted, an interactive graph.

    This function prompts the user to input the number of graphs they want to superimpose. 
    It then collects data for each graph, including file location, sheet name, column names 
    for excitation and emission wavelengths, and the wavelength of interest. It plots both 
    a static and an interactive graph showing the superimposed curves.

    Returns:
    None
    """

    while True:
        try:
            number_of_graph = int(input("How many graphs would you like to superimpose :"))
            if number_of_graph > 7:
                print("A maximum of 7 different graphs can be superimposed !")
            elif number_of_graph < 2:
                print("The number of graph should be at least 2 !")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

            
    # Extraction of the values of interest

    
    # Creation of lists to store the values
    Xs = []
    wavelengths = []
    Ys = []

    # Loop to collect variables for each graph
    while True:
        q1 = input("Are all the values in the same file ? (yes/no) ")
        if q1 == "yes":
            eem = read_excel()
            for i in range(1, int(number_of_graph) + 1):
                X = eem["EmWl [nm]"]
                wavelength = int(input(f"What is the excitation wavelength of interest for curve {i} in nm: "))
                Y = eem[wavelength]
                # Adding the variables to the corresponding list
                Xs.append(X)
                wavelengths.append(wavelength)
                Ys.append(Y)
            break
        elif q1 == "no":
            for i in range(1, int(number_of_graph) + 1):
                eem = read_excel()
                X = eem["EmWl [nm]"]
                wavelength = int(input(f"What is the excitation wavelength of interest for curve {i} in nm: "))
                Y = eem[wavelength]
                # Adding the variables to the corresponding list
                Xs.append(X)
                wavelengths.append(wavelength)
                Ys.append(Y)
            break
        elif q1 != "no":
            print("Please answer by 'yes' or 'no'.")
    
            
    # General shape of the graph

    
    # Size of the graph, formating of the axis and title of the graph
    plt.figure(figsize=(40,30))
    plt.title("Raman spectrum", fontsize=70)
    plt.xlabel(r'Excitation wavelength [nm]',  fontsize=50)
    plt.ylabel(r'Fluorescence', fontsize=50)

    # Graduation of the axis
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)

    
    # Plot of the superimposed point cloud 


    colors = ["black", "blue", "red", "green", "magenta", "yellow", "cyan"]
    for i in range(number_of_graph):
        EmWl = eem["EmWl [nm]"]
        Int = eem[wavelength]
        color = colors[i]
        wavelength = wavelengths[i]
        plt.plot(EmWl, Int, label = f'λ = {wavelength}',color = color)
        plt.legend(fontsize = 40)

        
    # Plot of the interactive graph

    # Creation of an interactive graphic with zoom
    fig = go.Figure() 

    # Add each curve from data in Excel files
    for i in range(number_of_graph):
        # Select columns corresponding to x and y values
        x_col_name = Xs[i]
        y_col_name = Ys[i]  
    
        # Add curve to figure
        color = colors[i]
        wavelength = wavelengths[i]
        fig.add_trace(go.Scatter(x=x_col_name, y=y_col_name, marker=dict(color= color), mode='lines', name=f'λ = {wavelength}'))

    # Configuration des boutons pour afficher/supprimer les courbes
    buttons = []

    # Add a button for each curve
    for i in range(len(Xs)):
        wavelength = wavelengths[i]
        button = dict(
        label=f'λ = {wavelength}',
        method="update",
        args=[{"visible": [True if j == i else False for j in range(len(Xs))]}, {"title": f'λ = {wavelength}'}])
        buttons.append(button)

    # Add a button to display all curves
    button_all = dict(
        label="All",
        method="update",
        args=[{"visible": [True for _ in range(len(Xs))]}, {"title": "All"}])
    buttons.append(button_all)

    # Add a button to hide all curves
    button_none = dict(
        label="None",
        method="update",
        args=[{"visible": [False for _ in range(len(Xs))]}, {"title": "None"}])
    buttons.append(button_none)

    # Configuration of the layout of the interactive graphic
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                buttons=buttons,
                direction="left",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.02,
                xanchor="left",
                y=1.1,
                yanchor="top",
                font=dict(size=14))], # Font size
        title='Interactive graphics with zoom',
        xaxis_title='Fluorescence', 
        yaxis_title='Excitation wavelength [nm]',
        title_font=dict(size=25),  # Size of the title 
        title_x=0.5,  # To center the title
        xaxis=dict(
            title='Fluorescence',
            title_font=dict(size=20),  # Size of the label of the x axis
            type="linear"),
        yaxis=dict(title='Excitation wavelength [nm]', 
                   title_font=dict(size=20)),  # Size of the label of the y axis
        hovermode='closest',
        height=650,  # Height in pixels
        width=850 )   # Width in pixels
    
    # Ask the user if he wants to display the interactive graph
    while True:
        choice2 = input("Would you like to plot an interactive graph ? (yes/no) : ").lower()
        if choice2 == "yes":
            fig.show()
            break
        elif choice2 == "no":
            break
        elif choice2 != "no":
            print("Please answer by 'yes' or 'no'.")

            
    # Displaying and saving the graph

    
    plt.savefig('Raman_spectrum.svg')  
    plt.show()

def plot_3D_contour_inter(eem, levels = 30, Normalisation = True):
    '''
    Plot an interactive 3D contour graph with the folowing axes:
        - x: the emmited wavelenght in nm
        - y: the exitation wavelenght in nm
        - z: the intensity in a.u or R.u depending if the data are normalised or not
    Args: 
        - eem: dataframe containing the eem matrice created with de read_eem function
        - levels: the number of levels showed on the graph. Higher values increase precision but can lead to a loss of legibility in certain areas where the intensity varies rapidly. Default value is set to 30
        - Normalisation: Boolean used to specify whether or not normalisation has already been carried out. Only used to change the colorbar unit between a.u and R.u.

    '''
    if Normalisation:
        unit = 'R.u'
    else:
        unit = 'a.u'
    x = np.array(eem['EmWl [nm]'])
    Z = eem.iloc[:, 1:].values
    y = np.array(eem.columns[1:])

    fig = go.Figure(data=go.Contour(x=x, y=y, z=Z.transpose(), colorscale='jet',ncontours=levels,))
    fig.update_layout(
    xaxis_title='λ<sub>em</sub> [nm]',
    yaxis_title='λ<sub>ex</sub> [nm]', 
    )
    fig.update_traces(line_width=0.5)
    fig.data[0].colorbar.title = f"Fl [{unit}]"
    
    fig.show()

def plot_3D_contour(eem, levels = 25, Normalisation = True):
    '''
    Plot an 3D contour graph with the folowing axes:
        - x: the emmited wavelenght in nm
        - y: the exitation wavelenght in nm
        - z: the intensity in a.u or R.u depending if the data are normalised or not
    Args: 
        - eem: dataframe containing the eem matrice created with de read_eem function
        - levels: the number of levels showed on the graph. Higher values increase precision but can lead to a loss of legibility in certain areas where the intensity varies rapidly. Default value is set to 25
        - Normalisation: Boolean used to specify whether or not normalisation has already been carried out. Only used to change the colorbar unit between a.u and R.u.

    '''
    if Normalisation:
        unit = 'R.u'
    else:
        unit = 'a.u'
   
    x = np.array(eem['EmWl [nm]'])
    Z = eem.iloc[:, 1:].values
    y = np.array(eem.columns[1:])
    X,Y = np.meshgrid(x,y)
    Z_transposed = np.transpose(Z)
    
    plt.contourf(X,Y,Z_transposed, cmap='jet', levels = levels) 
    plt.colorbar(label=f'Fl [{unit}]')

    plt.contour(X, Y, Z_transposed, colors='k',linewidths=0.5, levels = levels)
    plt.xlabel(r'$\lambda{em}$ [nm]')
    plt.ylabel(r'$\lambda{ex}$ [nm]')


    plt.show()  

def plot_3D_surface_inter(eem, Normalisation = True):
    '''
    Plot an 3D surface interactive graph with the folowing axes:
        - x: the emmited wavelenght in nm
        - y: the exitation wavelenght in nm
        - z: the intensity in a.u or R.u depending if the data are normalised or not
    Args: 
        - eem: dataframe containing the eem matrice created with de read_eem function
        - Normalisation: Boolean used to specify whether or not normalisation has already been carried out. Only used to change the colorbar unit between a.u and R.u.
    '''
    
    if Normalisation:
        unit = 'R.u'
    else:
        unit = 'a.u'
    x = np.array(eem['EmWl [nm]'])
    Z = eem.iloc[:, 1:].values
    y = np.array(eem.columns[1:])

    fig = go.Figure(data=go.Surface(x=x, y=y, z=Z.transpose(), colorscale='jet'))
    fig.update_layout(
        scene=dict(
            xaxis_title='λ<sub>em</sub> [nm]',
            yaxis_title='λ<sub>ex</sub> [nm]',
            zaxis_title=f'Fl [{unit}]'
        )
    )
    
    fig.show()

