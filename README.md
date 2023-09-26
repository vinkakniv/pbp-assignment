# PBP A - Vinka Alrezky As (2206820200)

- [Assignment 2](#assignment-2)
- [Assignment 3](#assignment-3)
- [Assignment 4](#assignment-4)

# Assignment 2 

Deployed URL: [vendream-machine](https://vendream-machine.adaptable.app/main/)


## Implementasi

### Membuat sebuah proyek Django baru: vending_machine

Langkah pertama adalah menciptakan proyek Django baru (setelah menghubungkan repositori lokal dan GitHub). Proses ini dimulai dengan menjalankan perintah `django-admin startproject vending_machine`, dengan `vending_machine` sebagai penamaan proyek yang dipilih. Ini akan membentuk struktur dasar proyek Django, termasuk berkas-berkas dan direktori-direktori yang esensial. 

### Membuat aplikasi dengan nama `main` pada Proyek

Setelah proyek telah dibuat, langkah selanjutnya adalah membuat aplikasi di dalamnya. Untuk menciptakan aplikasi baru dengan label `main` perintah yang dapat digunakan adalah `python manage.py startapp main`. Hasilnya adalah pembentukan direktori `main` dengan semua berkas yang dibutuhkan untuk aplikasi tersebut.

### Membuat model `Item` dalam aplikasi `main`
Di dalam aplikasi `main` perlu untuk mendefinisikan model yang menggambarkan entitas yang akan disimpan dalam database. Untuk tugas ini, model bernama `Item` akan memiliki tiga atribut:
- _name_: Atribut ini digunakan untuk menampung nama item dan memiliki tipe data _CharField_.
- _amount_: Atribut ini digunakan untuk menampung jumlah item dan memiliki tipe data _IntegerField_.
- _description_: Atribut ini digunakan untuk menampung deskripsi item dan memiliki tipe data _TextField_.

### Membuat sebuah fungsi di dalam berkas `views.py` yang bertugas untuk mengambil data dari model dan mengirimkannya ke dalam sebuah halaman HTML

Dalam berkas `views.py`, dibuat sebuah fungsi bernama view `(show_main)` yang menerima parameter _request_ dari pengguna. Fungsi ini menggunakan class dari model untuk melakukan kueri ke _database_ dan hasilnya disimpan dalam variabel data_main. Setelah itu, berkas `main.html` akan di-render, dan data akan dimasukkan ke dalam konteks yang nantinya akan ditampilkan di halaman HTML.

### Mengatur rute (`routing`) agar fungsi yang telah dibuat dalam berkas `views.py` dapat diakses

Pengaturan rute ini dilakukan dengan menambahkan `path('main/', include('main.urls'))` pada berkas `urls.py` dalam proyek vending_machine. Ini akan mengarahkan rute ke berkas `urls.py` di aplikasi main. Selanjutnya, berkas `urls.py` ini akan menjalankan fungsi view `show_main` yang terdapat dalam berkas `views.py`.

### Menyematkan data yang telah diperoleh ke dalam HTML menggunakan sintaksis Django yang khusus untuk pemetaan data dalam template

Pemetaan data dalam template dilakukan ketika fungsi view dalam berkas `views.py` merender berkas main.html. Saat proses render berlangsung, data akan dihubungkan dengan sintaksis template Django, yaitu {{ data }}. Data yang ada dalam konteks akan diekstraksi dan ditampilkan di halaman HTML dengan menggunakan perulangan untuk mengambil data dari _database_ yang akan ditampilkan.

### _Deployment_ ke Adaptable dan membuat `README.md` 
Menghubungkan akun Adaptable dengan GitHub dan memilih repositori proyek vending-machine. Ikuti panduan yang disediakan oleh platform tersebut untuk memulai proses _deployment_ aplikasi. Membuat `README.md` yang berisi point-point penjelasan terkait proses implementasi dan jawaban dari pertanyaan yang diberikan.



Selama proses implementasi, saya memastikan untuk memahami setiap langkah dengan baik, menyesuaikannya dengan kebutuhan proyek, dan menangani setiap detail sesuai dengan tutorial. Dengan cara ini, proyek dapat berjalan dengan lancar dan memenuhi semua persyaratan dari checklist yang telah diberikan.


## Bagan _Request-Response_

![](https://imgur.com/xUm0O9X.png)

Ketika _user_ mengajukan permintaan untuk mengakses aplikasi, berkas `urls.py` akan mengarahkan permintaan ke _view function_ yang sesuai di berkas `views.py`. Di sini, berkas `views.py` bertanggung jawab untuk mengakses dan memanipulasi data dalam _database_ melalui `models.py`. Fungsi ini dapat melakukan berbagai operasi pada data seperti menambahkan, memperbarui, mengambil, atau menghapus data, sesuai dengan jenis permintaan yang diterimanya.

Setelah data diproses di dalam `views.py`, langkah selanjutnya adalah menampilkannya kepada _user_. Ini dilakukan dengan cara me-_render_ atau memasukkan data ke dalam berkas HTML yang berfungsi sebagai _template_. Dalam berkas HTML tersebut, terdapat sintaksis yang akan digantikan sesuai dengan parameter yang diberikan oleh `views.py`. Hasilnya, halaman HTML akan ditampilkan kepada pengguna sebagai respons akhir dari permintaan yang telah diajukan.


## _Virtual Environment_

_Virtual environment_ berfungsi untuk mengisolasi dependensi dalam proyek Django, memungkinkan proyek untuk memiliki dependensi yang berbeda tanpa saling mengganggu. Ini memberikan fleksibilitas kepada pengembang untuk menghindari konflik antara versi dependensi yang berbeda. Meskipun teoretisnya mungkin untuk membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_, sebaiknya hal ini dihindari karena dapat menimbulkan masalah akibat tumpang tindihnya dependensi. Aplikasi bisa berjalan tanpa _virtual environment_ jika versi dari dependensi yang sudah terpasang di _global environment_ mendukung menjalankan aplikasi Django yang sedang dikembangkan.


## MVC, MVT, MVVM

MVC (_Model-View-Controller_), MVT (_Model-View-Template_), dan MVVM (_Model-View-ViewModel_) adalah tiga jenis arsitektur pengembangan perangkat lunak.

- MVC memisahkan aplikasi menjadi _Model_ (data dan logika), _View_ (tampilan pengguna), dan _Controller_ (pengendali interaksi).
- MVT adalah varian yang digunakan dalam Django, dengan Model yang mirip dengan MVC, _View_ sebagai antarmuka pengguna, dan _Template_ yang mengatur tampilan HTML.
- MVVM digunakan dalam aplikasi berbasis klien modern dan memisahkan _Model_ (data dan logika), _View_ (tampilan), dan _ViewModel_ (logika tampilan dan interaksi).

Perbedaan utama adalah penggunaan konteks aplikasi dan bagaimana tampilan dan logika dipisahkan, dengan MVC dan MVT lebih umum digunakan dalam aplikasi web tradisional, sedangkan MVVM digunakan dalam aplikasi berbasis klien modern.





# Assignment 3 

## Perbedaan Metode POST dan GET dalam _Form_ Django

Dalam Django _form_, perbedaan utama antara metode POST dan GET terletak pada bagaimana data dikirimkan ke server. Metode GET digunakan untuk mengambil data dari server dan data tersebut ditambahkan ke URL sebagai parameter _query_. Data ini dapat terlihat pada bar alamat browser dan biasanya digunakan untuk operasi yang bersifat non-sensitif, seperti pencarian atau penyaringan data.

Sebaliknya, metode POST digunakan untuk mengirimkan data ke server, seringkali untuk tindakan yang mengubah atau membuat data. Data yang dikirimkan melalui metode POST tidak terlihat dalam URL, sehingga lebih aman, terutama untuk informasi yang bersifat sensitif. Metode ini umumnya digunakan untuk formulir yang melibatkan informasi rahasia atau memiliki efek samping pada server, seperti mengirimkan data untuk membuat atau memperbarui catatan.


## Perbedaan Utama antara XML, JSON, dan HTML dalam Pengiriman Data

Dalam pengiriman data, XML lebih sesuai untuk konteks yang membutuhkan struktur data yang kompleks dan fleksibel dengan validasi yang ketat. JSON biasanya lebih cocok untuk pertukaran data antara aplikasi web dan server karena ringkas, mudah diproses, dan lebih efisien dalam penggunaan _bandwidth_. HTML, di sisi lain, digunakan untuk membuat tampilan halaman web dan bukan untuk pengiriman data terstruktur antara aplikasi.


## Keunggulan Penggunaan JSON dalam Pertukaran Data Aplikasi Web Modern

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena sintaksisnya yang sederhana dan mudah dibaca, efisiensinya dalam penggunaan _bandwidth_, kompatibilitas dengan berbagai bahasa pemrograman, serta fleksibilitasnya dalam merepresentasikan berbagai jenis data. Format ini juga cocok untuk pengembangan _RESTful API_, memungkinkan komunikasi yang efisien antara server dan klien dalam ekosistem web. Dengan berbagai keunggulan ini, JSON telah menjadi pilihan yang cocok utama untuk pertukaran data yang efisien dan efektif dalam dunia aplikasi web saat ini.


## Implementasi

#### Langkah 1: Membuat Input Form

Membuat Direktori Templates: Pertama, saya membuat direktori `templates` di dalam direktori utama proyek saya. Tujuannya adalah untuk menyimpan template HTML yang akan digunakan dalam aplikasi.

Membuat Template Dasar `base.html`: Di dalam direktori `templates`, saya membuat berkas `base.html` sebagai template dasar. Template ini akan digunakan sebagai kerangka untuk semua halaman web dalam proyek.

Membuat Berkas `forms.py`: Selanjutnya, saya membuat berkas `forms.py` di dalam aplikasi `main`. Di dalam berkas ini, saya mendefinisikan form Django yang disebut `ItemForm` agar pengguna dapat mengisi data objek model `Item`. Saya juga menambahkan fitur _category_ dan _price_ agar dapat disesuaikan dengan kebutuhan. Selain itu, saya memodifikasi berkas `models.py` untuk menyesuaikan perubahan ini.

Template untuk Input Data `create_item.html`: Kemudian, saya membuat berkas `create_item.html` di dalam direktori `templates`. Template ini digunakan untuk menampilkan form input data `Item`. Saya menggunakan `ItemForm` yang telah saya definisikan sebelumnya dalam template ini. Pengguna dapat mengisi data objek `Item` melalui form ini.

Membuat View `create_item`: Saya juga membuat view `create_item` di dalam berkas `views.py`. View ini bertugas menangani permintaan POST yang diterima dari form input. Saya menggunakan `ItemForm` untuk memvalidasi data yang dikirimkan melalui form dan menyimpannya ke database jika data tersebut valid.

#### Langkah 2: Menambahkan 5 Fungsi Views

Saya menambahkan 5 fungsi views dalam aplikasi `main` untuk menampilkan data `Item` dalam format yang berbeda, yaitu:

- `show_main`: Menampilkan data `Item` dalam format HTML.
- `show_xml`: Menampilkan data `Item` dalam format XML.
- `show_json`: Menampilkan data `Item` dalam format JSON.
- `show_xml_by_id`: Menampilkan data `Item` berdasarkan ID dalam format XML.
- `show_json_by_id`: Menampilkan data `Item` berdasarkan ID dalam format JSON. 

#### Langkah 3: Membuat Routing URL

Untuk menghubungkan setiap view dengan URL yang sesuai, saya melakukan konfigurasi routing URL di berkas "urls.py" dalam aplikasi `main`, yang sesuai dengan panduan tutorial yang ada. 

- `path('xml/', show_xml, name='show_xml')`,
- `path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id')`,
- `path('json/', show_json, name='show_json')`,
- `path('json/<int:id>/', show_json_by_id, name='show_json_by_id')`

Langkah terakhir, saya melakukan push berkas-berkas ke GitHub.


## Postman

### HTML
![](https://imgur.com/XYtaXzU.png)
### XML
![](https://imgur.com/T56PXnw.png)
### JSON
![](https://imgur.com/lkPlJVl.png)
### XML _by_ ID
![](https://i.imgur.com/RH78gEA.png)
### JSON _by_ ID
![](https://imgur.com/OAyUwMi.png)




# Assignment 4


## Django `UserCreationForm`

`UserCreationForm` adalah salah satu fitur bawaan yang disediakan oleh kelas ModelForm dalam Django, digunakan untuk membuat _form_ pembuatan pengguna baru yang dapat diintegrasikan ke dalam aplikasi web. _Form_ ini terdiri dari tiga bidang utama: _username_, _password_, dan _password confirmation_, yang berguna untuk mengonfirmasi kata sandi. `UserCreationForm` dapat diimport dari modul `django.contrib.auth.forms` untuk memanfaatkan fungsionalitasnya. Salah satu keunggulan utamanya adalah kemudahan penggunaan dan integrasi yang baik dengan sistem otentikasi Django. Form ini juga dapat disesuaikan sesuai dengan kebutuhan aplikasi, namun memiliki beberapa keterbatasan, seperti tidak mendukung fitur-fitur tambahan secara langsung dan tampilan baku yang mungkin perlu disesuaikan. 


## Autentikasi dan Otorisasi dalam Konteks Django

Autentikasi dalam Django adalah proses untuk memverifikasi identitas pengguna yang mencoba masuk ke dalam aplikasi web. Autentikasi dilakukan dengan memasukkan informasi seperti _username_ dan kata sandi yang benar. Tujuannya adalah memastikan bahwa hanya pengguna yang memiliki hak akses yang benar yang dapat masuk ke dalam akun dan menjaga keamanan informasi pribadi. Otorisasi, di sisi lain, adalah tentang menentukan apa yang diperbolehkan atau tidak diperbolehkan oleh pengguna setelah berhasil melakukan autentikasi

Autentikasi dan otorisasi sangat penting dalam menjaga keamanan dan privasi data pengguna dalam aplikasi web. Autentikasi memastikan hanya pengguna sah yang bisa mengakses akun, sementara otorisasi mengendalikan hak akses untuk mencegah akses yang tidak sah dan memastikan pengguna hanya bisa melakukan tindakan sesuai izin. Kombinasi keduanya adalah kunci utama dalam menjaga keamanan aplikasi web dan melindungi pengguna dari risiko keamanan.


## _Cookies_ dalam Konteks Aplikasi Web

_Cookies_ dalam konteks aplikasi web adalah sejumlah kecil data yang disimpan di _browser user_ ketika mereka berinteraksi dengan sebuah situs web. Fungsinya adalah untuk menyimpan informasi yang dapat diakses oleh server web ketika _user_ kembali ke situs tersebut.

Django menggunakan _cookies_ untuk mengelola data sesi _user_ melalui modul `django.contrib.sessions.middleware.SessionMiddleware`. Prosesnya dimulai saat _user_ mengunjungi situs web Django, di mana server web menghasilkan sebuah _session cookie_ dengan ID unik. _Cookie_ ini kemudian dikirim ke _browser user_, dan _browser_ akan menyimpannya. Setiap kali _user__ mengirim permintaan ke server, _session cookie_ akan disertakan dalam permintaan tersebut, yang memungkinkan server untuk mengidentifikasi _user_ dan mengambil data sesi yang sesuai. 


## Penggunaan _Cookies_

Penggunaan _cookies_ dalam pengembangan web memiliki sejumlah risiko potensial yang perlu diwaspadai. Secara default, keamanan _cookies_ tidak terjamin atau terancam, namun risikonya sangat tergantung pada bagaimana penggunaan _cookies_ diimplementasikan dan jenis informasi yang disimpan dalamnya. Salah satu risiko utama adalah potensi kebocoran data sensitif jika cookies tersebut tidak dienkripsi dengan baik.


## Implementasi

### Langkah 1: Mengimplementasikan Fungsi Registrasi, Login, dan Logout:

Pertama, saya membuat tiga fungsi baru dalam `views.py`:

Fungsi Registrasi (`register`):
    Fungsi `register` bertujuan untuk memungkinkan pengguna untuk membuat akun baru. Saya menggunakan `UserCreationForm` yang telah disediakan oleh Django untuk menangani proses pembuatan akun. Fungsi ini mengelola POST request, melakukan validasi form, dan menyimpan data pengguna jika form valid. Setelah berhasil, pesan sukses ditampilkan kepada pengguna, dan pengguna diarahkan ke halaman login.

Fungsi Login (`login_user`):
    Fungsi `login_user` mengurus proses login. Saya menggunakan fungsi authenticate dan login yang diimpor dari Django untuk mengautentikasi pengguna dan melakukan login jika autentikasi berhasil. Jika login gagal, pesan kesalahan ditampilkan kepada pengguna.

Fungsi Logout (`logout_user`):
    Fungsi `logout_user` mengelola proses logout. Ketika pengguna logout, sesi pengguna dihapus, dan pengguna diarahkan kembali ke halaman login.

### Langkah 2: Membuat Tampilan untuk Registrasi dan Login:

Selanjutnya, saya membuat berkas `register.html` dan `login.html` dalam folder templates untuk tampilan registrasi dan login. Dalam tampilan ini, pengguna dapat mengisi formulir dengan informasi yang diperlukan.
Selain itu, saya menambahkan tombol logout ke dalam berkas `main.html` agar pengguna yang telah login dapat logout dengan mudah.

### Langkah 3: Menghubungkan Fungsi ke URL:

Kemudian, saya menghubungkan setiap fungsi registrasi, login, dan logout ke URL yang sesuai dalam berkas `urls.py`. Hal ini memastikan bahwa pengguna dapat mengakses halaman tersebut melalui URL yang ditentukan.

### Langkah 4: Autentikasi Akses ke Halaman Main:

Saya juga melakukan autentikasi akses ke halaman Main agar hanya dapat diakses setelah login. Ini dilakukan dengan menambahkan kode `@login_required(login_url='/login')` di atas fungsi `show_main` dalam `views.py`. Pengguna yang belum login akan diarahkan ke halaman login terlebih dahulu.

### Langkah 5: Membuat Dua Akun Pengguna dan Menambahkan Data Dummy:

Saya membuat dua akun pengguna dengan _username_ dan _password_ berikut:

Akun 1:
- _username_: lidwina.jv
-  _password_: pbptest02

Akun 2:
- _username_: caressa.py
- _password_: pbptest01

Saya juga mengisi beberapa data _dummy_ ke dalam aplikasi menggunakan kedua akun tersebut.

### Langkah 6: Menghubungkan Model Item dengan User:

Untuk menghubungkan model Item dengan User, saya melakukan langkah-langkah berikut:

- Mengimport modul User dari `django.contrib.auth.models`.
- Menambahkan _field user_ ke dalam model Item menggunakan `ForeignKey`. Hal ini untuk mengaitkan setiap item dengan pengguna yang membuatnya.
- Mengedit fungsi `create_item` agar Django tidak langsung menyimpan objek yang dibuat ke _database_. Ini memungkinkan untuk mengisi _field user_ dengan objek User yang sedang login sebelum menyimpannya ke _database_.
- Mengubah fungsi `show_main` untuk menampilkan `name` yang merupakan _username_ pengguna yang sedang login.

### Langkah 7: Menampilkan Detail Informasi _User_ yang Sedang Login dan Menggunakan _Cookies_:

Saya mengimport modul `datetime` dan menambahkan fungsi baru dalam `login_user` yang dapat menambahkan `cookie`. `Cookies` ini digunakan untuk menyimpan informasi terkait waktu login terakhir pengguna. Informasi ini ditampilkan di halaman utama dalam elemen HTML dengan teks `"Sesi terakhir login"`. Saya juga mengubah fungsi `logout_user` untuk menghapus _cookie_ setiap kali pengguna logout.

