/**
	Automatically generated by Updater v1.0
	@author Daniel J. Finnegan
*/

#include <iostream>
#include "qrtracker.hpp"

int main(int argc, char **argv)
{
	int a = 5;
	int b = 6;
	QRTracker myQRTracker(a, b);

	int result = myQRTracker.computeNumber();

	std::cout << "The result is: " << result << std::endl;
	return 0;
}
