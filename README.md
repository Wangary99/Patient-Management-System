# Patient Management System

This is a simple web application created for a cloud computing assignment. The goal of the project is to build and deploy a Python-based "Patient Management System" on a free Platform as a Service (PaaS).

## 🚀 Live Demo

The application is deployed on Render and is live at the following URL:

**[https://<your-app-name>.onrender.com](https://<your-app-name>.onrender.com)**

*(Note: Please replace the link above with your actual URL from Render after deploying.)*

## 💻 Technology Stack

* **Backend:** Python
* **Web Framework:** Flask
* **Web Server:** Gunicorn
* **Platform (PaaS):** Render

## 🔧 How to Run Locally

To run this project on your own computer, follow these steps:

1.  Clone the repository:
    ```bash
    git clone [https://github.com/](https://github.com/)<your-github-username>/<your-repo-name>.git
    cd <your-repo-name>
    ```

2.  Create and activate a virtual environment:
    ```bash
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate

    # On MacOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Run the application:
    ```bash
    flask run
    ```

5.  Open your web browser and go to `http://127.0.0.1:5000` to see the app running.
