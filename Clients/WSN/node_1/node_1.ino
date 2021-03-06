#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <String.h>
#include <dht.h>
dht DHT;

#define dhtp 5// dht11 pin - nodemcu 1
int pirp=4; // output of pir sensor- nodemcu 2

// Update these with values suitable for your network.
const char* ssid = "vamsi1";
const char* password = "12345678";
const char* mqtt_server = "192.168.0.50";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
char msg2[50];
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
    char msg3[]="Motion Detected";
    char msg4[]="Neutral";
    
    int chk = DHT.read11(dhtp);
    snprintf (msg, 75, "%.2f", DHT.temperature);//test1-temp
    Serial.println(msg);
    client.publish("test1", msg);

    snprintf (msg2, 75, "%.2f", DHT.humidity);
    Serial.println(msg2);
    client.publish("test2", msg2);//test2-humidity
    
    if(digitalRead(pirp) == HIGH) // reading the data from the pir sensor
    {
     Serial.println("Motion detected");
     client.publish("test3", msg3);//test3-intrusion
    }
    else {
     Serial.println("No Motion detected");
     client.publish("test3", msg4);//test5-intrusion
    }
    delay(2000);
  }
}
