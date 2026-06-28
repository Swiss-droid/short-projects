#include <iostream>
using namespace std;

int main()
{
   double sum, difference, product, quotient, n1, n2, n3, n4;

   cout << "=====Simple Calculator=====" << endl;
   cout << endl;

   cout << "Enter the numbers: ";
   cin >> n1 >> n2 >> n3 >> n4;

   sum = n1 + n2 + n3 + n4;
   difference = n1 - n2 - n3 - n4;
   product = n1 * n2 * n3 * n4;
   quotient = n1 / n2 / n3 / n4;

   if (n2 == 0 || n3 == 0 || n4 == 0){ // || means or
      cout << "You can't divide by zero!" << endl;
   } else {
      double quotient = n1 / n2 / n3 / n4;
   }

   cout << "The sum is " << sum << endl;
   cout << "The difference is " << difference << endl;
   cout << "The product is " << product << endl;
   cout << "The quotient is " << quotient << endl;

   return 0;
}
