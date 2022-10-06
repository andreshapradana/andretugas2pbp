 # Tugas 4
 # Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF atau Cross-Sire Request Forgery sebenarnya adalah sebuah serangan terhadap aplikasi web yang memanfaatkan bug atau vulnerability pada aplikasi web dengan mengeksploitasi suatu task dari sebuah web dengan memanfaatkan autentikasi yang dimiliki oleh user (korban). Oleh karenna itu, kegunaan csrf_token pada form adalah untuk mengamankan web kita agar tidak terjadi eksploitasi tersebut. Apabila tidak ada potongan kode tersebut, maka aplikasi web yang dibuat menjadi tidak aman.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya, kita dapat membuatnya secara manual. Secara gambaran besar, pembuatan form secara manual akan kita tulis pada halaman form masing-masing data field yang diperlukan. Lalu kita seidakan juga input pada masing-masing label data field yang sudah ditulis.

 # Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada _database_, hingga munculnya data yang telah disimpan pada _template_ HTML.
 Dari submisi dimana user menekan tombol, sistem akan membuat sebuah request ke `views.py` sehingga akan disimpan dalam database. Lalu, akan dibuat sebuah form yang dicheck dulu apakah valid dengan is_valid() sehingga dapat disimpan dengan method save(). Fungsi yang dibuat di `views.py` akan menggunakan form dan memanggil kembali redirect untuk menampilkan data yang sudah diinput. Lalu, views.py akan melakukan render data ke HTML sehingga akan muncul pada template HTML.
 
# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya. <br />
Dalam checklist ini, saya menyalakan virtual environment terlebih dahulu. Lalu saya membuat aplikasi todolist dengan perintah `python manage.py startapp todolist` di cmd.
- Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.<br />
Saya menambahkan aplikasi todolist ke settings.py di project_django. Saya menambahkan todolist di variabel INSTALLED_APPS
- Membuat sebuah model Task dengan atribut yang sesuai<br />
Setelah itu saya mengisi models.py di todolist dengan atribut user, date, title, dan description. Lalu, saya lakukan perintah `python manage.py makemigrations` dan `python manage.py migrate`
- Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.<br />
Untuk implementasi form registrasi, saya membuka views.py di folder todolist dan mengimport redirect, UserCreationForm, dan messages. Lalu saya membuat sebuah fungsi. Lalu saya menambahkan fungsi register dengan kode berikut:
```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)
```
Lalu, saya membuat folder templates yang berisi `register.html` dengan kode berikut:
```py
{% extends 'base.html' %}

{% block meta %}
<title>Registrasi Akun</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Formulir Registrasi</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
Lalu, saya menambahkan path register ke urls.py di variabel urlpatterns `path('register/', register, name='register'),`

Untuk implementasi login, saya membuka views.py di folder todolist dan mengimport authenticate dan login. Lalu, saya membuat fungsi login_user dengan parameter request. Potongan kode sebagai berikut:
```py
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
```
Lalu saya menambahkan berkas HTML baru dengan nama login.html pada folder templates. Isi dari login.html adalah sebagai berikut:
```py
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>

</div>

{% endblock content %}
```
Lalu, saya menambahkan path login ke urls.py di variabel urlpatterns `path('login/', login_user, name='login'),`
Lalu saya menerestirksi akses halaman todolist dengan mengimport `login_required` pada views dan menambahkan kode `@login_required(login_url='/todolist/login/')` di atas fungsi show_todolist.<br />
Untuk membuat fungsi logout, saya membuka views.py. Saya mengimport logout dari django.contrib.auth. Lalu saya membuat fungsi bernama `logout_user` yang menerima parameter request.
```py
def logout_user(request):
    logout(request)
    return redirect('todolist:login')
```
Lalu saya membuka berkas todolist.html dan menambahkan button logout dengan kode berikut:
```py
<button><a href="{% url 'todolist:logout' %}">Logout</a></button>
```
Lalu, saya menambahkan path logout ke urls.py di variabel urlpatterns `path('logout/', logout_user, name='logout'),`

- Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.<br />
Implementasi checklist ini adalah dengan membuat `todolist.html` di templates. Lalu, saya implementasikan kode berikut:
```py
{% extends 'base.html' %}

 {% block content %}

  <h1>Assignment 4 PBP/PBD</h1>

  <h5>Name: </h5>
  <p>{{user}}</p>

  <table>
    <tr>
      <th>Date</th>
      <th>Task Title</th>
      <th>Description</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for task in list_todolist %}
    <tr>
        <th>{{task.date}}</th>
        <th>{{task.title}}</th>
        <th>{{task.description}}</th>
    </tr>
    {% endfor %}
  </table>
  <button><a href="{% url 'todolist:create_task' %}">Create New Task</a></button>
  <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
  <h2>{{Pesan}}</h2>

 {% endblock content %}
 ```
 - Membuat halaman form untuk pembuatan task.<br />
 Untuk implementasi checklist ini, saya membuat file baru `forms.py`. Saya mengimport model form dan membuat fungsi form baru.
```py
 class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
```
Lalu saya membuat fungsi di views.py dan mengimport segala hal yang penting seperti fungsi pada forms.
```py
def create_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tast telah berhasil dibuat!')
            return redirect('todolist:show_todolist')
    
    context = {'form':form}
    return render(request, 'createtask.html', context)
```
Saya membuat file html baru di templates yaitu `createtask.html`
```py
{% extends 'base.html' %}

{% block meta %}
<title>Registrasi Akun</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>New Task</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Create Task"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

Setelah itu saya menambahkan path di urls.py di variabel urlpatterns `path('createtask/', create_task, name='create_task'),`
- Membuat routing sehingga beberapa fungsi dapat diakses<br />
saya membuat file urls.py dan menambahkan beberapa potongan kode ke urlpatterns. Potongan kode sebagai berikut:
```py
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task')
]
```
 - Melakukan deployment ke Heroku<br />
 Setelah itu, saya push perubahan kode yang saya lakukan ke github dan melakukan deployment.
 - Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku<br />
 Saya membuat dua akun yaitu andrepengguna1 dan andrepengguna2. Lalu pada masing-masing akun, saya membuat 3 data tasks seperti berikut:
![image](https://user-images.githubusercontent.com/112604705/192695542-36f6776f-d3a2-470c-b13d-5093f7d340e1.png)
![image](https://user-images.githubusercontent.com/112604705/192695590-889dbaec-f0ed-4157-89bc-cab183c64716.png)

 Link Situs Web Heroku dapat diakses dari tautan berikut: https://andretugas2pbp.herokuapp.com/todolist/

# Tugas 5
# Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline CSS adalah dimana kode diletakkan di dalam sebuah tag HTML tertentu secara langsung. Inline CSS memiliki kelebihan yaitu permintaan HTTP yang lebih kecil. Kekurangan dari Inlince CSS adalah kode harus diterapkan pada setiap elemen dalam HTML, sehingga file akan terlihat kurang rapih dan sulit dibaca. Internal CSS adalah kode yang diletakkan di dalam bagian pada sebuah halaman. Internal CSS memiliki kelebihan dimana perubahan yang dilakukan hanya akan terjadi pada 1 halaman dan menggunakan satu file html. Internal CSS memiliki kekurangan bahwa perubahan hanya terjadi pada 1 halaman dan tidak efisien. External CSS adalah kode yang menghubungkan ke file.css eksternal. Perubahan apapun yang dibuat pada file CSS akan tampil pada website. Kelebihan dari External CSS adalah ukuran file HTML menjadi lebih kecil, rapih, mudah dibaca, dan file CSS yang sama dapat digunakan untuk banyak halaman HTML. Kekurangan dari External CSS adalah halaman tidak akan tertampil secara lengkap sebelum file CSS dipanggil.
# Penjelasan tag HTML5 yang Diketahui
`<body>` = Mendefinisikan isi dokumen <br />
`<br>` = Single line break <br />
`<button>` = Membuat sebuah tombol clickable <br />
`<html>` = Mendifinisikan root sebuah dokumen HTML <br />
`<p>` = Mendefinisikan sebuah paragraf <br />
`<style>`= memberikan informasi style, biasanya dengan CSS <br />
`<table>` = Mendefinisikan tabel <br />
`<td>`, `<th>`, `<tr>` = mendefinisikan cell, header cell, dan row cell. <br />
# Penjelasan Tipe CSS Selector
Type selector memilih elemen berdasarkan nama tag. Class selector memilih elemen berdasarkan nama class yang diberikan. ID selector hanya digunakan untuk satu elemen saja. Attribute selector memilih berdasarkan atribut. Universial selector memilih semua elemen pada sebuah range tertentu.
# Implementasi Checklist
- Kustomiasi Templat HTML dengan menggunakan CSS/Bootstrap
Pada implementasi ini, saya membuat navbar dengan bootstrap. Lalu, saya menambahkan style masing-masing pada HTML sehingga dapat didesain sekreatif mungkin.
- Menambahkan card
```py
<div class= "cards">
      <p>
        <span class="textwrap"><b>Date : </b></span><br>
        <span class="textwrap">{{task.date}}</span>
        </p>
        <p>
        <span class="textwrap"><b>Title : </b></span><br>
        <span class="textwrap">{{task.title}}</span>
        </p>
        <p>
        <span class="textwrap"><b>Description : </b></span><br>
        <span class="textwrap">{{task.description}}</span>
        </p>
        <p>
        <span class="textwrap"><b>Status : </b></span><br>
        {% if task.is_finished %}
        <span class="textwrap">Selesai</span>
        {% else %}
        <span class="textwrap">Belum Selesai</span>
        {% endif %}
      </p>
          <div class = "buttoncontainer">
          <form method="POST" action="{% url 'todolist:update_data' %}">
            {% csrf_token %} 
            <input type="hidden" name="id" value="{{x.id}}"/>
            <button type="submit">Update</button>
          </form>
          <form method="POST" action="{% url 'todolist:delete_data' %}">
            {% csrf_token %} 
            <input type="hidden" name="id" value="{{x.id}}"/>
            <button type="submit">Delete</button>
          </form>
        </div>
        <br>
    </div><br>
```
- Menjadikan responsive
Menambahkan potongan kode
```py
@media (max-width: 500px) {
    .layout {
      display: inline-flex;
      flex-direction: column;
    }
  }
```
Dengan ini, kita dapat mengakses menggunakan hp.
Lalu menambahkan `<meta name="viewport" content="width=device-width, initial-scale=1.0">` ke base.html.
Lalu edit masing-masing font size dengan properti vw.
# Link HerokuApp:
https://andretugas2pbp.herokuapp.com/todolist/
