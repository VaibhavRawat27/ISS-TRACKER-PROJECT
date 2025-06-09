from skyfield.api import EarthSatellite, load, wgs84, utc
from datetime import datetime, timedelta
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# 🌍 Map Image Setup
MAP_IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/8/83/Equirectangular_projection_SW.jpg"
response = requests.get(MAP_IMAGE_URL)
img_data = BytesIO(response.content)
img = Image.open(img_data)

map_width, map_height = 800, 400
img = img.resize((map_width, map_height), Image.Resampling.LANCZOS)

# 🛰️ TLE Data
name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   25159.07052714  .00008601  00000+0  15816-3 0  9996"
line2 = "2 25544  51.6400 352.2516 0001632 195.4618 310.3088 15.50064259513748"

# Skyfield Setup
ts = load.timescale()
satellite = EarthSatellite(line1, line2, name)
now = datetime.utcnow().replace(tzinfo=utc)

# Predict Positions for 24 Hours
positions = []
speeds = []
altitudes = []

for i in range(1440):
    t = ts.utc(now + timedelta(minutes=i))
    geo = satellite.at(t)
    sp = wgs84.subpoint(geo)
    lat, lon = sp.latitude.degrees, sp.longitude.degrees
    alt = sp.elevation.km
    vel = geo.velocity.km_per_s
    speed = (vel[0]**2 + vel[1]**2 + vel[2]**2)**0.5

    positions.append((t.utc_datetime(), lat, lon))
    altitudes.append(alt)
    speeds.append(speed)

# Tkinter GUI Setup
root = tk.Tk()
root.title("🛰️ ISS Trajectory & Telemetry")
root.geometry("1000x800")

# Top canvas for map
frame_top = tk.Frame(root)
frame_top.pack()

tk_img = ImageTk.PhotoImage(img)
canvas = tk.Canvas(frame_top, width=map_width, height=map_height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)

# Convert lat/lon to x/y on map
def geo_to_canvas(lat, lon):
    x = (lon + 180) * (map_width / 360)
    y = (90 - lat) * (map_height / 180)
    return x, y

# Info Panel
info_label = tk.Label(root, text="Initializing...", font=("Arial", 12), anchor="w", justify="left")
info_label.pack(pady=5, fill='x')

# Charts using Matplotlib
fig, ax = plt.subplots(2, 1, figsize=(8, 4), dpi=100)
fig.tight_layout(pad=3.0)
speed_line, = ax[0].plot([], [], color='blue', label="Speed (km/s)")
alt_line, = ax[1].plot([], [], color='green', label="Altitude (km)")

for i in range(2):
    ax[i].legend()
    ax[i].grid(True)

canvas_chart = FigureCanvasTkAgg(fig, master=root)
canvas_chart.get_tk_widget().pack()

# Animate ISS
index = 0
x_data, speed_data, alt_data = [], [], []

def animate():
    global index
    if index < len(positions):
        t, lat, lon = positions[index]
        alt = altitudes[index]
        speed = speeds[index]

        # Draw trail with dynamic color
        x, y = geo_to_canvas(lat, lon)
        color = f"#{random.randint(50,255):02x}{random.randint(50,255):02x}{255 - index//6:02x}"
        canvas.create_oval(x-2, y-2, x+2, y+2, fill=color, outline="")

        # Update info label
        info = f"🛰️ Time (UTC): {t.strftime('%Y-%m-%d %H:%M:%S')}\n🌍 Lat: {lat:.2f}°, Lon: {lon:.2f}°\n🚀 Speed: {speed:.2f} km/s\n📏 Altitude: {alt:.2f} km"
        info_label.config(text=info)

        # Update chart
        x_data.append(index)
        speed_data.append(speed)
        alt_data.append(alt)

        speed_line.set_data(x_data, speed_data)
        alt_line.set_data(x_data, alt_data)

        ax[0].set_xlim(0, max(20, index + 1))
        ax[0].set_ylim(min(speed_data)-0.5, max(speed_data)+0.5)
        ax[1].set_xlim(0, max(20, index + 1))
        ax[1].set_ylim(min(alt_data)-10, max(alt_data)+10)
        canvas_chart.draw()

        index += 1
        root.after(50, animate)
    else:
        print("✅ Animation done.")

animate()
root.mainloop()
