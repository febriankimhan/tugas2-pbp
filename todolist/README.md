# Link Heroku
http://tugas2-pbp-bian.herokuapp.com/todolist/

# Kegunaan `{% csrf_token %}` pada elemen `<form>`
CSRF (*Cross Site Request Forgery*) adalah salah satu ancaman keamanan pada *web* yang menyebabkan *user* melakukan sesuatu yang tidak diinginkannya. Aktivitas yang dilakukan '*user*' ini dilakukan dengan cara mengambil informasi kredensial dari akun *user* oleh penyerang dan melakukan berbagai aktivitas atas akun *user* ini. Maka, ketika kita mengisi suatu *form*, informasi yang kita masukkan bisa bocor ke tangan penyerang. Dengan menggunakan `{% csrf_token %}` pada elemen `<form>`, ancaman ini bisa dihindari.

# Apakah bisa membuat `<form>` secara manual?
Bisa. Langkah pertama yang diperlukan dalam membuat *form* secara manual adalah membuat model datanya terlebih dahulu. Lalu, kita buat *form* pada *file* HTML dengan method `POST`. Terakhir, kita buat sebuah fungsi pada `views.py` untuk mengambil data yang dimasukkan pada *form* tersebut dan menyimpannya pada *database*.

# Proses alur data pada submisi, penyimpanan, dan penampilan data
Saat pengguna memasukkan data-data yang dibutuhkan pada *form* HTML, data-data tersebut tidak akan tersimpan sampai pengguna mengklik *Submit* atau sesuatu lainnya yang menyebabkan data-data tersebut tersimpan di *database*. Menyimpan data-data tersebut ke *database* dilakukan oleh salah satu fungsi pada `views.py`. Fungsi ini akan membuat objek data baru berdasarkan model data yang ada, mengisi atribut-atributnya dengan data yang pengguna masukkan, lalu mengirimkan ke *database*. Kemudian, menampilkan data-data yang disimpan pada *database* dilakukan oleh fungsi yang lain pada `views.py`. Fungsi ini akan mengambil semua objek data yang dibutuhkan, lalu dikirimkan ke HTML untuk selanjutnya ditampilkan sesuai kebutuhan.

# Implementasi *checklist*
1. Menjalankan *virtual environment* di direktori tugas ini dan menjalankan perintah
```
python manage.py startapp todolist
```
2. - Tambahkan `"todolist",` di variable `INSTALLED_APPS` di dalam file `settings.py` yang ada pada folder `project_django`.
   - Tambahkan `path('todolist/', include('todolist.urls')),` ke dalam variabel `urlpatterns` di dalam file `urls.py` yang ada pada folder `project_django`. Dengan demikian, kita bisa mengakses link http://localhost:8000/todolist.
3. Menambahkan kode berikut pada file `models.py` yang ada di dalam folder `todolist`.
```
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length = 255)
    description = models.TextField()
```
4. - Implementasi *form* registrasi  
     - Membuat fungsi `register` pada `views.py` untuk membuat *form* menggunakan `UserCreationForm` dan menyimpan data *user*.
     - Membuat *file* HTML yang digunakan sebagai laman pengisian *form* registrasi menggunakan `UserCreationForm` yang sudah dibuat pada fungsi `register`.
   - Implementasi *form* *login*.
     - Membuat *file* HTML yang berisikan *form* untuk *login*.
     - Membuat fungsi `login_user` pada `views.py` yang digunakan untuk mengambil *username* dan *password* untuk mengecek apakah *user* terdaftar. Jika iya, *user* akan diarahkan ke laman yang dituju. Jika tidak, *user* akan diminta untuk *login* kembali. Selain itu, *cookies* pun diterapkan agar pengguna tidak perlu *login* terus-menerus setiap me-*reload* atau memuat URL lain.
     - Merestriksi 
   - Implementasi *logout*  
     Membuat fungsi `logout_user` yang akan memanggil fungsi `logout` bawaan dari `django.contrib.auth`. Fungsi ini juga menghapus `*cookies* dari pengguna yang *logout* tersebut serta membawa *user* ke halaman *login* kembali.
5. - Membuat fungsi `show_todolist` pada `views.py` yang berfungsi untuk mengambil semua data yang dibuat oleh *logged-in user* serta *username* dari *user* tersebut. Selain itu, fungsi ini akan direstriksi menggunakan `@login_required` sehingga hanya *user* yang sudah *login* yang bisa mengaksesnya. 
   - Membuat `todolist.html` yang berfungsi untuk menampilkan *username* dan *todolist* yang sudah dibuat *user* tersebut. *File* ini berisi elemen `<table>` untuk menampilkan semua *todolist* tersebut dengan rapi. Selain itu, dibuat juga tombol `Tambah Task Baru` serta tombol `Logout`. Tombol `Tambah Task Baru` akan mengarahkan kita ke `create-task.html` untuk menambahkan *task* baru, sedangkan tombol `Logout` akan menjalankan fungsi `logout_user`.
6. - Membuat `create-task.html` yang berisi elemen `<form>` dengan *method* `POST` untuk memasukkan judul dan deskripsi dari *task* yang akan dibuat.
   - Membuat fungsi `create_task` pada `views.py`. Fungsi ini akan membuat objek `Task` baru untuk menyimpan data-data yang dimasukkan *user*. Atribut `title` dan `description` dari objek tersebut diisi oleh masukkan dari *user*, sedangkan atribut `date` diisi dengan tanggal *user* mengirimkan *form* tersebut dan atribut `user` diisi dengan *username* dari *user* tersebut. Kemudian, data tersebut disimpan ke *database* dan *user* diarahkan kembali ke `todolist.html`.
7. Membuat *file* `urls.py` pada folder `todolist` yang berisikan kode berikut.
```
from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
]
```
8. Melakukan *push* ke GitHub saja karena repo yang digunakan adalah repo tugas sebelumnya yang sudah di-*setup* agar bisa melakukan *deployment* ke Heroku.
9. Berikut adalah *username* dan *password* dari dua akun yang masing-masing berisi tiga data dummy.
```
username: username1
password: dummy13579

username: username2
password: dummy24680
```