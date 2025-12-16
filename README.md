🧩 **8-Puzzle Solver: BFS vs DFS Comparison**

**Final Project Desain & Analisis Algoritma (DAA)**
Aplikasi GUI berbasis Python untuk memvisualisasikan dan membandingkan performa algoritma Breadth-First Search (BFS) dan Depth-First Search (DFS) dalam menyelesaikan permainan 8-Puzzle.

📖 **Deskripsi Proyek**

Proyek ini bertujuan untuk mendemonstrasikan bagaimana dua algoritma pencarian klasik bekerja dalam menyelesaikan masalah 8-Puzzle. Aplikasi ini dibangun menggunakan Python dengan antarmuka Tkinter.

Pengguna dapat menentukan jumlah pengujian (trials), dan aplikasi akan menjalankan simulasi untuk melihat algoritma mana yang lebih efisien dalam hal:

- Langkah (Cost): Berapa banyak pergeseran ubin yang dibutuhkan.
- Simpul (Nodes): Berapa banyak kemungkinan keadaan (state) yang diperiksa komputer.
- Waktu: Seberapa cepat komputer menemukan solusi.

**✨ Fitur Utama**

- Antarmuka Grafis (GUI): Mudah digunakan, visualisasi papan puzzle 3x3.
- Perbandingan Head-to-Head: Menjalankan BFS dan DFS pada puzzle acak yang sama persis.
- Jaminan Solusi: Puzzle yang dibangkitkan dijamin solvable (dapat diselesaikan).
- Log & Statistik: Menampilkan log detail setiap pengujian dan ringkasan rata-rata kinerja di akhir proses.

**🛠️ Prasyarat (Requirements)**

Aplikasi ini dibuat menggunakan Python 3.10. Pastikan Python sudah terinstal di komputer Anda.

Library yang digunakan adalah library bawaan Python (Standard Library), jadi tidak perlu melakukan pip install tambahan:

- tkinter (untuk GUI)
- collections (untuk struktur data Queue/Deque)
- random & time (untuk utilitas)

Catatan untuk pengguna Linux: Jika terjadi error ModuleNotFoundError: No module named '_tkinter', silakan install paket python3-tk.

**🚀 Cara Menjalankan**

Clone repositori ini (atau download file zip-nya):

git clone [https://github.com/username-anda/nama-repo-anda.git](https://github.com/username-anda/nama-repo-anda.git)
cd nama-repo-anda


Jalankan aplikasi:
Buka terminal/command prompt di dalam folder proyek, lalu ketik:

python gui.py


Penggunaan Aplikasi:

- Masukkan jumlah pengujian yang diinginkan pada kolom input (Default: 10).

- Klik tombol "Jalankan Perbandingan".

- Tunggu hingga proses selesai dan lihat hasilnya di kolom Log dan Ringkasan.

**🧠 Penjelasan Algoritma**

1. Breadth-First Search (BFS)

- Konsep: Mencari solusi melebar (layer per layer). Ia mengecek semua kemungkinan langkah 1, lalu semua kemungkinan langkah 2, dst.

- Kelebihan: Dijamin menemukan solusi terpendek (langkah paling sedikit).

- Kekurangan: Membutuhkan memori yang besar karena harus menyimpan banyak kemungkinan state di setiap level.

- Struktur Data: Menggunakan Queue (Antrian) - First In, First Out (FIFO).

2. Depth-First Search (DFS)

- Konsep: Mencari solusi mendalam. Ia akan mencoba satu jalur terus menerus sampai mentok atau ketemu solusi, baru mundur (backtrack) jika jalan buntu.

- Kelebihan: Implementasi sederhana, seringkali lebih hemat memori dibanding BFS pada kasus tertentu.

- Kekurangan: Tidak menjamin solusi terpendek. Hasil langkahnya bisa sangat panjang dan "berputar-putar".

- Struktur Data: Menggunakan Stack (Tumpukan) - Last In, First Out (LIFO).

**📂 Struktur File**

gui.py: File utama untuk menjalankan aplikasi. Berisi kode untuk antarmuka pengguna (Tkinter), visualisasi grid, dan logika pengulangan tes.

puzzle_solver.py: "Otak" dari aplikasi. Berisi:

Class Node: Representasi status papan. Dengan isi:

- Fungsi bfs() dan dfs(): Logika pencarian solusi.

- Fungsi get_neighbors(): Menentukan langkah yang valid (Atas, Bawah, Kiri, Kanan).

**👨‍💻 Author**

Dibuat oleh rfrz

Dibuat untuk memenuhi Tugas Akhir Mata Kuliah Desain & Analisis Algoritma.
