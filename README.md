# 🛰️ ISS Tracker – Real-Time Space Visualization Project

This project is a complete International Space Station (ISS) tracking system designed for both web and desktop platforms. It visualizes the live position, speed, and altitude of the ISS using real-time APIs and orbital prediction data. The goal is to provide an interactive, educational tool to understand how the ISS moves and where it orbits at any given time.

---

## 🌟 Project Highlights

### 🌐 Web-Based ISS Tracker
- Displays the **real-time location** of the ISS on a world map.
- **Live updating telemetry** including latitude, longitude, altitude, and speed.
- **Automatic refresh** every 10 seconds.
- **Reverse geolocation** to show the country or ocean below the ISS.
- Visual **yellow trail** showing the historical path of the ISS.
- Beautiful UI with dark mode and animated charts for:
  - 📈 Altitude (km)
  - 🚀 Speed (km/h)

### 🖥️ Desktop ISS Trajectory Simulation (Tkinter App)
- Predicts ISS trajectory over the **next 24 hours** using Two-Line Element (TLE) data.
- Simulates motion on a 2D map with colored trail path.
- Includes **real-time charts** (using `matplotlib`) for:
  - Speed in km/s
  - Altitude in km
- Displays region name, current time (UTC), and telemetry values.
- Smooth animation using GUI-based rendering with dynamic color visuals.

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `real_time_iss_tracker.html` | Web-based live ISS tracker built with JavaScript, HTML5 Canvas, and Chart.js |
| `iss_tracker_visualization.py` | Python desktop app with real-time simulation and charts using Tkinter and Skyfield |
| `iss_data.csv` | Sample or logged ISS telemetry data including position, speed, altitude, region |
| `requirements.txt` | Lists all Python libraries required for running the desktop app |
| `README.md` | Documentation file describing the project |

---

## 🧠 Technologies & Concepts Used

- **Skyfield Library**: For satellite tracking using TLE (Two Line Element) data
- **Chart.js**: Real-time chart rendering in the browser
- **Matplotlib**: Live charts in the desktop application
- **Pillow (PIL)**: Image handling for background maps
- **Geolocation API**: Identifies region under ISS in real-time
- **Tkinter**: GUI toolkit used for desktop-based visualization
- **Web APIs**: Fetches live ISS telemetry from open data sources

---

## 📊 Educational Impact

This project was designed as a self-driven research and development exercise. It helps in:

- Understanding how satellites orbit the Earth
- Working with real-time and predictive space data
- Visualizing complex data with interactive UI/UX
- Learning full-stack skills: HTML/CSS/JS + Python + APIs + Charts

---

## 📌 Notes

- The web version is lightweight and requires no server or backend.
- The desktop version uses precise orbital calculations based on NASA's TLE data.
- The charts update in real-time, giving insight into the dynamics of ISS movement.

---

## 📸 Visuals

- ISS real-time map view with trail
- Chart views showing altitude/speed over time
- Desktop Tkinter simulation interface
  ![image](https://github.com/user-attachments/assets/df5f088d-132f-4190-885c-638043d9c24f)
  ![image](https://github.com/user-attachments/assets/8586d5c5-e539-4b0a-8f4d-166fe75a2cc8)
  ![image](https://github.com/user-attachments/assets/102fd45e-8623-48e2-b431-4fe3117f8784)
  
  Visit website for real tracker - https://iss-tracker-web.web.app/
  [ISS_Tracker_Report.docx](https://github.com/user-attachments/files/20657858/ISS_Tracker_Report.docx)





---

## 🛰️ Credits

- TLE and orbital data from [Celestrak](https://www.celestrak.com/)
- Live telemetry API from [wheretheiss.at](https://wheretheiss.at/)
- Reverse geolocation by [OpenStreetMap via Maps.co](https://geocode.maps.co/)
- Developed by Vaibhav Rawat as part of a solo research & learning initiative
