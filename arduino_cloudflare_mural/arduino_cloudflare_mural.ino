const int tempoPot = A0;
const int colorCountPot = A1;
const int palettePot = A2;
const int rotatorPot = A3;
const int rotatorPot2 = A4;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char received = Serial.read();
    if (received == 'R') {
      int tempoValue = analogRead(tempoPot);
      int colorCountValue = analogRead(colorCountPot);
      int paletteValue = analogRead(palettePot);
      int newvalue = analogRead(rotatorPot);
      int newnewvalue = analogRead(rotatorPot2);

      // Send the raw analog values
      Serial.print(tempoValue);
      Serial.print(",");
      Serial.print(colorCountValue);
      Serial.print(",");
      Serial.print(paletteValue);
      Serial.print(",");
      Serial.print(newvalue);
      Serial.print(",");
      Serial.println(newnewvalue);
    }
  }
}
