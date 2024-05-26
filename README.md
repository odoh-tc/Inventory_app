# Inventory Management App

This is an inventory management application. This app allows users to manage their inventory efficiently, enabling them to add, update, delete, and search for products easily

## Features

- Add, update, delete, and search for products.
- View the current stock of products.
- User-friendly interface with React Bootstrap components.
- Fast and efficient API powered by FastAPI.
- Data persistence using SQLite database.
- Asynchronous ORM operations with Tortoise ORM.

## Tech Stack

- **Backend**:

  - FastAPI
  - SQLite
  - Tortoise ORM

- **Frontend**:

  - React
  - React Bootstrap
  - React Router

- **Containerization**:
  - Docker
  - Docker Compose

## Getting Started

To run the application locally, follow these steps:

1. Clone this repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd inventory-management-app`
3. Install dependencies for backend and frontend:

```sh
    cd api
    pip install -r requirements.txt
    cd ../frontend
    npm install
```

4. Start the backend and frontend services:

```sh
   docker-compose up
```

5. Access the application at [http://localhost:3000](http://localhost:3000) in your browser.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
