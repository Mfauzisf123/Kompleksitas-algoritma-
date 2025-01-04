def find_subsets_with_target_sum(arr, target_sum):
    solutions = []

    def explore(subset, total, start):
        # Jika total saat ini sama dengan target_sum, simpan subset
        if total == target_sum:
            solutions.append(subset[:])  # Salin subset saat ini
            return

        # Jika total melebihi target atau indeks di luar jangkauan, hentikan eksplorasi
        if total > target_sum or start >= len(arr):
            return

        # Coba tambahkan elemen saat ini ke subset
        subset.append(arr[start])
        explore(subset, total + arr[start], start)  # Tetap di indeks yang sama

        # Kembalikan keadaan sebelum mencoba elemen berikutnya
        subset.pop()
        explore(subset, total, start + 1)  # Lanjutkan ke elemen berikutnya

    explore([], 0, 0)
    return solutions

# Contoh penggunaan
numbers = [2, 4, 6, 8, 10]
target_value = 10

result = find_subsets_with_target_sum(numbers, target_value)
print(f"Semua subset dengan jumlah {target_value}: {result}")
