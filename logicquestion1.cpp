#include <iostream>

/*
Three young men accused of stealing donuts from the C&D make the following statements:
1. A: “B is guilty, and C is innocent.”
2. B: “If A is guilty, then so is C.”
3. C: “I’m innocent, but at least one of the others is guilty.”

(a) If all these statements are true, who is guilty? 
*/

using namespace std;
int main(void)
{
    cout << "question a: ";
    for (char guilt = 'A'; guilt <= 'C'; ++guilt)
    {
        bool statement1 = guilt == 'B' && guilt != 'C';
        bool statement2 = guilt != 'A' || guilt == 'C';
        bool statement3 = guilt != 'C' && (guilt == 'A') + (guilt == 'B') >= 1;
        if (statement1 + statement2 + statement3 == 3)
            cout << guilt << " is guilty" << endl;
    }
}
