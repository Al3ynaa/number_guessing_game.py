# Number Guessing Game

## Algoritma

1. **Başla**
2. **`number_to_guess = random.randint(1, 100)`** # 1 ile 100 arasında rastgele bir sayı seç
3. **`while True:`** # Sonsuz döngü başlat
   4. Kullanıcıdan sayı tahmini al (integer olarak) **`guess = int(input())`**
   5. Eğer **`guess < number_to_guess`**:
      - "Too low!" yazdır
   6. Eğer **`guess > number_to_guess`**:
      - "Too high!" yazdır
   7. Eğer **`guess == number_to_guess`**:
      - "Tebrikler! Sayıyı bildiniz!" yazdır
      - Döngüyü **`break`** ile sonlandır
   8. Eğer kullanıcı geçerli bir sayı girmezse:
      - "Lütfen geçerli bir sayı girin." yazdır
      - Döngüye devam et
9. **Bitti**

