#include <LiquidCrystal.h>

// create an object
LiquidCrystal lcd(12,11,5,4,3,2); // RS, EN, D4, D5, D6, D7

void setup() {
  lcd.begin(16,2); // 16 cols, 2 rows
  lcd.print("HELLO");
}

void loop() {
  lcd.clear();
  delay(1000);
  lcd.print("Hello World!!"); // first line
  lcd.setCursor(0,1);
  lcd.print("Hello Madhu!!"); // second line
  delay(1000); // 1000ms
}
