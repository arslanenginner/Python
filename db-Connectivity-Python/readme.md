
This project demonstrates how to connect to a MySQL database using Python and Tkinter. It provides a graphical user interface (GUI) to fetch and display data from a database as well as add new records (cities) to the database.

The project performs the following tasks:

*  Fetch data from the Country table in the world database and display it in a formatted manner.
*  Add new city data to the City table in the database, including city name, country code, district, and population.

Technologies Used:
* Python:Programming language used to build the application.
* Tkinter: Used for building the GUI (Graphical User Interface).
* MySQL: Database management system used to store and retrieve data.


How to Run
1. Install MySQL Workbench and Set Up the Database
Install MySQL Workbench

Install MySQL Server and you have MySQL server installed and running on your local machine. 
During installation, make sure to select the world database as part of the default setup.

use the provided data.sql file to add extra tables and columns to the database.

2. Configure the Connection in the Script
Update Database Credentials: Open the GUI_database.py file and replace the host, user, and password fields with your MySQL server credentials.

3. Install Dependencies

* For linux:
sudo apt update
sudo apt install python3 python3-pip
pip3 install mysql-connector-python

* For windows: 
Downlaod and install python
apt install pip
pip install tk
pip install mysql-connector-python

python3 GUI_database.py

