# Requirements
At least the following flow should be implemented:

> Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw

For simplification, there are only 1 dollar bills in this world, no cents. Thus account balance can be represented in integer.

Your code doesn't need to integrate with a real bank system, but keep in mind that we may want to integrate it with a real bank system in the future. It doesn't have to integrate with a real cash bin in the ATM, but keep in mind that we'd want to integrate with that in the future. And even if we integrate it with them, we'd like to test our code. Implementing bank integration and ATM hardware like cash bin and card reader is not a scope of this task, but testing the controller part (not including bank system, cash bin etc) is within the scope.

A bank API wouldn't give the ATM the PIN number, but it can tell you if the PIN number is correct or not.

Based on your work, another engineer should be able to implement the user interface. You don't need to implement any REST API, RPC, network communication etc, but just functions/classes/methods, etc.

You can simplify some complex real world problems if you think it's not worth illustrating in the project.

---

## class TellerMachine
### Methods
* Insert Card
* Input PIN
* Select Operation
** Select Account 
** Show Balance
** Deposit
** Withdraw
* Show the result of operation

## class BankCard
### Attributes
* Card Number (Conceptually, manage as key of Dictionary at DataBase)
* PIN Number
### Methods
* PIN Number Authentication

## class Account
All the Account must be associated with BankCard.
### Attributes
* Account Number (Conceptually, manage as key of Dictionary at DataBase)
* Balance
### Methods
* Deposit
* Withdraw
* Get Balance

## class ATMDataProvider
### Attributes
* Dictionary for BankCard
* Dictionary for Account
* Dictionary for association table of BankCard and Account
### Methods
* Add BankCard
* Add Account
* Associate BankCard and Account
* List up all the BankCard and Account
* Validate BankCard Number
* Get the list of Cccount associated with specific BankCard Number
* Get the Account by BankCard instance
* Get the BankCard instance with PIN validation

## class ATMServiceProvider
### Attributes
* ATMDataBase
* Temporal : Inserted Card Information
* Temporal : Selected Account Information
### Methods
* Issue Account via ATMDB (need card information)
* Issue BankCard via ATMDB
* Authentication
* Deposit
* Withdraw
* Get Balance
* Remove Card : Reset current authencation information
