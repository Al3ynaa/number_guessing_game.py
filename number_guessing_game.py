import random

number_to_guess = random.randint(1, 100)

# Sonsuz döngü başlatıyoruz
while True:
    try:
        # Kullanıcıdan tahmin almak için input() kullanıyoruz
        guess = int(input("Guess the number between 1 and 100:"))
        
        # Burada if-elif-else ile tahminin doğru olup olmadığını kontrol ediyoruz
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            break  # Doğru tahmin yapıldığında döngüyü sonlandırıyoruz

    except ValueError:
        print("Please enter a valid number")  # Eğer geçerli bir sayı girilmezse hata mesajı
