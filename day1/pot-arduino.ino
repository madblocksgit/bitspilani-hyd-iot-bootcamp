
// values range from 0 to 2^10 = 1024-1 = 1023
// 0 to 5V -> 0 to 1023 - 10bit ADC

int pot=A0;

void setup() {
  pinMode(pot,INPUT);
  Serial.begin(9600);
}

void loop() {
  
  int m=analogRead(pot);
  Serial.println(m);
}
