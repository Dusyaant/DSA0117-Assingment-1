#include <iostream>
#include <string>
#include <cctype>

using namespace std;

class StringConverter {
private:
    string originalString;

public:
    // Constructor
    StringConverter(string str) {
        originalString = str;
    }

    // Function to convert string to uppercase
    string toUpperCase() {
        string upperStr = originalString;
        for (int i = 0; i < upperStr.length(); i++) {
            upperStr[i] = toupper(upperStr[i]);
        }
        return upperStr;
    }

    // Function to convert string to lowercase
    string toLowerCase() {
        string lowerStr = originalString;
        for (int i = 0; i < lowerStr.length(); i++) {
            lowerStr[i] = tolower(lowerStr[i]);
        }
        return lowerStr;
    }

    // Function to display the conversions
    void displayConversions() {
        cout << "The string in upper case: " << toUpperCase() << endl;
        cout << "The string in lower case: " << toLowerCase() << endl;
    }
};

int main() {
    string input;

    cout << "Enter the string: ";
    getline(cin, input);

    // Create an object of StringConverter class
    StringConverter converter(input);

    // Display the conversions
    converter.displayConversions();

    return 0;
}