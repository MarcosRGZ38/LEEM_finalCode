#include <SparkFun_u-blox_GNSS_v3.h>
#include <Wire.h>

SFE_UBLOX_GNSS myGNSS;


void setup(){
  delay(1000);

  Serial.begin(115200);
  while(!Serial){
    ; //wait for serial port to connect
  }
  
  Wire.begin();
  if(myGNSS.begin() == false){
    Serial.println(F("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing."));
    while (1);
  }

  myGNSS.setI2COutput(COM_TYPE_UBX);
}

void loop(){
  if(myGNSS.getPVT()){
    long latitude = myGNSS.getLatitude();
    long longuitude = myGNSS.getLongitude();
    long altitude = myGNSS.getAltitude();
    long all = 1000*latitude + 10*longuitude + altitude;
    Serial.println(all);
  
  }

  if(myGNSS.getNAVHPPOSECEF()){
    long accuracy = myGNSS.getPositionAccuracy();
    Serial.println(accuracy);
  }
  
}
