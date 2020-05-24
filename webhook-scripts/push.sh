#!/bin/sh
curl -s \
  --form-string "token=APP_TOKEN" \
  --form-string "user=USER_KEY" \
  --form-string "message=you got mail motha focka" \
  https://api.pushover.net/1/messages.json
