#include <iostream>
using namespace std;

int main()
{
   int year, n;

   cout << "Enter the year: ";
   cin >> year;
   cout << "Enter the number of days: ";
   cin >> n;

   if (n % 4 = 0) {
       cout << "It's a leap year!" << endl;
      { if (year % 100 = 0 && year % 400 = 0)
         cout << "It's divisible by 100 and 400." << endl
      } else {
         cout << "It's not divisible!" << endl;
      }
   } else {
      cout << "It's not a leap year!" << endl;
   }

   return 0;
}
