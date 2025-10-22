/*
Memory Bank - Flash Card Activity
CSC 134
norrisa
9/22/25
Purpose: Help students practice common programming questions
Similar to Answer Checker but with pre-stored questions
*/

#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>  // for rand() and srand()
#include <ctime>    // for time()
using namespace std;

// Structure to hold a question and answer pair
struct Question {
    string question;
    string answer;
    string topic;
};

// Function declarations
void displayWelcome();
void displayMenu();
void practiceMode(vector<Question>& questions);
void showAllQuestions(vector<Question>& questions);
void addCustomQuestion(vector<Question>& questions);
void displayScore(int correct, int total);
bool checkAnswer(string userAnswer, string correctAnswer);
void initializeQuestions(vector<Question>& questions);

int main() {
    // Initialize random seed
    srand(time(0));
    
    // Create vector to store questions
    vector<Question> questions;
    
    // Load pre-stored questions
    initializeQuestions(questions);
    
    // Display welcome message
    displayWelcome();
    
    int choice = 0;
    
    // Main program loop
    do {
        displayMenu();
        cout << "Enter your choice (1-4): ";
        cin >> choice;
        cout << endl;
        
        switch(choice) {
            case 1:
                practiceMode(questions);
                break;
            case 2:
                showAllQuestions(questions);
                break;
            case 3:
                addCustomQuestion(questions);
                break;
            case 4:
                cout << "Thank you for using Memory Bank! Good luck on your quiz!" << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
                break;
        }
        cout << endl;
        
    } while (choice != 4);
    
    return 0;
}

void displayWelcome() {
    cout << "========================================" << endl;
    cout << "    Welcome to Memory Bank!" << endl;
    cout << "    Flash Card Practice System" << endl;
    cout << "========================================" << endl;
    cout << "Practice common programming questions to improve your quiz scores!" << endl;
    cout << endl;
}

void displayMenu() {
    cout << "--- Memory Bank Menu ---" << endl;
    cout << "1. Practice Mode (Random Questions)" << endl;
    cout << "2. Review All Questions" << endl;
    cout << "3. Add Custom Question" << endl;
    cout << "4. Exit" << endl;
    cout << endl;
}

void practiceMode(vector<Question>& questions) {
    if (questions.empty()) {
        cout << "No questions available!" << endl;
        return;
    }
    
    cout << "--- Practice Mode ---" << endl;
    cout << "How many questions would you like to practice? ";
    int numQuestions;
    cin >> numQuestions;
    
    if (numQuestions <= 0) {
        cout << "Invalid number of questions." << endl;
        return;
    }
    
    // Limit to available questions
    if (numQuestions > (int)questions.size()) {
        numQuestions = questions.size();
    }
    
    int correct = 0;
    string userAnswer;
    
    cout << endl << "Starting practice session..." << endl;
    cout << "Type your answer and press Enter. Answers are not case-sensitive." << endl;
    cout << "========================================" << endl;
    
    for (int i = 0; i < numQuestions; i++) {
        // Pick a random question
        int randomIndex = rand() % questions.size();
        Question& currentQ = questions[randomIndex];
        
        cout << "Question " << (i + 1) << " of " << numQuestions << endl;
        cout << "Topic: " << currentQ.topic << endl;
        cout << currentQ.question << endl;
        cout << "Your answer: ";
        
        // Clear the input buffer
        cin.ignore();
        getline(cin, userAnswer);
        
        if (checkAnswer(userAnswer, currentQ.answer)) {
            cout << "✓ Correct!" << endl;
            correct++;
        } else {
            cout << "✗ Incorrect. The correct answer is: " << currentQ.answer << endl;
        }
        cout << "----------------------------------------" << endl;
    }
    
    displayScore(correct, numQuestions);
}

void showAllQuestions(vector<Question>& questions) {
    if (questions.empty()) {
        cout << "No questions available!" << endl;
        return;
    }
    
    cout << "--- All Questions Review ---" << endl;
    cout << "Total questions: " << questions.size() << endl;
    cout << "========================================" << endl;
    
    for (int i = 0; i < (int)questions.size(); i++) {
        cout << "Question " << (i + 1) << ":" << endl;
        cout << "Topic: " << questions[i].topic << endl;
        cout << "Q: " << questions[i].question << endl;
        cout << "A: " << questions[i].answer << endl;
        cout << "----------------------------------------" << endl;
    }
}

void addCustomQuestion(vector<Question>& questions) {
    Question newQ;
    
    cout << "--- Add Custom Question ---" << endl;
    cout << "Enter topic: ";
    cin.ignore(); // Clear input buffer
    getline(cin, newQ.topic);
    
    cout << "Enter question: ";
    getline(cin, newQ.question);
    
    cout << "Enter answer: ";
    getline(cin, newQ.answer);
    
    questions.push_back(newQ);
    
    cout << "Question added successfully!" << endl;
    cout << "Total questions now: " << questions.size() << endl;
}

void displayScore(int correct, int total) {
    double percentage = (double)correct / total * 100.0;
    
    cout << "========================================" << endl;
    cout << "    Practice Session Complete!" << endl;
    cout << "========================================" << endl;
    cout << "Score: " << correct << " out of " << total << endl;
    cout << "Percentage: " << (int)percentage << "%" << endl;
    
    if (percentage >= 90) {
        cout << "Excellent! You're ready for the quiz!" << endl;
    } else if (percentage >= 80) {
        cout << "Good job! A little more practice and you'll ace it!" << endl;
    } else if (percentage >= 70) {
        cout << "Not bad! Keep practicing to improve your score." << endl;
    } else {
        cout << "Keep studying! Practice makes perfect!" << endl;
    }
}

bool checkAnswer(string userAnswer, string correctAnswer) {
    // Convert both answers to lowercase for case-insensitive comparison
    for (int i = 0; i < (int)userAnswer.length(); i++) {
        userAnswer[i] = tolower(userAnswer[i]);
    }
    for (int i = 0; i < (int)correctAnswer.length(); i++) {
        correctAnswer[i] = tolower(correctAnswer[i]);
    }
    
    return userAnswer == correctAnswer;
}

void initializeQuestions(vector<Question>& questions) {
    // Pre-stored programming questions based on CSC 134 curriculum
    
    questions.push_back({"What C++ keyword is used to declare a constant variable?", 
                        "const",
                        "Variables"});
    
    questions.push_back({"What data type would you use to store a person's age?", 
                        "int",
                        "Data Types"});
    
    questions.push_back({"What data type would you use to store a price with decimal places?", 
                        "double",
                        "Data Types"});
    
    questions.push_back({"What C++ statement is used to display output to the screen?", 
                        "cout",
                        "Input/Output"});
    
    questions.push_back({"What C++ statement is used to get input from the keyboard?", 
                        "cin",
                        "Input/Output"});
    
    questions.push_back({"What operator is used to check if two values are equal?", 
                        "==",
                        "Operators"});
    
    questions.push_back({"What operator is used to assign a value to a variable?", 
                        "=",
                        "Operators"});
    
    questions.push_back({"What keyword starts a conditional statement in C++?", 
                        "if",
                        "Control Structures"});
    
    questions.push_back({"What keyword is used for the alternative condition in an if statement?", 
                        "else",
                        "Control Structures"});
    
    questions.push_back({"What is the name of the function where C++ programs start execution?", 
                        "main",
                        "Functions"});
    
    questions.push_back({"What type of loop checks the condition before executing the body?", 
                        "while",
                        "Loops"});
    
    questions.push_back({"What type of loop is best when you know exactly how many times to repeat?", 
                        "for",
                        "Loops"});
    
    questions.push_back({"What operator gives you the remainder after division?", 
                        "%",
                        "Math"});
    
    questions.push_back({"What do we call the process of finding and fixing errors in code?", 
                        "debugging",
                        "Programming Concepts"});
    
    questions.push_back({"What symbol is used to end most statements in C++?", 
                        ";",
                        "Syntax"});
}