#include <iostream>
using namespace std;

int main()
{
   float num1, num2, sum, difference, product, quotient;
   char operationalSign;

   cout << "Enter the two numbers: ";
   cin >> num1 >> num2;

   cout << "Enter the operationalSign: ";
   cin >> operationalSign;

   if (operationalSign == "A"){
      sum = num1 + num2;
      cout << sum << endl;
   }

   if (operationalSign == "S") {
      difference = num1 - num2;
      cout << difference << endl;
   }

   if (operationalSign == "D") {
      quotient = num1 / num2;
      if (num2 == 0) {
         cout << "You can't divide by zero! Try again." << endl;
      } else {
         cout << quotient << endl;
      }
   }

   if (operationalSign == "M") {
      product = num1 * num2;
      cout << product << endl;
   }

}
