/**
 * Returns TeXML for the welcome message
 * @return {String}
 */
exports.welcome = function welcome() {
  return `<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Gather action="/ivr/menu" numDigits="1" method="POST">
    <Say loop="3">Thanks for calling the E T Phone Home Service. Please press 1 for directions. Press 2 for a list of planets to call.</Say>
  </Gather>
</Response>`;
};

/**
 * Returns TeXML for the menu based on digit pressed
 * @param {String} digit - The digit pressed
 * @return {String}
 */
exports.menu = function menu(digit) {
  const optionActions = {
    '1': giveExtractionPointInstructions,
    '2': listPlanets,
  };

  return (optionActions[digit])
    ? optionActions[digit]()
    : redirectWelcome();
};

/**
 * Returns TeXML for the planets menu based on digit pressed
 * @param {String} digit - The digit pressed
 * @return {String}
 */
exports.planets = function planets(digit) {
  const optionActions = {
    '2': '+19295566487',
    '3': '+17262043675',
    '4': '+16513582243',
  };

  if (optionActions[digit]) {
    return `<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>${optionActions[digit]}</Dial>
</Response>`;
  }

  return redirectWelcome();
};

/**
 * Returns TeXML with extraction instructions
 * @return {String}
 */
function giveExtractionPointInstructions() {
  return `<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say voice="Polly.Amy-Neural" language="en-GB">To get to your extraction point, get on your bike and go down the street. Then Left down an alley. Avoid the police cars. Turn left into an unfinished housing development. Fly over the roadblock. Go passed the moon. Soon after you will see your mother ship.</Say>
  <Say voice="Polly.Amy-Neural" language="en-GB">Thank you for calling the ET Phone Home Service - the adventurous alien's first choice in intergalactic travel</Say>
  <Hangup/>
</Response>`;
}

/**
 * Returns TeXML to list planets
 * @return {String}
 */
function listPlanets() {
  return `<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Gather action="/ivr/planets" numDigits="1" method="POST">
    <Say voice="Polly.Amy-Neural" language="en-GB" loop="3">To call the planet Broh doe As O G, press 2. To call the planet DuhGo bah, press 3. To call an oober asteroid to your location, press 4. To go back to the main menu, press the star key</Say>
  </Gather>
</Response>`;
}

/**
 * Returns TeXML with redirect to welcome
 * @return {String}
 */
function redirectWelcome() {
  return `<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say voice="Polly.Amy-Neural" language="en-GB">Returning to the main menu</Say>
  <Redirect>/ivr/welcome</Redirect>
</Response>`;
}
