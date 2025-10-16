# Capstone-Project

![PET ADOPTION ERD](<Screenshot 2025-10-12 111608.png>)


User Stories:
- As a user, I want to sign up and log in.
- As a user, I want to view a list of available pets.
- As a user, I can choose pets I’m interested in adopting.
- As a user, I want to mark pets as favourites.
- As a user, I want to unamrk pets as favourites.
- As a user, I want to see my favourited pets in my profile.
- As a user, I want to submit an adoption request for a pet via a form.
- As a user, I want to see the status of my adoption requests (pending, approved, rejected).
- As a user, I want to see a list of my adopted pets.
- As a user, I want to filter pets by age, breed, or type.

Admin Stories: 
- As an admin, I want to add new pets with their information.
- As an admin, I want to edit or delete existing pets.
- As an admin, I want to view and manage user profiles.
- As an admin, I want to display all adoption requests.
- As an admin, I want to approve/decline adoption requests.


To install and run the project:
1. git clone 
2. cd capstone-project then cd petsadoption
3. pipenv install django
4. pipenv shell
(create Database)
in your terminal:
5. psql -U postgres 
enter your password then :
6. CREATE DATABASE dbname
login into pgAdmnin and check the db was created succesfully
7. change database credentials in DATABASES in (settings.py) 
8. python manage.py makemigrations
9. python manage.py migrate
10. python manage.py runserver