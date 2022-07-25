# Yummy Fingerfood

A simple restaurant website created with Django 4.0  
It features:

- Menu app
  - Anonymous visibility
  - Admin can add, edit or delete items
  - Each sub-Menu has its own model
  - Menu models use model-inheritance for code brevity
  - All Menu pages use one, single HTML template file
- Ordring app
  - Fully functional CRUD operations
  - Order history
  - Authenticated-Only visibility
  - Place Order based on the Menu models (ManyToMany relation)
  - User cannot view or modify other users' Orders
- API endpoints
  - Menu items
  - Account authentication (Soon)
  - Place Order (Soon)
- Accounts app
  - Custom User Model
  - Utilize Phone Number instead of username
  - Registration and Authentication
  - User Profile
- Test Cases
  - Each App has its own extensive test cases
  
The API endpoint is intended to be integrated with a front-end framework (such as React) if the need arises later on.

## Notice

The website is almost fully localized into Persian using I18N and verbose_name. This is intended for end users.  
Everything back-end was kept in English and the naming is, I believe, fairly straightforward.  
I'm planning to do an English version of the Website in future.

## Usage

Clone/download the project and install the dependencies (preferably inside a virtual environment) based on the `requirements.txt`.  
Migrations are already included, run `python manage.py migrate` to apply them.  
Create admin with `python manage.py createsuperuser` command. Then, run the server.
