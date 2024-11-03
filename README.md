# haiku-generator

CMPSC445 Team Project - Haiku Generator

## Prerequisites

Make sure you have the following installed on your machine:

- Python (3.x)
- Node.js (14.x or higher)
- npm (Node Package Manager)

## Setup Instructions

### Backend Setup (Flask)

Create and activate a virtual environment:
```
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required Python packages:
```
pip install -r requirements.txt
```

Run the Flask app:
```
python app.py
```

The backend will be running at http://localhost:5000

### Frontend Setup (React)

```
cd frontend
npm install
npm start
```

## Accessing the Application

Once both the backend and frontend are running, you can access the application in your web browser at:

* Frontend: http://localhost:3000
* Backend API: http://localhost:5000/api/data