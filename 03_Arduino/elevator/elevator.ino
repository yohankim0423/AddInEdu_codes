const int R_LED[3] = {A0, 4, 7};
const int Y_LED[4] = {2, 3, 5, 6};
const int G_LED[3] = {8, 9, 10};
const int BUTTON[3] = {11, 12, 13};

// 버튼의 마지막 상태를 저장하는 배열
int lastButtonState[3] = {LOW, LOW, LOW}; // 초기 상태는 눌리지 않은 상태(LOW)로 설정

// LED의 상태를 저장하는 배열 (0은 꺼짐, 1은 켜짐)
int ledState[3] = {LOW, LOW, LOW};

// 현재 층을 나타내는 변수, 1층에서 시작
int currentFloor = 0; // R_LED 배열에서 1층을 나타내는 인덱스는 0입니다.

void setup() {
  for (int i = 0; i < 3; i++) {
    pinMode(R_LED[i], OUTPUT);
    pinMode(G_LED[i], OUTPUT);
    digitalWrite(G_LED[i], LOW); // G_LED를 꺼진 상태로 초기화
    if (i < 4) {
      pinMode(Y_LED[i], OUTPUT);
    }
    pinMode(BUTTON[i], INPUT_PULLUP);
  }
  digitalWrite(R_LED[currentFloor], HIGH); // 시작 시 1층 R_LED를 켜짐 상태로 설정
}

void loop() {
  for (int i = 0; i < 3; i++) {
    int currentButtonState = digitalRead(BUTTON[i]);

    // 버튼의 상태가 마지막으로 확인했던 것과 다르고, 버튼이 눌렸다면
    if (currentButtonState != lastButtonState[i] && currentButtonState == LOW)
    {
      digitalWrite(G_LED[i], HIGH);
      // 이전 층의 R_LED를 끄고, 새로운 층의 R_LED를 켜기
      digitalWrite(R_LED[currentFloor], LOW);
      
      // 현재 층에서 목적지 층까지의 모든 중간 층의 R_LED를 순차적으로 켜고 끄기
      int direction = (i > currentFloor) ? 1: -1; // 이동 방향 결정
      for (int floor = currentFloor; floor !=i; floor += direction)
      {
        digitalWrite(R_LED[floor], HIGH); // 중간 층의 R_LED를 켜기
        delay(1500); // 1.5초 동안 켜진 상태 유지
        digitalWrite(R_LED[floor], LOW); // 중간 층의 R_LED를 끄기
        
        // Y_LED 제어
        if (direction == 1 && floor < 2)
        { // 위로 이동 시 Y_LED 순차적으로 켜고 끄기
          digitalWrite(Y_LED[floor * 2], HIGH); // 첫 번째 Y_LED 켜기
          delay(1500);
          digitalWrite(Y_LED[floor * 2], LOW); // 첫 번째 Y_LED 끄기

          digitalWrite(Y_LED[floor * 2 + 1], HIGH); // 두 번째 Y_LED 켜기
          delay(1500);
          digitalWrite(Y_LED[floor * 2 + 1], LOW); // 두 번째 Y_LED 끄기
        }
        else if (direction == -1 && floor > 0)
        { // 아래로 이동 시 Y_LED 순차적으로 켜고 끄기
          digitalWrite(Y_LED[(floor - 1) * 2 + 1], HIGH); // 두 번째 Y_LED 켜기
          delay(1500);
          digitalWrite(Y_LED[(floor - 1) * 2 + 1], LOW); // 두 번째 Y_LED 끄기

          digitalWrite(Y_LED[(floor - 1) * 2], HIGH); // 첫 번째 Y_LED 켜기
          delay(1500);
          digitalWrite(Y_LED[(floor - 1) * 2], LOW); // 첫 번째 Y_LED 끄기
        }
      }
        
      // 최종 목적지 층의 R_LED를 켜기
      currentFloor = i;
      digitalWrite(R_LED[currentFloor], HIGH);
      delay(1500); // 목적지 층에서 1.5초 동안 R_LED를 켜진 상태로 유지
      digitalWrite(G_LED[i], LOW); // G_LED를 끄기
        
      
    }

    // 마지막 버튼 상태를 현재 상태로 업데이트
    lastButtonState[i] = currentButtonState;
  }

  // 엘리베이터의 층 이동 로직에 따라 R_LED를 업데이트하는 코드를 여기에 추가할 수 있습니다.
}
