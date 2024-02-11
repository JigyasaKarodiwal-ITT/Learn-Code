#include <iostream>
#include <algorithm>


int kaprekar_calculation(int num) {
    int digits[4];
    for (int i = 3; i >= 0; --i) {
        digits[i] = num % 10;
        num /= 10;
    }

    std::sort(digits, digits + 4);
    int ascending = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3];
    int descending = digits[3] * 1000 + digits[2] * 100 + digits[1] * 10 + digits[0];
    
    
    return descending - ascending;
}


int steps_to_reach_kaprekar_const(int num) {
    const int kaprekar_const = 6174;
    int count = 0;

    while (num != kaprekar_const && num != 0) {
        int nextStep = kaprekar_calculation(num);

        
        std::cout << num << " -> " << nextStep << std::endl;

    
        num = nextStep;
        if ( num == 0 ) {
            break;
        }

        count++;
    }

    return count;
}
int getUserInput() {
    int num;
    std::cout << "Enter a 4-digit number: ";
    std::cin >> num;

    return num;
}

void displayResult(int steps) {
    std::cout << "Number of steps to reach 6174: " << steps << std::endl;
}

int main() {
    int num = getUserInput();

    if (num < 1000 || num > 9999) {
        std::cerr << "Please enter a valid 4-digit number." << std::endl;
        return 1;
    }

    int steps = steps_to_reach_kaprekar_const(num);
    displayResult(steps);

    return 0;
}
