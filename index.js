const Alpaca = require('@alpacahq/alpaca-trade-api')

const APIKey = "PKQU3UMD89C6VSJGZRAV"
const APISecret = "IsaGQPd9bhv4nH5ahSJO4MvSNKPKXiG2RHZpAbyK"

const alpaca = new Alpaca({
    keyId: APIKey,
    secretKey: APISecret,
    paper: true
  });

  async function printAccount() {
    const account = await alpaca.getAccount();
    console.log(account);
  }

  printAccount();

