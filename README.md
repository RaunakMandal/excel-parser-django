# Excel Parser using Django
This repo contans the required code for the Excel Parser application.

## What this application does?
This application is majorly to be used to parse .XLS or .XLSX files and show it in a Tabular format. As per the requirement, the we have to upload a Excel sheet like this:

After the upload is complete, the application is supposed to show an output like this:

## Additional Features
1. Drag and Drop Excel file to upload.
2. File Size/Type Checking, both in frontend and backend.
3. Sorting, Pagination, Search are implemented

## Tech Stack
- Python 3.x
- Django
- PostgreSQL
- HTML/CSS/JS

## How to Run the app
### Local
1. Make sure you have installed `python 3.x`
2. In the root directory, open a Terminal/Powershee/Command window and run `pip install -r requirements.txt`
3. Once all the dependencies are installed, run `python manage.py runserver`
4. After the server is up and running, you can go to [http://localhost:8000/products](http://localhost:8000/products)
   
### Run the Deployed App
Alternatively, you can simply head over to [https://excel-parser-django.onrender.com/products](https://excel-parser-django.onrender.com/products) to use the deployed App on Render.

## Screenshots