from flask import Flask, request, jsonify

app = Flask(__name__)

# Этот маршрут будет принимать данные с твоей формы
@app.route("/api/form", methods=["POST"])
def handle_form():
    data = request.get_json()
    
    # Просто выводим полученные данные в терминал (для отладки)
    print("Полученные данные:", data)
    
    # Отправляем обратно на фронт
    return jsonify({
        "status": "success",
        "received": data
    })

# Эта строка не нужна на Render, но пригодится при локальном запуске
if __name__ == "__main__":
    app.run(debug=True)
