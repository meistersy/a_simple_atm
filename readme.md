# How to run
## Execute Source Code
1. Python 3 must be installed.
2. Clone repository into local workspace
3. Open cmd.exe or power shell
4. Move to local repository in command line console.
5. Execute $ python3 teller_machine.py

## Test program in Console
1. You can see the initial screen on console as below :
```
> python .\teller_machine.py
9880-2290-6302-7713
2025-3450-4562-8140
9180-3349-7481-7032
INSERT CARD('xxxx-xxxx-xxxx-xxxx') >>
```
2. Typing the card number at the prompt and press enter key and the program asks PIN number. the PIN number is fixed as 0000 for test.
3. Then program shows account list associated with the card.
```
INSERT CARD('xxxx-xxxx-xxxx-xxxx') >> 9180-3349-7481-7032
INPUT PIN Number('xxxx') >> 0000
Account List >>
59640-49179-37775
SELECT Account ID >>
```
4. Typing the account ID and press enter as similar with card number. Program shows available option for operation.
```
SELECT Account ID >> 59640-49179-37775
1) see Balance
2) Deposit
3) withdraw
select Operation (1-3) >>
```
5. If you select 1) see Balance, the balance of account shows on the screen. Program asks remove the card or not after each operation.
```
select Operation (1-3) >> 1
Balance :  0
Remove Card? (y/n) >>n
1) see Balance
2) Deposit
3) withdraw
select Operation (1-3) >>
```
6. Below is the example result of deposit and withdraw operation. Program shows the balance after each operation. If you try to withdraw more money than balance, program shows warning message and withdraw operation not performed.
```
select Operation (1-3) >> 2
INSERT Cash to deposit >> 50000
Balance :  50000
Remove Card? (y/n) >>n
1) see Balance
2) Deposit
3) withdraw
select Operation (1-3) >> 3
INPUT Cash to withdraw >> 60000
!!! too much cashes to withdraw !!!
Balance :  50000
Remove Card? (y/n) >>n
1) see Balance
2) Deposit
3) withdraw
select Operation (1-3) >> 3
INPUT Cash to withdraw >> 30000
Balance :  20000
Remove Card? (y/n) >>
```
7. If you want to exit the program, input 'q' or 'Q' at the any prompt.
```
Remove Card? (y/n) >>q
>
```


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
  * Select Account 
  * Show Balance
  * Deposit
  * Withdraw
* Show the result of operation

## class BankCard
### Attributes
* Card Number (Conceptually, manage as key of Dictionary at DataBase)
* PIN Number
### Methods
* PIN Number Authentication
* PIN Number Change

## class Account
All the Account must be associated with BankCard.
### Attributes
* Account ID (Conceptually, manage as key of Dictionary at DataBase)
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
* Add Account (must be associated with card)
* List up all the BankCard and Account
* Get the Account IDs by BankCard instance
* Get the Account Instance by Account ID
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
