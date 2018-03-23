#!/bin/sh
#deoloy sitewhere

echo "atm deploy sitewhere..."

sudo sh jdk.sh

sudo sh mon.sh

sudo sh hiveMQ.sh

sudo sh sitewhere.sh

