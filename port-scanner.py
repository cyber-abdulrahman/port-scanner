import socket
print("===== Port Scanner =====")
target = input("Enter a domain or IP address: ")

ports = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}

print()
print(f"Target: {target}")
print()
for port in ports:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"{port} {ports[port]} OPEN")
    else:
        print(f"{port} {ports[port]} CLOSED")

    sock.close()