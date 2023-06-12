import Alpaca from '@alpacahq/alpaca-trade-api';

const APIKey = "PK4SM17D2X87CLG9DKNZ"
const APISecret = "Vq0tsrV80WngGbal6HaT1TPYInyCYADhBKihjnAC"

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

