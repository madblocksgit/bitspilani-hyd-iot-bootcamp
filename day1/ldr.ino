// light sensor - A0

int light=A0;

void setup() {
  pinMode(light,INPUT);
  Serial.begin(9600);
}

void loop() {
  Serial.println(analogRead(light));
}
