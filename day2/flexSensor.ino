
int flexSensor=A0;

void setup() {
  pinMode(flexSensor,INPUT);
  Serial.begin(9600);
}

void loop() {
  int m=analogRead(flexSensor); // reading
  Serial.println(m); // logging
}
