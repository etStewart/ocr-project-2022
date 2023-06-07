const Alpaca = require('@alpacahq/alpaca-trade-api');  //import alpaca API package I installed via NPM

//object used to access different API requests
const Alpaca = new Alpaca({
    keyID: environment.env.APIKey,
    secretID: environment.env.APISecret,
    paper: true
});

async function printAccount() {
    const account = await alpaca.getAccount();
    console.log(account);
}

printAccount();

