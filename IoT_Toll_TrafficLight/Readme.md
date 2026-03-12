<div align="center">

<!-- Animated Banner -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:1a3a5c,50:2e75b6,100:00c853&height=200&section=header&text=🚦%20IoT%20Toll%20Traffic%20Light&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=URL-Based%20Highway%20Signal%20Control%20System&descAlignY=58&descColor=a8d8f0&animation=fadeIn"/>

<br/>

<!-- Badges Row 1 -->
<img src="https://img.shields.io/badge/Platform-ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white"/>
<img src="https://img.shields.io/badge/MCU-Arduino%20Nano-00979D?style=for-the-badge&logo=arduino&logoColor=white"/>
<img src="https://img.shields.io/badge/Network-ENC28J60%20Ethernet-1a3a5c?style=for-the-badge&logo=ethernet&logoColor=white"/>
<img src="https://img.shields.io/badge/Control-Web%20%2F%20URL-2e75b6?style=for-the-badge&logo=googlechrome&logoColor=white"/>

<br/><br/>

<!-- Badges Row 2 -->
<img src="https://img.shields.io/badge/LEDs-354%20per%20unit-FFD700?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQTUgNSAwIDAgMCA3IDdhNSA1IDAgMCAwIDUgNXY4aDJWMTJhNSA1IDAgMCAwIDUtNUE1IDUgMCAwIDAgMTIgMnoiLz48L3N2Zz4=&logoColor=black"/>
<img src="https://img.shields.io/badge/Protocol-HTTP%20REST-00c853?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Use%20Case-Toll%20Booth%20%2F%20Highway-ff6f00?style=for-the-badge&logo=roadmap&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-blueviolet?style=for-the-badge"/>

<br/><br/>

> **A smart, web-controlled traffic light system for highways and toll booths.**  
> Red and green high-power LED arrays signal *Stop & Pay* or *Payment Complete*,  
> controlled remotely over a network using **ESP32**, **ENC28J60**, and **Arduino Nano**.

<br/>

</div>

---

## 📖 Table of Contents

- [✨ Features](#-features)
- [🏗️ System Architecture](#️-system-architecture)
- [⚙️ Hardware Components](#️-hardware-components)
- [🔌 Wiring & Pin Connections](#-wiring--pin-connections)
- [🌐 Web Control Interface](#-web-control-interface)
- [🔧 How to Build](#-how-to-build)
- [💡 Working Principle](#-working-principle)
- [🌍 Importance & Applications](#-importance--applications)
- [⚠️ Safety Notes](#️-safety-notes)
- [❤️ Acknowledgements](#️-acknowledgements)

---

## ✨ Features

<div align="center">

| Feature | Description |
|:-------:|:------------|
| 🌐 **Web-Controlled** | Change light states via simple URL commands from any browser |
| 🔌 **ESP32 + ENC28J60** | Network-enabled IoT device for high-speed, wired response |
| ⚡ **High-Power LEDs** | 354 LEDs per unit — split across green and red arrays |
| 🔁 **8-Channel Relay** | Isolated relay switching for robust power control |
| 🚦 **Toll Booth Ready** | Engineered for highway overhead mounting |
| 📡 **REST API** | Extend and integrate with larger traffic management systems |

</div>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        OPERATOR TERMINAL                        │
│              Browser  →  http://<ip>/stop  or  /go              │
└───────────────────────────┬─────────────────────────────────────┘
                            │  HTTP GET Request (LAN)
                            ▼
┌───────────────────────────────────────┐
│         ENC28J60 Ethernet Module      │  ◄─── SPI Bus ───►  ESP32
│         (Wired Network Interface)     │
└───────────────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────┐
│              ESP32 Core               │
│   Parses URL  →  Sets GPIO Outputs    │
│   GPIO14 / GPIO27 / GPIO26 / GPIO15   │
│   GPIO32 / GPIO33 / GPIO25 / GPIO21   │
└───────────────────────────────────────┘
                            │  GPIO Signal Lines
                            ▼
┌───────────────────────────────────────┐
│           Arduino Nano                │
│       (Relay Drive Logic)             │
└───────────────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────┐
│        8-Channel Relay Module         │
│      LN1─LN4 (RED)  │  LN5─LN8 (GREEN) │
└──────────────┬────────────────────────┘
               │
       ┌───────┴────────┐
       ▼                ▼
 ┌──────────┐     ┌──────────┐
 │ RED LED  │     │ GREEN LED│
 │  DRIVER  │     │  DRIVER  │
 └────┬─────┘     └────┬─────┘
      ▼                ▼
 🔴 RED ARRAY     🟢 GREEN ARRAY
  (354 LEDs)       (354 LEDs)
  [ STOP / PAY ]  [ GO / CLEAR ]
```

---

## ⚙️ Hardware Components

| # | Component | Model / Spec | Qty | Role |
|---|-----------|-------------|-----|------|
| 1 | **ESP32 Dev Board** | ESP32-WROOM-32 | 1 | Main controller + HTTP web server |
| 2 | **ENC28J60 Ethernet** | SPI, 3.3V logic | 1 | Wired network interface |
| 3 | **Arduino Nano** | ATmega328P, 5V | 1 | Relay control logic |
| 4 | **8-Channel Relay Module** | 5V coil, 10A/250VAC | 1 | Power switching |
| 5 | **High-Power LED Array — Red** | 354 LEDs total | 1 | STOP signal |
| 6 | **High-Power LED Array — Green** | 354 LEDs total | 1 | GO / clear signal |
| 7 | **LED Driver Board** | Constant current | 2 | Drive LED arrays |
| 8 | **3.3V Power Regulator** | 5V → 3.3V | 1 | Voltage conversion for ENC28J60 |
| 9 | **Ethernet Cable** | CAT5e / CAT6 | 1 | Network connection |
| 10 | **Weatherproof Enclosure** | IP65+ rated | 1 | Outdoor mounting |

---

## 🔌 Wiring & Pin Connections

### ESP32 ↔ ENC28J60 (SPI)

| ENC28J60 Pin | ESP32 GPIO | Notes |
|:------------:|:----------:|-------|
| `Vcc (5V)` | `Vin` → 3.3V converted | Voltage stepped down for ESP32 logic level |
| `GND` | `GND` | Common ground |
| `SCK` | `GPIO18` | SPI Clock |
| `SO` *(MISO)* | `GPIO19` | Master In Slave Out |
| `SI` *(MOSI)* | `GPIO23` | Master Out Slave In |
| `CS` | `GPIO05` | Chip Select (active LOW) |

---

### ESP32 GPIO → Relay Module

| Relay Channel | ESP32 GPIO | Function |
|:-------------:|:----------:|----------|
| `LN1` | `GPIO14` | Relay Channel 1 |
| `LN2` | `GPIO27` | Relay Channel 2 |
| `LN3` | `GPIO26` | Relay Channel 3 |
| `LN4` | `GPIO15` | Relay Channel 4 |
| `LN5` | `GPIO32` | Relay Channel 5 |
| `LN6` | `GPIO33` | Relay Channel 6 |
| `LN7` | `GPIO25` | Relay Channel 7 |
| `LN8` | `GPIO21` | Relay Channel 8 |

---

### Relay Module Power

| Relay Pin | Source | Notes |
|:---------:|:------:|-------|
| `VCC (5V)` | 5V Supply | Powers relay coils |
| `GND` | Common GND | Shared ground reference |

---

## 🌐 Web Control Interface

The ESP32 hosts a lightweight HTTP server on your local network. Control the traffic light by navigating to URL endpoints in any browser or HTTP client.

### Endpoints

```http
GET http://<device-ip>/stop     →  🔴 RED ON   |  🟢 GREEN OFF
GET http://<device-ip>/go       →  🟢 GREEN ON  |  🔴 RED OFF
GET http://<device-ip>/status   →  📊 Returns current state (JSON)
```

### Example

```bash
# Turn on STOP signal (Red LEDs)
curl http://192.168.1.50/stop

# Turn on GO signal (Green LEDs)
curl http://192.168.1.50/go

# Check current state
curl http://192.168.1.50/status
# → {"state": "go", "red": false, "green": true}
```

---

## 🔧 How to Build

**Step 1 — Assemble Nano + Relay Module**

Mount the Arduino Nano alongside the 8-channel relay module. Connect digital output pins `D2–D9` to `IN1–IN8`. Power the relay module from a dedicated 5V rail.

**Step 2 — Wire LED Drivers to Relays**

Connect the constant-current LED driver boards to relay `NO` (Normally Open) contacts. Assign `LN1–LN4` to the Red array driver and `LN5–LN8` to the Green array driver.

**Step 3 — Connect ESP32 + ENC28J60**

Wire SPI connections per the table above. Step down the 5V supply to 3.3V for the ENC28J60. Connect ESP32 GPIO relay lines (`GPIO14–GPIO21`) to the Nano control input bus.

**Step 4 — Flash Firmware**

Upload the ESP32 sketch via **Arduino IDE** or **PlatformIO**. Set your static IP, subnet, and gateway in the config block. Flash the Arduino Nano relay sketch. Test all URL endpoints on the local network before deployment.

**Step 5 — Mount LED Arrays**

Install red and green LED arrays on highway poles at a height of **5–7 m** for visibility. Use **IP65+** weatherproof enclosures. Route cabling back to the control box.

**Step 6 — Deploy at Toll Booth**

Connect via RJ45 Ethernet to the toll booth local network. Issue `/stop` and `/go` commands from the operator terminal and verify switching. Apply firewall rules restricting access to authorized terminals only.

---

## 💡 Working Principle

```
Operator issues URL command
        │
        ▼
ENC28J60 receives Ethernet frame
        │
        ▼
ESP32 parses HTTP route (/stop or /go)
        │
        ▼
ESP32 sets GPIO pins HIGH/LOW
        │
        ▼
Arduino Nano reads GPIO signal lines
        │
        ▼
Nano drives 8-channel relay module
        │
    ┌───┴───┐
    ▼       ▼
RED Driver  GREEN Driver
activated   activated
    │           │
    ▼           ▼
🔴 STOP      🟢 GO
```

- 🔴 **Red LEDs** → Driver ON → Relay energized → *"Stop & Pay"*
- 🟢 **Green LEDs** → Driver ON → Relay energized → *"Payment Complete — Proceed"*

---

## 🌍 Importance & Applications

This project addresses a real infrastructure need at highway toll checkpoints by replacing manual operator signaling with a reliable, networked IoT solution.

**Benefits:**
- ✅ Eliminates human signaling errors at toll gates
- ✅ Faster vehicle throughput with instant electronic switching
- ✅ Remote operation reduces staffing requirements
- ✅ Audit trail via server-side HTTP request logging
- ✅ Scalable to multiple lanes from a single control panel

**Smart City Integration Potential:**
- 🔗 REST API enables integration with toll management software
- 📡 Extendable to MQTT for centralized city traffic dashboards
- 📷 ANPR camera integration for automatic payment verification
- 🔄 OTA firmware updates via ESP32 Wi-Fi fallback
- 📊 Data analytics on peak hours, wait times, and throughput

---

## ⚠️ Safety Notes

> **🔴 High Voltage Warning**  
> LED driver boards and relay output circuits may operate at mains voltage. All high-voltage wiring must be performed by a **qualified electrician**. Use properly rated enclosures and comply with local electrical codes.

> **🔒 Network Security**  
> Restrict access to the ESP32 server by IP allowlist or place the device on a dedicated VLAN. Avoid public internet exposure without a firewall. Consider HTTP basic authentication for endpoints.

> **🌧️ Weatherproofing**  
> All outdoor components must be **IP65 or higher**. Use UV-resistant conduit for cable runs. Inspect enclosure seals every 6 months in high-humidity environments.

---

## ❤️ Acknowledgements

- [Espressif ESP32 Documentation](https://docs.espressif.com/)
- [Microchip ENC28J60 Datasheet](https://www.microchip.com/en-us/product/ENC28J60)
- [Arduino Nano Reference](https://docs.arduino.cc/hardware/nano)
- [UIPEthernet Library](https://github.com/UIPEthernet/UIPEthernet)
- Arduino 8-Channel Relay Module — Generic Module Docs

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:00c853,50:2e75b6,100:1a3a5c&height=120&section=footer&animation=fadeIn"/>

**Built with ❤️ for smarter, safer highway infrastructure**  
*ESP32 · ENC28J60 · Arduino Nano · IoT · Smart City*

</div>