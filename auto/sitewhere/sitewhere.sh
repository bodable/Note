#!/bin/sh
#sitewhere release

echo "atm installing sitewhere release"

cd /opt
wget https://s3.amazonaws.com/sitewhere/sitewhere-server-1.7.0.tgz
tar -zxvf sitewhere-server-1.7.0.tgz
mv sitewhere-server-1.7.0 /opt/sitewhere
export SITEWHERE_HOME=/opt/sitewhere
cd /opt/sitewhere/bin
sh startup.sh &
