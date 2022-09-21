# Perbedaan JSON, XML, dan HTML
Json atau JavaScript Object Notation adalah sebuah format untuk menyimpan dan mentransport (Delivery) data. XML atau eXtensible Markup Languange juga merupakan format untuk menyimpan dan delivery data. HTML atau Hypertext Markup Languange adalah sebuah sistem untuk menampilkan text files, font, warna, grafik, dan hyoerlink effect dalam halaman World Wide Web.
Perbedaan JSON dan XML adalah sebagai berikut:
XML menghasilkan dokumen XML.
# Alasan memerlukan data delivery dalam pengimplementasian sebuah platform
Data delivery dalam pengimplementasian sebuah platform sangatlah penting untuk penukaran data.
# Implementasi Checklist
- Menambah suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu
Dalam checklist ini, saya menyalakan virtual environment terlebih dahulu. Lalu saya membuat aplikasi mywatchlist dengan perintah `python manage.py startapp wishlist` di cmd. 
- Menambahkan path mywatchlist sehingga dapat mengakses http://localhost:8000/mywatchlist
Saya menambahkan aplikasi mywatchlist ke settings.py di project_django. Saya menambahkan mywatchlist di variabel INSTALLED_APPS
- Membyat sebuah model MyWatchList dengan atribut yang sesuai
Setelah itu saya mengisi models.py di mywatchlist dengan atribut watched, title, rating, release_date, dan review. Lalu, saya lakukan perintah `python manage.py makemigrations` dan `python manage.py migrate`
- Menambahkan minimal 10 data untuk objek MyWatchList
Saya mengimplementasi ini dengan membuat folder bernama fixtures dan file yang bernama `initial_mywatchlist_data.json`. Isi dari file tersebut adalah data objek seperti berikut:
```py
{
        "model":"mywatchlist.mywatchlist",
        "pk":1,
        "fields":{
            "watched":"Yes",
            "title":"The Dark Knight",
            "rating": "5.0",
            "release_date":"18 July 2008",
            "review":"One of the best film i have ever watched with a very interesting character stories."
        }
    }
```
Lalu saya melakukan perintah `python manage.py loaddata initial_mywatchlist_data.json` untuk memasukkan data ke database lokal.
- Mengimplementasikan sebuah fitur untuk menyajikamn data yang telah dibuat dalam format HTML, XML, dan JSON dan membuat routing sehingga data dapat diakses dengan urlnya masing-masing
Saya mengimplementasi fitur dalam HTML dengan menambahkan fungsi pada views.py yang mengembalikan request, "mywatchlist.html", dan context yang berisi sebuah data. Lalu, saya membuat folder bernama templtes dan berkas bernama mywatchlist.html dan mengisinya dengan template web page yang sesuai sebagai berikut:
```py
{% extends 'base.html' %}

 {% block content %}

  <h1>Assignment 3 PBP/PBD</h1>

  <h5>Name: </h5>
  <p>{{nama}}</p>

  <h5>Student ID: </h5>
  <p>{{NPM}}</p>

  <table>
    <tr>
      <th>Watched</th>
      <th>Movie Title</th>
      <th>Rating</th>
      <th>Release Date</th>
      <th>Review</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for movie in list_movie %}
    <tr>
        <th>{{movie.watched}}</th>
        <th>{{movie.title}}</th>
        <th>{{movie.rating}}</th>
        <th>{{movie.release_date}}</th>
        <th>{{movie.review}}</th>
    </tr>
    {% endfor %}
  </table>

  <h2>{{Pesan}}</h2>

 {% endblock content %}
 ```
 Lalu saya membuat file urls.py dan menambahkan `path('html/', show_mywatchlist, name='show_mywatchlist'),` ke dalam urlpatterns. Lalu saya juga menambahkan `path('mywatchlist/', include('mywatchlist.urls')),` ke urls.py dalam folder project_django
Saya mengimplementasi fitur XML dengan membuat sebuah fungsi show_xml dan show_xml_by_id di views.py. Fungsi yang saya implementasikan sebagai berikut:
```py
def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Lalu, saya membuka urls.py dan mengimport semua fungsi xml yang sudah saya tulis. Lalu saya menambahkan path url ke dalam urlpatterns untuk routingnya
```py
path('xml/', show_xml, name='show_xml'),
path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
```
Saya mengimplementasi fitur json dengan membuat sebuah fungsi show_json dan show_json_by_id di views.py. Fungsi yang saya implementasikan sebagai berikut:
```py
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Lalu, saya membuka urls.py dan mengimport semua json yang sudah saya tulis. Lalu saya menambahkan path url ke dalam url patterns untuk routingnya
```py
path('json/', show_json, name='show_json'),
path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
```
- Melakukan deployment ke Heroku
Untuk deploy saya menambahkan potongan kode `release: sh -c 'python manage.py migrate && python manage.py loaddata initial_mywatchlist_data.json'. Setelah itu, saya push perubahan code yang saya tulis ke github dan melakukan deploy ke Heroku app seperti biasa. Link akses:
https://andretugas2pbp.herokuapp.com/mywatchlist/html/
https://andretugas2pbp.herokuapp.com/mywatchlist/xml/
https://andretugas2pbp.herokuapp.com/mywatchlist/json/
- Mengakses tiga URL di atas menggunakan postman
Saya melakukan ini dengan menambahkan 3 link di atas ke website postman. Berikut hasil screenshot:
- HTML
![image](https://user-images.githubusercontent.com/112604705/191491263-39e223b7-9340-4de4-9aab-c46606d15a3a.png)
- XML
![image](https://user-images.githubusercontent.com/112604705/191491533-bedaf1c6-b18c-422b-8fbb-bc4b23151841.png)
- JSON
![image](https://user-images.githubusercontent.com/112604705/191491633-e0e7291f-7fd6-4416-a377-e5f35722ae19.png)


- Menambahkan unit test pada tests.py
Saya mengimplementasikan checklist ini dengan mengikuti cara di power point week 3 dan penjelasan dosen pada kelas. Kode yang saya implementasikan adalah sebagai berikut:
```py
class AppTest(TestCase):
    def test_app_html(self):
        response = Client().get('https://andretugas2pbp.herokuapp.com/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_app_xml(self):
        response = Client().get('https://andretugas2pbp.herokuapp.com/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

    def test_app_json(self):
        response = Client().get('https://andretugas2pbp.herokuapp.com/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
```
