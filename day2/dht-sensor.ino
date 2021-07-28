
#include "DHT.h"

// DHT is a class, created an object

DHT dht(2,DHT11);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {

  float temp=dht.readTemperature();
  float hum=dht.readHumidity();

  Serial.print("Temp: ");
  Serial.print(temp);
  Serial.print(", Hum: ");
  Serial.print(hum);
  Serial.println();
  delay(1000);
 
}

