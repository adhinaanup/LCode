#include <stdbool.h>
bool isPalindrome(int x) 
{
    if (x < 0) 
        return false;
    int digit = 0;
    long int s = 0;
    int num = x;

    while (x > 0)
    {
        digit = x % 10;
        s = s * 10 + digit;
        x = x / 10;
    }

    if (s==num)
        return 1;
    else
        return 0;
}
