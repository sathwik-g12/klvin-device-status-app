# ⚡ Dynamic Device Status Web App

A full-stack web application that monitors and displays *real-time device status (Online/Offline)* for multiple companies using Flask, PostgreSQL, and Vanilla JavaScript.

---

## 🧩 Overview

This project dynamically tracks whether a device is online or offline based on its latest reading timestamp in the database.  
If the device has no record or its last update is older than 2 minutes, it is marked as offline, otherwise online.

It provides:
- REST API built with Flask + PostgreSQL
- Responsive frontend built with HTML, CSS, and JavaScript
- Auto-refresh every few seconds to update device statuses
- Dark mode, sorting, and search features for better UX

---

## 🛠 Tech Stack

*Backend*
- Python (Flask)
- PostgreSQL
- psycopg2
- Flask-CORS
- dotenv

*Frontend*
- HTML5, CSS3, Vanilla JavaScript
- Font Awesome (icons)
- Responsive grid layout

---

📋 Features

* [cite_start]*Company Selection:* A dynamic dropdown menu to select a company, populated from the backend[cite: 22, 91].
* [cite_start]*Device Display:* Devices for the selected company are shown as "tiles" or "cards"[cite: 24, 97].
* *Real-time Status:* Each device tile shows:
    * [cite_start]Device Name[cite: 26, 97].
    * [cite_start]Current Status (Online/Offline) with visual indicators (green/red)[cite: 24, 27, 97].
* [cite_start]*Automatic Refresh:* Device statuses automatically refresh every 8 seconds [cite: 100] [cite_start](Requirement was 10s [cite: 28]).
* *Bonus: Filtering & Sorting:*
    * [cite_start]A search bar to filter devices by name[cite: 94, 98].
    * [cite_start]A dropdown to sort devices alphabetically or by online status[cite: 95, 96, 98].
* [cite_start]*Bonus: Theme Toggle:* A dark mode/light mode toggle for the UI[cite: 90].


---

## ⚙ Setup Instructions

### 1️ Clone the Repository

```bash
git clone https://github.com/<your-username>/klvin-device-status-app.git
cd klvin-device-status-app
