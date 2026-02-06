---
name: telnyx-account-notifications-go
description: >-
  Configure notification channels and settings for account alerts and events.
  This skill provides Go SDK examples.
metadata:
  author: telnyx
  product: account-notifications
  language: go
---

# Telnyx Account Notifications - Go

## Installation

```bash
go get github.com/team-telnyx/telnyx-go
```

## Setup

```go
import (
  "context"
  "fmt"

  "github.com/team-telnyx/telnyx-go"
  "github.com/team-telnyx/telnyx-go/option"
)

client := telnyx.NewClient(
  option.WithAPIKey(os.Getenv("TELNYX_API_KEY")),
)
```

All examples below assume `client` is already initialized as shown above.

## List notification channels

List notification channels.

`GET /notification_channels`

```go
page, err := client.NotificationChannels.List(context.TODO(), telnyx.NotificationChannelListParams{

})
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", page)
```

## Create a notification channel

Create a notification channel.

`POST /notification_channels`

```go
notificationChannel, err := client.NotificationChannels.New(context.TODO(), telnyx.NotificationChannelNewParams{

})
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", notificationChannel.Data)
```

## Get a notification channel

Get a notification channel.

`GET /notification_channels/{id}`

```go
notificationChannel, err := client.NotificationChannels.Get(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", notificationChannel.Data)
```

## Update a notification channel

Update a notification channel.

`PATCH /notification_channels/{id}`

```go
notificationChannel, err := client.NotificationChannels.Update(
  context.TODO(),
  "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  telnyx.NotificationChannelUpdateParams{
    NotificationChannel: telnyx.NotificationChannelParam{

    },
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", notificationChannel.Data)
```

## Delete a notification channel

Delete a notification channel.

`DELETE /notification_channels/{id}`

```go
notificationChannel, err := client.NotificationChannels.Delete(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", notificationChannel.Data)
```

## List all Notifications Events Conditions

Returns a list of your notifications events conditions.

`GET /notification_event_conditions`

```go
page, err := client.NotificationEventConditions.List(context.TODO(), telnyx.NotificationEventConditionListParams{

})
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", page)
```

## List all Notifications Events

Returns a list of your notifications events.

`GET /notification_events`

```go
page, err := client.NotificationEvents.List(context.TODO(), telnyx.NotificationEventListParams{

})
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", page)
```

## List all Notifications Profiles

Returns a list of your notifications profiles.

`GET /notification_profiles`

```go
page, err := client.NotificationProfiles.List(context.TODO(), telnyx.NotificationProfileListParams{

})
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", page)
```

## Create a notification profile

Create a notification profile.

`POST /notification_profiles`

```go
notificationProfile, err := client.NotificationProfiles.New(context.TODO(), telnyx.NotificationProfileNewParams{

})
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", notificationProfile.Data)
```

## Get a notification profile

Get a notification profile.

`GET /notification_profiles/{id}`

```go
notificationProfile, err := client.NotificationProfiles.Get(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", notificationProfile.Data)
```

## Update a notification profile

Update a notification profile.

`PATCH /notification_profiles/{id}`

```go
notificationProfile, err := client.NotificationProfiles.Update(
  context.TODO(),
  "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  telnyx.NotificationProfileUpdateParams{
    NotificationProfile: telnyx.NotificationProfileParam{

    },
  },
)
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", notificationProfile.Data)
```

## Delete a notification profile

Delete a notification profile.

`DELETE /notification_profiles/{id}`

```go
notificationProfile, err := client.NotificationProfiles.Delete(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", notificationProfile.Data)
```

## List notification settings

List notification settings.

`GET /notification_settings`

```go
page, err := client.NotificationSettings.List(context.TODO(), telnyx.NotificationSettingListParams{

})
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", page)
```

## Add a Notification Setting

Add a notification setting.

`POST /notification_settings`

```go
notificationSetting, err := client.NotificationSettings.New(context.TODO(), telnyx.NotificationSettingNewParams{

})
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", notificationSetting.Data)
```

## Get a notification setting

Get a notification setting.

`GET /notification_settings/{id}`

```go
notificationSetting, err := client.NotificationSettings.Get(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", notificationSetting.Data)
```

## Delete a notification setting

Delete a notification setting.

`DELETE /notification_settings/{id}`

```go
notificationSetting, err := client.NotificationSettings.Delete(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
if err != nil {
  panic(err.Error())
}
fmt.Printf("%+v\n", notificationSetting.Data)
```
