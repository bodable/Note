#!/bin/sh
#deoloy sitewhere

echo "atm starting sitewhere..."

service mongod start

#cd /opt/hivemq-3.0.2/bin
#./run.sh &

cd /opt/sitewhere/bin
sudo sh startup.sh &



