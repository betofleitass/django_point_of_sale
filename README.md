## Django Point of Sale (POS) 💸

<a><img src="https://user-images.githubusercontent.com/95726794/212497770-a3e241e7-0c77-4573-9d22-8f0ae813e958.png" width="70%" heigth="70%"></a>
<br></br>
<a><img src="https://user-images.githubusercontent.com/95726794/212497784-80a48617-759c-4415-aa1c-4591b9892c3d.png" width="70%" heigth="70%"></a>

## Table of Contents:
- [Description](#description)
- [Features](#features)
- [Screenshots](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Run it locally](#run-it-locally)
- [Contributing](#contributing)
- [License](#license)

## Description

Django Point of Sale (POS)
This is a project for learning purposes

## Screenshots
[Click Here](django_point_of_sale/tree/master/screenshots/README.md)

## Features
- Login Page with User authentication
- Dashboard Page with statistics and graphs
- DataTables with print, copy, to CSV, and to PDF buttons
- Categories Management (CRUD)
- Products Management (CRUD)
- Point of Sale (POS)
  - Search and add product to list
  - Calculate automatically the subtotal, grand total, tax amount
  - Remove product from the list
  - Update Item Quantity and Recalculate Total
  - Choose sale customer
  - Sale validation paid amount and at least one product
- Sales Management
  - List all Sales
  - View Sale details
  - Print Sale Receipt


## Tech Stack

- Frontend: HTML, CSS, JavaScript, Boostrap, SweetAlert, DataTables,
- Backend: Django, Python, Ajax, SQLite, 

## Installation
    
  1. Clone or download the repository:

  ` git clone https://github.com/betofleitass/django_point_of_sale`

  2. Go to the project directory

  ` cd django_point_of_sale`

  2. Create a virtual environment :

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

  3. Install dependencies:

  ` pip install -r requirements.txt`
  
## Run it locally

1. Go to the project directory: `cd django_point_of_sale`

2. Make database migrations:  
  `python manage.py makemigrations` and 
  `python manage.py migrate`

3. Create superuser `python manage.py createsuperuser` 
  
   with the following data: `username: admin,
    password: admin,
    email: admin@admin`

4. Run the server: `python manage.py runserver`

5. Open a browser and go to: `http://127.0.0.1:8000/`

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
