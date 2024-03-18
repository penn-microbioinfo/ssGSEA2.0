#!/bin/bash

input_gct=$1
db=$2
output_prefix=$3

Rscript /home/ec2-user/ssGSEA2.0/ssgsea-cli.R \
	-i $input_gct \
	-o $output_prefix \
	-n rank \
	-w 0.75 \
	-c "z.score" \
	-t "area.under.RES" \
	-s NES \
	-p 100000 \
	-m 5 \
	-d $db \
	-e TRUE \
	-x TRUE \
	-g TRUE \
	-l TRUE
