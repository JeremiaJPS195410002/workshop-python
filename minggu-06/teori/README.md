# Errors and Exceptions
Setidaknya, ada 2 jenis error yang dapat dibedakan, yaitu: syntax _error_ dan _exception_.

## **1. Syntax Error**
Syntax _error_, juga dikenal sebagai _parsing error_, mungkin merupakan jenis keluhan yang sering ditemui saat menggunakan _Python_.

## **2. Exceptions**
Jika suatu statement atau expression secara syntax benar, hal itu dapat menyebabkan error saat mengeksekusinya. _Error_ (kesalahan) yang terdeteksi selama eksekusi disebut exception. 

## **3.Handling Exceptions**
Memungkinkan untuk menulis program yang menangani _selected exception_. 
* Sebuah _try_ statement mungkin memiliki lebih dari 1 klausa, untuk menentukan penanganan _exception_ yang berbeda. Paling banyak hanya 1 _handler_ yang akan dieksekusi. _Handler_ hanya menangani _exception_ yang terjadi di klausa _try_ yang sesuai, bukan di _handler_ lain dari statement _try_ yang sama. Klausa **except** dapat menyebutkan beberapa _exception_ sebagai _parenthesized tuple_.

## **4. Raising Exceptions**
_Raise_ statement memungkinkan programmer untuk memaksa pengecualian (exception) tertentu terjadi. Satu-satunya argumen _raise_ menunjukkan pengecualian (exception) yang akan diajukan. Harus berupa _exception instance_ atau _exception class_. Jika _exception class_ dilewatkan, secara implisit dipanggil konstruktornya tanpa argumen. 

## **5. Exception Chaining**
Statement _raise_ memungkinkan opsional yang memungkinkan _chaining exception_. _Chaining exception_ terjadi secara otomatis ketika _exception_ dinaikkan di dalam bagian **_except_** atau **_finally_**.

## **6. User-defined Exceptions**
Program dapat memberi nama _exception_ mereka sendiri dengan membuat _exception class_ baru. _Exception class_ dapat didefinisikan melakukan apapun yang dapat dilakukan class lain, tetapi biasanya dibuat sederhana. Sebagian besar _exception_ didefinisikan dengan nama yang diakhiri dengan "_Error_". 

## **7. Defining Clean-up Actions**
Statement _try_ memiliki kalusa opsional lain yang dimaksudkan untuk mendefinisikan tindakan _clean-up_ yang harus dilakukan dalam semua keadaan. 

## **8. Predefined Clean-up Actions**
Beberapa object menentukan tindakan _clean-up_ standar yang harus dilakukan ketika object tidak lagi diperlukan. 
