import tkinter as tk
from tkinter import font, scrolledtext

import time
import random

from puzzle_solver import bfs, dfs, get_neighbors

BG_COLOR = "#f0f0f0"
GRID_COLOR = "#a3a3a3"
TILE_COLOR = "#ffffff"
FONT_STYLE = ("Helvetica", 24, "bold")
BUTTON_FONT = ("Helvetica", 12)
RESULT_FONT = ("Courier", 10)

GOAL_STATE = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)


def generate_solvable_puzzle(shuffles=100):
    state = GOAL_STATE
    for _ in range(shuffles):
        neighbors = get_neighbors(state)
        random_choice = random.choice(neighbors)
        state = random_choice[0]
    return state


class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle Solver: Perbandingan BFS vs DFS")
        self.root.configure(bg=BG_COLOR)
        self.root.geometry("500x700")

        self.tiles = []
        self.create_widgets()
        self.update_grid(generate_solvable_puzzle())

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg=BG_COLOR, padx=10, pady=10)
        main_frame.pack(fill="both", expand=True)

        control_frame = tk.Frame(main_frame, bg=BG_COLOR)
        control_frame.pack(pady=5)

        tk.Label(control_frame, text="Jumlah Pengujian:", font=BUTTON_FONT, bg=BG_COLOR).pack(side="left", padx=(0, 5))

        self.trials_entry = tk.Entry(control_frame, width=5, font=BUTTON_FONT)
        self.trials_entry.insert(0, "10")
        self.trials_entry.pack(side="left")

        self.run_button = tk.Button(control_frame, text="Jalankan Perbandingan", font=BUTTON_FONT,
                                    command=self.run_comparison)
        self.run_button.pack(side="left", padx=10)

        grid_frame = tk.Frame(main_frame, bg=GRID_COLOR, bd=2)
        grid_frame.pack(pady=10)
        for i in range(3):
            row_tiles = []
            for j in range(3):
                tile = tk.Label(grid_frame, text="", width=4, height=2, bg=TILE_COLOR, font=FONT_STYLE, relief="raised",
                                borderwidth=2)
                tile.grid(row=i, column=j, padx=2, pady=2)
                row_tiles.append(tile)
            self.tiles.append(row_tiles)

        results_area_frame = tk.Frame(main_frame, bg=BG_COLOR)
        results_area_frame.pack(fill="both", expand=True, pady=(10, 0))

        tk.Label(results_area_frame, text="Log Pengujian:", font=BUTTON_FONT, bg=BG_COLOR).pack(anchor="w")
        self.log_area = scrolledtext.ScrolledText(results_area_frame, height=10, font=RESULT_FONT, wrap=tk.WORD)
        self.log_area.pack(fill="both", expand=True)
        self.log_area.config(state='disabled')

        tk.Label(results_area_frame, text="Hasil Akhir (Rata-rata):", font=BUTTON_FONT, bg=BG_COLOR).pack(anchor="w",
                                                                                                          pady=(10, 0))
        self.summary_label = tk.Label(results_area_frame, text="", font=RESULT_FONT, bg="#e0e0e0", justify="left",
                                      wraplength=480, padx=5, pady=5)
        self.summary_label.pack(fill="x", pady=(0, 5))

    def update_grid(self, state):
        for i in range(3):
            for j in range(3):
                number = state[i][j]
                self.tiles[i][j].config(text=str(number) if number != 0 else "",
                                        bg=TILE_COLOR if number != 0 else "#d3d3d3")

    def log(self, message):
        self.log_area.config(state='normal')
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)
        self.log_area.config(state='disabled')

    def run_comparison(self):
        self.run_button.config(state="disabled")

        self.log_area.config(state='normal')
        self.log_area.delete('1.0', tk.END)
        self.log_area.config(state='disabled')
        self.summary_label.config(text="Proses perbandingan sedang berjalan...")

        try:
            num_trials = int(self.trials_entry.get())
            if num_trials <= 0: raise ValueError
        except ValueError:
            num_trials = 10
            self.trials_entry.delete(0, tk.END)
            self.trials_entry.insert(0, "10")

        bfs_stats = {'cost': 0, 'nodes': 0, 'time': 0.0, 'wins': 0}
        dfs_stats = {'cost': 0, 'nodes': 0, 'time': 0.0, 'wins': 0}

        for i in range(1, num_trials + 1):
            self.log(f"=============== PENGUJIAN KE-{i}/{num_trials} ===============")

            puzzle = generate_solvable_puzzle()
            self.update_grid(puzzle)
            self.root.update()

            start_time = time.time()
            dfs_result = dfs(puzzle, GOAL_STATE)
            dfs_time = time.time() - start_time
            if dfs_result:
                dfs_stats['wins'] += 1
                dfs_path_len, dfs_nodes_exp = dfs_result[1], dfs_result[2]
                dfs_stats['cost'] += dfs_path_len
                dfs_stats['nodes'] += dfs_nodes_exp
                dfs_stats['time'] += dfs_time
                self.log(f"DFS: Berhasil! Langkah={dfs_path_len}, Simpul={dfs_nodes_exp:,.0f}, Waktu={dfs_time:.4f}s")
            else:
                self.log(f"DFS: Gagal menemukan solusi.")

            start_time = time.time()
            bfs_result = bfs(puzzle, GOAL_STATE)
            bfs_time = time.time() - start_time
            if bfs_result:
                bfs_stats['wins'] += 1
                bfs_path_len, bfs_nodes_exp = bfs_result[1], bfs_result[2]
                bfs_stats['cost'] += bfs_path_len
                bfs_stats['nodes'] += bfs_nodes_exp
                bfs_stats['time'] += bfs_time
                self.log(f"BFS: Berhasil! Langkah={bfs_path_len}, Simpul={bfs_nodes_exp:,.0f}, Waktu={bfs_time:.4f}s")
            else:
                self.log(f"BFS: Gagal menemukan solusi.")

            self.log("=" * 50 + "\n")
            self.root.update()

        avg_bfs_cost = bfs_stats['cost'] / bfs_stats['wins'] if bfs_stats['wins'] > 0 else 0
        avg_bfs_nodes = bfs_stats['nodes'] / bfs_stats['wins'] if bfs_stats['wins'] > 0 else 0
        avg_bfs_time = bfs_stats['time'] / bfs_stats['wins'] if bfs_stats['wins'] > 0 else 0

        avg_dfs_cost = dfs_stats['cost'] / dfs_stats['wins'] if dfs_stats['wins'] > 0 else 0
        avg_dfs_nodes = dfs_stats['nodes'] / dfs_stats['wins'] if dfs_stats['wins'] > 0 else 0
        avg_dfs_time = dfs_stats['time'] / dfs_stats['wins'] if dfs_stats['wins'] > 0 else 0

        summary_text = (
            f"----------------- BFS  ------------------\n"
            f"Berhasil Ditemukan   : {bfs_stats['wins']} / {num_trials}\n"
            f"Rata-rata Pergerakan : {avg_bfs_cost:.2f} langkah\n"
            f"Rata-rata Simpul     : {avg_bfs_nodes:,.0f} simpul\n"
            f"Rata-rata Waktu      : {avg_bfs_time:.4f} detik\n\n"
            f"----------------- DFS  ------------------\n"
            f"Berhasil Ditemukan   : {dfs_stats['wins']} / {num_trials}\n"
            f"Rata-rata Pergerakan : {avg_dfs_cost:.2f} langkah\n"
            f"Rata-rata Simpul     : {avg_dfs_nodes:,.0f} simpul\n"
            f"Rata-rata Waktu      : {avg_dfs_time:.4f} detik"
        )

        self.summary_label.config(text=summary_text)
        print(summary_text)

        self.run_button.config(state="normal")


if __name__ == "__main__":
    main_root = tk.Tk()
    app = PuzzleGUI(main_root)
    main_root.mainloop()


# # Nama file: gui.py
# # Versi Final dengan Log per-Loop dan Hasil Akhir
# # Dibuat dengan rujukan Python 3.10
#
# import tkinter as tk
# from tkinter import font, scrolledtext  # DIUBAH: Impor scrolledtext untuk area log
#
# import time
# import random
#
# from puzzle_solver import bfs, dfs, get_neighbors
#
# # --- Definisi warna dan font ---
# BG_COLOR = "#f0f0f0"
# GRID_COLOR = "#a3a3a3"
# TILE_COLOR = "#ffffff"
# FONT_STYLE = ("Helvetica", 24, "bold")
# BUTTON_FONT = ("Helvetica", 12)
# RESULT_FONT = ("Courier", 10)
#
# # Goal state tetap
# GOAL_STATE = (
#     (1, 2, 3),
#     (8, 0, 4),
#     (7, 6, 5)
# )
#
#
# def generate_solvable_puzzle(shuffles=100):
#     state = GOAL_STATE
#     for _ in range(shuffles):
#         neighbors = get_neighbors(state)
#         random_choice = random.choice(neighbors)
#         state = random_choice[0]
#     return state
#
#
# class PuzzleGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("8-Puzzle Solver: Perbandingan BFS vs DFS")
#         self.root.configure(bg=BG_COLOR)
#         # DIUBAH: Ukuran window diperbesar untuk menampung log
#         self.root.geometry("500x700")
#
#         self.tiles = []
#         self.create_widgets()
#         self.update_grid(generate_solvable_puzzle())
#
#     def create_widgets(self):
#         main_frame = tk.Frame(self.root, bg=BG_COLOR, padx=10, pady=10)
#         main_frame.pack(fill="both", expand=True)
#
#         # --- Frame untuk Kontrol (Input dan Tombol) ---
#         control_frame = tk.Frame(main_frame, bg=BG_COLOR)
#         control_frame.pack(pady=5)
#
#         tk.Label(control_frame, text="Jumlah Pengujian:", font=BUTTON_FONT, bg=BG_COLOR).pack(side="left", padx=(0, 5))
#
#         self.trials_entry = tk.Entry(control_frame, width=5, font=BUTTON_FONT)
#         self.trials_entry.insert(0, "10")
#         self.trials_entry.pack(side="left")
#
#         self.run_button = tk.Button(control_frame, text="Jalankan Perbandingan", font=BUTTON_FONT,
#                                     command=self.run_comparison)
#         self.run_button.pack(side="left", padx=10)
#
#         # --- Papan Puzzle (tidak berubah) ---
#         grid_frame = tk.Frame(main_frame, bg=GRID_COLOR, bd=2)
#         grid_frame.pack(pady=10)
#         for i in range(3):
#             row_tiles = []
#             for j in range(3):
#                 tile = tk.Label(grid_frame, text="", width=4, height=2, bg=TILE_COLOR, font=FONT_STYLE, relief="raised",
#                                 borderwidth=2)
#                 tile.grid(row=i, column=j, padx=2, pady=2)
#                 row_tiles.append(tile)
#             self.tiles.append(row_tiles)
#
#         # DIUBAH: Frame baru untuk menampung area log dan hasil akhir
#         results_area_frame = tk.Frame(main_frame, bg=BG_COLOR)
#         results_area_frame.pack(fill="both", expand=True, pady=(10, 0))
#
#         # BARU: Area log yang bisa di-scroll
#         tk.Label(results_area_frame, text="Log Pengujian:", font=BUTTON_FONT, bg=BG_COLOR).pack(anchor="w")
#         self.log_area = scrolledtext.ScrolledText(results_area_frame, height=10, font=RESULT_FONT, wrap=tk.WORD)
#         self.log_area.pack(fill="both", expand=True)
#         self.log_area.config(state='disabled')  # Awalnya tidak bisa diedit
#
#         # BARU: Area untuk hasil akhir/rata-rata
#         tk.Label(results_area_frame, text="Hasil Akhir (Rata-rata):", font=BUTTON_FONT, bg=BG_COLOR).pack(anchor="w",
#                                                                                                           pady=(10, 0))
#         self.summary_label = tk.Label(results_area_frame, text="", font=RESULT_FONT, bg="#e0e0e0", justify="left",
#                                       wraplength=480, padx=5, pady=5)
#         self.summary_label.pack(fill="x", pady=(0, 5))
#
#     def update_grid(self, state):
#         for i in range(3):
#             for j in range(3):
#                 number = state[i][j]
#                 self.tiles[i][j].config(text=str(number) if number != 0 else "",
#                                         bg=TILE_COLOR if number != 0 else "#d3d3d3")
#
#     def log(self, message):
#         """Fungsi helper untuk menambahkan teks ke area log."""
#         self.log_area.config(state='normal')  # Aktifkan untuk menulis
#         self.log_area.insert(tk.END, message + "\n")
#         self.log_area.see(tk.END)  # Auto-scroll ke bawah
#         self.log_area.config(state='disabled')  # Non-aktifkan lagi
#
#     def run_comparison(self):
#         # Non-aktifkan tombol selama proses berjalan
#         self.run_button.config(state="disabled")
#
#         # Bersihkan log dan hasil sebelumnya
#         self.log_area.config(state='normal')
#         self.log_area.delete('1.0', tk.END)
#         self.log_area.config(state='disabled')
#         self.summary_label.config(text="Proses perbandingan sedang berjalan...")
#
#         try:
#             num_trials = int(self.trials_entry.get())
#             if num_trials <= 0: raise ValueError
#         except ValueError:
#             num_trials = 10
#             self.trials_entry.delete(0, tk.END)
#             self.trials_entry.insert(0, "10")
#
#         bfs_stats = {'cost': 0, 'nodes': 0, 'time': 0.0, 'wins': 0}
#         dfs_stats = {'cost': 0, 'nodes': 0, 'time': 0.0, 'wins': 0}
#
#         for i in range(1, num_trials + 1):
#             self.log(f"=============== PENGUJIAN KE-{i}/{num_trials} ===============")
#
#             puzzle = generate_solvable_puzzle()
#             self.update_grid(puzzle)
#             self.root.update()
#
#             # --- Jalankan DFS ---
#             start_time = time.time()
#             dfs_result = dfs(puzzle, GOAL_STATE)
#             dfs_time = time.time() - start_time
#             if dfs_result:
#                 dfs_stats['wins'] += 1
#                 dfs_path_len, dfs_nodes_exp = dfs_result[1], dfs_result[2]
#                 dfs_stats['cost'] += dfs_path_len
#                 dfs_stats['nodes'] += dfs_nodes_exp
#                 dfs_stats['time'] += dfs_time
#                 self.log(f"DFS: Berhasil! Langkah={dfs_path_len}, Simpul={dfs_nodes_exp:,.0f}, Waktu={dfs_time:.4f}s")
#             else:
#                 self.log(f"DFS: Gagal menemukan solusi.")
#
#             # --- Jalankan BFS ---
#             start_time = time.time()
#             bfs_result = bfs(puzzle, GOAL_STATE)
#             bfs_time = time.time() - start_time
#             if bfs_result:
#                 bfs_stats['wins'] += 1
#                 bfs_path_len, bfs_nodes_exp = bfs_result[1], bfs_result[2]
#                 bfs_stats['cost'] += bfs_path_len
#                 bfs_stats['nodes'] += bfs_nodes_exp
#                 bfs_stats['time'] += bfs_time
#                 self.log(f"BFS: Berhasil! Langkah={bfs_path_len}, Simpul={bfs_nodes_exp:,.0f}, Waktu={bfs_time:.4f}s")
#             else:
#                 self.log(f"BFS: Gagal menemukan solusi.")
#
#             self.log("=" * 50 + "\n")
#             self.root.update()
#
#         # --- Siapkan Teks Hasil Akhir ---
#         avg_bfs_cost = bfs_stats['cost'] / bfs_stats['wins'] if bfs_stats['wins'] > 0 else 0
#         avg_bfs_nodes = bfs_stats['nodes'] / bfs_stats['wins'] if bfs_stats['wins'] > 0 else 0
#         avg_bfs_time = bfs_stats['time'] / bfs_stats['wins'] if bfs_stats['wins'] > 0 else 0
#
#         avg_dfs_cost = dfs_stats['cost'] / dfs_stats['wins'] if dfs_stats['wins'] > 0 else 0
#         avg_dfs_nodes = dfs_stats['nodes'] / dfs_stats['wins'] if dfs_stats['wins'] > 0 else 0
#         avg_dfs_time = dfs_stats['time'] / dfs_stats['wins'] if dfs_stats['wins'] > 0 else 0
#
#         summary_text = (
#             f"----------------- BFS  ------------------\n"
#             f"Berhasil Ditemukan   : {bfs_stats['wins']} / {num_trials}\n"
#             f"Rata-rata Pergerakan : {avg_bfs_cost:.2f} langkah\n"
#             f"Rata-rata Simpul     : {avg_bfs_nodes:,.0f} simpul\n"
#             f"Rata-rata Waktu      : {avg_bfs_time:.4f} detik\n\n"
#             f"----------------- DFS  ------------------\n"
#             f"Berhasil Ditemukan   : {dfs_stats['wins']} / {num_trials}\n"
#             f"Rata-rata Pergerakan : {avg_dfs_cost:.2f} langkah\n"
#             f"Rata-rata Simpul     : {avg_dfs_nodes:,.0f} simpul\n"
#             f"Rata-rata Waktu      : {avg_dfs_time:.4f} detik"
#         )
#
#         self.summary_label.config(text=summary_text)
#         print(summary_text)
#
#         # Aktifkan kembali tombol setelah selesai
#         self.run_button.config(state="normal")
#
#
# if __name__ == "__main__":
#     main_root = tk.Tk()
#     app = PuzzleGUI(main_root)
#     main_root.mainloop()