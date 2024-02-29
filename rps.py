import random

while True: 
    get_player_choice = input("Сделайте выбор — камень, ножницы или бумага: ")
    choise = ["камень", "бумага", "ножницы"]
    get_computer_choice = random.choice(choise)
    print(f"\nВы выбрали {get_player_choice}, компьютер выбрал {get_computer_choice}.\n")
    if get_player_choice == get_computer_choice:
        print(f"Оба пользователя выбрали {get_player_choice}. Ничья!!")
    elif get_player_choice == "камень":
        if get_computer_choice == "ножницы":
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif get_player_choice == "бумага":
        if get_computer_choice == "камень":
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif get_player_choice == "ножницы":
        if get_computer_choice == "бумага":
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")
    play_game = "" 
    play_game = input("Сыграем еще? (д/н): ") 
    if play_game.lower() != "д": 
        break 