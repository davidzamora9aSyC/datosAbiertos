import requests
import socket

# Fuerza el uso de IPv4
original_getaddrinfo = socket.getaddrinfo

def getaddrinfo_ipv4(*args, **kwargs):
    return original_getaddrinfo(*args, family=socket.AF_INET, **kwargs)

socket.getaddrinfo = getaddrinfo_ipv4

try:
    response = requests.get("https://www.datos.gov.co/resource/qhpu-8ixx.json")
    print("Status code:", response.status_code)
    print("Response:", response.text[:100])  # Muestra los primeros 100 caracteres
except requests.exceptions.RequestException as e:
    print("Error:", e)
 