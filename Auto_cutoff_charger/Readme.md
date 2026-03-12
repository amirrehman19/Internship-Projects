# ⚡ Auto Cut-Off Charger for Scooty
## Automatic 12V Battery Charging Circuit with Overcharge Protection

> 🔋 *Smart charging that knows when to stop — protecting your battery, extending its life.*

[![Domain](https://img.shields.io/badge/Domain-Analog%20Electronics-yellow?style=flat-square)]()
[![IC](https://img.shields.io/badge/IC-LM358%20Comparator-orange?style=flat-square)]()
[![Voltage](https://img.shields.io/badge/Battery-12V%20Lead--Acid-red?style=flat-square)]()
[![Switching](https://img.shields.io/badge/Switching-Relay%20Based-blue?style=flat-square)]()
[![Simulation](https://img.shields.io/badge/Simulation-Proteus-blueviolet?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)]()

---

## 📌 Project Overview

A **safe and reliable automatic charging circuit** for a 12V scooter battery — designed to prevent overcharging and extend battery life. The system uses an **LM358 comparator** for precision voltage sensing, **relay-based switching** for safe current handling, and **LED indicators** for real-time status monitoring.

> 💡 Simple, DIY-friendly, and built entirely from readily available components.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔌 **Automatic Cut-Off** | Stops charging the moment battery reaches full voltage |
| 🛡️ **Overcharge Protection** | Prevents voltage damage — significantly extends battery lifespan |
| 🔁 **Relay-Based Switching** | Handles high current safely with isolated relay contact |
| 📏 **Precision Voltage Sensing** | LM358 op-amp comparator monitors voltage continuously |
| 💡 **LED Indicators** | Green = Charging · Red = Fully charged / Cut-off |
| 🔧 **DIY-Friendly** | All components are inexpensive and widely available |

---

## ⚙️ Working Principle

```
┌─────────────────────────────────────────────────────────────┐
│                  CHARGING SYSTEM FLOW                       │
│                                                             │
│  230V AC Mains                                              │
│       │                                                     │
│       ▼                                                     │
│  TR1 Transformer (230V → 12V AC)                           │
│       │                                                     │
│       ▼                                                     │
│  BR1 Bridge Rectifier (AC → DC)                            │
│       │                                                     │
│       ▼                                                     │
│  C1 + C2 Filter Capacitors (Smooth DC)                     │
│       │                                                     │
│       ▼                                                     │
│  U1 LM358 Comparator                                        │
│  (Monitors battery voltage vs RV1 reference)               │
│       │                                                     │
│   ┌───┴────────────────────────┐                           │
│   ▼                            ▼                           │
│ Voltage < Threshold       Voltage = Full Charge            │
│                                                             │
│ 🟢 Green LED ON           🔴 Red LED ON                    │
│ Q1 Transistor OFF         Q1 Transistor ON                 │
│ RL1 Relay CLOSED          RL1 Relay OPEN                   │
│ ⚡ Charging IN PROGRESS   🛑 Charging CUT OFF              │
└─────────────────────────────────────────────────────────────┘
```

The **LM358 comparator** continuously compares the battery voltage against a **preset reference voltage** (adjusted via potentiometer RV1). The moment battery voltage hits the full-charge threshold, the comparator output switches — triggering **Q1 transistor** → energizing **RL1 relay** → disconnecting the charger.

---

## 💡 LED Status Indicators

| LED | Color | Status | Meaning |
|-----|-------|--------|---------|
| D5 | 🟢 **Green** | ON | Battery is charging |
| D7, D8 | 🔴 **Red** | ON | Battery fully charged — charger disconnected |

---

## 🧩 Component List

| Ref | Component | Specification | Qty |
|-----|-----------|--------------|-----|
| `TR1` | Transformer | 230V AC → 12V AC | 1 |
| `BR1` | Bridge Rectifier | Full-wave rectification | 1 |
| `C1` | Electrolytic Capacitor | 1000 µF / 25V | 1 |
| `C2` | Electrolytic Capacitor | 100 µF / 25V | 1 |
| `U1` | **LM358 Comparator IC** | Dual op-amp | 1 |
| `R1` | Resistor | 10 kΩ | 1 |
| `R2` | Resistor | 220 Ω | 1 |
| `R4` | Resistor | 1 kΩ | 1 |
| `R5` | Resistor | 1 Ω | 1 |
| `R6` | Resistor | 1 MΩ | 1 |
| `RV1` | **Preset Potentiometer** | 15 kΩ (cutoff threshold) | 1 |
| `Q1` | BC547 NPN Transistor | Relay driver | 1 |
| `RL1` | **12V Relay** | Main switching element | 1 |
| `D1,D3,D9,D10` | 1N4007 Diodes | Rectification & protection | 4 |
| `D2` | 6A10 Diode | High-current rectifier | 1 |
| `D5` | LED Green | Charging indicator | 1 |
| `D7, D8` | LED Red | Cut-off indicator | 2 |
| `D11` | 1N4738A Zener Diode | Voltage reference stabilizer | 1 |
| `V1` | 12V Battery | Load (scooter battery) | 1 |

---

## 🔧 How to Build

**Step 1 — Transformer & Rectifier**
Connect `TR1` to 230V AC input. Wire output to `BR1` bridge rectifier. Filter the DC output using `C1` and `C2` in parallel.

**Step 2 — Comparator Circuit**
Wire `U1 (LM358)` with `RV1` potentiometer setting the reference voltage on the non-inverting input. Connect battery voltage (through resistor divider) to the inverting input.

**Step 3 — Transistor & Relay**
Connect `Q1 (BC547)` base to the LM358 output via `R4`. Wire the collector to `RL1` relay coil. Add `D1` (flyback diode) across the relay coil for protection.

**Step 4 — LED Indicators**
Wire `D5 (Green LED)` with series resistor `R2` across the charging path. Wire `D7/D8 (Red LEDs)` to indicate relay activation (cut-off state).

**Step 5 — Calibration**
Connect a fully discharged 12V battery. Plug in the charger. Use a multimeter to monitor battery voltage. **Slowly adjust `RV1`** until the relay clicks off at your target full-charge voltage (typically **13.8V–14.4V** for lead-acid).

**Step 6 — Test**
Verify Green LED lights during charging. Confirm Red LED activates and relay disconnects at full charge. Re-test with a fully charged battery to confirm immediate cut-off.

---

## 🔬 Circuit Simulation

> Circuit designed and simulated in **Proteus** — verifying correct comparator switching, relay timing, and LED behavior before physical assembly.

---

## ⚠️ Safety Notes

> 🔴 **High Voltage Warning** — The transformer primary operates at **230V AC mains voltage**. All high-voltage wiring must follow local electrical safety codes.

| Safety Rule | Detail |
|-------------|--------|
| ⚡ Use a fuse | Place in series with AC input line |
| 🔌 Check polarity | LEDs, diodes, and capacitors are polarity-sensitive |
| 🎛️ Adjust RV1 slowly | Monitor voltage while calibrating to avoid overvoltage |
| 🌡️ Ventilate enclosure | Transformer generates heat during operation |
| 🔒 Enclose the circuit | Never leave mains-connected circuit exposed |

---

## ✅ Conclusion

This auto cut-off charger provides a **simple, reliable, and cost-effective** solution for safely charging 12V scooter batteries. The LM358 comparator ensures precision voltage detection, the relay provides robust switching, and the LED indicators give clear visual feedback — all from a circuit built entirely with common components.

> *"Charge smart — let the circuit decide when it's done."*

---

## 🛠️ Tools & Technologies

`LM358 Op-Amp Comparator` · `Relay Switching` · `BC547 Transistor` · `Bridge Rectifier` · `Proteus Simulation` · `Analog Circuit Design` · `12V Lead-Acid Battery`

---

## 👤 About

| | |
|-|---|
| 👨‍💻 **Engineer** | Amir Rehman |
| 🏛️ **Institution** | NUST — PNEC, Karachi |
| 🌐 **GitHub** | [@amirrehman19](https://github.com/amirrehman19) |

---

⬅️ *Back to [Internship Projects Portfolio](../README.md)*
