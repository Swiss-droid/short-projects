#include <iostream>
using namespace std;

int main() {

 float employeePensionFund = 0.075;   //7.5%
 float employerPensionFund = 0.13;
 float employeeContribution;
 int employeeSalary, employerSalary, employerContribution;

 cout << "Enter the employee salary: ";
 cin >> employeeSalary;
 cout << "Enter the employer's salary: ";
 cin >> employerSalary;

 employeeContribution = employeePensionFund * employeeSalary;
 employerContribution = employerPensionFund * employerSalary;

 cout << "The total pension fund contribution for the employee is R" << employeeContribution << "." << endl;
 cout << "The total pension fund contribution for the employer is R" << employerContribution << "." << endl;

 return 0;
}
