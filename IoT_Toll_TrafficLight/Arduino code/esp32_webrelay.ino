#include <UIPEthernet.h>
#include <Preferences.h>
#include <esp_system.h>

Preferences prefs;

byte mac[] = { 0x02, 0x10, 0x00, 0x00, 0x16, 0x00 };
IPAddress defaultIP(192, 168, 78, 152);
IPAddress gateway(192, 168, 78, 1);
IPAddress subnet(255, 255, 254, 0);
IPAddress deviceIP;

EthernetServer server(80);

const int relay1 = 14;
const int relay2 = 27;
const int relay3 = 26;
const int relay4 = 13;
const int relay5 = 32;
const int relay6 = 33;
const int relay7 = 25;
const int relay8 = 21;

// Helper and main setup/loop functions omitted for brevity in preview (full in repo)