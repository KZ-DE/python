void setup() {
  Serial.begin(115200);
  pinMode(PC13, OUTPUT);
  analogWriteFrequency(50);  
}

void loop() {
  if (Serial.available() > 0) {
    int center_x = Serial.parseInt();
    Serial.read();                     
    int center_y = Serial.parseInt();  
    digitalWrite(PC13, LOW);
    int hasil = map(center_x, 190, 500, 0, 180);
    setServoAngle(A0, constrain(hasil, 0, 180));
  } else {
    digitalWrite(PC13, HIGH);
    setServoAngle(A0, 0 );
  }
}

float mapFloat(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

void setServoAngle(int pin, int angle) {
  int dutyCycle = mapFloat(angle, 0, 180, 5, 30);
  analogWrite(pin, dutyCycle);
}