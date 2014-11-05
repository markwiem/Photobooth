/*
This RFduino sketch demonstrates a full bi-directional Bluetooth Low
Energy 4 connection between an iPhone application and an RFduino.

This sketch works with the rfduinoLedButton iPhone application.

The button on the iPhone can be used to turn the green led on or off.
The button state of button 1 is transmitted to the iPhone and shown in
the application.
*/

#include <RFduinoBLE.h>

// pin 3 on the RGB shield is the red led
// (can be turned on/off from the iPhone app)
int led = 3;

// pin 5 on the RGB shield is button 1
// (button press will be shown on the iPhone app)
int button = 5;

int ledState = 0;
int buttonState = 0;
boolean set = false;

void setup() {
 
  Serial.begin(9600); 
  // led turned on/off from the iPhone app
  pinMode(led, OUTPUT);

  // button press will be shown on the iPhone app)
  pinMode(button, INPUT);
}

void loop() {
  
   if (Serial.available() > 0)
    {
     
      buttonState = digitalRead(button);
    
    if (buttonState == LOW)
    {
      //Serial.println("No");
      set = false;
      //Serial.println (set);
      //digitalWrite(led, HIGH);
    }
    if (buttonState == HIGH && set == false)
    {
      Serial.print("Button\r\n");
      set = true;
      Serial.println (set);
      //digitalWrite(led, LOW);
    }
    
    
     char light = Serial.read();
           
     if (light == '0')
     {
        digitalWrite(led, LOW);
     }
     if (light == '1')
     {
        digitalWrite(led, HIGH);
     }
   }
}
