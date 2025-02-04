import argparse
import sys
import subprocess
import os

ssgsea_home = "/home/ubuntu/dev/ssGSEA2.0"

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--gcts", action = "store", help = "Path to directory containing the input GCT files.")
parser.add_argument("-o", "--output", action = "store", help = "Prefix for output.")
parser.add_argument("-d", "--db", action = "store", help = "Path to GMT file to run GCTs against, generating enrichment scores.")
parser.add_argument("-p", "--nperm", action = "store", default = 1000, type = int, help = "Number of permutations to generate pvalues. Default = 1000")
parser.add_argument("--sparecores", action = "store", default = 0, type = int, help = "Number of CPU cores to leave available while running ssGSEA. Default = 0.")
args = parser.parse_args()

gcts = [os.path.join(args.gcts,x) for x in os.listdir(args.gcts) if x.endswith(".gct")]

assert len(gcts) > 0, f"No input GCT files found at {args.gcts}"

for gct in gcts:
    output = os.path.basename(gct).replace(".gct", f"{args.output}.gct")
    call_ssgsea = [
            "Rscript", os.path.join(ssgsea_home, "ssgsea-cli.R"),
            "--input", gct,
            "--output", output,
            "--norm", "rank",
            "--weight", "0.75",
            "--correl", "z.score",
            "--test", "area.under.RES",
            "--score", "NES",
            "--perm", str(args.nperm),
            "--minoverlap", "5",
            "--db", args.db,
            "--export", "TRUE",
            "--extendedoutput", "TRUE",
            "--globalfdr", "TRUE",
            "--lightspeed", "TRUE",
            "--sparecores", str(args.sparecores),
            "--scrdir", ssgsea_home
            ]

    print(" ".join(call_ssgsea))
    p = subprocess.run(call_ssgsea, capture_output = True, shell = False)
    if p.returncode != 0:
        print(p.stdout)
        print(p.stderr)
