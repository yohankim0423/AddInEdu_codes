#include <Servo.h>

Servo servo;
bool flag;

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(9);
  servo.write(0);
  flag = 0;
}

void loop() 
{
  // put your main code here, to run repeatedly:
  int light = analogRead(A0);
  Serial.println(light);

  if (light > 700)
  {
    if (flag == 0) 
    {
      servo.write(20);
      delay(400);
      flag = 1;
    }
  }

  if (light < 700)
  {
    if (flag == 1)
    {
      servo.write(0);
      delay(0);
      flag = 0;
    }
  }
  
}
