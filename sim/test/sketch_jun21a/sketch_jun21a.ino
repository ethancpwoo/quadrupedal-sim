int flag = 0;
float x = 1;
float a = 1;
float b = 1;
float c = 1;
float d = 1; 
float e = 1;
float f = 1;
float g = 1;
float h = 1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(flag == 0) {
    if(Serial.available() > 0) {
      //Serial.println("Message is available");
      flag = 1;
      Serial.println("configed");
    }
    else {
      Serial.println("Nothing in buffer");
    }
  }
  else {
    Serial.flush();
    x = Serial.parseFloat();
    a = Serial.parseFloat();
    b = Serial.parseFloat();
    c = Serial.parseFloat();
    d = Serial.parseFloat();
    e = Serial.parseFloat();
    f = Serial.parseFloat();
    g = Serial.parseFloat();
    h = Serial.parseFloat();
    // //Serial.println(x);
    // Serial.println(a);
    // Serial.println(b);
    // Serial.println(c);
    // Serial.println(d);
    // Serial.println(e);
    // Serial.println(f);
    // Serial.println(g);
    // Serial.println(h);
  }

  
}
