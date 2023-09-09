// Define the maximum number of ICs and connections
const int MAX_ICS = 10;
const int MAX_CONNECTIONS = 14;

// Struct to store the mapping of an Arduino pin to an IC pin
struct ICPinMapping {
  int arduinoPin;
  int icPin;
};

// Array to store the pin mappings for all the ICs
ICPinMapping pinMappings[MAX_ICS][MAX_CONNECTIONS];

void setup() {
  Serial.begin(9600); // Initialize Serial Monitor
}

void loop() {
  int numICs; // Variable to store the number of ICs

  // User input of number of ICs to detect
  Serial.print("Enter the number of ICs to detect: ");
  while (!Serial.available()) {} // Wait for user input
  numICs = Serial.parseInt(); // Read user input as integer
  Serial.read();
  Serial.println(numICs); // Print newline

  int numConnections[numICs]; // Array to store the number of connections for each IC

  // Loop for each IC
  for (int i = 0; i < numICs; i++) {
    // User input of number of connections for the current IC
    Serial.print("Enter the number of connections for IC ");
    Serial.print(i + 1);
    Serial.print(": ");
    while (!Serial.available()) {} // Wait for user input
    numConnections[i] = Serial.parseInt(); // Read user input as integer
    Serial.read();
    Serial.println(numConnections[i]); // Print newline

    // Loop for detecting pin mappings for the current IC
    for (int j = 0; j < numConnections[i]; j++) {
      // User input of Arduino pin number connected to the IC pin
      Serial.print("Enter the Arduino pin number for connection ");
      Serial.print(j + 1);
      Serial.print(" of IC ");
      Serial.print(i + 1);
      Serial.print(": ");
      while (!Serial.available()) {} // Wait for user input
      pinMappings[i][j].arduinoPin = Serial.parseInt(); // Read user input as integer
      Serial.read();
      Serial.println(pinMappings[i][j].arduinoPin); // Print newline

      // User input of IC pin number corresponding to the Arduino pin
      Serial.print("Enter the IC pin number corresponding to Arduino pin ");
      Serial.print(pinMappings[i][j].arduinoPin);
      Serial.print(": ");
      while (!Serial.available()) {} // Wait for user input
      pinMappings[i][j].icPin = Serial.parseInt(); // Read user input as integer
      Serial.read();
      Serial.println(pinMappings[i][j].icPin); // Print newline
    }
  }

for (int i = 0; i < numICs; i++) {
  for (int j = 0; j < numConnections[i]; j++) {  
    pinMode(pinMappings[i][j].arduinoPin, INPUT);
    int inputvalue = digitalRead(pinMappings[i][j].arduinoPin);
    Serial.print("IC");
    Serial.print(i+1);
    Serial.print(" Pin ");
    Serial.print(pinMappings[i][j].icPin);
    Serial.print(" Value: ");
    Serial.println(inputvalue);
    delay(1100);
  }
}
delay(1000);
// Loop through all ICs
for (int i = 0; i < numICs; i++) {
  ICPinMapping* currentMappings = pinMappings[i];
  
  // Loop through all the connections for the current IC
  for (int j = 0; j < numConnections[i]; j++) {
    int currentICPin = currentMappings[j].icPin;
    int arduinoPin = currentMappings[j].arduinoPin;
    // Loop through all the other ICs
    for (int k = i + 1; k < numICs; k++) {
      ICPinMapping* otherMappings = pinMappings[k];
      
      // Loop through all the connections for the other IC
      for (int l = 0; l < numConnections[k]; l++) {
        int otherICPin = otherMappings[l].icPin;
        int otherarduinoPin = otherMappings[l].arduinoPin;      
        int outputPin1Input = arduinoPin, inputPin2Input = otherarduinoPin;
        pinMode(outputPin1Input, OUTPUT);
        digitalWrite(outputPin1Input, HIGH);
        pinMode(inputPin2Input, INPUT_PULLUP);
        delay(1000);
        int inputState2 = digitalRead(inputPin2Input);
        digitalWrite(outputPin1Input, LOW);
        delay(1000);
        int inputState3 = digitalRead(inputPin2Input);
        Serial.print("Continuity between IC pin ");
        Serial.print(currentICPin);
        Serial.print(" (IC");
        Serial.print(i + 1);
        Serial.print(") and IC pin ");
        Serial.print(otherICPin);
        Serial.print(" (IC");
        Serial.print(k + 1);
        Serial.print("): ");
        if (inputState2 == HIGH && inputState3 == LOW) {
          Serial.println("Yes"); // Print "No" if continuity is not detected
        } else {
          Serial.println("No");  // Print "Yes" if continuity is detected
        }
        delay(1000);
      }
    }
  }
}
}