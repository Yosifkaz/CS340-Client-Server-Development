# CS 340 Grazioso Salvare Dashboard

This repository contains my final portfolio submission for CS 340 Client/Server Development. The project was built for the Grazioso Salvare scenario, where the goal was to create a MongoDB-backed dashboard that helps identify dogs that may be good candidates for search-and-rescue training.

The main artifacts included in this repository are my Project Two dashboard code and the Project Two README document. The dashboard uses a Python CRUD module to connect to MongoDB, retrieve animal shelter records, and display the data through an interactive dashboard with rescue-type filters, an interactive data table, a geolocation chart, and a breed distribution chart.

## Repository Contents

- `ProjectTwoDashboard.ipynb` - Final Dash dashboard notebook for Project Two
- `CRUD_Python_Module.py` - Reusable Python CRUD module for MongoDB access
- `CS340_Project_Two_README.docx` - Project Two README document with screenshots and reproduction steps
- `Grazioso Salvare Logo.png` - Logo used for dashboard branding
- `screenshots/` - Dashboard screenshots showing the required filter states

## Reflection

### How do you write programs that are maintainable, readable, and adaptable?

I write maintainable, readable, and adaptable programs by keeping the code organized, using clear names, adding comments where they help, and separating responsibilities instead of putting everything into one place. In this course, the best example of that was the CRUD Python module from Project One. Instead of writing MongoDB connection code directly inside every dashboard callback, I created a reusable `AnimalShelter` class with create, read, update, and delete methods.

The advantage of working this way was that the dashboard code in Project Two stayed cleaner and easier to understand. The dashboard handled the user interface, filters, table, and charts, while the CRUD module handled the database connection and database operations. This made the project easier to test, easier to update, and easier to reuse. In the future, I could use the same CRUD module as a starting point for other applications that need Python to connect to MongoDB, such as inventory systems, customer dashboards, reporting tools, or other database-driven web apps.

### How do you approach a problem as a computer scientist?

I approach a problem as a computer scientist by first breaking down what the client actually needs, then turning those needs into smaller technical steps. For this project, Grazioso Salvare needed a dashboard that could filter animal shelter data by rescue type and show the results in a way that was useful and easy to understand. I started by identifying the database requirements, then built the CRUD module, then connected that module to the dashboard widgets.

This project felt different from earlier assignments because it was not just about writing one script or solving one small problem. It required putting multiple pieces together: MongoDB as the database, Python as the programming language, the CRUD module as the controller logic, and Dash as the dashboard interface. In the future, I would use the same strategy for other client database projects: understand the client’s goals, design the database queries around those goals, separate the database logic from the interface, and test each part before combining everything into the final application.

### What do computer scientists do, and why does it matter?

Computer scientists solve problems by designing systems that can process information, automate work, and help people make better decisions. This matters because many organizations have large amounts of data, but the data is not useful unless it can be accessed, filtered, and understood.

For a company like Grazioso Salvare, this kind of project could make their work much easier. Instead of manually searching through thousands of animal shelter records, the dashboard lets users filter dogs by rescue category, view matching records in a table, and see location information on a map. This saves time, reduces mistakes, and helps the organization focus on finding the best dogs for rescue training. The project shows how client/server development can turn raw database records into a useful tool that supports real decisions.

## Note About Credentials

This project was created in the SNHU Codio course environment. The MongoDB credentials shown in the code are local course demonstration credentials only. In a real production deployment, credentials should be stored securely using environment variables or a secrets manager instead of being hardcoded.
