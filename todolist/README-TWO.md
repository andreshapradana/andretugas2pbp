# Tugas 6
# Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
Asynchronous programming merupakan model pemrograman yang bersifat multithread sehingga program daat berjalan secara paralel. Model ini dapat mengrimkan banyak request ke server dan meningkatkan jumlah output yang dihasilkan karena proses dapat berjalan secara bersamaan.<br />
Synchronous programming merupakan model pemrograman yang bersifat singlethread sehingga hanya dapat menjalankan satu program pada satu waktu. Model ini hanya dapat mengirimkan request satu per satu dan akan menunggu sampai request yang dikirim selesai dijalankan oleh server. Synchronous programming cenderung lebih lama dalam pelaksanaannya.
#  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Sesuai istilahnya, Event-Driven Programming adalah paradigma dimana sebuah pelaksanaan program akan tergantung oleh suatu kejadian atau event occurance. Kemunculan event akan dipantau oleh sebuah event listener yang nantinya akan memanggil event handler untuk mengeksekusi program sesuai event yang terjadi.<br />
Dalam tugas ini, penerapannya adalah saat user menekan tombol add pada modal add. Dimana handler saat event terjadi adalah pemanggilan `async function addTodolist()` agar data todolist yang diinput user akan ditambah dan disimpan ke dalam database.
# Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX akan membuat user tidak harus melakukan refresh pada webpage browser untuk update datanya. AJAX melakukan pertukaran data antara web browser dan server serta melakukan render untuk menampilkan data yang didapatkan dari server. Hal yang membedakan AJAX dengan HTTP request adalah user tidak harus menunggu agar seluruh webpage selesai loading. AJAX dapat mengakses data dari sumber eksternal meskipun webpage sudah selesai loading.
# Implementasi Checklist
- Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.<br />
```py
@login_required(login_url='/todolist/login/')
def get_todolist_json(request):
    todolist = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', todolist))
```
- Membuat file html todolist dalam Ajax.<br />
Isi file HTML ini sama dengan file todolist yang menggunakan cards. Hanya menyesuaikan data menggunakan asynchronous functions.
- Membuyat fungsi untuk mengembalikan data todolist ajax
```py
def todolist(request):
    return render(request, "todolist_ajax.html")
```
- Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.<br />
```py
    path('json/', todolist, name='todolist_ajax'),
    path('json-view/', get_todolist_json, name='get_todolist_json'),
```
- membuat tag untuk menyimpan data yang diambil dari database dengan AJAX. <br />
`<div id="ajax-cards"></div>`
- Membuat async function untuk mengambil data dari fungsi pada views dan menambahkannya ke tag yang bersesuaian, lalu melakukan refresh page secara asinychronous
```py
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>


  <script>
    async function getTodolist(){
      return fetch("{% url 'todolist:get_todolist_json' %}").then((res) => res.json())
    }

    async function refreshTodolist(){
      document.getElementById("ajax-cards").innerHTML = ""
      const todolist = await getTodolist()
      let htmlString = ``
      todolist.forEach(item=> {
        console.log(item)
        htmlString+=`\n
        <div class="cards">
          <div class="container">
            <br>
            <h4><b>Date</b></h4>
            <p>${item.fields.date}</p>
            <h4>Title</h4>
            <p>${item.fields.title}</p>
            <h4>Description</h4>
            <p>${item.fields.description}</p>
          </div> <br>
        </div> <br>
        `
      });
      document.getElementById("ajax-cards").innerHTML = htmlString
      
    }
    refreshTodolist()
  </script>
  ```
  - Membuat form modal dengan bootsrap untuk user menambahkan todolist
  ```py
  <div id="ajax-cards"></div>
  <div class = "buttoncontainer">
  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">Add task</button>
  </div>
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">New Task</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form id="form">
            {% csrf_token %} 
            <div class="mb-3">
              <label for="recipient-name" class="col-form-label">Ttile:</label>
              <input type="text" class="form-control" name="title">
            </div>
            <div class="mb-3">
              <label for="message-text" class="col-form-label">Description:</label>
              <textarea class="form-control" name="description"></textarea>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary" id="msg" data-bs-dismiss="modal">Add</button>
        </div>
      </div>
    </div>
  </div>

  </div>
  ```
  - Membuat fungsi asynchronous sebagai event handler saat button add ditekan user
  ```py
  async function addTodolist() {
    fetch("{% url 'todolist:add_todolist_item' %}", {
          method: "POST",
          body: new FormData(document.querySelector('#form'))
      }).then(refreshTodolist)
    return false
  }

  document.getElementById("msg").onclick = addTodolist
  ```
  - membuat fungsi di views untuk menyimpan data yang diinput user di database lalu menambahkan routing di urls
  ```py
  @login_required(login_url='/todolist/login/')
    def add_todolist_item(request):
        if request.method == 'POST':
            title = request.POST.get("title")
            description = request.POST.get("description")

            new_todolist = Task(title=title, description=description, user=request.user)
            new_todolist.save()

            return HttpResponse(b"CREATED", status=201)

        return HttpResponseNotFound()
    ```
    `path('add/', add_todolist_item, name='add_todolist_item'),`