#!/bin/bash

input_gct=$1
db=$2
output_prefix=$3
ncores=8

Rscript /home/ec2-user/ssGSEA2.0/ssgsea-cli.R \
	--input $input_gct \
	--output $output_prefix \
	--norm rank \
	--weight 0.75 \
	--correl "z.score" \
	--test "area.under.RES" \
	--score NES \
	--perm 100000 \
	--minoverlap 5 \
	--db $db \
	--export TRUE \
	--extendedoutput TRUE \
	--globalfdr TRUE \
	--lightspeed TRUE \
        --cores $ncores
