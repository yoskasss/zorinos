import socket
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController, Button

# Sunucu bilgileri
SERVER_HOST = "1.1.1.1"  # Sunucu IP adresini buraya yazın
SERVER_PORT = 12345

# Klavye ve fare denetleyicileri
keyboard = KeyboardController()
mouse = MouseController()

# Sunucuya bağlan
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"Sunucuya bağlanıldı: {SERVER_HOST}:{SERVER_PORT}")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        commands = data.strip().split("\n")
        for command in commands:
            if command.startswith("KEY:"):
                key = command.split(":")[1]
                try:
                    keyboard.type(key)
                except Exception:
                    pass
            elif command.startswith("MOVE:"):
                x, y = map(int, command.split(":")[1].split(","))
                mouse.position = (x, y)
            elif command.startswith("CLICK:"):
                _, x, y, button, state = command.split(":")
                x, y = int(x), int(y)
                button = Button.left if "Button.left" in button else Button.right
                mouse.position = (x, y)
                if state == "DOWN":
                    mouse.press(button)
                else:
                    mouse.release(button)
