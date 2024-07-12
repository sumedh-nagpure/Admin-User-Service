```markdown
# Admin User Service

This repository contains a Django application for managing admin users and services for a utility company.

## Features

- **Admin User Management**: CRUD operations for admin users.
- **Service Management**: Handle service requests submitted by customers.
- **Authentication**: User authentication and authorization mechanisms.
- **Responsive UI**: Bootstrap-based responsive design for easy use on different devices.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sumedh-nagpure/Admin-User-Service.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the application at `http://localhost:8000`.
2. Use the admin panel (`http://localhost:8000/admin/`) for user and service management.
3. Use the user panel (`http://localhost:8000/signup/`)
4. Submit service requests through the customer-facing interface.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

[MIT License](LICENSE)
```
