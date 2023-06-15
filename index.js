//fetching the alpaca API
const Alpaca = require('@alpacahq/alpaca-trade-api')
const _ = require('lodash');
const SMA = require('technicalindicators').SMA;

//keys for project
const APIKey = "PKQU3UMD89C6VSJGZRAV"
const APISecret = "IsaGQPd9bhv4nH5ahSJO4MvSNKPKXiG2RHZpAbyK"

//using object to store necessary data
const alpaca = new Alpaca({
    keyId: APIKey,
    secretKey: APISecret,
    paper: true
  });

//using an asynchornis function to call the data from my alpaca account
async function printAccount() {
    const account = await alpaca.getAccount();
    console.log(account);
}

  printAccount();

