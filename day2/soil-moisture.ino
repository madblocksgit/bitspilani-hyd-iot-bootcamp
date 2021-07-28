
// Soil Moisture Sensor

int soil=A0;

void setup() {
  pinMode(soil,INPUT); 
  Serial.begin(9600); // baud, (pins - 0,1)
}

void loop() {

  int m=analogRead(soil);
  Serial.println(m);
  delay(100); // 100ms
  
}
