### 2020.01.16

#### General
* [ ] Review bot examples natalia.py

#### Code management
* [ ] Create bot class
* [ ] Substitute new bot into old bot files
* [ ] Test out bot functionality
  * [ ] Remove member from group with http request
  * [ ] Add member to group with http request
  * [ ] Send direct message to member
  * [ ] Return telegram username
  * [ ] Save username to local file
  * [ ] Return all members in group

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
* [ ] Fetching users
  * [ ] Return all members within channels
  * [ ] Store channel members to local file
* [ ] Private message myself from bot using either username or user_id
* [ ] Use correct bot
  * [ ] Update bot photo
  * [ ] Update bot token to work with atta_payments_bot
