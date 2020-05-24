#include <iostream>
#include <cstring>

int main()
{
	char str[1000];
	std::cin >> str;
	int count = 0;
	for (int i = 0; i < strlen(str); i++)
		if (str[i] == 'b')
			count += 1;
	std::cout << count << std::endl;
	return 0;
}