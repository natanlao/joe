# Documentation only
sqlite3 signal_backup.db 'SELECT body FROM sms WHERE address = (SELECT _id FROM recipient WHERE signal_profile_name = "NAME") AND protocol = 31337;'
# Replace NAME with the first name of the person to query. Using this
# approach because I noticed that:
# 1. Some messages that I sent were listed under the same `address`
#    (we expect only messages received)
# 2. All messages that were received had `protocol = 31337`
