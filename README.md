# Hotel Booking System

This is a hotel booking system built using Python Django for the backend and Next.js for the frontend.

## Features

- User authentication and authorization
- Hotel room booking and management
- Payment gateway integration
- Admin dashboard for managing bookings and users

## Installation and Setup

### Prerequisites

- Python 3.x
- Node.js
- npm or yarn
- PostgreSQL

### Backend Setup (Django)

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hotel_booking.git
   cd hotel_booking/backend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the `backend` directory and add the following environment variables:

   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/hotel_booking
   ```

5. Apply migrations and start the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### Frontend Setup (Next.js)

1. Navigate to the frontend directory:

   ```bash
   cd ../frontend
   ```

2. Install the required packages:

   ```bash
   npm install
   # or
   yarn install
   ```

3. Create a `.env.local` file in the `frontend` directory and add the following environment variables:

   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000/api
   ```

4. Start the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

## Usage

1. Open your browser and navigate to `http://localhost:3000` to access the frontend.
2. Use the admin panel at `http://localhost:8000/admin` to manage bookings and users.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
