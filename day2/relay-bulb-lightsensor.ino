
// Light --> Arduino --> Relay

int relay=2;
int light=3;

void setup() {
  pinMode(relay,OUTPUT);
  pinMode(light,INPUT);
}

void loop() {
  int m=digitalRead(light);
  if(m==0) {
    digitalWrite(relay,1); // relay - off (IN - 1 (5V) - 0)
    delay(1000);
  }    
  else {
    digitalWrite(relay,0); // relay - on (IN - 0 (0V) - 5V)
    delay(1000);
  }
  
}
