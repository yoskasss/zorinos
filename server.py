import socket
from pynput import keyboard, mouse

# Sunucu bilgileri
HOST = "0.0.0.0"  # Tüm ağ arabirimlerini dinle
PORT = 12345

def handle_keyboard(key):
    try:
        data = f"KEY:{key.char}\n"
    except AttributeError:
        data = f"KEY:{key}\n"
    conn.send(data.encode())

def handle_mouse_move(x, y):
    data = f"MOVE:{x},{y}\n"
    conn.send(data.encode())

def handle_mouse_click(x, y, button, pressed):
    state = "DOWN" if pressed else "UP"
    data = f"CLICK:{x},{y},{button},{state}\n"
    conn.send(data.encode())

# Ağ bağlantısını başlat
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Sunucu {HOST}:{PORT} adresinde dinleniyor...")

    conn, addr = server_socket.accept()
    print(f"Bağlantı alındı: {addr}")

    with keyboard.Listener(on_press=handle_keyboard), mouse.Listener(on_move=handle_mouse_move, on_click=handle_mouse_click):
        try:
            print("Klavyeden ve fareden girişler aktarılıyor...")
            while True:
                pass  # Dinlemeye devam et
        except KeyboardInterrupt:
            print("Sunucu durduruluyor...")
