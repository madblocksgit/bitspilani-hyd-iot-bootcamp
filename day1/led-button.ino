int button=6;
int led=3;

void setup() {
  pinMode(button,INPUT); // read permission
  pinMode(led,OUTPUT); // write permission
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(button)==0) // on (pressed)
    digitalWrite(led,1);
  else
    digitalWrite(led,0); // off (not pressed)
}
