def generate_permutations(arr):
    result = []  # List untuk menyimpan semua permutasi

    def dfs(current_path, used_elements):
        # Jika panjang jalur sama dengan panjang array asli, simpan permutasi ke hasil
        if len(current_path) == len(arr):
            result.append(current_path[:])
            return

        # Iterasi untuk setiap elemen dalam array
        for idx in range(len(arr)):
            if used_elements[idx]:  # Lewati elemen yang sudah digunakan
                continue
            
            # Tandai elemen ini sebagai sudah digunakan
            used_elements[idx] = True
            current_path.append(arr[idx])  # Tambahkan elemen ini ke jalur

            # Lakukan rekursi untuk menelusuri jalur berikutnya
            dfs(current_path, used_elements)

            # Backtrack: Kembalikan status elemen dan hapus elemen terakhir
            current_path.pop()
            used_elements[idx] = False

    # Memulai proses DFS dengan jalur kosong dan semua elemen belum digunakan
    dfs([], [False] * len(arr))
    return result

# Contoh penggunaan
numbers = [1, 2, 3, 4, 5]
all_permutations = generate_permutations(numbers)
print(f"Semua permutasi dari {numbers}: {all_permutations}")
