const {welcome, menu, planets} = require('../../src/ivr/handler');

describe('IvrHandler#Welcome', () => {
  it('should serve TeXML with gather', () => {
    const texml = welcome();
    const count = countWord(texml);

    // TeXML verbs (opening and closing tags)
    expect(count('Gather')).toBe(2);
    expect(count('Say')).toBe(2);

    // TeXML options
    expect(texml).toContain('action="/ivr/menu"');
    expect(texml).toContain('numDigits="1"');
    expect(texml).toContain('loop="3"');

    // TeXML content
    expect(texml).toContain('Thanks for calling the E T Phone Home Service');
  });
});

describe('IvrHandler#Menu', () => {
  it('should redirect to welcome with digits other than 1 or 2', () => {
    const texml = menu();
    const count = countWord(texml);

    // TeXML verbs - Say appears twice (opening and closing tags)
    expect(count('Say')).toBe(2);
    expect(count('Redirect')).toBe(2);

    // TeXML content
    expect(texml).toContain('/ivr/welcome');
  });

  it('should serve TeXML with say twice and hangup', () => {
    const texml = menu('1');
    const count = countWord(texml);

    // TeXML verbs - Say appears 4 times (2 pairs of opening/closing tags)
    expect(count('Say')).toBe(4);
    // Hangup is a self-closing tag - check for its presence
    expect(texml).toContain('<Hangup/>');

    // TeXML content
    expect(texml).toContain(
      'To get to your extraction point, get on your bike and go down the ' +
      'street. Then Left down an alley. Avoid the police cars. Turn left ' +
      'into an unfinished housing development. Fly over the roadblock. Go ' +
      'passed the moon. Soon after you will see your mother ship.'
    );
    expect(texml).toContain(
      'Thank you for calling the ET Phone Home Service'
    );
  });

  it('should serve TeXML with gather and say', () => {
    const texml = menu('2');
    const count = countWord(texml);

    // TeXML verbs (opening and closing tags)
    expect(count('Gather')).toBe(2);
    expect(count('Say')).toBe(2);

    // TeXML options
    expect(texml).toContain('action="/ivr/planets"');
    expect(texml).toContain('numDigits="1"');

    // TeXML content
    expect(texml).toContain(
      'To call the planet Broh doe As O G, press 2. To call the planet DuhGo ' +
      'bah, press 3. To call an oober asteroid to your location, press 4. To ' +
      'go back to the main menu, press the star key'
    );
  });
});

describe('IvrHandler#Planets', () => {
  it('should redirect to welcome with digits other than 2, 3 or 4', () => {
    const texml = planets();
    const count = countWord(texml);

    // TeXML verbs
    expect(count('Say')).toBe(2);
    expect(count('Redirect')).toBe(2);

    // TeXML content
    expect(texml).toContain('/ivr/welcome');
  });

  it('should serve TeXML with dial', () => {
    const texml = planets('4');

    // TeXML verbs
    expect(texml).toContain('<Dial>');

    // TeXML content
    expect(texml).toContain('+16513582243');
  });
});

/**
 * Counts how many times a word is repeated
 * @param {String} paragraph
 * @return {String[]}
 */
function countWord(paragraph) {
  return (word) => {
    const regex = new RegExp(`\\<${word}[ |>]|\\<\\/${word}>`);
    return (paragraph.split(regex).length - 1);
  };
}
