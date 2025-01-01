from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

# Create Flask application
app = Flask(__name__)
CORS(app)  # Allow requests from external sources

# Set up database connection
def get_db_connection():
    return mysql.connector.connect(
        host="junction.proxy.rlwy.net",  # Адрес сервера базы данных на Railway
        user="root",  # Ваш пользователь
        password="OskBxFUBaYfJfETGmzOdJzwnafdvTBRw",  # MySQL password
        database="railway",  # Имя базы данных на Railway
        port=28776  # Указываем порт, который предоставлен Railway
    )

# Get all categories from the database
@app.route('/api/categories', methods=['GET'])
def get_categories():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM categories")  # Query the categories table
    categories = cursor.fetchall()

    categories_list = [
        {"id": category[0], "name": category[1], "preview_link": category[2]} for category in categories
    ]

    cursor.close()
    connection.close()

    return jsonify(categories_list)

# Get videos by category ID
@app.route('/api/videos/<int:category_id>', methods=['GET'])
def get_videos_by_category(category_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT v.id, v.name, v.preview_link, v.video_id, v.category_id, v.description, c.name as category_name
        FROM videos v
        JOIN categories c ON v.category_id = c.id
        WHERE v.category_id = %s
    """, (category_id,))
    videos = cursor.fetchall()

    videos_list = [
        {
            "id": video[0],
            "name": video[1],
            "preview_link": video[2],
            "video_id": video[3],
            "category_id": video[4],
            "description": video[5],
            "category_name": video[6],
        }
        for video in videos
    ]

    cursor.close()
    connection.close()

    return jsonify(videos_list)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
