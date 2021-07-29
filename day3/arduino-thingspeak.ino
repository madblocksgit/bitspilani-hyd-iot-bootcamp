#include "DHT.h"

DHT dht(2,DHT11);

void setup() {

  dht.begin();
  Serial.begin(9600);
}

void loop() {

  Serial.print("#"); // SOF
  Serial.print(dht.readTemperature());
  Serial.print(","); // Seperator
  Serial.print(dht.readHumidity());
  Serial.print(","); // Seperator
  Serial.println("~"); // EOF
  delay(1000);
}
