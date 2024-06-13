const int SoundSensor = A0;
const int LED_LIST[] = {6, 7, 8, 9, 10, 11, 12, 13};
const int length = sizeof(LED_LIST) / sizeof (int);

int minSound = 100;
int maxSound = 500;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for (int i = 0; i < length; i++)
  {
    pinMode(LED_LIST[i], OUTPUT);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  int level = analogRead(SoundSensor);
  if (level < 55) 
  {
    level = 55;
  }
  else if (level > 1300)
  {
    level = 1300;
  }

  int volume = map(level, 55, 950, 0, sizeof(LED_LIST));

  // Serial.println(level);
  for (int i = 0; i < length; i++)
  { 
    if ((i + 1) <= volume)
    {
      digitalWrite(LED_LIST[i], HIGH);
    }
    else 
    {
      digitalWrite(LED_LIST[i], LOW);
    }
  }
}