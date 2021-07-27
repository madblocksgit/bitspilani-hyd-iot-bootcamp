int pir=7;
int buzzer=8;

void setup() {
  pinMode(buzzer,OUTPUT);
  pinMode(pir,INPUT);
  Serial.begin(9600);
}

void loop() {
  int m=digitalRead(pir);
  if(m==1) // motion detected
    digitalWrite(buzzer,1);
  else
    digitalWrite(buzzer,0);
}
