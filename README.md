# Cars_api
The project under the Django platform is related to a car sales company considering the maximum number of 10 billion products (cars).

Characteristics of products (cars): car name, number of cylinders, number of passengers, car color, cylinder volume, owner's name


# how to run project?
1- create virutal env
```
  pythonx -m venv .venv

```
2- activate virutal env
  ```
  source .venv/bin/activate

```
3- install dependencies 
  ```
  pipx install -r requirements.txt

```
4-  creating database 
  ```
  ./manage.py makemigrations
  ./manage.py migrate

```
# Tabels:
- User
- Car

# Tecnologies:
- rest_framework
- django_filters
- drf_yasg
- elastic search
  
