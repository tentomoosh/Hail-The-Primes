# Hail_the_Primes<br><br>
*Overview:*<br>
The "Hail_the_Primes" application is a Python program designed to identify prime numbers within a user-specified range. It incorporates functions to determine prime numbers, handle user input for specifying the range, and print the identified prime numbers.

*Purpose:*<br>
The purpose of this program is to provide users with a simple tool to find prime numbers within a given range. Prime numbers have various applications in mathematics, cryptography, and computer science, making it useful to have a tool to quickly identify them.

*Functionality:*
1. Prime Number Identification:<br>
The program utilizes the am_i_prime function to check whether a given number is prime. It iterates through the numbers in the specified range and appends prime numbers to a list.

2. User Input Handling:<br>
The get_user_input function prompts the user to enter the start and end values of the range within which prime numbers should be identified. It ensures that the start value is less than the end value and handles any invalid inputs.

3. Finding Primes in Range:<br>
The find_primes_in_range function utilizes the am_i_prime function to find prime numbers within the specified range. It returns a list of prime numbers found in the range.

4. Main Functionality:<br>
The main function serves as the entry point of the program. It calls the get_user_input function to obtain the range from the user, then calls the find_primes_in_range function to find prime numbers within that range. Finally, it prints the identified prime numbers to the console.

How to Run:<br><br>
To run the "Hail_the_Primes" application, follow these steps:<br><br>

Ensure you have Python installed on your system.
Download or clone the source code from the repository.
Open a terminal or command prompt and navigate to the directory containing the source code.
Run the program by executing the following command:
***python Hail_the_Primes.py***
Follow the on-screen prompts to enter the start and end values of the range.
Once the program finishes execution, it will display the identified prime numbers within the specified range.
Time Complexity<br><br>
The time complexity of the prime number identification algorithm used in this program is approximately O(sqrt(n)) for checking each number in the range, where n is the largest number in the range. This is because the algorithm checks divisibility up to the square root of each number to determine primality.







