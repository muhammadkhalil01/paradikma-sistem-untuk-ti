# Paradikma Sistem untuk TI

Project ini merupakan implementasi **arsitektur Monolith dan Microservices** menggunakan **Python, Flask, dan REST API**.

Project dibuat untuk mempelajari perbedaan antara sistem monolith dengan sistem yang terdiri dari beberapa service yang saling berkomunikasi melalui HTTP/REST API.

## Teknologi yang Digunakan

* **Python**
* **Flask**
* **Requests**
* **REST API**
* **HTTP / JSON**
* **Microservices Architecture**
* **Monolithic Architecture**

## Struktur Project

```text
paradikma-sistem-untuk-ti/
│
├── monolith_app.py
├── book_service.py
├── order_service.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Arsitektur Sistem

Project ini memiliki tiga aplikasi utama:

### 1. Monolith Application

File:

```text
monolith_app.py
```

Aplikasi monolith menggabungkan beberapa fungsi sistem dalam satu aplikasi.

### 2. Book Service

File:

```text
book_service.py
```

Book Service bertanggung jawab untuk menyediakan data buku melalui REST API.

Contoh endpoint:

```text
GET /books
GET /books/<id>
```

### 3. Order Service

File:

```text
order_service.py
```

Order Service digunakan untuk membuat pesanan dan berkomunikasi dengan Book Service menggunakan library `requests`.

Alur komunikasinya:

```text
Client
   │
   ▼
Order Service
   │
   │ HTTP Request
   ▼
Book Service
   │
   ▼
Data Buku
```

Order Service akan memeriksa apakah buku yang diminta tersedia pada Book Service sebelum membuat order.

## Instalasi

Pastikan sudah menginstal:

* Python 3.x
* pip
* Git

### 1. Clone Repository

```bash
git clone https://github.com/muhammadkhalil01/paradikma-sistem-untuk-ti.git
```

Masuk ke folder project:

```bash
cd paradikma-sistem-untuk-ti
```

### 2. Membuat Virtual Environment

Windows:

```bash
python -m venv venv
```

Aktifkan:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
```

Aktifkan:

```bash
source venv/bin/activate
```

### 3. Install Dependency

```bash
pip install -r requirements.txt
```

## Menjalankan Project

Karena project menggunakan beberapa service, jalankan setiap service pada terminal yang berbeda.

### Terminal 1 — Book Service

```bash
python book_service.py
```

Book Service digunakan oleh Order Service untuk mendapatkan informasi buku.

### Terminal 2 — Order Service

```bash
python order_service.py
```

Order Service akan melakukan komunikasi dengan Book Service melalui HTTP.

### Terminal 3 — Monolith

```bash
python monolith_app.py
```

Monolith Application menjalankan sistem dalam satu aplikasi.

## Komunikasi Antar-Service

Order Service menggunakan library `requests` untuk mengakses Book Service.

Konfigurasi URL Book Service terdapat pada:

```python
BOOK_SERVICE_URL = "http://localhost:5001"
```

Contoh komunikasi:

```text
Order Service
      │
      │ GET /books/<book_id>
      ▼
Book Service
      │
      │ JSON Response
      ▼
Order Service
```

## Contoh Pengujian

### Mengecek Data Buku

Gunakan browser, Postman, atau curl:

```bash
curl http://localhost:5001/books
```

### Membuat Order

Contoh request:

```http
POST /orders
Content-Type: application/json
```

Body:

```json
{
    "book_id": 1
}
```

Order Service kemudian akan memeriksa `book_id` tersebut ke Book Service.

## Perbedaan Arsitektur

### Monolith

```text
┌─────────────────────────────┐
│       Monolith App          │
│                             │
│  Book │ Order │ Business    │
│       Logic                 │
└─────────────────────────────┘
```

Seluruh fungsi berada dalam satu aplikasi.

### Microservices

```text
┌──────────────┐
│ Book Service │
└──────┬───────┘
       │
       │ REST API
       │
┌──────▼───────┐
│ Order Service│
└──────────────┘
```

Setiap service memiliki tanggung jawab yang lebih spesifik dan dapat berkomunikasi melalui REST API.

## Tujuan Pembelajaran

Project ini bertujuan untuk memahami:

1. Konsep arsitektur monolith.
2. Konsep arsitektur microservices.
3. Pembuatan REST API menggunakan Flask.
4. Komunikasi antar-service menggunakan HTTP.
5. Penggunaan library `requests`.
6. Pertukaran data menggunakan JSON.
7. Perbedaan struktur monolith dan microservices.
8. Cara menjalankan beberapa service secara terpisah.

##  Author

**Muhammad Khalil**

GitHub:

https://github.com/muhammadkhalil01

Repository:

https://github.com/muhammadkhalil01/paradikma-sistem-untuk-ti

---

## 📚 Status Project

Project ini dibuat sebagai bagian dari pembelajaran/praktikum **Paradigma Sistem untuk TI** dengan fokus pada implementasi **Monolithic Architecture dan Microservices Architecture menggunakan Flask**.
