_password=`openssl rand -base64 32` 
echo -e "$_password\n$_password" | sudo passwd root; echo "$_password"
echo $_password
