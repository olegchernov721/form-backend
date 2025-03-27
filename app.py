from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Этот маршрут будет принимать данные с твоей формы
@app.route("/api/form", methods=["POST"])
def handle_form():
    # Получаем обычные поля
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    comment = request.form.get("comment")
    checkbox = request.form.get("checkbox")

    # Получаем файл
    avatar = request.files.get("avatar")

    print("Получено:", name, email, phone, comment, checkbox)
    if avatar:
        print("Файл:", avatar.filename)

    return jsonify({
        "status": "success",
        "received": {
            "name": name,
            "email": email,
            "phone": phone,
            "comment": comment,
            "checkbox": checkbox,
            "avatar_filename": avatar.filename if avatar else "не загружен"
        }
    })

# Эта строка не нужна на Render, но пригодится при локальном запуске
if __name__ == "__main__":
    app.run(debug=True)
