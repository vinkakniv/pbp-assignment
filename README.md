# PBP A - Vinka Alrezky As (2206820200)

- [Assignment 2](#assignment-2)
- [Assignment 3](#assignment-3)


💡## Assignment 2 

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





📌## Assignment 3 


## Perbedaan Metode POST dan GET dalam _Form_ Django

Dalam Django _form_, perbedaan utama antara metode POST dan GET terletak pada bagaimana data dikirimkan ke server. Metode GET digunakan untuk mengambil data dari server dan data tersebut ditambahkan ke URL sebagai parameter _query_. Data ini dapat terlihat pada bar alamat browser dan biasanya digunakan untuk operasi yang bersifat non-sensitif, seperti pencarian atau penyaringan data.

Sebaliknya, metode POST digunakan untuk mengirimkan data ke server, seringkali untuk tindakan yang mengubah atau membuat data. Data yang dikirimkan melalui metode POST tidak terlihat dalam URL, sehingga lebih aman, terutama untuk informasi yang bersifat sensitif. Metode ini umumnya digunakan untuk formulir yang melibatkan informasi rahasia atau memiliki efek samping pada server, seperti mengirimkan data untuk membuat atau memperbarui catatan.


## Perbedaan Utama antara XML, JSON, dan HTML dalam Pengiriman Data

Dalam pengiriman data, XML lebih sesuai untuk konteks yang membutuhkan struktur data yang kompleks dan fleksibel dengan validasi yang ketat. JSON biasanya lebih cocok untuk pertukaran data antara aplikasi web dan server karena ringkas, mudah diproses, dan lebih efisien dalam penggunaan _bandwidth_. HTML, di sisi lain, digunakan untuk membuat tampilan halaman web dan bukan untuk pengiriman data terstruktur antara aplikasi.


## Keunggulan Penggunaan JSON dalam Pertukaran Data Aplikasi Web Modern

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena sintaksisnya yang sederhana dan mudah dibaca, efisiensinya dalam penggunaan _bandwidth_, kompatibilitas dengan berbagai bahasa pemrograman, serta fleksibilitasnya dalam merepresentasikan berbagai jenis data. Format ini juga cocok untuk pengembangan _RESTful API_, memungkinkan komunikasi yang efisien antara server dan klien dalam ekosistem web. Dengan berbagai keunggulan ini, JSON telah menjadi pilihan yang cocok utama untuk pertukaran data yang efisien dan efektif dalam dunia aplikasi web saat ini.


## Implementasi


## Postman

### HTML
![](https://imgur.com/XYtaXzU.png)
### XML
![](https://imgur.com/T56PXnw.png)
### JSON
![](https://imgur.com/lkPlJVl.png)
### XML _by_ ID
![](https://imgur.com/jq8bJml.png)
### JSON _by_ ID
![](https://imgur.com/g7dU9Iv.png)


