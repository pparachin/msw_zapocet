import time
import hashlib
from pynput.mouse import Listener


mouse_data = []


def current_time_hash():
    current_time = time.time()
    seed_base = hashlib.sha256(str(current_time).encode()).hexdigest()

    return seed_base


def gather_user_input():
    user_input = input("Zadejte náhodný řetězec úhozů na klávesnici: ")

    user_input_hash = hashlib.sha256(user_input.encode()).hexdigest()

    return user_input_hash


def on_move(x, y):
    global mouse_data
    mouse_data.append((x, y))


def gather_mouse_movement(duration=5):
    print(f"Po dobu {duration} sekund pohybujte náhodně myší po obrazovce")

    print("Sledování pohybu myši...")
    with Listener(on_move=on_move) as listener:
        time.sleep(duration)
        listener.stop()
    print("Sledování pohybu myši ukončeno")

    coordinates_string = "".join([f"{x},{y}" for x, y in mouse_data])

    mouse_movement_hash = hashlib.sha256(coordinates_string.encode()).hexdigest()
    return mouse_movement_hash


def main():
    # Krok 1: Získání náhodného vstupu od uživatele
    user_seed = gather_user_input()

    # Krok 2: Získání náhodného vstupu od uživatele
    mouse_seed = gather_mouse_movement()

    # Krok 3: Získání času
    time_stamp = current_time_hash()

    # Krok 4: Kombinace všech vstupů
    final_seed = hashlib.sha256((user_seed + mouse_seed + time_stamp).encode()).hexdigest()

    # Krok 5: Převod na číslo
    final_seed = int(final_seed, 16)

    # Krok 6: Výstup
    print(f"Váš náhodný řetězec: {final_seed}")


if __name__ == "__main__":
    main()
