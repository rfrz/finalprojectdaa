import collections


class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


def get_neighbors(state):
    neighbors = []
    state_list = [list(row) for row in state]

    pos_x, pos_y = -1, -1
    for i in range(3):
        for j in range(3):
            if state_list[i][j] == 0:
                pos_x, pos_y = i, j
                break

    moves = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}

    for action, (dx, dy) in moves.items():
        new_x, new_y = pos_x + dx, pos_y + dy

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state_list = [list(row) for row in state_list]
            new_state_list[pos_x][pos_y], new_state_list[new_x][new_y] = new_state_list[new_x][new_y], \
            new_state_list[pos_x][pos_y]
            new_state_tuple = tuple(tuple(row) for row in new_state_list)
            neighbors.append((new_state_tuple, action))

    return neighbors


def get_solution_path(node):
    path = []
    current = node
    while current.parent is not None:
        path.append(current.action)
        current = current.parent
    path.reverse()
    return path


def bfs(initial_state, goal_state):
    queue = collections.deque([Node(initial_state)])
    visited = {initial_state}
    nodes_expanded = 0

    while queue:
        node = queue.popleft()
        nodes_expanded += 1

        if node.state == goal_state:
            path = get_solution_path(node)
            return path, len(path), nodes_expanded

        for neighbor_state, action in get_neighbors(node.state):
            if neighbor_state not in visited:
                visited.add(neighbor_state)
                child_node = Node(neighbor_state, parent=node, action=action)
                queue.append(child_node)

    return None, 0, nodes_expanded


def dfs(initial_state, goal_state):
    stack = [Node(initial_state)]
    visited = {initial_state}
    nodes_expanded = 0

    while stack:
        node = stack.pop()
        nodes_expanded += 1

        if node.state == goal_state:
            path = get_solution_path(node)
            return path, len(path), nodes_expanded

        for neighbor_state, action in reversed(get_neighbors(node.state)):
            if neighbor_state not in visited:
                visited.add(neighbor_state)
                child_node = Node(neighbor_state, parent=node, action=action)
                stack.append(child_node)

    return None, 0, nodes_expanded

# # Nama file: puzzle_solver.py
# # Berisi logika inti untuk 8-Puzzle, termasuk algoritma BFS dan DFS.
# # Dibuat dengan rujukan Python 3.10
#
# import collections
#
#
# # Kelas Node merepresentasikan satu simpul dalam pohon pencarian.
# # Ini penting untuk melacak jejak (path) dari awal sampai akhir.
# class Node:
#     def __init__(self, state, parent=None, action=None):
#         """
#         Inisialisasi sebuah Node.
#         - state: Representasi papan puzzle saat ini (tuple dari tuple).
#         - parent: Node sebelumnya (dari mana kita sampai ke sini).
#         - action: Gerakan yang diambil dari parent untuk sampai ke state ini.
#         """
#         self.state = state
#         self.parent = parent
#         self.action = action
#
#     # Digunakan untuk membandingkan dua node, berguna untuk pengecekan.
#     def __eq__(self, other):
#         return isinstance(other, Node) and self.state == other.state
#
#     # Diperlukan agar Node bisa dimasukkan ke dalam set (untuk 'visited').
#     def __hash__(self):
#         return hash(self.state)
#
#
# def get_neighbors(state):
#     """
#     Fungsi untuk mendapatkan semua kemungkinan langkah (neighbor) dari state saat ini.
#     """
#     neighbors = []
#     # Mengubah tuple menjadi list agar bisa dimodifikasi.
#     state_list = [list(row) for row in state]
#
#     # Cari posisi kotak kosong (direpresentasikan dengan None atau 0, kita pakai 0).
#     # Di soal Anda, kotak kosong tidak ada angkanya. Kita anggap saja sebagai 0.
#     pos_x, pos_y = -1, -1
#     for i in range(3):
#         for j in range(3):
#             if state_list[i][j] == 0:
#                 pos_x, pos_y = i, j
#                 break
#
#     # Operator: Atas, Bawah, Kiri, Kanan
#     moves = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}
#
#     for action, (dx, dy) in moves.items():
#         new_x, new_y = pos_x + dx, pos_y + dy
#
#         # Cek apakah gerakan valid (tidak keluar dari papan 3x3).
#         if 0 <= new_x < 3 and 0 <= new_y < 3:
#             # Buat salinan state untuk dimodifikasi.
#             new_state_list = [list(row) for row in state_list]
#             # Tukar posisi kotak kosong dengan tetangganya.
#             new_state_list[pos_x][pos_y], new_state_list[new_x][new_y] = new_state_list[new_x][new_y], \
#             new_state_list[pos_x][pos_y]
#             # Ubah kembali ke tuple agar bisa di-hash.
#             new_state_tuple = tuple(tuple(row) for row in new_state_list)
#             neighbors.append((new_state_tuple, action))
#
#     return neighbors
#
#
# def get_solution_path(node):
#     """
#     Fungsi untuk menelusuri kembali dari node tujuan ke node awal untuk mendapatkan path.
#     """
#     path = []
#     current = node
#     while current.parent is not None:
#         path.append(current.action)
#         current = current.parent
#     path.reverse()  # Dibalik agar urutannya dari awal ke akhir.
#     return path
#
#
# def bfs(initial_state, goal_state):
#     """
#     Implementasi algoritma Breadth-First Search (BFS).
#     Menggunakan struktur data antrian (queue) - First-In, First-Out. [cite: 85]
#     """
#     # Antrian untuk menyimpan node yang akan dieksplorasi.
#     # collections.deque lebih efisien daripada list untuk operasi pop dari kiri.
#     queue = collections.deque([Node(initial_state)])
#
#     # Set untuk menyimpan state yang sudah dikunjungi agar tidak ada perulangan.
#     visited = {initial_state}
#
#     # Melacak berapa banyak simpul yang diekspansi.
#     nodes_expanded = 0
#
#     # Loop selama antrian tidak kosong.
#     while queue:
#         # Ambil node pertama dari antrian (FIFO).
#         node = queue.popleft()
#         nodes_expanded += 1
#
#         # Cek apakah ini adalah goal state.
#         if node.state == goal_state:
#             path = get_solution_path(node)
#             return path, len(path), nodes_expanded
#
#         # Jika bukan goal state, dapatkan semua tetangganya.
#         for neighbor_state, action in get_neighbors(node.state):
#             # Jika tetangga belum pernah dikunjungi.
#             if neighbor_state not in visited:
#                 # Tandai sudah dikunjungi.
#                 visited.add(neighbor_state)
#                 # Buat node baru untuk tetangga tersebut.
#                 child_node = Node(neighbor_state, parent=node, action=action)
#                 # Masukkan ke dalam antrian.
#                 queue.append(child_node)
#
#     # Jika antrian kosong dan solusi tidak ditemukan.
#     return None, 0, nodes_expanded
#
#
# def dfs(initial_state, goal_state):
#     """
#     Implementasi algoritma Depth-First Search (DFS).
#     Menggunakan struktur data tumpukan (stack) - Last-In, First-Out. [cite: 166]
#     """
#     # Tumpukan (stack) untuk menyimpan node yang akan dieksplorasi.
#     # Kita bisa menggunakan list Python biasa sebagai stack.
#     stack = [Node(initial_state)]
#
#     # Set untuk menyimpan state yang sudah dikunjungi.
#     visited = {initial_state}
#
#     # Melacak berapa banyak simpul yang diekspansi.
#     nodes_expanded = 0
#
#     # Loop selama stack tidak kosong.
#     while stack:
#         # Ambil node terakhir dari stack (LIFO).
#         node = stack.pop()
#         nodes_expanded += 1
#
#         # Cek apakah ini adalah goal state.
#         if node.state == goal_state:
#             path = get_solution_path(node)
#             return path, len(path), nodes_expanded
#
#         # Jika bukan goal state, dapatkan semua tetangganya.
#         # Kita balik urutan tetangga agar eksplorasi lebih intuitif (misal: Up, Down, Left, Right).
#         for neighbor_state, action in reversed(get_neighbors(node.state)):
#             # Jika tetangga belum pernah dikunjungi.
#             if neighbor_state not in visited:
#                 # Tandai sudah dikunjungi.
#                 visited.add(neighbor_state)
#                 # Buat node baru untuk tetangga tersebut.
#                 child_node = Node(neighbor_state, parent=node, action=action)
#                 # Masukkan ke dalam tumpukan.
#                 stack.append(child_node)
#
#     # Jika stack kosong dan solusi tidak ditemukan.
#     return None, 0, nodes_expanded