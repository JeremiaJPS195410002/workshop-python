# Input dan Output
Terdapat beberapa cara untuk menamplikan output dari suatu program

## **1. Fancier Output Formatting**
Ada 2 cara untuk menulis values: expression statement dan fungsi _print()_. Ada cara lain yaitu menggunakan method _write()_ dalam file objek. Ketika ingin menggunakan tampilan cepat, anda dapat mengonversi nilai apapun menjadi string dengan menggunakan fungsi _repr()_ atau _str()_
* Fungsi _str()_ untuk mengembalikan repesentasi nilai yang fairly human-readable
* Fungsi _repr()_ untuk menghasilkan representasi yang dapat dibaca oleh interpreter

### **1.1 Formatted String Literals**
Disingkat _f-string_, memungkinkan anda memasukkan nilai ekspresi Python dalam string dengan mengawali menggunakan _f_ atau _F_ dan menulis ekspresi sebagai {expression}. 

### **1.2 The String _format()_ Method**

### **1.3 Manual String Formatting**
Metode _str.just()_ dalam objek string membenarkan string di bidang dengan lebar tertentu dengan mengisinya dengan spasi di sebelah kiri. 

## **2. Reading and Writing Files**
_open()_ mengembalikan objek file, dan paling sering menggunakan 2 argument: _open(filename, mode)_. Biasanya file dibuka dalam mode teks,, artinya anda membaca dan menulis string dari dan menuju ke file. Mode ini harus digunakan untuk semua file yang tidak berisi teks. 

### **2.1 Method of File Objects**
Untuk membaca file content, panggil dengan _f.read(size)_, yang membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). _size_ adalah argumen numerik opsional. Ketika _size_ dihilangkan atau negatif, seluruh isi file akan dibaca dan dikembalikan.

### **2.2 Saving Structured Data with JSON**
String dapat dengan mudah ditulis dan dibaca dari sebuah file. Pyhton memungkinkan anda untuk menggunakan format pertukaran data yang disebut JSON(_JavaScript Object Nation_)