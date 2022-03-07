# **MODULES**
Module adalah file yang berisi definisi dan statements Python. Nama file biasanya menggunakan ekstensi _.py_. Dalam sebuah Module, nama Module (sebagai string) tersedia sebagai nilai dari variabel global.

## **1. More on Modules**
Module dapat berisi statement yang dapat dieksekusi beserta definisi fungsi. Statement ini dimasudkan untuk inisiasi Module. Hanya dieksekusi saat pertama kali nama Module ditemukan dalam statement _import_. Module dapat melakukan _import_ ke Module lain. 

### **1.1 Executing Modules as Scripts**
Ketika menjalankan Python module dengan _python fibo.py <arguments>_ kode pada Module akan dieksekusi jika telah di import. 

### **1.2 The Module Search Path**
Saat Module bernama _spam_ diimport, pertama-tama interpreter mencari Module bawaan dengan nama tersebut. Jika tidak ditemukan, maka akan mencari file bernama _spam.py_ didalam direktori yang diberikan variabel _sys.path_ yang diinisialisasi dari lokasi ini:
* Direktori yang berisi input script.
* PYTHONPATH(daftar nama direktori dengan syntax yang sama dengan variabel shell PATH).
* Instalasi default.
### **1.3 Compiled Python Files**
Untuk mempercepat loading Module, Python menyimpan varsi kompilasi dari setiap Module di direktori dengan nama Module _version.pyc_. Pyhton memeriksa tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat apakah itu kadaluwarsa dan perlu dikompilasi ulang. Proses ini dilakukan secara otomatis. 

## **2. Standard Modules**
Beberapa Module dibangun dalam interpreter; ini menyediakan akses ke operasi yang bukan bagian inti dari bahasa tetaoi tetap dibangun. Kumpulan Module tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. 

## **3. The dir() Function**
Fungsi bawaan(built-in function) dir() digunakan untuk mengetahui nama yang didefinisikan oleh Module. 

## **4. Packages**
Packages adalah cara untuk menyusun namespace Module dengan menggunakan "dotted module names". 
### **4.1 Importing * from a Packages**
Pembuat package juga bisa memutuskan untuk tidak mendukung(support), jika tidak mengimport * dari package mereka.
### **4.2 Intra-package References**
Ketika package disusun menjadi sub package, dapat menggunakan absolute import untuk merujuk ke submodule atau package yang serupa.
### **4.3 Packages in Multiple Directories**
Pacakge mendukung 1 atribut khusus. Ini diinisialisasikan menjadi list yang berisi nama direktori. Meskipun fitur ini tidak sering diperlukan, fitur ini dapat digunakan untuk memperluas kumpulan modul yang ditemukan dalam sebuah package.