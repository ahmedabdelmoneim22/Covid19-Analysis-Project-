#>>How to display SQL Table in Python Tkinter.
import pyodbc
import tkinter as tk
from tkinter import ttk
def fetch_data():
    selected_country = country_combo.get()
    # Connect to SQL Server
    conn = pyodbc.connect(connection_string)
    cursor0 = conn.cursor()
    # people Vaccinated Population.
    cursor0.execute(f"Select *,(RollingPeopleVaccinated/Population) * 100 as PercentOfPeopleVaccinated from Covid19Project.dbo.PercentOfPopulationVaccinated where location like '%{selected_country}%' and Continent is not null order by 2,3")
    rows1 = cursor0.fetchall()
    # Clear previous data in the TreeView.
    for row in treeview0.get_children():
        treeview0.delete(row)
    # Insert fetched data into the TreeView.
    i = 0
    for row in rows1:
        treeview0.insert('', 'end', values=(rows1[i][0], rows1[i][1], rows1[i][2], rows1[i][3], rows1[i][4], rows1[i][5], rows1[i][6]))
        i = i + 1
    conn = pyodbc.connect(connection_string)
    cursor1 = conn.cursor()
    # Death Percentages By Country And Date.
    cursor1.execute(f"Select Location, date,population,total_cases,total_deaths,(total_deaths/total_cases)*100 as DeathPercentage From Covid19Project.dbo.CovidDeaths Where location like '%{selected_country}%' and continent is not null  order by 1,2")
    rows = cursor1.fetchall()
    # Clear previous data in the TreeView.
    for row in treeview.get_children():
        treeview.delete(row)
    # Insert fetched data into the TreeView.
    i = 0
    for row in rows:
        treeview.insert('', 'end', values=(rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5]))
        i = i + 1
    conn = pyodbc.connect(connection_string)
    cursor2 = conn.cursor()
    # Population Infected Percentages By Country And Date.
    cursor2.execute(
        f"Select Location,date,Population,total_cases,total_deaths,(total_cases/population)*100 as PercentPopulationInfected From Covid19Project.dbo.CovidDeaths  Where location like '%{selected_country}%' order by 1,2")
    rows2 = cursor2.fetchall()
    # Clear previous data in the TreeView.
    for row in treeview1.get_children():
        treeview1.delete(row)
    # Insert fetched data into the TreeView.
    i = 0
    for row in rows2:
        treeview1.insert('', 'end',
                         values=(rows2[i][0], rows2[i][1], rows2[i][2], rows2[i][3], rows2[i][4], rows2[i][5]))
        i = i + 1
    conn = pyodbc.connect(connection_string)
    cursor3 = conn.cursor()
    # Highest Infection Rate By Country And Date.
    cursor3.execute("Select Location,date,Population,total_cases,total_deaths,(total_cases/population)*100 as PercentPopulationInfected From Covid19Project.dbo.CovidDeaths order by PercentPopulationInfected DESC")
    rows3 = cursor3.fetchall()
    # Clear previous data in the TreeView.
    for row in treeview2.get_children():
        treeview2.delete(row)
    # Insert fetched data into the TreeView.
    i = 0
    for row in rows3:
        treeview2.insert('', 'end',values=(rows3[i][0], rows3[i][1], rows3[i][2], rows3[i][3], rows3[i][4], rows3[i][5]))
        i = i + 1
    conn = pyodbc.connect(connection_string)
    cursor4 = conn.cursor()
    # Highest Infection Rate By Country And Population DESC.
    cursor4.execute("Select Location,Population,MAX(total_cases) as HighestInfectionCount,Max((total_cases/population))*100 as PercentPopulationInfected From Covid19Project.dbo.CovidDeaths Group by Location, Population order by PercentPopulationInfected DESC")
    rows4 = cursor4.fetchall()
    # Clear previous data in the TreeView.
    for row in treeview3.get_children():
        treeview3.delete(row)
    # Insert fetched data into the TreeView.
    i = 0
    for row in rows4:
        treeview3.insert('', 'end', values=(rows4[i][0], rows4[i][1], rows4[i][2], rows4[i][3]))
        i = i + 1
    conn = pyodbc.connect(connection_string)
    cursor5 = conn.cursor()
    # Highest Death Count By Country And Population DESC.
    cursor5.execute("Select Location, Population, MAX(total_deaths) as HighestDeathsCount,  Max((total_deaths/population))*100 as PercentPopulationDeaths From Covid19Project.dbo.CovidDeaths Group by Location, Population order by PercentPopulationDeaths DESC")
    rows5 = cursor5.fetchall()
    # Clear previous data in the TreeView.
    for row in treeview4.get_children():
        treeview4.delete(row)
    # Insert fetched data into the TreeView.
    i = 0
    for row in rows5:
        treeview4.insert('', 'end', values=(rows5[i][0], rows5[i][1], rows5[i][2], rows5[i][3]))
        i = i + 1
    conn = pyodbc.connect(connection_string)
    cursor6 = conn.cursor()
    # Sum of Total Cases,Sum of Total Deaths,The Percentage of Death.
    cursor6.execute(f"Select SUM(new_cases) as total_cases,SUM(cast(new_deaths as int)) as total_deaths,SUM(cast(new_deaths as int))/SUM(New_Cases)*100 as DeathPercentage From Covid19Project.dbo.CovidDeaths where continent is not null and location like '%{selected_country}%' order by 1,2")
    rows6 = cursor6.fetchall()
    # Clear previous data in the TreeView.
    for row in treeview5.get_children():
        treeview5.delete(row)
    # Insert fetched data into the TreeView.
    i = 0
    for row in rows6:
        treeview5.insert('', 'end', values=(rows6[i][0], rows6[i][1], rows6[i][2]))
        i = i + 1
    conn = pyodbc.connect(connection_string)
    cursor7 = conn.cursor()
    # Total Death Count By Country.
    cursor7.execute(f"Select Location, MAX(cast(Total_deaths as int)) as TotalDeathCount From Covid19Project.dbo.CovidDeaths Where continent is not null and location like '%{selected_country}%' Group by Location order by TotalDeathCount DESC")
    rows7 = cursor7.fetchall()
    # Clear previous data in the TreeView.
    for row in treeview6.get_children():
        treeview6.delete(row)
    # Insert fetched data into the TreeView.
    i = 0
    for row in rows7:
        treeview6.insert('', 'end', values=(rows7[i][0], rows7[i][1]))
        i = i + 1
    conn = pyodbc.connect(connection_string)
    cursor9 = conn.cursor()
    # Total Vaccinations , PercentOfPeopleVaccinations.
    cursor9.execute(f"Select SUM(New_vaccinations) as total_Vaccinations, sum(New_vaccinations/Population) * 100 as PercentOfPeopleVaccinated from Covid19Project.dbo.PercentOfPopulationVaccinated where location like '%{selected_country}%' and Continent is not null order by 1,2")
    rows9 = cursor9.fetchall()
    # Clear previous data in the TreeView.
    for row in treeview8.get_children():
        treeview8.delete(row)
    # Insert fetched data into the TreeView.
    i = 0
    for row in rows9:
        treeview8.insert('', 'end', values=(rows9[i][0], rows9[i][1]))
        i = i + 1
    # Close Connection.
    conn.close()
root = tk.Tk()
root.geometry("1400x500")
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
# Create a Canvas widget.
canvas = tk.Canvas(root)
canvas.configure(background="white")
canvas.pack(side="left", fill="both", expand=True)
# Add a Frame inside the Canvas.
style = ttk.Style()
style.configure("Custom.TFrame", background="#0477BF")
frame = ttk.Frame(canvas,style="Custom.TFrame")
canvas.create_window((0, 0), window=frame, anchor="nw")
# Configure the Canvas to resize with the window.
canvas.bind("<Configure>", on_configure)
# Create a vertical Scrollbar for the Canvas.
vsb = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
vsb.pack(side="right", fill="y")
canvas.configure(yscrollcommand=vsb.set)
# Create a horizontal Scrollbar for the Canvas.
#hsb = ttk.Scrollbar(root, orient="horizontal", command=canvas.xview)
#hsb.pack(side="bottom", fill="x")
#canvas.configure(xscrollcommand=hsb.set)
##########################################
style = ttk.Style()
style.configure("Red.TLabel", background="#0477BF",foreground="#A6032F")
root.title("Covid 19 Disease Statistics By Country Project")
root.configure(background="White")
TitleLabel = ttk.Label(frame,text="Coronavirus Disease Statistics By Country",
                       style="Red.TLabel",width=50,font=('Helvetica', 24,'bold'),anchor="center")
TitleLabel.pack(pady=10)
FilterLabel = ttk.Label(frame,text="Filter The Data By Country",
                        style="Red.TLabel",font=('Helvetica', 14,'bold'),anchor="center")
FilterLabel.pack(pady=10)
#def on_country_select(event):
#    selected_country = country_combo.get()
#    print("Selected Country:", selected_country)
def get_the_Countries():
    server = '.'
    database = 'Covid19Project'
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    countries = []
    conn = pyodbc.connect(connection_string)
    cursorC = conn.cursor()
    cursorC.execute("Select location from Covid19Project.dbo.CovidDeaths group by location order by location")
    rowsC = cursorC.fetchall()
    i = 0
    for row in rowsC:
        countries.append(rowsC[i][0])
        i = i + 1
    conn.close()
    return countries
countries = get_the_Countries()
country_var = tk.StringVar()
# Create a Combobox.
country_combo = ttk.Combobox(frame, textvariable=country_var, values=countries,width=38,font=('bold'))
country_combo.set('Egypt')
country_combo.pack(pady=10)
# Bind a function to execute when a country is selected
#country_combo.bind("<<ComboboxSelected>>", on_country_select)
# Create Fetch Data button.
fetch_button = tk.Button(frame, text="View Data",
                         command=fetch_data,width=20,
                         font=('Helvetica',14,'bold'),background="#0477BF",fg="#A6032F",activebackground="#A6032F",activeforeground="#0477BF")
fetch_button.pack(pady=10)
# Connect to SQL Server.
server = '.'
database = 'Covid19Project'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
treeLabel0 = tk.Label(frame,text="Statistics Of People Vaccinated & Percent of Population Vaccinated By Country",
                      font=('Helvetica',14,'bold'),background="#0477BF",fg="#A6032F")
treeLabel0.pack(pady=10)
treeview0 = ttk.Treeview(frame)
treeview0['columns'] = ("Continent","Location","Date","Population","New Vaccinations","Rolling People Vaccinated","Percent Of People Vaccinated")
treeview0.column("#0",width=0,minwidth=0)
treeview0.column("Continent",anchor="center")
treeview0.column("Location",anchor="center")
treeview0.column("Date",anchor="center")
treeview0.column("Population",anchor="center")
treeview0.column("New Vaccinations",anchor="center")
treeview0.column("Rolling People Vaccinated",anchor="center")
treeview0.column("Percent Of People Vaccinated",anchor="center")
treeview0.heading("#1",text="Continent")
treeview0.heading("#2",text="Location")
treeview0.heading("#3",text="Date")
treeview0.heading("#4",text="Population")
treeview0.heading("#5",text="New Vaccinations")
treeview0.heading("#6",text="Rolling People Vaccinated")
treeview0.heading("#7",text="Percent Of People Vaccinated")
treeview0.pack()
treeLabel = tk.Label(frame,text="Statistics Of Total Cases & Total Deaths & Death Percentage By Country",
                      font=('Helvetica',14,'bold'),background="#0477BF",fg="#A6032F")
treeLabel.pack(pady=10)
treeview = ttk.Treeview(frame)
treeview['columns'] = ("Location","Date","Population","Total Cases","Total Deaths","Death Percentage")
treeview.column("#0",width=0,minwidth=0)
treeview.column("Location",anchor="center")
treeview.column("Date",anchor="center")
treeview.column("Population",anchor="center")
treeview.column("Total Cases",anchor="center")
treeview.column("Total Deaths",anchor="center")
treeview.column("Death Percentage",anchor="center")
treeview.heading("#1", text="Location")
treeview.heading("#2", text="Date")
treeview.heading("#3", text="Population")
treeview.heading("#4", text="Total Cases")
treeview.heading("#5", text="Total Deaths")
treeview.heading("#6", text="Death Percentage")
treeview.pack()
treeLabel1 = tk.Label(frame,text="Statistics Of Total Deaths & Percent Population Infected By Country",
                      font=('Helvetica',14,'bold'),background="#0477BF",fg="#A6032F")
treeLabel1.pack(pady=10)
treeview1 = ttk.Treeview(frame)
treeview1['columns'] = ("Location","Date","Population","Total Cases","Total Deaths","Percent Population Infected")
treeview1.column("#0",width=0,minwidth=0)
treeview1.column("Location",anchor="center")
treeview1.column("Date",anchor="center")
treeview1.column("Population",anchor="center")
treeview1.column("Total Cases",anchor="center")
treeview1.column("Total Deaths",anchor="center")
treeview1.column("Percent Population Infected",anchor="center")
treeview1.heading("#1", text="Location")
treeview1.heading("#2", text="Date")
treeview1.heading("#3", text="Population")
treeview1.heading("#4", text="Total Cases")
treeview1.heading("#5", text="Total Deaths")
treeview1.heading("#6", text="Percent Population Infected")
treeview1.pack()
treeLabel2 = tk.Label(frame,text="Statistics Of Countries Highest Total Deaths & Population Infected",
                      font=('Helvetica',14,'bold'),background="#0477BF",fg="#A6032F")
treeLabel2.pack(pady=10)
treeview2 = ttk.Treeview(frame)
treeview2['columns'] = ("Location","Date","Population","Total Cases","Total Deaths","Percent Population Infected")
treeview2.column("#0",width=0,minwidth=0)
treeview2.column("Location",anchor="center")
treeview2.column("Date",anchor="center")
treeview2.column("Population",anchor="center")
treeview2.column("Total Cases",anchor="center")
treeview2.column("Total Deaths",anchor="center")
treeview2.column("Percent Population Infected",anchor="center")
treeview2.heading("#1", text="Location")
treeview2.heading("#2", text="Date")
treeview2.heading("#3", text="Population")
treeview2.heading("#4", text="Total Cases")
treeview2.heading("#5", text="Total Deaths")
treeview2.heading("#6", text="Percent Population Infected")
treeview2.pack()
treeLabel3 = tk.Label(frame,text="Statistics Of Countries Highest Infected Count & Percent Population Infected",
                      font=('Helvetica',14,'bold'),background="#0477BF",fg="#A6032F")
treeLabel3.pack(pady=10)
treeview3 = ttk.Treeview(frame)
treeview3['columns'] = ("Location","Population","HighestCount","PercentInfected")
treeview3.column("#0",width=0,minwidth=0)
treeview3.column("Location",anchor="center")
treeview3.column("Population",anchor="center")
treeview3.column("HighestCount",anchor="center")
treeview3.column("PercentInfected",anchor="center")
treeview3.heading("#1", text="Location")
treeview3.heading("#2", text="Population")
treeview3.heading("#3", text="Highest Infection Count")
treeview3.heading("#4", text="Percent Population Infected")
treeview3.pack()
treeLabel4 = tk.Label(frame,text="Statistics Of Countries Highest Death Count & Percent Population Death",
                      font=('Helvetica',14,'bold'),background="#0477BF",fg="#A6032F")
treeLabel4.pack(pady=10)
treeview4 = ttk.Treeview(frame)
treeview4['columns'] = ("Location","Population","HighestDeathsCount","PercentPopulationDeaths")
treeview4.column("#0",width=0,minwidth=0)
treeview4.column("Location",anchor="center")
treeview4.column("Population",anchor="center")
treeview4.column("HighestDeathsCount",anchor="center")
treeview4.column("PercentPopulationDeaths",anchor="center")
treeview4.heading("#1", text="Location")
treeview4.heading("#2", text="Population")
treeview4.heading("#3", text="Highest Deaths Count")
treeview4.heading("#4", text="Percent Population Deaths")
treeview4.pack()
treeLabel5 = tk.Label(frame,text="Statistics Of Total Cases Deaths Deaths Percentage By Country",
                      font=('Helvetica',12,'bold'),background="#0477BF",fg="#A6032F")
treeLabel5.pack(pady=10)
treeview5 = ttk.Treeview(frame)
treeview5['columns'] = ("Total Cases","Total Deaths","Death Percentage")
treeview5.column("#0",width=0,minwidth=0)
treeview5.column("Total Cases",anchor="center")
treeview5.column("Total Deaths",anchor="center")
treeview5.column("Death Percentage",anchor="center")
treeview5.heading("#1", text="Total Cases")
treeview5.heading("#2", text="Total Deaths")
treeview5.heading("#3", text="Death Percentage")
treeview5.pack()
treeLabel6 = tk.Label(frame,text="Statistics Of Total Death Count By Country",
                      font=('Helvetica',10,'bold'),background="#0477BF",fg="#A6032F")
treeLabel6.pack(pady=10)
treeview6 = ttk.Treeview(frame)
treeview6['columns'] = ("Location","Total Death Count")
treeview6.column("#0",width=0,minwidth=0)
treeview6.column("Location",anchor="center")
treeview6.column("Total Death Count",anchor="center")
treeview6.heading("#1", text="Location")
treeview6.heading("#2", text="Total Death Count")
treeview6.pack()
treeLabel4 = tk.Label(frame,text="Statistics Of Total&Percent Vaccinated By Country",
                      font=('Helvetica',10,'bold'),background="#0477BF",fg="#A6032F")
treeLabel4.pack(pady=10)
treeview8 = ttk.Treeview(frame)
treeview8['columns'] = ("Total Vaccinations","Percent Of People Vaccinated")
treeview8.column("#0",width=0,minwidth=0)
treeview8.column("Total Vaccinations",anchor="center")
treeview8.column("Percent Of People Vaccinated",anchor="center")
treeview8.heading("#1", text="Total Vaccinations")
treeview8.heading("#2", text="Percent Of People Vaccinated")
treeview8.pack()
#-----------------------------------------------------------
space_Label = tk.Label(frame,text="",background="#0477BF")
space_Label.pack(pady=40)
reference_Label = tk.Label(frame,text="The Reference Of Data Is\n World Health Organization (WHO)",fg="#149AD8"
                           ,font=('Helvetica',12,'bold'),height=3)
reference_Label.pack(side="left",pady=0)
from PIL import Image,ImageTk
WHO_image =Image.open("WHOLogo.jpg").resize((120,50))
my_image = ImageTk.PhotoImage(WHO_image)
WHO_Label = tk.Label(frame,image=my_image,height=59)
WHO_Label.pack(side="left")
root.resizable(False, False)
root.mainloop()
#Display Database Data in Gui;
#--------------------------End of Project By Ahmed AL Saidi---
