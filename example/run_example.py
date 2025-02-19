#!/usr/bin/env python
import os
import sys

# Find locuszoom binary. 
sys.argv[0] = os.path.abspath(sys.argv[0]);
lzbin = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]),"../bin/locuszoom"));

# Run a quick example from the Kathiresan et al. data. 
cmd = "%(bin)s --metal Kathiresan_2009_HDL.txt --refgene FADS1 --pvalcol P.value" % {'bin' : lzbin};
print "Running: %s" % cmd;
os.system(cmd); 
