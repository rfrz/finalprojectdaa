# 🧩 8-Puzzle Solver: BFS vs DFS Comparison

> **Final Project Desain & Analisis Algoritma (DAA)**

Aplikasi GUI berbasis Python ini dirancang untuk memvisualisasikan dan membandingkan performa dua algoritma pencarian klasik, **Breadth-First Search (BFS)** dan **Depth-First Search (DFS)**, dalam menyelesaikan permainan 8-Puzzle.

## 📖 Deskripsi Proyek

Proyek ini mendemonstrasikan bagaimana algoritma pencarian bekerja menyelesaikan masalah puzzle angka. Dibangun dengan antarmuka **Tkinter**, aplikasi ini memungkinkan pengguna untuk:

1.  Menentukan jumlah pengujian (*trials*).
2.  Menjalankan simulasi otomatis pada puzzle acak yang sama.
3.  Membandingkan efisiensi algoritma berdasarkan:
    * **Langkah (Cost):** Jumlah pergeseran ubin.
    * **Simpul (Nodes):** Jumlah state yang diperiksa.
    * **Waktu:** Kecepatan menemukan solusi.

## ✨ Fitur Utama

* **Antarmuka Grafis (GUI):** Visualisasi papan puzzle 3x3 yang interaktif dan mudah dipahami.
* **Perbandingan *Head-to-Head*:** BFS dan DFS diuji pada konfigurasi puzzle acak yang **sama persis** untuk keadilan data.
* **Jaminan Solusi (*Solvable*):** Algoritma pembangkit puzzle menjamin setiap puzzle yang dibuat pasti bisa diselesaikan.
* **Log & Statistik:** Menampilkan log detail per pengujian dan ringkasan rata-rata kinerja di akhir proses.

## 🛠️ Prasyarat (Requirements)

Kode ini dikembangkan menggunakan **Python 3.10**.

Library yang digunakan adalah modul bawaan Python (*Standard Library*), sehingga **tidak perlu instalasi `pip` tambahan**:
* `tkinter` (GUI)
* `collections` (Struktur data Deque)
* `random`, `time` (Utilitas)

> **Catatan untuk pengguna Linux:** Jika mengalami error `ModuleNotFoundError: No module named '_tkinter'`, silakan install paket `python3-tk` melalui terminal.

## 🚀 Cara Menjalankan

1.  **Clone Repository** (atau download zip):
    ```bash
    git clone [https://github.com/username-anda/nama-repo-anda.git](https://github.com/username-anda/nama-repo-anda.git)
    cd nama-repo-anda
    ```

2.  **Jalankan Aplikasi:**
    Buka terminal di dalam folder proyek dan ketik:
    ```bash
    python gui.py
    ```

3.  **Penggunaan:**
    * Masukkan jumlah pengujian pada kolom input (Default: 10).
    * Klik tombol **"Jalankan Perbandingan"**.
    * Tunggu proses selesai dan analisis hasilnya di kolom Log.

## 🧠 Penjelasan Algoritma

### 1. Breadth-First Search (BFS)
* **Konsep:** Mencari solusi secara melebar (*layer per layer*). Mengecek semua kemungkinan 1 langkah, lalu 2 langkah, dst.
* **Kelebihan:** Dijamin menemukan solusi **terpendek** (optimal).
* **Kekurangan:** Boros memori karena menyimpan banyak state antrian.
* **Struktur Data:** Queue (Antrian) - *First In, First Out (FIFO)*.

### 2. Depth-First Search (DFS)
* **Konsep:** Mencari solusi secara mendalam. Mencoba satu jalur terus menerus hingga mentok atau ketemu solusi, baru mundur (*backtrack*).
* **Kelebihan:** Implementasi sederhana dan hemat memori pada kasus tertentu.
* **Kekurangan:** **Tidak menjamin** solusi terpendek. Jalur solusi bisa sangat panjang dan berputar-putar.
* **Struktur Data:** Stack (Tumpukan) - *Last In, First Out (LIFO)*.

## 📂 Struktur File

| Nama File | Deskripsi |
| :--- | :--- |
| `gui.py` | **Main Program.** Menjalankan GUI Tkinter, visualisasi grid, dan mengatur loop pengujian. |
| `puzzle_solver.py` | **Logic Core.** Berisi implementasi fungsi `bfs()`, `dfs()`, `get_neighbors()`, dan class `Node`. |

---

**👨‍💻 Author**
* **Dibuat oleh:** rfrz
* *Tugas Akhir Mata Kuliah Desain & Analisis Algoritma.*
