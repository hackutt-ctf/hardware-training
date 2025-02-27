const String correctPin = "1234";
String enteredPin = "";

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("Entrez le code PIN : ");
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read(); 

    if (receivedChar == '\n' || receivedChar == '\r') {
      if (enteredPin == correctPin) {
        Serial.println("Code correct !");
      } else {
        Serial.println("Code incorrect !");
      }
      enteredPin = "";
      Serial.println("Entrez le code PIN : ");
    } else {
      enteredPin += receivedChar;
    }
  }
}

