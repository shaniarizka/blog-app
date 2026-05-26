# 📰 MyBlog - Portal berita sederhana menggunakan Django Framework

Aplikasi web portal berita sederhana menggunakan Django Framework dengan sistem halaman public dan dashboard admin CRUD.

# Fitur Utama
## Halaman Public
* Landing page berita
* Detail berita
* Search berita
* Filter kategori
* Responsive UI
* Human readable time (contoh: 5 jam lalu)

## Dashboard Admin
* Login admin
* Dashboard statistik sederhana
* CRUD berita
* CRUD kategori
* Upload gambar berita

# Teknologi yang Digunakan
* Django untuk Backend Framework
* Bootstrap 5 untuk Frontend UI
* SQLite untuk Database
* Django Admin untuk Dashboard CRUD
* HTML/CSS untuk tampilan website

# Struktur Folder
blog-app/
│
├── articles/
│   ├── migrations/
│   ├── templates/
│   │   ├── public/
│   │   └── dashboard/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
├── templates/
│   └── base.html
│
├── db.sqlite3
├── manage.py
└── README.md

# Cara Install & Menjalankan
1. Clone Repository
    git clone https://github.com/shaniarizka/blog-app
2. Masuk Folder Project
    cd blog-app
3. Buat Virtual Environment
    python -m venv venv
4. Aktifkan Virtual Environment
    Windows
    venv\\Scripts\\activate
    Linux/Mac
    source venv/bin/activate
5. Install Dependency
    pip install django pillow
6. Jalankan Migration
    python manage.py migrate
7. Buat Superuser
    python manage.py createsuperuser
8. Jalankan Server
    python manage.py runserver
9. Buka Browser
    Homepage: http://127.0.0.1:8000/
    Admin: http://127.0.0.1:8000/admin

# Akun Admin
Gunakan akun superuser yang dibuat saat menjalankan:
    python manage.py createsuperuser

# Tampilan Aplikasi
## Public Page
* List berita
* Search berita
* Filter kategori
* Detail berita

## Dashboard Admin
* CRUD berita
* CRUD kategori
* Statistik sederhana

# Database
Project menggunakan SQLite database bawaan Django.

# Developer
Project dibuat untuk memenuhi tugas UAS Praktikum PPL menggunakan Django Framework.