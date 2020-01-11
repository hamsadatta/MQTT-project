#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <TinyGPS++.h>
#include <SoftwareSerial.h>
#define LED D0
char msg[9];
char msg1[9];
char msg2[9];
static const double LONDON_LAT = 13.61050457, LONDON_LON = 79.42950;

static const int RXPin = 12, TXPin = 13;
static const uint32_t GPSBaud = 9600;

// The TinyGPS++ object
TinyGPSPlus gps;

// The serial connection to the GPS device
SoftwareSerial ss(RXPin, TXPin);

const char* ssid = "vamsi1";
const char* password = "12345678";
const char* mqtt_server = "192.168.0.50";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
int value = 0;

void setup()
{
  Serial.begin(115200);
  ss.begin(GPSBaud);
  pinMode(LED,OUTPUT);
  digitalWrite(LED, HIGH);
  setup_wifi();
  client.setServer(mqtt_server, 1883);

}

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("inTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    snprintf (msg, 9, "%2.6f", gps.location.lat());
    Serial.println(msg);   
    snprintf (msg1, 9, "%3.6f", gps.location.lng());
    Serial.println(msg1);
    unsigned long distanceKmToLondon =(unsigned long)TinyGPSPlus::distanceBetween(gps.location.lat(),gps.location.lng(),LONDON_LAT, LONDON_LON) / 1000;
    snprintf (msg2, 9, "%d", distanceKmToLondon);
    Serial.println(msg2);
    client.publish("test7",msg); //test7=lat
    client.publish("test8",msg1); //test8=lon
    client.publish("test9",msg2); //test9=dist
  }
  else if((char)payload[0] == 'f') {
    
       digitalWrite(LED,LOW);
       delay(2000);
       digitalWrite(LED,HIGH);
  }
}


void loop()
{

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  long now = millis();
  if (now - lastMsg > 2000) {
      
  lastMsg = now;
  client.subscribe("test6");
  client.setCallback(callback);
  smartDelay(1000);
  }
}

// This custom version of delay() ensures that the gps object
// is being "fed".
static void smartDelay(unsigned long ms)
{
  unsigned long start = millis();
  do 
  {
    while (ss.available())
      gps.encode(ss.read());
  } while (millis() - start < ms);
}

