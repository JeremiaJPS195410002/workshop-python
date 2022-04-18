# Brief Tour of the Standard Library

## 10.1 Operating System Interface
Modul _os_ menyediakan lusinan fungsi untuk berinteraksi dengan _Operating System_. Pastikan untuk menggunakan _import os_. Hal ini akan mencegah _os.open()_ membayangi fungsi _open()_ bawaan yang beroperasi jauh berbeda. Fungsi _built-in dir()_ dan _help()_ berguna sebagai bantuan interaktif untuk bekerja dengan modul besar. Untuk tugas manajemen file dan direktori harian, modul _shutil_ menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan (_easy to use_). 

## 10.2 File Wildcards
Modul _glob_ menyediakan fungsi untuk membuat daftar file dari direktori pencarian wildcard (bisa dilihat pada file _fileWildcards_ di folder src)

## 10.3 Command Line Arguments
_Common utility scripts_ sering kali perlu memproses _command line arguments_. Argument ini disimpan dalam atribut _argv_ modul _sys_ sebagai _list_. 

## 10.4 Error Output Redirection and Program Termination
Modul _sys_ juga memiliki atribut untuk _stdin_, _stdout_, dan _stderr_. 

## 10.5 String Pattern Matching
Modul _re_ menyediakan regular expression tools untuk pemrosesan string tingkat lanjut. Untuk pencocokan dan manipulasi yang kompleks, regular expressions menawarkan solusi yang ringkas dan dioptimalkan

## 10.6 Mathematics
* Modul _math_ memberikan akses ke C library function untuk floating point math
* Modul _random_ menyediakan tools untuk membuat pilihan acak (file Mathematics folder src).
* Modul _statistics_ menghitung sifat statistik dasar dari data numerik, seperti rata-rata (mean), median, varians, dan masih banyak lagi. 

## 10.7 Internet Access
Ada sejumlah modul untuk mengakses internet dan memproses protokol internet, yang paling sederhana adalah _urllib.request_ (mengambil data dari URL) dan _smtplib_ (untuk mengirim e-mail)

## 10.8 Dates and Times
Modul _datetime_ menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara sederhana. Fokus implementasinya pada member extraction untuk pengformatan dan manipulasi output. 

## 10.9 Data Compression
Common data archiving dan compression formats secara langsunng didukung oleh modul, seperti: _zlib_, _gzip_, _bz2_, _lzma_, 
_zipfile_ dan _tarfile_

## 10.10 Performance Measurement
Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari pendekatan yang berbeda untuk masalah yang sama. Modul _timeit_ menunjukkan keunggulan kinerja sederhana: 

## 10.11 Quality Control
Modul _doctest_ menyediakan tools untuk memindai modul dan memvalidasi tes yang tertanam dalam program's docstings. Test construction sederhana memotong dan menempelkan panggilan biasa beserta hasilnya ke dalam docstring. Mpdul unittest tidak semudah modul doctest, tetapi memungkinkan serangkaian tes yang lbih komprehensif untuk dipeetahankan dalam bentuk file terpisah. 

## 10.22 Batteries Included
Pyhton memiliki filosofi batteries included. 
* Modul xmlrpc.clinet dan xmlrpc.server membuat penerapan panggilang prosedur jarak jauh menjadi tugas yang mudah. 
* Package _email_ adalah library untuk mengelola pesan email, termasuk MIME dan dokumen pesan berbasis RFC2822 lainnya. Package _email_ memiliki perangkat lengkap untuk membangun atau mengdekode struktur pesan yang kompleks dan untuk mengimplementasikan encoding internet dan protokol header. 
* Package _json_ menyediakan dukungan kuat untuk menguraikan format pertukaran data. 
* Modul sqlite3 adalah pembungkus untuk library database SQLite. 
