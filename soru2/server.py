import socket
import threading
import pickle

def receive_data(connection):
    """
    Bağlantıdan gelen veriyi alır ve 512 byte'lık parçalara ayırarak birleştirir.
    """
    received_data = b""
    while True:
        chunk = connection.recv(512)
        if not chunk:
            break
        received_data += chunk
        if len(chunk) < 512:
            break
    return received_data

def handle_client(connection, address):
    """
    İstemci bağlantısını işler. Bağlantıdan gelen paketleri alır ve içeriklerini ekrana yazdırır.
    """
    print("Bağlantı sağlandı:", address)

    # Bağlantıdan gelen veriyi al
    data = receive_data(connection)
    
    # Alınan veriyi pickle modülü kullanarak paketlere ayır
    received_packets = pickle.loads(data)
    
     # Alınan paketlerin içeriğini ekrana yazdır
    for packet in received_packets:
        print("Paket ID:", packet['packet_id'])
        print("Paket Bölünen No:", packet['packet_number'])
        print("Paket İçeriği:", packet['packet_content'])

    

def main():
    
    """
    Ana fonksiyon. Sunucuyu başlatır ve gelen istemci bağlantılarını işler.
    """
    
    host = "127.0.0.1"  # Sunucu IP adresi
    port = 12345         # Port numarası

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print("Sunucu başlatıldı. İstemci bekleniyor...")

        while True:
             # İstemci bağlantısını kabul et
            connection, address = server_socket.accept()
            # İstemci bağlantısını işleyecek yeni bir iş parçacığı oluştur
            client_thread = threading.Thread(target=handle_client, args=(connection, address))
            client_thread.start()

if __name__ == "__main__":
    main()
