#!/bin/bash

eval "$(ssh-agent -s)" # Start ssh-agent cache
chmod 600 .travis/id_rsa # Allow read access to the private key
ssh-add .travis/id_rsa # Add the private key to SSH

git config --global push.default matching
git remote add deploy ssh://git@$IP:$PORT$DEPLOY_DIR
git push deploy master

# Skip this command if you don't need to execute any additional commands after deploying.
ssh apps@$IP -p $PORT <<EOF
  cd $DEPLOY_DIR
  pip3 install -r requirements.txt
  python3 restmanager/manage.py migrate
  python3 restmanager/manage.py runserver
EOF
