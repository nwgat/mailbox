#!/bin/sh
# download https://github.com/muquit/mailsend-go/releases/download/v1.0.9/mailsend-go_1.0.9_linux-64bit.tar.gz
mailsend-go -sub "Test"  -smtp smtp.gmail.com -port 587 \
     auth \
      -user jsnow@gmail.com -pass "secret" \
     -from "jsnow@gmail.com" -to  "mjane@example.com" \
     body \
       -msg "You got mail motha focker :P"
