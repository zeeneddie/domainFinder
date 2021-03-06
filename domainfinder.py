#!/usr/bin/env python3
import argparse
from hackerTarget import getHackerTarget
from threatCrowd import getThreatCrowd

def main():
	# Arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('-d','--domain',dest='domain',required=True,help='Provide a domain')

	#Set Args
	args = parser.parse_args()
	domain = args.domain
	
	#Sources
	domains = getHackerTarget(domain)
	domains = domains + getThreatCrowd(domain)	
	#Remove Duplicates
	unDomains = []
	for elem in domains:
		if elem not in unDomains:
			unDomains.append(elem)
	
	#Print Domains
	print(*unDomains, sep="\n")
main()
