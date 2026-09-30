from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

orders = []

BOOK_SERVICE_URL = "http://localhost:5001"


@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    book_id = data.get('book_id')

    # Komunikasi antar service:
    # Tanya Book Service apakah buku ada
    try:
        response = requests.get(
            f"{BOOK_SERVICE_URL}/books/{book_id}"
        )

        if response.status_code == 200:
            book_data = response.json()

            if book_data['stock'] > 0:
                order = {
                    "id": len(orders) + 1,
                    "book_id": book_id,
                    "status": "berhasil"
                }

                orders.append(order)

                return jsonify(order), 201

        return jsonify({
            "error": "Buku tidak tersedia"
        }), 400

    except requests.exceptions.ConnectionError:
        return jsonify({
            "error": "Book Service sedang down!"
        }), 500


if __name__ == '__main__':
    # Order service berjalan di port 5002
    app.run(port=5002, debug=True)