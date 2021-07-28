// Bulb - My Home
// User - Faraway 

int relay=2;

void setup() {
  pinMode(relay,OUTPUT);
  Serial.begin(9600);
}

void loop() { //on

  while(Serial.available()) {
    String s=Serial.readString();
    if(s=="on") {
      digitalWrite(relay,0); // on
    } else if(s=="off") {
      digitalWrite(relay,1); // off
    }
  }
}
