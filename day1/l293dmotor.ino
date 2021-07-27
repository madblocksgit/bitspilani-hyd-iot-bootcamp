int en1=2;
int in1=3;
int in2=4;

void setup() {
  pinMode(en1,OUTPUT);
  pinMode(in1,OUTPUT);
  pinMode(in2,OUTPUT);
}

void loop() {
  digitalWrite(en1,1);
  digitalWrite(in1,1); // direction - 1
  digitalWrite(in2,0);
}
