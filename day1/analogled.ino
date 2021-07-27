
// values range from 0 to 2^10 = 1024-1 = 1023
// 0 to 5V -> 0 to 1023 - 10bit ADC

int pot=A0;
int led=6;
void setup() {
  pinMode(led,OUTPUT);
  pinMode(pot,INPUT);
  Serial.begin(9600);
}

void loop() {
  
  analogWrite(led,analogRead(pot)); // 0 to 1023
}
