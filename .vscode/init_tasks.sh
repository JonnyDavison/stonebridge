#!/bin/bash

<<<<<<< HEAD
=======
# Creates a user record for the current Cloud9 user
>>>>>>> yarn/main
# Gives a personalised greeting
# Adds configuration options for SQLite
# Creates run aliases
# Author: Matt Rudge

echo "Setting the greeting"
sed -i "s/USER_NAME/$GITPOD_GIT_USER_NAME/g" ${GITPOD_REPO_ROOT}/README.md
<<<<<<< HEAD
=======
echo "Creating the gitpod user in MySQL"
RESULT="$(mysql -sse "SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = 'gitpod')")"
if [ "$RESULT" = 1 ]; then
  echo "gitpod already exists"
else
  mysql -e "CREATE USER 'gitpod'@'%' IDENTIFIED BY '';" -u root
  echo "Granting privileges"
  mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'gitpod'@'%' WITH GRANT OPTION;" -u root
fi
>>>>>>> yarn/main
echo "Creating .sqliterc file"
echo ".headers on" > ~/.sqliterc
echo ".mode column" >> ~/.sqliterc
echo "Your workspace is ready to use. Happy coding!"
