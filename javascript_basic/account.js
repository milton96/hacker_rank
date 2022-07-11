'use strict';

class Account {
    balance = 0;
    constructor(balance) {
        this.balance = balance;
    }

    debit(amount) {
        if (this.balance < amount) return false;

        this.balance -= amount;
        return true;
    }

    getBalance() {
        return this.balance;
    }

    credit(amount) {
        this.balance += amount;
    }
}

function main() {
    console.log('hola');
}

main();