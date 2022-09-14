Nama    : Andresha Pradana
NPM     : 2106651591

# Pertanyaan 1 : Pembuatan Bagan
Hasil bagan request client ke web aplikasi berbasis Django dan kaitannya dapat dilihat di link berikut:
GDrive https://drive.google.com/file/d/1BWqLdLqJGZpg2ei6wk2lULPj0pqmpWCj/view?usp=sharing

# Pertanyaan 2 : Penggunaan Virtual Environment
Penggunaan virtual environment dilakukan karena penggunaan ini sudah menjadi best practice saat menggunakan Django. Virtual environment digunakan untuk mengeliminasi konfik dependencies.Virtual environment akan mengisolasi package dan dependencies dari sebuah aplikasi. Oleh karena itu, saat mengerjakan sebuah aplikasi atau proyek django sebaiknya kita menggunakan virtual environment agar perubahan yang terjadi di dalam sebuah proyek tidak mempengaruhi proyek lainnya. Setiap proyek Django yang dikerjakan sebaiknya memiliki virtual environmentnya sendiri.
# Apakah kita tetap dapat menggunakan Django tanpa menggunakan virtual environment
Sesuai dengan penjelasan tentang penggunaan virtual environment, kita dapat membuat aplikasi web berbasis Django tanpa virtual environment. Namun, penggunaan virtual environment sudah menjadi best practice dan membantu saat kita mengerjakan lebih dari satu aplikasi agar tidak saling mempengaruhi satu sama lain.

# Implementasi Poin 1 - Poin 4
Sebelum itu, saya melakukan langkah-langkah yang sama seperti pada Tutorial 1 sampai load data di file json ke dalam database Django lokal. Implementasi yang saya lakukan pada poin 1 adalah dengan menambahkan fungsi routing yang sudah pernah dilakukan pada Tutorial 1 sebelumnya di urls.py. Kode yang diimplementasi adalah sebagai berikut:
"""
app_name = 'catalog'

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
]

"""
Setelah membuat membuat sebuah fungsi pada views.py, langkah berikutnya adalah dengan mengimport models yang sudah dibuat di dalam file views.py untuk pengambilan data dari database. Lalu, langkah berikutnya adalah mengimplementasikan kode untuk memanggil fungsi query dan menyimpannya. Implementasinya adalah sebagai berikut: 
"""
def show_catalog(request):
    data_catalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_catalog,
        'nama': 'Andresha Pradana', 
        'NPM' : '2106651591'
    }
    return render(request, "katalog.html", context)
"""
Langkah berikutnya adalah melakukan mapping data yang telah di render pada fungsi views dan memunculkannya di halaman HTML. Kita dapat menggunakan file katalog.html Implementasi yang saya lakukan adalah mengganti "Fill me!" dengan data yang benar seperti 
"""
....
<h5>Name: </h5>
  <p>{{nama}}</p>

  <h5>Student ID: </h5>
  <p>{{NPM}}</p>
  ....
"""
Langkah berikutnya adalah melakukan iterasi terhadap barang yang ada di list barang tergantung dengan urutan yang ada di tabel. Potongan kodenya terdapat di file katalog.html dimulai dari looping for sampai endfor.
Implementasi deployment juga saya lakukan dengan mengikuti langkah-langkah pada Tutorial 0. Dengan procfile yang sudah ada, saya langsung membuat sebuah aplikasi baru di Heroku. Saya juga menambahkan konfigurasi di settings.py project Django. Lalu, saya menyalin API KEY dan APP NAME dan menyimpannya. Data tersebut lalu ditambahkan di bagian Secrets untuk GitHub Actions dengan menambahkan pasangan Name-Value yang benar. Namenya adalah HEROKPU_APP_NAME dan HEROKU_API_KEY. Lalu valuenya adalah sesuai dengan nama variabelnya dan data yang sudah disimpan tadi. Setelah menambahkan secrets, saya run kembali all failed jobs dan melakukan deploy. Aplikasi Django dapat diakses di link https://andretugas2pbp.herokuapp.com/katalog/
