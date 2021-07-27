int led=3;

void setup() {
  
  // GPIO - Port Declaration
  pinMode(led,OUTPUT); // write for pin 3
}

void loop() {
  digitalWrite(led,1); // ON State
}
