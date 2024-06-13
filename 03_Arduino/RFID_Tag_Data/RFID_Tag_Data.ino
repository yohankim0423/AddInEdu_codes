#include <SPI.h>
#include <MFRC522.h>

const int RST_PIN = 9;
const int SS_PIN = 10;
MFRC522 rc522(SS_PIN, RST_PIN);

void toBytes(byte* buffer, int data, int offset = 0)
{
  buffer[offset] = data & 0xFF;
  buffer[offset + 1] = (data >> 8) & 0xFF;
}

MFRC522::StatusCode checkAuth(int index, MFRC522::MIFARE_Key key)
{
  MFRC522::StatusCode status =
   rc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, index, &key, &(rc522.uid));
  
  if (status != MFRC522::STATUS_OK)
  {
    Serial.print("Authentication Failed : ");
    Serial.println(rc522.GetStatusCodeName(status));
  }

  return status;
}

MFRC522::StatusCode writeString(int index, MFRC522::MIFARE_Key key, String data)
{
  //check auth
  MFRC522::StatusCode status = checkAuth(index, key);
  if (status != MFRC522::STATUS_OK)
  {
    return status;
  }

  // convert string to char array
  char buffer[16];
  memset(buffer, 0x00, sizeof(buffer));
  data.toCharArray(buffer, data.length() + 1);

  // write data
  status == rc522.MIFARE_Write(index, (byte*)&buffer, 16);
  if (status != MFRC522::STATUS_OK)
  {
    Serial.print("Write Failed : ");
    Serial.println(rc522.GetStatusCodeName(status));
  }

  return status;
}

MFRC522::StatusCode writeInteger(int index, MFRC522::MIFARE_Key key, int data)
{
  // check auth
  MFRC522::StatusCode status = checkAuth(index, key);
  if (status != MFRC522::STATUS_OK)
  {
    return status;
  }

  // write integer
  byte buffer[16];
  memset(buffer, 0x00, sizeof(buffer));
  toBytes(buffer, data);

  status = rc522.MIFARE_Write(index, buffer, sizeof(buffer));
  if (status != MFRC522::STATUS_OK)
  {
    Serial.print("Write Failed : ");
    Serial.println(rc522.GetStatusCodeName(status));
  }

  return status;
}

MFRC522::StatusCode readString(int index, MFRC522::MIFARE_Key key, String& data)
{
  // check auth
  MFRC522::StatusCode status = checkAuth(index, key);
  if (status != MFRC522::STATUS_OK)
  {
    return status;
  }

  // read data
  byte buffer[18];
  byte length = 18;

  status = rc522.MIFARE_Read(index, buffer, &length);
  if (status != MFRC522::STATUS_OK)
  {
    Serial.print("Read Failed : ");
    Serial.print(rc522.GetStatusCodeName(status));
  }
  else
  {
    data = String((char*)buffer);
  }
  return status;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  SPI.begin();
  rc522.PCD_Init();
  Serial.println("start!");
}

void loop() {
  // put your main code here, to run repeatedly:
  String cmd = "";
  while (Serial.available() > 0)
  {
    cmd = Serial.readStringUntil('\n');
  }

  if (!rc522.PICC_IsNewCardPresent()) {
    return;
  }

  if (!rc522.PICC_ReadCardSerial()){
    return;
  }

  const int index = 60; // block index
  
  //set key value
  MFRC522::MIFARE_Key key;
  for (int i = 0; i<6; i++)
  {
    key.keyByte[i] = 0xFF;
  }
  
  MFRC522::StatusCode status;
  if (cmd.length() > 0)
  {
    Serial.print("cmd : ");
    switch(cmd.charAt(0))
    {
      case 'w':
        // Serial.println("write");
        // status = writeStrint(60, key, "nomaefg");
        // break;
        Serial.print("write ");
        switch (cmd.charAt(1))
        {
          case 's':
            Serial.println("string");
            status = writeString(60, key, "nomaefg");
            break;

          case 'i':
            Serial.println("integer");
            // String data;
            status = writeInteger(61, key, 32767);
            rc522.PICC_DumpToSerial(&(rc522.uid));
            // Serial.println(data);
            break;
          default:
            Serial.println("unknown type");
            status = MFRC522::STATUS_ERROR;
            break;
        }
        break;

    }

    if (status == MFRC522::STATUS_OK)
    {
        Serial.println("success!");
    }

  }

  // if (cmd.length() > 0 && cmd == "w")
  // {
  //   Serial.print("cmd : ");
  //   Serial.println(cmd);
  // }
  // else
  // {
  //   return;
  // }

    // set key value
  // MFRC522::MIFARE_Key key;
  // for (int i = 0; i < 6; i++)
  // {
  //   key.keyByte[i] = 0xFF;
  // }

  // //check auth
  // status = rc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, index, &key, &(rc522.uid));
  // if (status !=MFRC522::STATUS_OK)
  // {
  //   Serial.print("Authentication Failed : ");
  //   Serial.println(rc522.GetStatusCodeName(status));
  //   return;
  // }

  //define buffer
  // char data[16];
  // memset(data, 0x00, sizeof(data));
  // //string to char array
  // String name = "nomaefg";
  // name.toCharArray(data, name.length() + 1);
  // //write data
  // status = rc522.MIFARE_Write(index, (byte*)&data, 16);
  // if (status != MFRC522::STATUS_OK)
  // {
  //   Serial.print("Write Failed : ");
  //   Serial.println(rc522.GetStatusCodeName(status));
  //   return;
  // }
  // rc522.PICC_DumpToSerial(&(rc522.uid));
  // delay(100);

}