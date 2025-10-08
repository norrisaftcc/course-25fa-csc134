# Memory Bank - Flash Card Practice System

## Description
Memory Bank is a C++ flash card activity designed to help CSC 134 students practice common programming questions and improve their quiz scores. Unlike Answer Checker where users provide questions at runtime, Memory Bank comes pre-loaded with programming questions.

## Features

### 1. Practice Mode (Random Questions)
- Select how many questions you want to practice
- Questions are randomly selected from the question bank
- Provides immediate feedback on answers
- Shows final score and percentage
- Gives encouraging messages based on performance

### 2. Review All Questions
- View all available questions and answers
- Organized by topic (Variables, Data Types, Input/Output, etc.)
- Great for studying before taking the practice quiz

### 3. Add Custom Questions
- Teachers and parents can add new questions
- Students can add questions they want to practice
- Questions are added to the current session

### 4. User-Friendly Interface
- Clear menu system
- Case-insensitive answer checking
- Progress tracking during practice sessions
- Helpful feedback messages

## How to Compile and Run

```bash
g++ memory_bank.cpp -o memory_bank
./memory_bank
```

## Sample Questions Included

The program includes 15 pre-stored questions covering:
- **Variables**: const keyword
- **Data Types**: int, double
- **Input/Output**: cout, cin
- **Operators**: ==, =, %
- **Control Structures**: if, else
- **Functions**: main function
- **Loops**: while, for
- **Programming Concepts**: debugging
- **Syntax**: semicolon

## Educational Benefits

- **For Students**: Practice common quiz questions anytime
- **For Parents**: Set up additional practice questions for children
- **For Teachers**: Supplement classroom learning with interactive practice

## Usage Tips

1. Start with "Review All Questions" to see what's available
2. Use "Practice Mode" for active learning and testing
3. Add custom questions for topics you want to focus on
4. Aim for 90%+ scores before taking actual quizzes

## Answer Guidelines

- Answers are not case-sensitive
- Type exactly what's expected (e.g., "const", "cout", "==")
- For symbols, type them as shown (e.g., ";" for semicolon)