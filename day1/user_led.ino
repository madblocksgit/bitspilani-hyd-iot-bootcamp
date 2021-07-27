int led=3;
void setup() {
  pinMode(led,OUTPUT);
  Serial.begin(9600); // baud, (pins - 0,1)
}

void loop() {
  Serial.println("LED ON - on");
  Serial.println("LED OFF - off");
  while(!Serial.available()); // 0 (no data) len(data) - off
  String a=Serial.readString();
  if(a=="on") 
    digitalWrite(led,1);
  else if(a=="off")
    digitalWrite(led,0);
}
