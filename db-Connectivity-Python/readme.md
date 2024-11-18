# MySQL Database Connection with Python and Tkinter

This project demonstrates how to connect to a MySQL database using Python and Tkinter. It provides a graphical user interface (GUI) to fetch and display data from the database, as well as add new records (cities) to it.

## Project Features

- **Fetch Data**: Retrieve data from the `Country` table in the `world` database and display it in a user-friendly format.
- **Add Data**: Add new city records to the `City` table in the database, including:
  - City name
  - Country code
  - District
  - Population

## Technologies Used

- **Python**: Programming language used to build the application.
- **Tkinter**: Library used to create the GUI (Graphical User Interface).
- **MySQL**: Database management system used to store and retrieve data.

## How to Run

### 1. Install MySQL Workbench and Set Up the Database

- **Install MySQL Server**:  
  Download and install MySQL Server on your local machine from [MySQL Downloads](https://dev.mysql.com/downloads/installer/).  
  During installation, make sure to select the `world` database as part of the default setup.

- **Add Tables and Columns**:  
  Use the provided `data.sql` file to add extra tables and columns to the `world` database. You can execute this SQL file through MySQL Workbench or any MySQL client.

### 2. Configure Database Connection in the Script

- Open the `GUI_database.py` file.  
- Update the following fields with your MySQL server credentials:
  - `host`
  - `user`
  - `password`

### 3. Install Dependencies
- **For Linux**: Open your terminal and run the following commands:

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install mysql-connector-python tk
```
- **For Windows**: Follow these steps:
  1. Install Python from [Python Downloads](https://www.python.org/downloads/) and ensure that `pip` is installed during the installation.
  2. Open the command prompt and run the following commands:
```bash
pip install tk mysql-connector-python
```
### 4. Run the Application
Once the dependencies are installed, run the Python script to start the GUI application:

```bash
python3 GUI_database.py


