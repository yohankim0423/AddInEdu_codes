int digits [10][7]
{
  {1,1,1,1,1,1,0}, // digit 0
  {0,1,1,0,0,0,0}, // digit 1
  {1,1,0,1,1,0,1}, // digit 2
  {1,1,1,1,0,0,1}, // digit 3
  {0,1,1,0,0,1,1}, // digit 4
  {1,0,1,1,0,1,1}, // digit 5
  {1,0,1,1,1,1,1}, // digit 6
  {1,1,1,0,0,0,0}, // digit 7
  {1,1,1,1,1,1,1}, // digit 8
  {1,1,1,1,0,1,1}, // digit 9
};

const int BUTTON_PIN = 13;
int clicks = 0;

void displayDigit(int d)
{
  if (digits[d][0]==1) digitalWrite(2, LOW); else digitalWrite(2, HIGH); //A
  if (digits[d][1]==1) digitalWrite(3, LOW); else digitalWrite(3, HIGH); //B
  if (digits[d][2]==1) digitalWrite(4, LOW); else digitalWrite(4, HIGH); //C
  if (digits[d][3]==1) digitalWrite(5, LOW); else digitalWrite(5, HIGH); //D
  if (digits[d][4]==1) digitalWrite(6, LOW); else digitalWrite(6, HIGH); //E
  if (digits[d][5]==1) digitalWrite(7, LOW); else digitalWrite(7, HIGH); //F
  if (digits[d][6]==1) digitalWrite(8, LOW); else digitalWrite(8, HIGH); //G

}

int buttonPress()
{
  int press;
  int buttonState;
  static int prevButtonState = LOW;
  buttonState = digitalRead(BUTTON_PIN);
  press = (buttonState == HIGH && prevButtonState == LOW);
  prevButtonState = buttonState;
  return press;
}

void setup() {
  // put your setup code here, to run once:
  pinMode(2, OUTPUT); // Segment A
  pinMode(3, OUTPUT); // Segment B
  pinMode(4, OUTPUT); // Segment C
  pinMode(5, OUTPUT); // Segment D
  pinMode(6, OUTPUT); // Segment E
  pinMode(7, OUTPUT); // Segment F
  pinMode(8, OUTPUT); // Segment G

}

void loop() {
  // put your main code here, to run repeatedly:
  if (buttonPress())
  {
    clicks++;
    if (clicks > 9)
    {
      clicks = 0;
    }
    displayDigit(clicks);
    Serial.println(clicks);
  }

}
