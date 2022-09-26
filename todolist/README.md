# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
Dalam checklist ini, saya menyalakan virtual environment terlebih dahulu. Lalu saya membuat aplikasi todolist dengan perintah `python manage.py startapp todolist` di cmd.
- Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
Saya menambahkan aplikasi todolist ke settings.py di project_django. Saya menambahkan todolist di variabel INSTALLED_APPS
- Membuat sebuah model Task dengan atribut yang sesuai
Setelah itu saya mengisi models.py di todolist dengan atribut user, date, title, dan description. Lalu, saya lakukan perintah `python manage.py makemigrations` dan `python manage.py migrate`
- Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
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
Lalu, saya menambahkan path register ke urls.py di variabel `urlpatterns path('register/', register, name='register'),`
