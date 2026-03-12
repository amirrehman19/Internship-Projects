⚡ Auto Cut-Off Charger for Scooty

A safe and reliable automatic charging circuit for a 12V scooter battery, designed to prevent overcharging and extend battery life. This project leverages relays, diodes, voltage sensing, and a comparator to create an efficient cutoff system.

🔹 Features

Automatic Cut-Off – Stops charging when the battery is fully charged.

Overcharge Protection – Increases battery lifespan.

Relay-Based Switching – Ensures safe current handling.

Voltage Sensing – Uses LM358 comparator for precision.

LED Indicators – Shows charging and cutoff status.

DIY-Friendly – Built using readily available components.

🔹 Working Principle

The charger continuously monitors the battery voltage. When the voltage reaches the preset threshold (full charge), the comparator triggers the relay to disconnect the charger, preventing overcharging.

Green LED indicates charging in progress.

Red LED indicates battery is fully charged and charging is cut off.

The system is simple, reliable, and ideal for hobbyists or small projects requiring a 12V battery automatic charging solution.

🔹 Circuit Diagram


Circuit diagram simulated in Proteus showing the complete Auto Cut-Off Charger.

🔹 Component List
Component	Description	Quantity
TR1	230V AC to 12V AC Transformer	1
BR1	Bridge Rectifier	1
C1	Electrolytic Capacitor, 1000µF/25V	1
C2	Electrolytic Capacitor, 100µF/25V	1
U1	LM358 Comparator IC	1
R1	Resistor, 10kΩ	1
R2	Resistor, 220Ω	1
R4	Resistor, 1kΩ	1
R5	Resistor, 1Ω	1
R6	Resistor, 1MΩ	1
RV1	Preset Potentiometer, 15kΩ	1
Q1	BC547 NPN Transistor	1
RL1	12V Relay	1
D1, D3, D9, D10	1N4007 Diodes	4
D2	6A10 Diode	1
D5	LED Green	1
D7, D8	LED Red	2
D11	1N4738A Zener Diode	1
V1	12V Battery	1
🔹 How to Build

Assemble all components according to the schematic.

Connect the transformer, bridge rectifier, LM358 IC, relay, diodes, resistors, and capacitors.

Set the reference voltage using the preset potentiometer for your battery's full charge cutoff.

Test the system with a 12V battery to ensure automatic cutoff works properly.

Observe LED indicators to monitor charging status.

🔹 Notes & Tips

Ensure all connections are secure and polarity is correct for LEDs, diodes, and capacitors.

Use a fuse in series with the input AC line for extra safety.

Adjust RV1 slowly while monitoring battery voltage to avoid overvoltage.