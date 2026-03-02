#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string number;

    cin >> number;

    string reversed = number;
    reverse(reversed.begin(), reversed.end());

    if (number == reversed) {
        cout << "It is palindrome" << endl;
    }
    else {
        cout << "It is not palindrome" << endl;
    }

    return 0;
}