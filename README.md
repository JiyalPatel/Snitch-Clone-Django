# Snitch Clone Django

**Snitch Clone Django** is an e-commerce web application based on the Django framework. This project provides a robust backend with an admin panel for managing products, users, orders, and more.


## Installation

To get started with the Snitch Clone Django project, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/JiyalPatel/Snitch-Clone-Django.git
    cd snitch-clone-django
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv env
    .\env\Scripts\activate  # On Mac use `source env/bin/activate` 
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser account for the admin panel (optional):**

    ```bash
    python manage.py createsuperuser
    ```

    For demonstration purposes, the default admin username and password are set to `admin`.

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    - Open your browser and go to `http://127.0.0.1:8000/` to view the e-commerce site.
    - Access the admin panel at `http://127.0.0.1:8000/admin/` using the username `admin` and password `admin`.

