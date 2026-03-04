import socket # Import the socket module, which is useful for everything network related

#define the ports we want to scan and their corresponding names in a dictionary
PORT_NAMES = {
    80: "HTTP",
    443: "HTTPS",
    22: "SSH",
    21: "FTP",
    25: "SMTP",
    3306: "MySQL",
    1433: "MSSQL",
    }

for port in PORT_NAMES:
  # socket class allows us to create a socket object, which is used to connect to the target host and port
  # AF_INET is the address family for IPv4, and SOCK_STREAM indicates we are using TCP
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(0.5)

  # utilizes the loopback address to check OUR network for open ports. We need to pass this as a tupple
  status = s.connect_ex(("127.0.0.1", port))
  #status will be 0 if the connection was successful, meaning the port is open
  if status == 0:
    print(f"Port {port} ({PORT_NAMES[port]}) is open.")
  else:
    print(f"Port {port} ({PORT_NAMES[port]}) is closed.")
  