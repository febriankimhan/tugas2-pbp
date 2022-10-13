# Perbedaan *synchronous* dengan *asynchronous programming*
Pada *synchronous* programming, operasi-operasi yang ada hanya bisa dilakukan satu persatu. Selain itu, operasi-operasi tersebut harus dilakukan secara berurutan. Pada *asynchronous programming*, operasi-operasi yang ada bisa dilakukan secara bersamaan. Selain itu, operasi-operasi tersebut bisa dijalankan tanpa perlu menunggu operasi-operasi lainnya selesai dijalankan.

# Paradigma *Event-Driven Programming*
*Event-Driven Programming* adalah paradigma di mana jalannya program ditentukan oleh *event*/aksi yang dilakukan oleh user. Salah satu contohnya adalah ketika user melakukan *delete task*, *task* tersebut akan hilang dari halaman todolist.

# Penerapan *asynchronous programming* pada AJAX
Pada AJAX, data yang dimasukkan maupun diminta dari server bisa dilakukan pada latar belakang, yaitu ketika web sedang dijalankan. Selain itu, perubahan yang terjadi pada halaman web tersebut bisa dilakukan tanpa harus membuat user menunggu.

# Implementasi *checklist*
1. AJAX POST
   - Membuat fungsi baru pada `views.py` untuk mengembalikan data todolist dari user tersebut dalam bentuk JSON.
   - Menambahkan path `/todolist/json/` pada `urls.py` yang merujuk pada fungsi di atas.
   - Membuat fungsi `fetch` yang berguna untuk mengambil data-data tersebut.
2. AJAX GET
   - Membuat sebuah modal yang berisi form untuk memasukkan task baru.
   - Mengganti atribut `href` pada tombol `Tambah Task Baru` menjadi `onclick` yang merujuk ke modal di atas sehingga ketika tombol tersebut diklik, modal tersebut akan muncul.
   - Membuat fungsi baru pada `views.py` untuk menambahkan task baru ke *database*.
   - Menambahkan path `/todolist/add/` pada `urls.py` yang merujuk pada fungsi di atas.
   - Membuat fungsi `fetch` yang berguna untuk mengambil data-data pada form tersebut dan memasukannya ke *database*.
   - Menambahkan atribut `data-bs-dismiss="modal"` pada tombol submit sehingga modal bisa tertutup ketika user men-submit formnya.
   - Membuat fungsi `refreshTodolist` menggunakan AJAX GET yang akan menampilkan semua task dari user tersebut secara asinkronus.