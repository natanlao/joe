# I didn't actually run this like a shell script since I'm lazy. This
# is just here for documentation purposes.
# Obviously, replace $NAME with the person's name and ensure that **.json
# will glob properly (i.e., specify directory as necessary)
jq -r '.[] | select(.user_profile["full_name"] == $NAME) | .text' **.json