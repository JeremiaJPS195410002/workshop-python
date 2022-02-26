# **DATA STRUCTURES**

## **1. More on Lists**
Beberapa method dalam objek list: 
### a. _list.append(x)_
   Menambahkan item di akhir list.
### b. _list.extend(iterable)_
   Memperluas list dengan menambahkan semua item dari iterable. 
### c. _list.insert(i, x)_
   Menyisipkan item pada posisi tertentu. 
### d. _list.remove(x)_
   Menghapus item pertama dari list yang nilainya sama dengan _x_
### e. _list.pop([i])_
   Menghapus item pada posisi yang diberikan dalam list, dan mengembalikannya. Jika tidak ada indeks yang ditentukan, a.pop() menghapus dan mengembalikan item terakhir dalam list. 
### f. _list.clear()_
   Menghapus semua item dari list.
### g. _list.index(x[, start[, end]])_
   Mengembaikan indeks berbasis 0(nol) dalam item pertama list yang nilainya sama dengan _x_. Menampilkan _ValueError_ jika tidak ada item. 
### h. _list.count(x)_
   Mengembalikan beberapa kali nilai _x_ muncul dalam list. 
### i. _list.sort(*, key=none, reverse=False)_
   Mengurutkan item dari list di tempat(argumen dapat digunakan untuk penyesuaian sort). 
### j. _list.reserve()_
   Membalikkan elemen list di tempatnya. 
### k. _list.copy()_
   Mengembalikan salinan list yang pendek. 


**1.1 Lists as Stacks(Tumpukan)**
Method list mempermudahkan untuk menggunakan list sebagai stack(tumpukan), dimana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil. Untuk menambahkan item ke bagian atas stack, gunakan _append()_. Untuk mengambil item dari atas stack, gunakan _pop()_ tanpa explicit index. 

**1.2 Lists as Queues(Antrian)**
Sangat memungkinkan untuk menggunakan list sebagai antrian, dimana elemen pertama yang ditambah adalah elemen pertama yang diambil. Namun, list menjadi tidak efisien untuk tujuan ini. 

**1.3 List Comprehensions(Pemahaman)**
Menyediakan cara ringkas untuk membuat list. List Comprehensions terdiri dari tanda kurung yang berisi ekspresi diikuti oleh klausa _for_, lalu 0(nol) atau lebih klausa _for_ atau _if_. Hasilnya adalah list baru yang dihasilkan dari evaluasi ekspresi dalam konteks klausa _for_ dan _if_ yang mengikuti. 

**1.4 Nested Lists Comprehensions(Bersarang)**

## **2. Del Statement**
Pernyataan _del_ digunakan untuk menghapus item dari list yang diberikan indeksnya alih-alih nilainya. Berbeda dari metode _pop()_ yang mengembalikkan nilai. Pernyataan _del_ juga dapat digunakan untuk menghapus beberapa bagian dari list, atau menghapus seluruh list. Pernyataan _del_ juga bisa digunakan untuk menghapus seluruh variabel

## **3. Tuples and Sequences**
Python adalah bahasa pemrograman yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data standar lainnya seperti _tuple_. _Tuple_ terdiri dari sejumlah nilai yang dipisahkan dengan koma. 
_Tuple_ tampak mirip dengan list. Keduanya sering digunakan dalam situasi dan tujuan yang berbeda. _Tuple_ tidak dapat diubah, dan biasanya berisi urutan elemen heterogen yang diakses via _unpacked_. List bisa berubah, dan elemennya merupakan homogen dan diakses dengan mengulangi list. 

## **4. Sets(Himpunan)**
Python juga menyertakan tipe data untuk himpunan. Himpunan adalah kumpulan yang tidak berurutan tanpa elemen duplikat. 

## **5. Dictionaries**
Tipe data lain dalam Python adalah _dictionary_. _Dictionaries_ ditemukan dalam bahasa lain sebagai memori asosiatif atau array asosiatif. Tidak seperti _sequences_, yang di index oleh range angka, _dictionaries_ di indec oleh kunci, yang dapat berupa tipe apapun yang tidak dapat diubah; string dan angka selalu bisa menjadi kunci. _Tuple_ dapat digunakan sebagai kunci jika hanya berisi string, angka atau _tuple_(jika sebuah _tuple_ berisi objek yang bisa berubah baik secara langsung maupun tidak langsung, maka tidak dapat digunakan sebagai kunci). List tidak bisa digunakan sebagai kunci, karena list dapat dimodifikasi menggunakan index assignments, slice assignment aau method seperti _append()_ dan _extend()_.

## **6. Looping Techniques**
Saat melakukan looping _dictionaries_, kunci dan nilai yang sesuai dapat diambil pada waktu yang sama, dengan menggunakan method _items()_. Saat melakukan looping melalui list, index posisi dan nilai yang sesuai dapat diambil pada waktu yang sama menggunakan fungsi _enumerate()_. 
Untuk melakukan looping dari dua atau lebih sequences secara bersamaan, entries dapat dipasangkan dengan fungsi _zip()_. Untuk melakukan looping sequences secara terbalik(reverse), pertama tentukan sequences dalam arah maju dan kemudian panggil fungsi _reversed()_. 
Untuk looping sequences dalam sorted order, gunakan fungsi _sorted()_ yang mengembalikan list baru yang di sortir. 
Menggunakan _set()_ pada sequences yang menghilangkan elemen duplikat. penggunaan _sorted()_ dalam kombinasi dengan _set()_ pada list adalah cara idiomatis untuk mengulang elemen unik dari sequence yang diurutkan. 

## **7. More on Conditions**
Kondisi dalam pernyataan _while_ dan _if_ dapat berisi operator apa saja, bukan hanya perbandingan. Perbandingan(Comparisons) dapat digabungkan menggunakan _Boolean_ dan _or_ dan hasil perbandingan(ekspresi _Boolean_) dapat dinegasikan dengan _not_.

## **8. Comparing Sequences and Other Types**
Objek sequences biasanya dapat dibandingkan dengan objek lain dengan jenis sequences yang sama. Perbandingan menggunakan lexicographical ordering: dua item pertama dibandingkan, jika berbeda maka menentukan hasil perbandingan. Jika sama, maka dua item berikutnya dibandingkan, dan seterusnya sampai salah satu sequences habis. 