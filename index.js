// Importing required modules
const _ = require('lodash'); // Lodash library for utility functions
const Alpaca = require('@alpacahq/alpaca-trade-api'); // Alpaca trade API module
const SMA = require('technicalindicators').SMA; // Technical Indicators module for calculating SMA

// API key and secret key for Alpaca
const apiKey = 'PKBFRFWBV2IIXYC9BPQ5';
const secretKey = '9rZHrcqHyVAqh6TrljCTayCfghqTmY9HRpkBK7uE';

// Creating an instance of Alpaca with API key and secret key
const alpaca = new Alpaca({
  keyId: apiKey,
  secretKey: secretKey,
  paper: true
});
async function printAccount() {
  const account = await alpaca.getAccount();
  console.log(account);
}

// Function to initialize the moving averages
async function initializeAverages() {
  // Fetching initial data (bars) for SPY symbol
  const initialData = await alpaca.getBars(
    '1Min', // Bar timeframe (1 minute)
    'SPY', // Symbol (stock) to fetch data for
    {
      limit: 50, // Limiting the number of bars to retrieve
      until: new Date() // Fetching bars until the current date
    }
  );

  // Extracting close values from the initial data
  const closeValues = _.map(initialData.SPY, (bar) => bar.c);

  // Calculating moving averages with periods of 20 and 50 using the close values
  let sma20 = new SMA({ period: 20, values: closeValues });
  let sma50 = new SMA({ period: 50, values: closeValues });

  // Printing the results of the moving averages
  console.log(`sma20: ${sma20.getResult()}`);
  console.log(`sma50: ${sma50.getResult()}`);
}

// Calling the function to initialize the moving averages
initializeAverages();


