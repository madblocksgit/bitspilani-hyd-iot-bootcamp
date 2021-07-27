int trig=3;
int echo=2;
int buzzer=8;
float duration;
float distance;

void setup() {
  pinMode(buzzer,OUTPUT);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  Serial.begin(9600);
}

void loop() {
  // Falling Edge - High to LOW
  digitalWrite(trig,LOW);
  delayMicroseconds(2);
  
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  
  duration=pulseIn(echo,HIGH); 
  distance=0.01723*duration;
  Serial.println(distance); // speed=distance/time
  
  if(distance<20)
    digitalWrite(buzzer,1);
  else
    digitalWrite(buzzer,0);
}
