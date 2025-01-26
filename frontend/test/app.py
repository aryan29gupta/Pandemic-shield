from flask import Flask, request, render_template
import mysql.connector

# Initialize Flask app
app = Flask(__name__)

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",  # Replace with your MySQL username
    "password": "12345",  # Replace with your MySQL password
    "database": "pandemicshield_database",
}

# Route for login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get data from form
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            # Connect to the database
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Insert data into the users table
            query = "INSERT INTO login (email, password) VALUES (%s, %s)"
            cursor.execute(query, (email, password))
            connection.commit()

            return "Data stored successfully!"
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    return render_template("index2.html")


if __name__ == "__main__":
    app.run(debug=True)
