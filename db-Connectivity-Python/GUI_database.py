import mysql.connector
from tkinter import *
from tkinter import messagebox

# Connect to the MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # replace with your username
        password="root",  # replace with your password
        database="world"
    )

# Function to fetch and display data
def fetch_data():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Country LIMIT 10;")
    records = cursor.fetchall()
    conn.close()

    # Clear previous data in the text area
    text_area.delete(1.0, END)

    # Format and display the data
    for row in records:
        country_code, country_name, continent, region, area, year, population, life_expectancy, gdp, gdp_per_capita, official_name, government, head_of_state, code, iso_code = row
        formatted_data = (
            f"Country Code: {country_code}\n"
            f"Country Name: {country_name}\n"
            f"Continent: {continent}\n"
            f"Region: {region}\n"
            f"Area: {area}\n"
            f"Year: {year}\n"
            f"Population: {population}\n"
            f"Life Expectancy: {life_expectancy}\n"
            f"GDP: {gdp}\n"
            f"GDP per Capita: {gdp_per_capita}\n"
            f"Official Name: {official_name}\n"
            f"Government Type: {government}\n"
            f"Head of State: {head_of_state}\n"
            f"Code: {code}\n"
            f"ISO Code: {iso_code}\n"
            f"{'=' * 40}\n"  # Separator line
        )
        text_area.insert(END, formatted_data)

# Function to add a new city
def add_city():
    city_name = city_name_entry.get()
    country_code = country_code_entry.get()
    district = district_entry.get()
    population = population_entry.get()

    if city_name and country_code and district and population:
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO City (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %s);",
                           (city_name, country_code, district, int(population)))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "City added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Create the main window
root = Tk()
root.title("Database GUI")

# Create the layout
frame = Frame(root)
frame.pack(pady=20, fill=BOTH, expand=True)

# Fetch data button with padding
fetch_button = Button(frame, text="Fetch Data", command=fetch_data)
fetch_button.grid(row=0, column=0, padx=10, pady=10)

# City entry fields with padding
Label(frame, text="City Name").grid(row=1, column=0, padx=5, pady=5)
city_name_entry = Entry(frame)
city_name_entry.grid(row=1, column=1, padx=5, pady=5)

Label(frame, text="Country Code").grid(row=2, column=0, padx=5, pady=5)
country_code_entry = Entry(frame)
country_code_entry.grid(row=2, column=1, padx=5, pady=5)

Label(frame, text="District").grid(row=3, column=0, padx=5, pady=5)
district_entry = Entry(frame)
district_entry.grid(row=3, column=1, padx=5, pady=5)

Label(frame, text="Population").grid(row=4, column=0, padx=5, pady=5)
population_entry = Entry(frame)
population_entry.grid(row=4, column=1, padx=5, pady=5)

# Add city button with padding
add_button = Button(frame, text="Add City", command=add_city)
add_button.grid(row=5, columnspan=2, pady=10)

# Text area to display fetched data with padding
text_area = Text(root, width=60, height=15)
text_area.pack(pady=20, fill=BOTH, expand=True, padx=10)

# Optional: Set some padding inside the text area by adding new lines before and after content
text_area.config(padx=10, pady=10)  # Add padding around the text inside the text area

# Set minimum size for the window
root.minsize(600, 400)

root.mainloop()
