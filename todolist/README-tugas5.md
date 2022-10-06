# Perbedaan Inline, Internal, dan External CSS
**Inline CSS:** Implementasi CSS dilakukan di dalam tag HTML.
- Kelebihan: memiliki *highest priority* yang berarti semua Inline CSS yang diterapkan pasti akan muncul.
- Kekurangan: file HTML akan menjadi sangat berantakan jika Inline CSS digunakan terlalu banyak.

**Internal CSS:** Implementasi CSS dilakukan di luar tag HTML dan di dalam file HTML.
- Kelebihan: file HTML lebih rapi dibanding dengan penggunaan Inline CSS.
- Kekurangan: file HTML menjadi lebih panjang.

**External CSS:** Implementasi CSS tidak dilakukan di dalam file HTML, melainkan di dalam file CSS.
- Kelebihan: file HTML menjadi rapi dan CSS bisa digunakan pada banyak halaman web sekaligus.
- Kekurangan: file CSS harus di-*load* terlebih dahulu sebelum bisa diterapkan pada halaman web.

# Contoh-Contoh Tag HTML5
- `<p>`: menuliskan sebuah paragraf
- `<a>`: membuat sebuah *hyperlink*
- `<h1>-<h6>`: membuat sebuah *header*
- `<form>`: membuat sebuah form untuk memasukkan input user

# Tipe-Tipe CSS Selector
- Element Selector: menggunakan tag HTML sebagai *selector* untuk penerapan CSS
- ID Selector: menggunakan ID yang ada pada atribut tag HTML sebagai *selector* untuk penerapan CSS
- Class Selector: menggunakan class yang ada pada atribut tag HTML sebagai *selector* untuk penerapan CSS

# Implementasi Checklist
1. Kustomisasi halaman web  
   - Kustomisasi *login*  
     Meletakkan form *login* pada sebuah *card* dan mengganti *style* input *field*-nya dengan *style floating* sehingga label dari setiap *field* akan mengecil dan melayang ke atas setiap user memasukkan sesuatu. *Style* tombol *login* dan warna latar belakang juga diganti.
   - Kustomisasi *register*  
     Meletakkan *form* registrasi pada sebuah *card* dan emngganti warna latar belakang.
   - Kustomisasi *create-task*  
     Membuat *navbar* yang berisi tombol *logout* dan tulisan "Todolist-ku" yang bisa mengarahkan user ke halaman utama *todolist*. Selain itu, form pembuatan task baru diletakkan pada sebuah card, menambahkan tombol untuk *Cancel* pembuatan task, mengganti *style* tombol *Submit* dan *Cancel*, serta mengganti warna latar belakang.
   - Kustomisasi halaman utama *todolist* menggunakan *cards*  
     Membuat *navbar* yang berisi tombol *logout* dan `Tambah Task Baru` serta tulisan "Todolist-ku" yang bisa mengarahkan user ke halaman utama *todolist*. Kemudian, setiap task yang dibuat akan ditampilkan dengan *cards*. Jika user tidak memiliki task, maka web akan menampilkan `Kamu tidak punya todolist, nih.`
2. Membuat keempat halaman menjadi *responsive*  
   Pada dasarnya, menggunakan Bootstrap sudah membuat halaman web menjadi *responsive*. Namun, perlu ada modifikasi tambahan agar halaman yang ditampilkan dapat benar-benar terbaca, seperti
   - Menerapkan `max-width` dalam persen pada tiap *card* agar ukurannya tidak melebihi ukuran layar *device* user.
   - Menggunakan tag `<ul>` dalam menampilkan tombol-tombol yang ada di *navbar*.