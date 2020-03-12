### 2020.01.16

#### Braintree payments with Telegram group
* __Braintree__
  * [ ] Send test API request
  * [ ] Create sample invoice
  * [ ] Determine interval of reminders (?)
  * [ ] Send transaction data to local directory
* __Telegram__
  * [ ] Create subscription bot


---
### 2020.01.19

#### Storing user data from Telegram
* `users.csv`
  - user_id, last_invoice_id, subscription_term(months), banned
* `admins.csv`
  - user_id, username
* `invoices.csv`
  - invoice_id, date, user_id, subscription_term (months), braintree_link
* `atta_free.csv` and `atta_paid.csv`
  - username, user_id, in_paid


#### Goal: message all members in ATTA regular that are not in ATTA elite
* [x] Add chat_id to config.yaml for both atta channels
* [x] Fetching users
  * [x] Return all members in public channel (1.25)
  * [x] Return all members in private channel (1.25)
  * [x] Store channel members to local file (1.25)
* [x] Send messages
  * [x] From my account to another user using username
  * [x] From my account to another user using user_id
  * [x] From bot to another using username (1.25)
    * Impossible to send direct messages from bot
  * [x] From bot to another using user_id
    * Impossible to send direct messages from bot
* [ ] Managing members
  * [ ] Invite a user to a group
  * [x] Remove a user from a group with their user_id
  * [ ] Unban a user to invite back to channel
  * [x] Make a user an admin and add to admin document
* [ ] Reminding members


---
### 2020.01.23

#### Potential bot uses
* Announcement of bot and `/start` command
* Send messages to users
* Manage ATTA subscriber group
  * Add/remove members
  * Notify members when their subscription is close to expiring
1. Send message to username
