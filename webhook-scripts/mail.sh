#!/bin/sh
# download https://github.com/muquit/mailsend-go/releases/download/v1.0.9/mailsend-go_1.0.9_linux-64bit.tar.gz
# usage: mail.sh your@email.com
./mailsend-go -sub "MailboxNinja"  -smtp server.com -port 587 \
     auth \
      -user hello@nwgat.ninja -pass "yourpassword" \
     -from "hello@nwgat.ninja" -to  ""$1"" \
     body \
       -msg "i pity the fool that dont pick up his mail ;)"
