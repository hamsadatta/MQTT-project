#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <String.h>
#include <dht.h>
dht DHT;

#define dhtp 5// dht11 pin - nodemcu 1
int pirp=4; // output of pir sensor- nodemcu 2
int led=14; // led pin
int buzzer=12;// buzzer pin

// Update these with values suitable for your network.
const char* ssid = "vamsi1";
const char* password = "12345678";
const char* mqtt_server = "192.168.0.50";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
////////////////////////////////////////////////////////////////////////////////


void setup_wifi()

{

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

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}


//////////////////////////////////////////////////////////////////////////////////

void reconnect() 
{
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "node1";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("test2", "hello world");
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

///////////////////////////////////////////////////////////////////////////////////////////

void setup()
{
pinMode(pirp, INPUT);// setting pir output as arduino input
pinMode(led, OUTPUT);//setting led as output
pinMode(buzzer, OUTPUT);//setting buzzer as output
digitalWrite(led, LOW); // setting led to low
digitalWrite(buzzer, LOW); // setting buzzer to low 
  
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

/////////////////////////////////////////////////////////////////////////////////////////////

void loop()
{

  if (!client.connected())
  {
    reconnect(); 
  }
  client.loop();

  long now = millis();
  if (now - lastMsg > 2000) 
  {
    lastMsg = now;
    char msg[]="Motion Detected";
     Serial.println("Motion detected");
     client.publish("test1", msg);

    delay(2000);
  }
}
