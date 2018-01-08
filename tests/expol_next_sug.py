#!usr/bin/python
import argparse

parser = argparse.ArgumentParser(description='Program To Output Next Logical Export Policy Number')
parser.add_argument('-cluser', dest='cluster', type=str, help='Existing or Valid cDOT Cluster')
parser.add_argument('-vserver', dest='vserver', type=str, help='Existing or Valid Vserver Name')

args =parser.parse_args()
print args.cluster


