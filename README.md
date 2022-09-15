Link Heroku: http://tugas2-pbp-bian.herokuapp.com/katalog/

1. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.**  
    ![Bagan MTV Architecture Django](https://lucid.app/documents/view/4a1a0706-12c4-47ba-9810-7ad42862a43f)

2. **Jelaskan kenapa menggunakan *virtual environment*? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?**  
    Setiap kita mengerjakan sebuah proyek, berbagai *package* ataupun *framework* akan kita gunakan untuk membantu pekerjaan kita. Tentunya, *package* dan *framework* ini rutin di-*update* demi meningkatkan kegunaannya. Terkadang, dalam *update*-*update* ini ada beberapa fungsi yang berubah ataupun hilang (yang diganti dengan fungsi yang baru). Jika proyek kita menggunakan fungsi-fungsi tersebut, maka ini bisa merusak program yang sudah kita buat pada proyek ini. Disinilah kegunaan *virtual environment*, di mana kita bisa menggunakan *package* atau *framework* tersebut tanpa khawatir terjadi perubahan di dalamnya. Namun, ini bukan berarti kita tidak bisa membuat proyek, seperti aplikasi web berbasis Django, tanpa *virtual environment*. Hanya saja, akan ada resiko yang sudah dijelaskan sebelumnya yang bisa terjadi.

3. **Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**  
    Untuk poin 1, saya membuat fungsi berikut
    ```
    def show_catalog(request):
        data_katalog = CatalogItem.objects.all()
        context = {
            'list_barang': data_katalog,
            'nama': 'Febrian Dwi Kimhan',
            'npm': '2106706691'
        }
        return render(request, "katalog.html", context)
    ```
    di mana `data_katalog` menyimpan semua objek dari *class* `CatalogItem` dan `context` menyimpan variabel-variabel yang berisi data yang sesuai yang akan digunakan pada file `html`.  
    Untuk poin 2, saya membuat kode berikut pada katalog/urls/py.
    ```
    from django.urls import path
    from katalog.views import show_catalog

    app_name = 'katalog'

    urlpatterns = [
        path('', show_catalog, name='show_catalog'),
    ]
    ```
    Selain itu, saya juga menambahkan
    ```
    path('katalog/', include('katalog.urls')),
    ```
    pada variabel `urlpatterns`. Dengan demikian, kita bisa membuka app katalog jika kita me-*request*-nya.  
    Untuk poin 3, sebelum bisa memetakan data yang ada ke file `html`, kita perlu memastikan bahwa data serta modelnya sudah siap. Karena sudah disiapkan, maka kita bisa terapkan model tersebut ke database dengan menjalankan perintah
    `python manage.py makemigrations` dan `python manage.py migrate`. Setelah itu, kita perlu memasukkan data yang ada di *file* `.json` ke dalam database dengan perintah `python manage.py loaddata initial_wishlist_data.json`.  
    Kemudian, kita bisa ubah *file* `html` agar data yang ada bisa kita tampilkan dengan sesuai. Maka, isi file `html` tersebut menjadi
    ```
    {% extends 'base.html' %}

     {% block content %}

      <h1>Lab 1 Assignment PBP/PBD</h1>

      <h5>Name: </h5>
      <p>{{nama}}</p>

      <h5>Student ID: </h5>
      <p>{{npm}}</p>

      <table>
        <tr>
          <th>Item Name</th>
          <th>Item Price</th>
          <th>Item Stock</th>
          <th>Rating</th>
          <th>Description</th>
          <th>Item URL</th>
        </tr>
        {% comment %} Add the data below this line {% endcomment %}
        {% for barang in list_barang %}
          <tr>
              <th>{{barang.item_name}}</th>
              <th>{{barang.item_price}}</th>
              <th>{{barang.item_stock}}</th>
              <th>{{barang.rating}}</th>
              <th>{{barang.description}}</th>
              <th>{{barang.item_url}}</th>
          </tr>
        {% endfor %}
      </table>

     {% endblock content %}
    ```  
    Untuk poin 4, untuk bisa melakukan `deployment` pada Heroku, maka saya perlu membuat aplikasinya terlebih dahulu. Setelah itu, saya perlu memastikan *file*-*file* pendukung untuk `deployment` ini, seperti `Procfile`, `.github/workflows/dpl.yml`, `.gitignore`, serta `settings.py` di proyek Django-nya. Setelah itu, pada `Settings -> Secrets -> Actions` di repo GitHub saya. Lalu, saya buat `repository secret` baru dan menuliskan `HEROKU_APP_NAME` di bagian NAME dan nama aplikasi saya, yaitu `tugas2-pbp-bian` di bagian VALUE. Setelah itu, saya simpan dan jalankan *workflow* yang ada. 