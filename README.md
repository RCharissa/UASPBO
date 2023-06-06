Penjelasan source code:
Program tersebut merupakan contoh implementasi konsep OOP (Object-Oriented
Programming) dalam pemrograman menggunakan library Tkinter untuk membuat
aplikasi Notepad sederhana. Berikut adalah penjelasan konsep OOP yang
diterapkan dalam program tersebut:
1. Kelas:
 - Tk: Kelas utama yang mewakili jendela utama aplikasi. Digunakan untuk
membuat instance dari kelas Tkinter.
 - Menu: Kelas yang digunakan untuk membuat objek menu pada jendela utama.
 - Text: Kelas yang digunakan untuk membuat widget teks pada jendela utama.
2. Objek:
 - root: Objek dari kelas Tk yang merupakan jendela utama aplikasi.
 - menu_bar: Objek dari kelas Menu yang merupakan menu utama pada jendela
utama.
 - file_menu: Objek dari kelas Menu yang merupakan submenu "File" pada menu
utama.
 - edit_menu: Objek dari kelas Menu yang merupakan submenu "Edit" pada
menu utama.
 - text: Objek dari kelas Text yang merupakan area teks pada jendela utama.
3. Metode:
 - new_file(): Metode untuk menghapus teks dalam widget teks ketika opsi
"New" di menu "File" dipilih.
 - open_file(): Metode untuk membuka dialog pemilihan file dan membaca isi
file yang dipilih, kemudian menampilkannya pada widget teks.
- save_file(): Metode untuk menyimpan isi widget teks ke file yang sedang aktif.
Jika belum ada file yang aktif, metode ini akan memanggil save_file_as().
 - save_file_as(): Metode untuk membuka dialog pemilihan file untuk
menyimpan isi widget teks sebagai file baru.
 - cut_text(): Metode untuk memotong teks yang dipilih dalam widget teks.
 - copy_text(): Metode untuk menyalin teks yang dipilih dalam widget teks.
 - paste_text(): Metode untuk menyisipkan teks dari clipboard ke widget teks.
 - root.mainloop(): Metode untuk memulai loop utama aplikasi, menampilkan
jendela dan menangani interaksi pengguna.
4. Variabel:
 - current_file: Variabel yang digunakan untuk menyimpan path file yang sedang
aktif.
Dengan menggunakan konsep OOP, program Notepad tersebut dapat
dibuat lebih terstruktur dan modular. Setiap komponen (jendela, menu, widget)
diwakili oleh objek yang memiliki metode dan properti sendiri. Hal ini
memudahkan dalam pengelolaan dan pemeliharaan kode.


Penjelasan output code:
jelasan Output:
Kode yang diberikan akan menghasilkan jendela Notepad sederhana dengan
antarmuka pengguna. Jendela ini memiliki beberapa opsi menu seperti "File" dan
"Edit", serta area teks di mana pengguna dapat memasukkan dan mengedit teks.
Output visual yang dihasilkan adalah sebagai berikut:
1. Jendela Notepad akan terbuka dengan judul "Notepad".
2. Di bagian atas jendela, Anda akan melihat menu bar yang berisi dua menu:
"File" dan "Edit".
Gambar 2. 1 Tampilan Menu File Gambar 2. 2 Tampilan Menu Edit
7
3. Ketika menu "File" diklik, akan muncul submenu dengan opsi sebagai berikut:
"New", "Open", "Save", "Save As", dan "Exit".
4. Ketika menu "Edit" diklik, akan muncul submenu dengan opsi "Cut", "Copy",
dan "Paste".
5. Di bawah menu bar, terdapat area teks di mana pengguna dapat memasukkan
teks atau mengedit teks yang sudah ada.
6. Jendela Notepad akan tetap terbuka dan responsif terhadap interaksi pengguna.
7. Ketika opsi-opsi seperti "New", "Open", "Save", "Save As", "Exit", "Cut",
"Copy", atau "Paste" dipilih, aksi yang sesuai akan dilakukan.
Output dari kode tersebut adalah jendela Notepad yang dapat digunakan
untuk membuat, membuka, dan menyimpan file teks, serta melakukan manipulasi
teks dasar seperti memotong, menyalin, dan menempelkan. Namun, tidak ada
tampilan grafis atau isi teks awal yang ditampilkan secara khusus dalam output
kode tersebut.
