# 🌦️ Weather App - Backend API

This is the Python/Flask backend that powers my Full-Stack Weather App.

Its job is to:
1.  Provide a custom `/api/weather` endpoint to fetch current weather.
2.  Provide a custom `/api/cities` endpoint to power the autocomplete search.

---

## 🔗 Frontend Repository

The Angular frontend that consumes this API can be found here:

**[github.com/maksymiliankoscielniak/weather-app-frontend](https://github.com/maksymiliankoscielniak/weather-app-frontend)**

---

## 🏃‍♀️ How to Run

1.  **Clone this repository:**
    ```bash
    git clone [https://github.com/maksymiliankoscielniak/python-weather-app.git](https://github.com/maksymiliankoscielniak/python-weather-app.git)
    cd python-weather-app
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # (or .\venv\Scripts\activate on Windows)
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create your `.env` file:**
    * In the root folder, create a file named `.env`.
    * Add your OpenWeatherMap API key to it:
        `API_KEY="your_secret_api_key_goes_here"`

5.  **Run the server:**
    ```bash
    python app.py
    ```
    
The server will be running on `http://localhost:5000`.
