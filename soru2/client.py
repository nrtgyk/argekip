import socket
import pickle

def send_data(connection, data):
    """
    Bağlantı üzerinden veriyi gönderir.
    """
    total_sent = 0
    while total_sent < len(data):
         # Veriyi 512 byte'lık parçalara bölerek gönderir
        sent = connection.send(data[total_sent:total_sent+512])
        if sent == 0:
             # Bağlantı kesilirse hata fırlatır
            raise RuntimeError("Bağlantı kesildi")
        total_sent += sent

def create_packets(data, packet_size=512):
    """
    Veriyi paketlere böler.
    """
    # Veriyi paketlere bölme
    num_packets = (len(data) + packet_size - 1) // packet_size
    packets = []

    for i in range(num_packets):
        start_index = i * packet_size
        end_index = min(start_index + packet_size, len(data))
        # Her bir paket için ID oluşturur ve paketin içeriğini belirler
        packet_content = data[start_index:end_index]
        packet = {
            "packet_id": 0,
            "packet_number": i,
            "packet_content": packet_content
        }
        packets.append(packet)

    return packets

def main():
    """
    Ana fonksiyon. İstemci tarafından girilen veriyi paketler halinde sunucuya gönderir.
    """
    host = "127.0.0.1"  # Sunucu IP adresi
    port = 12345         # Port numarası

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        
        while True:
            # Kullanıcıdan veri alır
        
            message = input("Gönderilecek veriyi girin: ")
            message_bytes = message.encode()
            packets = create_packets(message_bytes)    # Veriyi paketlere böler
            
            data_to_send = pickle.dumps(packets)  # Paketleri gönderir
            send_data(client_socket, data_to_send)

if __name__ == "__main__":
    main()
