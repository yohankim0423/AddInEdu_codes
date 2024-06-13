#include <Servo.h>

int pos = 0;
const int PUSH_BUTTON = 12;
bool flag;
bool direction;
Servo servo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(9);
  pinMode(PUSH_BUTTON, INPUT);
  flag = false;
  direction = true;

}

void loop() {

  int button_status = digitalRead(PUSH_BUTTON);

  if (button_status == HIGH) {
    if (flag == false) {
      flag = true;
      Serial.println("Push");
      if (direction == true) {
        if (pos < 180) {
        pos +=10;
        Serial.println(pos);
        }
        else if (pos == 180) {
          direction = false;
        }
       }
      else if (direction == false) {
        pos -= 10;
        Serial.println(pos);
       }
       if (pos == 0) {
        direction = true;
       }
      }
    }  
  if (button_status == LOW) {
    if (flag == true) {
      flag = false;
      Serial.println("Pull");
    }
  }

  servo.write(pos);
  delay(20);

}