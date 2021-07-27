
// to print Hello World

void setup() {
  
  Serial.begin(9600); // baud, (pins - 0,1)
}

void loop() {
  Serial.println("Hello World!");
  delay(1000);
  
}

