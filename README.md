## Django Point of Sale (POS) 💸

A Point of Sale web app for businesses built with Python and Django for learning purposes.

<a><img src="https://user-images.githubusercontent.com/95726794/212497770-a3e241e7-0c77-4573-9d22-8f0ae813e958.png" width="70%" heigth="70%"></a>
<br></br>
<a><img src="https://user-images.githubusercontent.com/95726794/212497784-80a48617-759c-4415-aa1c-4591b9892c3d.png" width="70%" heigth="70%"></a>

## Table of Contents:
- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Run it locally](#run-it-locally)
- [Contributing](#contributing)
- [License](#license)

## Screenshots
[Click Here](screenshots/README.md)

## Features
- Login Page with User authentication
- Dashboard Page with statistics and graphs
- DataTables with print, copy, to CSV, and to PDF buttons
- Categories and Products Management
- Clients Management
- Sales Management


## Tech Stack

- Frontend: HTML, CSS, JavaScript, Boostrap, SweetAlert, DataTables
- Backend: Django, Python, Ajax, SQLite 

## Installation

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- [pip package manager](https://pip.pypa.io/en/stable/installation/)
- [git](https://git-scm.com/downloads)
  
#### Browser Compatibility Notice: Firefox NOT Supported ‼
#### Please Use Chrome or Edge Browsers ‼
    
  1. Clone or download the repository:

  ` git clone https://github.com/betofleitass/django_point_of_sale`

  2. Go to the project directory

  ` cd django_point_of_sale`

  3. Create a virtual environment :

  PowerShell:
  ```
   python -m venv venv
   venv\Scripts\Activate.ps1
  ```
  
  Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

  4. Install dependencies:  
  ` pip install -r requirements.txt`
  
  5.  Update pip and setuptools  
  ` python -m pip install --upgrade pip setuptools`  
  
  6. Install GTK to create the PDF files:  
   [Official documentation](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)
  
  7. Windows Users (IMPORTANT)‼:

     Only Windows 11 64-bit is supported ‼

     After installing GTK, you need to add it to your system's Path environment variable. Follow these steps:

      - Assuming you installed GTK at:
        `C:\Program Files\GTK3-Runtime Win64\bin`  
        This will be your new variable that you need to add to Path
        
      - Refer to this tutorial for detailed instructions on adding to the Path environment variable:
        [Tutorial add to the Path enviroment variable](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/)  
    
      - If you encounter an error such as "cannot load library," refer to this documentation for troubleshooting:
        [Missing Library Error](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#missing-library)  
  
  9. Restart your computer: After completing the steps above, it is essential to restart your computer for the changes to take effect properly. ‼
  
## Run it locally
After restarting your computer

1. Go to the project directory: `cd django_point_of_sale`

2. Activate the virtual enviroment

    PowerShell:
    ```
     venv\Scripts\Activate.ps1
    ```
    
    Linux:
    ```
    source venv/bin/activate
    ```
3. Go to the django_pos folder: `cd django_pos`

4. Make database migrations:  
  `python manage.py makemigrations` and 
  `python manage.py migrate`

5. Create superuser `python manage.py createsuperuser` 
  
   with the following data, or with the data you prefer:
   `username: admin,
    password: admin,
    email: admin@admin`

7. Run the server: `python manage.py runserver`

8. Open a browser and go to: `http://127.0.0.1:8000/`

9. Log In with your superuser credentials.
    

## Contributing

Contributions are always welcome!

- Fork this repository;

- Create a branch with your feature: `git checkout -b my-feature`;

- Commit your changes: `git commit -m "feat: my new feature"`;

- Push to your branch: `git push origin my-feature`.

## Authors

- [@betofleitass](https://www.github.com/betofleitass)

##  License

This project is under [MIT License.](https://choosealicense.com/licenses/mit/)

[Back to top ⬆️](#django-point-of-sale-pos-)
