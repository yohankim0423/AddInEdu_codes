const int SoundSensor = A0;
const int LED_R1 = 4;
const int LED_R2 = 5;
const int LED_Y3 = 6;
const int LED_Y4 = 7;
const int LED_G5 = 8;
const int LED_G6 = 9;
const int LED_B7 = 10;
const int LED_B8 = 11;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  int level = analogRead(SoundSensor);
  if (level <= 0)
  {
    level = 0;
  }
  else if (level >= 800)
  {
    level = 800;
  }

  if (level >= 50 && level < 100)
  {
    digitalWrite(LED_R1, HIGH);
    digitalWrite(LED_R2, LOW);
    digitalWrite(LED_Y3, LOW);
    digitalWrite(LED_Y4, LOW);
    digitalWrite(LED_G5, LOW);
    digitalWrite(LED_G6, LOW);
    digitalWrite(LED_B7, LOW);
    digitalWrite(LED_B8, LOW);
  }

  else if (level >= 120 && level < 140)
  {
    digitalWrite(LED_R1, HIGH);
    digitalWrite(LED_R2, HIGH);
    digitalWrite(LED_Y3, LOW);
    digitalWrite(LED_Y4, LOW);
    digitalWrite(LED_G5, LOW);
    digitalWrite(LED_G6, LOW);
    digitalWrite(LED_B7, LOW);
    digitalWrite(LED_B8, LOW);
  }

  else if (level >= 140 && level < 160)
  {
    digitalWrite(LED_R1, HIGH);
    digitalWrite(LED_R2, HIGH);
    digitalWrite(LED_Y3, HIGH);
    digitalWrite(LED_Y4, LOW);
    digitalWrite(LED_G5, LOW);
    digitalWrite(LED_G6, LOW);
    digitalWrite(LED_B7, LOW);
    digitalWrite(LED_B8, LOW);
  }

  else if(level >= 160 && level < 180)
  {
    digitalWrite(LED_R1, HIGH);
    digitalWrite(LED_R2, HIGH);
    digitalWrite(LED_Y3, HIGH);
    digitalWrite(LED_Y4, HIGH);
    digitalWrite(LED_G5, LOW);
    digitalWrite(LED_G6, LOW);
    digitalWrite(LED_B7, LOW);
    digitalWrite(LED_B8, LOW);
  }

  else if(level >= 180 && level < 200)
  {
    digitalWrite(LED_R1, HIGH);
    digitalWrite(LED_R2, HIGH);
    digitalWrite(LED_Y3, HIGH);
    digitalWrite(LED_Y4, HIGH);
    digitalWrite(LED_G5, HIGH);
    digitalWrite(LED_G6, LOW);
    digitalWrite(LED_B7, LOW);
    digitalWrite(LED_B8, LOW);
  }

  else if(level >= 200 && level < 220)
  {
    digitalWrite(LED_R1, HIGH);
    digitalWrite(LED_R2, HIGH);
    digitalWrite(LED_Y3, HIGH);
    digitalWrite(LED_Y4, HIGH);
    digitalWrite(LED_G5, HIGH);
    digitalWrite(LED_G6, HIGH);
    digitalWrite(LED_B7, LOW);
    digitalWrite(LED_B8, LOW);
  }

  else if(level >= 220 && level < 240)
  {
    digitalWrite(LED_R1, HIGH);
    digitalWrite(LED_R2, HIGH);
    digitalWrite(LED_Y3, HIGH);
    digitalWrite(LED_Y4, HIGH);
    digitalWrite(LED_G5, HIGH);
    digitalWrite(LED_G6, HIGH);
    digitalWrite(LED_B7, HIGH);
    digitalWrite(LED_B8, LOW);
  }
  else
  {
    digitalWrite(LED_R1, LOW);
    digitalWrite(LED_R2, LOW);
    digitalWrite(LED_Y3, LOW);
    digitalWrite(LED_Y4, LOW);
    digitalWrite(LED_G5, LOW);
    digitalWrite(LED_G6, LOW);
    digitalWrite(LED_B7, LOW);
    digitalWrite(LED_B8, LOW);
  }


  Serial.println(level);
  delay(200);
}
