JSON_FILE = "./config/option_data.json"
if [ -e $(JSON_FILE) ]
then
  name=$(cat $(JSON_FILE) | jq '.Name' | sed 's/^.*"\(.*\(.*\)".*$/\1/')
  echo name
fi