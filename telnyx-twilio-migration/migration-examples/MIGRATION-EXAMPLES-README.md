# Telnyx Migration Examples

This directory contains source code examples of Twilio applications that have been migrated to use Telnyx APIs. These are intended as reference implementations for understanding migration patterns and best practices.

## Directory Structure

```
migration-examples/
├── python-flask/          # Flask-based Python applications
│   ├── sms2fa-flask/           # SMS Two-Factor Authentication
│   ├── clicktocall-flask/      # Click-to-Call functionality
│   ├── ivr-phone-tree-python/  # IVR Phone Tree system
│   ├── authy2fa-flask/         # Authy-compatible 2FA
│   └── airtng-masked-numbers-flask/  # Masked phone numbers for marketplace
│
├── nodejs/                # Node.js/Express applications
│   ├── ivr-phone-tree-node/    # IVR Phone Tree system
│   ├── browser-calls-node/     # Browser-based calling
│   └── ivr-recording-node/     # IVR with call recording
│
├── ruby/                  # Ruby on Rails applications
│   ├── account-verification-rails/     # Phone verification system
│   └── anonymous-communications-rails/ # Masked communications
│
├── java/                  # Java/Spring applications
│   └── account-security-quickstart-spring/  # 2FA and account security
│
└── django/                # Django applications
    ├── automated-survey-django/      # Automated phone surveys
    ├── call-tracking-django/         # Call tracking and analytics
    ├── appointment-reminders-django/ # SMS appointment reminders
    └── ivr-recording-django/         # IVR with recording capabilities
```

## Repository Contents

Each repository contains:

- **Source code** - The actual application code
- **README.md** - Setup and usage instructions
- **MIGRATION-PLAN.md** - Step-by-step migration approach
- **MIGRATION-REPORT.md** - Results and findings from the migration
- **Configuration files** - Requirements, package.json, Gemfile, etc.
- **Tests** - Where available

## Migration Patterns

Common patterns you'll find across these examples:

1. **Voice API**: Converting Twilio TwiML to Telnyx TeXML
2. **Messaging API**: SMS and MMS functionality using Telnyx
3. **Authentication**: 2FA and verification flows
4. **IVR Systems**: Interactive voice response implementations

## Notes

- These are the migrated (Telnyx) versions of the original Twilio sample applications
- Original .git directories and build artifacts have been excluded to reduce size
- The migration plans and reports document the specific changes made during migration
