'use strict';

/**
 * TeXML VoiceResponse Builder
 * Similar to Twilio's VoiceResponse for generating TeXML XML
 */

class VoiceResponse {
  constructor() {
    this.xml = '<?xml version="1.0" encoding="UTF-8"?><Response>';
  }

  say(text, options = {}) {
    const opts = this._buildAttributes(options);
    this.xml += `<Say${opts}>${text}</Say>`;
    return this;
  }

  play(url, options = {}) {
    const opts = this._buildAttributes(options);
    this.xml += `<Play${opts}>${url}</Play>`;
    return this;
  }

  gather(options = {}) {
    const opts = this._buildAttributes(options);
    this.xml += `<Gather${opts}>`;
    return new Gather(this);
  }

  dial(options = {}) {
    const opts = this._buildAttributes(options);
    this.xml += `<Dial${opts}>`;
    return new Dial(this);
  }

  hangup() {
    this.xml += '<Hangup/>';
    return this;
  }

  redirect(url) {
    this.xml += `<Redirect>${url}</Redirect>`;
    return this;
  }

  record(options = {}) {
    const opts = this._buildAttributes(options);
    this.xml += `<Record${opts}/>`;
    return this;
  }

  toString() {
    return this.xml + '</Response>';
  }

  _buildAttributes(options) {
    const attrs = Object.entries(options)
      .map(([k, v]) => ` ${k}="${v}"`)
      .join('');
    return attrs;
  }

  _appendToXml(str) {
    this.xml += str;
  }
}

class Gather {
  constructor(voiceResponse) {
    this.voiceResponse = voiceResponse;
    this.closed = false;
  }

  say(text, options = {}) {
    if (this.closed) throw new Error('Gather already closed');
    const attrs = Object.entries(options)
      .map(([k, v]) => ` ${k}="${v}"`)
      .join('');
    this.voiceResponse._appendToXml(`<Say${attrs}>${text}</Say>`);
    return this;
  }

  play(url, options = {}) {
    if (this.closed) throw new Error('Gather already closed');
    // Check if first arg is an object (options) and second is the URL
    // or if first arg is the URL and second is options
    // Original Twilio API: gather.play(url, options) or gather.play(options, url)
    // Since url can be string and options object, detect based on type
    const actualUrl = typeof url === 'string' ? url : options;
    const actualOptions = typeof url === 'string' ? options : url;
    const opts = Object.entries(actualOptions || {})
      .map(([k, v]) => ` ${k}="${v}"`)
      .join('');
    this.voiceResponse._appendToXml(`<Play${opts}>${actualUrl}</Play>`);
    return this;
  }

  toString() {
    if (!this.closed) {
      this.voiceResponse._appendToXml('</Gather>');
      this.closed = true;
    }
    return this.voiceResponse;
  }
}

class Dial {
  constructor(voiceResponse) {
    this.voiceResponse = voiceResponse;
    this.closed = false;
  }

  number(num, options = {}) {
    if (this.closed) throw new Error('Dial already closed');
    const opts = Object.entries(options)
      .map(([k, v]) => ` ${k}="${v}"`)
      .join('');
    this.voiceResponse._appendToXml(`<Number${opts}>${num}</Number>`);
    return this;
  }

  toString() {
    if (!this.closed) {
      this.voiceResponse._appendToXml('</Dial>');
      this.closed = true;
    }
    return this.voiceResponse;
  }
}

module.exports = { VoiceResponse };
