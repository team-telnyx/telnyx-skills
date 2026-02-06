---
name: telnyx-seti-ruby
description: >-
  Access SETI (Space Exploration Telecommunications Infrastructure) APIs. This
  skill provides Ruby SDK examples.
metadata:
  author: telnyx
  product: seti
  language: ruby
---

# Telnyx Seti - Ruby

## Installation

```bash
gem install telnyx
```

## Setup

```ruby
require "telnyx"

client = Telnyx::Client.new(
  api_key: ENV["TELNYX_API_KEY"], # This is the default and can be omitted
)
```

All examples below assume `client` is already initialized as shown above.

## Retrieve Black Box Test Results

Returns the results of the various black box tests

`GET /seti/black_box_test_results`

```ruby
telnyx = Telnyx::Client.new(api_key: "My API Key")

response = telnyx.seti.retrieve_black_box_test_results

puts(response)
```
