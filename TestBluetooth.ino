#include <Servo.h>
#include <SoftwareSerial.h>

#define rxPin 0 // Broche 1 en tant que RX, à raccorder sur TX du HC-05
#define txPin 1 // Broche 0 en tant que TX, à raccorder sur RX du HC-05

SoftwareSerial mySerial(rxPin, txPin);

Servo myservo1;
Servo myservo2;

int command;
int right;
int left;

void setup() {
  // Bluetooth
  // define pin modes for tx, rx pins:
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);
  mySerial.begin(9600);
  Serial.begin(9600);

  // Moteurs
  myservo1.attach(5);  // attaches the servo on pin 2
  myservo2.attach(6);  // attaches the servo on pin 3
  myservo1.write(90);
  myservo2.write(90);
}

void loop() {
  delay(10);
  command = 0;
  right = 90;
  left = 90;

  // when characters arrive over the serial port...
  if(Serial.available()) {
    command = Serial.read();

    if (command & 1) {
      left = left - 20;
      right = right + 20;
    } else if (command & 2) {
      left = left + 20;
      right = right - 20;
    }
    if (command & 4) {
      left = left - 15;
      right = right - 15;
    } else if (command & 8) {
      left = left + 15;
      right = right + 15;
    }

    myservo1.write(left);
    myservo2.write(right);
  }
}