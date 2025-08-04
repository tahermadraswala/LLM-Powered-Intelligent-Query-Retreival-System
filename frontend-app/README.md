# Frontend Application

This is a frontend application designed to complement the existing backend application for an insurance claims processing system. The application allows users to input their insurance queries and receive responses based on the backend processing.

## Project Structure

```
frontend-app
├── public
│   └── index.html          # Main HTML file serving as the entry point
├── src
│   ├── App.tsx            # Main component of the application
│   ├── main.tsx           # Entry point for the React application
│   ├── components
│   │   └── QueryForm.tsx  # Component for user query input
│   ├── styles
│   │   └── App.css        # CSS styles for the application
├── package.json            # npm configuration file
├── tsconfig.json           # TypeScript configuration file
└── README.md               # Documentation for the project
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd frontend-app
   ```

2. **Install Dependencies**
   Make sure you have Node.js installed. Then run:
   ```bash
   npm install
   ```

3. **Run the Application**
   To start the development server, run:
   ```bash
   npm start
   ```

4. **Open in Browser**
   Navigate to `http://localhost:3000` in your web browser to view the application.

## Usage

- The application provides a form for users to input their insurance queries.
- Upon submission, the queries are sent to the backend for processing, and the responses are displayed to the user.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.