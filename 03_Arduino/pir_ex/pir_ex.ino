const int PIR = 2;
const int LED = 4;
int count = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(PIR, INPUT);
  pinMode(LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int tmp = digitalRead(PIR);

  // Serial.println(tmp);
  
  if (count == 500 && tmp != 1)
  {
    count = 0;
    digitalWrite(LED, tmp);
    Serial.println("No one is here!");
  }
  else if (count != 500 && tmp == 1)
  {
    count = 0;
    digitalWrite(LED, tmp);
    Serial.println("Five more seconds!");
  }
  else
  {
    count++;
  } 
  // Serial.println(count);
  delay(10);
}