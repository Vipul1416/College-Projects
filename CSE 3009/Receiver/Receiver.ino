
#include <LiquidCrystal_I2C.h>
#include <VirtualWire.h>


// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x3f, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);

  const int buttonPin1=2;
  const int buttonPin2=4;
  const int ledPin1=8;
  int threshold=0;
  int buttonState1=0;
  int lastbuttonState1=0;
  int buttonState2=0;
  int lastbuttonState2=0;
  
// LED's
int ledPin = 13;
int ledPin2 = 7;
const int datain = 12;

// Sensors 
int Sensor1Data;

// RF Transmission container
char Sensor1CharMsg[4]; 

void setup() {
  // sets the digital pin as output
  pinMode(ledPin, OUTPUT);      
  pinMode(ledPin1,OUTPUT);
  pinMode(ledPin2,OUTPUT);
  pinMode(buttonPin1,INPUT);
  pinMode(buttonPin2,INPUT);
  
    // initialize the LCD 
  lcd.begin(16,2);
// Turn on the blacklight and print a message.
  lcd.backlight();
  lcd.setCursor(1, 0);
  lcd.print("Soil Moisture");
  lcd.setCursor(1, 1);
  lcd.print("measure system");
  delay(3000);
  lcd.clear();
    // VirtualWire 
    // Initialise the IO and ISR
    // Required for DR3100
    vw_set_ptt_inverted(true); 
    vw_set_rx_pin(datain);
    // Bits per sec
    vw_setup(2000);     
    
    // Start the receiver PLL running
    vw_rx_start();
    Serial.begin(9600);
    delay(300);
    Serial.println("Moisure and Threshold");
    delay(700);
           

} // END void setup

void loop(){
    
    buttonState1 = digitalRead(buttonPin1);
    buttonState2 = digitalRead(buttonPin2);
    
    //if(buttonState2==HIGH){ 
      if(buttonState1!=lastbuttonState1){
        if(buttonState1==HIGH){    
          threshold+=5;
          digitalWrite(ledPin1,HIGH);
        }   
        else{
          digitalWrite(ledPin1,LOW);
        }
        lastbuttonState1=buttonState1;
      }
      if(buttonState2!=lastbuttonState2){
        if(buttonState2==HIGH){    
          threshold-=1;
          digitalWrite(ledPin1,HIGH);
        }   
        else{
          digitalWrite(ledPin1,LOW);
        }
        lastbuttonState2=buttonState2;
      }
   lcd.setCursor(1,1);
   lcd.print("*Threshold: ");
   if(threshold<10 and threshold>=0) lcd.print(" ");
   lcd.print(threshold);
   //}
     
    uint8_t buf[VW_MAX_MESSAGE_LEN];
    uint8_t buflen = VW_MAX_MESSAGE_LEN;
    
    // Non-blocking
    if (vw_get_message(buf, &buflen)) 
    {
    int i;
        // Turn on a light to show received good message 
        digitalWrite(13, true); 
    
        // Message with a good checksum received, dump it. 
        for (i = 0; i < buflen; i++)
    {            
          // Fill Sensor1CharMsg Char array with corresponding 
          // chars from buffer.   
          Sensor1CharMsg[i] = char(buf[i]);
    }
        
        // Null terminate the char array
        // This needs to be done otherwise problems will occur
        // when the incoming messages has less digits than the
        // one before. 
        Sensor1CharMsg[buflen] = '\0';
        
        // Convert Sensor1CharMsg Char array to integer
        Sensor1Data = atoi(Sensor1CharMsg);

          lcd.setCursor(1, 0);
        lcd.print("*Moisture :");
        Serial.print("*Moisture :");
        if (Sensor1Data < 10) 
        {lcd.print("  "); 
        Serial.print("  ");
        }
        else
        {lcd.print(" "); 
        lcd.print(Sensor1Data);
        lcd.print("%");
        }
        //delay(3000);
        if(Sensor1Data<threshold){
            digitalWrite(7,true);
        }
        else{
            digitalWrite(7,false);
        }
        
        digitalWrite(13, false);
    }

    
       
        // Turn off light to and await next message
        //digitalWrite(13,true);
}
