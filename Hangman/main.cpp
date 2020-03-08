#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

int main() {
  /* Create variables to store the word + number of wrong guesses */
  string word;
  char guess;
  string prev_guesses;
  int wrong_guesses=0;


  /* Prompt the user and store the input data in a variable */
  cout << "Input a word to guess: ";
  cin >> word;

  string word_blanks=word;
  int word_length=word.length();

  for(int i=0; i< word_length; i++){
    word_blanks[i]='_';
    word[i]=tolower(word[i]);
  }


  cout << word << endl;
  cout << word.length() << endl;

//Loop logic, Make Guess, if good guess show fill in letter, else add to bad guess count
//Keep going until out of guesses or word filled in



  while(wrong_guesses <= 5 & word_blanks.find('_') != std::string::npos){

    cout << "You have " << 5-wrong_guesses << " lives left" << endl;
    if (prev_guesses.length() > 0){cout << "You have guessed: " << prev_guesses << endl;}

    guess=' ';

    while(!isalpha(guess)){
    cout << word_blanks << endl;
    cout << "Please Guess a letter: ";
    cin >> guess;

    /*First check validity of guess, then if valid change to lower case if guess*/
    if(!isalpha(guess)){cout << endl << "Not A Letter";}

    else if(prev_guesses.find(guess) != std::string::npos) {guess=' '; cout << "you have already guessed this letter" << endl;}
    else{guess=tolower(guess);}
  }
    prev_guesses=prev_guesses + guess + " ";

    if (word.find(guess) != std::string::npos){
    for(int i=0; i< word_length; i++){
      if(word[i]==guess){word_blanks[i]=guess;}}}
    else{wrong_guesses++;}
    } ;

  /*Game Over, message based on win/loss */
  if(wrong_guesses>=5){cout << "You Lose! The word was: " << word;}
  else{cout << "You Win!" << endl;}}
