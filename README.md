## Budgets

The application should allow for creating several users.
Each user can create a list of any number of budgets and share it with any number of users.
The budget consists of income and expenses. They are grouped into categories

## Local setup

* create .env
```shell
cp backend/.env.example backend/.env
```

* build and run all services
```shell
docker-compose up -d --build
```

* run Django migrations
```shell
docker-compose exec web python manage.py migrate
```
