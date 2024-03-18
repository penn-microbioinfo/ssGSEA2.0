#!/bin/bash

gct_dir=$1
db=$2

for gct in $(ls ${gct_dir}/*.gct); do
	gct_base=$(basename $gct)
	bash /home/ec2-user/call_ssgsea-cli.bash $gct $db ${gct_base/.gct/}

done
