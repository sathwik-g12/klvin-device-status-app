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

## ⚙ Setup Instructions

### 1️ Clone the Repository

```bash
git clone https://github.com/<your-username>/klvin-device-status-app.git
cd klvin-device-status-app
