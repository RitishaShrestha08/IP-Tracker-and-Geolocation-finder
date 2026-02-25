import socket
import requests
import tkinter as tk
from tkinter import messagebox

# ---------------- IP PORT SCANNER ---------------- #
def scan_ports():
    ip = ip_entry.get()
    result_text.delete(1.0, tk.END)

    common_ports = [21, 22, 23, 25, 53, 80, 443, 3306]
    result_text.insert(tk.END, f"Scanning IP: {ip}\n\n")

    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                result_text.insert(tk.END, f"Port {port}: OPEN\n")
            else:
                result_text.insert(tk.END, f"Port {port}: CLOSED\n")
            sock.close()
        except:
            result_text.insert(tk.END, "Error scanning ports\n")
            break

# ---------------- IP GEOLOCATION ---------------- #
def get_location():
    ip = ip_entry.get()
    result_text.delete(1.0, tk.END)

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data["status"] == "success":
            result_text.insert(tk.END, f"IP: {ip}\n")
            result_text.insert(tk.END, f"Country: {data['country']}\n")
            result_text.insert(tk.END, f"Region: {data['regionName']}\n")
            result_text.insert(tk.END, f"City: {data['city']}\n")
            result_text.insert(tk.END, f"ISP: {data['isp']}\n")
            result_text.insert(tk.END, f"Latitude: {data['lat']}\n")
            result_text.insert(tk.END, f"Longitude: {data['lon']}\n")
        else:
            result_text.insert(tk.END, "Invalid IP address\n")

    except:
        messagebox.showerror("Error", "Unable to fetch location")

# ---------------- GUI DESIGN ---------------- #
root = tk.Tk()
root.title("IP Scanner & Geolocation Finder")
root.geometry("450x400")

title = tk.Label(root, text="IP Scanner & Geolocation Finder",
                 font=("Arial", 14, "bold"))
title.pack(pady=10)

ip_label = tk.Label(root, text="Enter IP Address:")
ip_label.pack()

ip_entry = tk.Entry(root, width=30)
ip_entry.pack(pady=5)

scan_btn = tk.Button(root, text="Scan Ports", command=scan_ports)
scan_btn.pack(pady=5)

geo_btn = tk.Button(root, text="Get Geolocation", command=get_location)
geo_btn.pack(pady=5)

result_text = tk.Text(root, height=15, width=50)
result_text.pack(pady=10)

disclaimer = tk.Label(
    root,
    text="Educational use only. Scan IPs you own or have permission for.",
    font=("Arial", 8),
    fg="red"
)
disclaimer.pack()

root.mainloop()

