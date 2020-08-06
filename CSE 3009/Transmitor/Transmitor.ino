#include <VirtualWire.h>

// LED's
const int ledPin = 13;

// Sensors 
const int Sensor1Pin = A0;
 

int Sensor1Data;
int Sensor2Data;
char Sensor1CharMsg[4]; 

void setup() {

 // PinModes 
 // LED 
 pinMode(ledPin,OUTPUT);
 // Sensor(s)
 pinMode(Sensor1Pin,INPUT);

  vw_set_ptt_inverted(true);
  vw_set_tx_pin(12);

 // VirtualWire setup
 vw_setup(2000);     // Bits per sec

}

void loop() {
  
  // Read and store Sensor 1 data
  Sensor1Data = analogRead(Sensor1Pin);
  Sensor2Data = map(Sensor1Data, 1023,0,0,100);
  
  // Convert integer data to Char array directly 
  itoa(Sensor2Data,Sensor1CharMsg,10);
  
 digitalWrite(13, true); // Turn on a light to show transmitting
 vw_send((uint8_t *)Sensor1CharMsg, strlen(Sensor1CharMsg));
 vw_wait_tx(); // Wait until the whole message is gone
 digitalWrite(13, false); // Turn off a light after transmission
 delay(200); 
 
} // END void loop...
