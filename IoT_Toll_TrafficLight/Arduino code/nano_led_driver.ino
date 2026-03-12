// Arduino Nano Code to control LED drivers via MOSFET and relays

const int inputPin = 2;         // Connected to relay output from ESP32 circuit
const int greenMosfetPin = 3;   // Controls Green LED driver (NO)
const int redMosfetPin = 4;     // Controls Red LED driver (NC)

void setup() {
  pinMode(inputPin, INPUT);
  pinMode(greenMosfetPin, OUTPUT);
  pinMode(redMosfetPin, OUTPUT);
}

void loop() {
  int relayState = digitalRead(inputPin);

  if (relayState == HIGH) {
    // Relay is in NO position → turn GREEN ON, RED OFF
    digitalWrite(greenMosfetPin, HIGH);
    digitalWrite(redMosfetPin, LOW);
  } else {
    // Relay in NC → turn RED ON, GREEN OFF
    digitalWrite(greenMosfetPin, LOW);
    digitalWrite(redMosfetPin, HIGH);
  }

  delay(100); // slight debounce
}