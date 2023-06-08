import Alpaca from '/Users/ethan/node_modules/@alpacahq/alpaca-trade-api';  //import alpaca API package I installed via NPM

//assinging API keys to veriables
const APIKey = "PKUEDSU4AC0X6V7YX0DG";
const APISecret = "a67GoahEfGkQNLIhxAMArTYpyOqgy49zaFWbxzQl"

//object used to access different API requests
const Alpaca = new Alpaca({
    keyID: APIKey,
    secretID: APISecret,
    paper: true
});

async function printAccount() {
    const account = await account();
    console.log(account);
}

printAccount();

