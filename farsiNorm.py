#!/usr/bin/python
#farsiNorm.py
#Weston Feely
#10/17/13
import sys, re, fileinput, argparse

#Compile diacritics regex
norm_accents = re.compile(ur'[\u0610\u0611\u0612\u0613\u0614\u0615\u0616\u0617\u0618\u0619\u061a\u064b\u064c\u064d\u064e\u064f\u0650\u0651\u0652\u0653\u0654\u0655\u0656\u0657\u0658\u0659\u065a\u065b\u065c\u065d\u065e\u065f\u0670\u06d6\u06d7\u06d8\u06d9\u06da\u06db\u06dc\u06df\u06e0\u06e1\u06e2\u06e3\u06e4\u06e7\u06e8\u06ea\u06eb\u06ec\u06ed]',flags=re.U)
numerals = {ur'\u0660':ur'0',ur'\u0661':ur'1',ur'\u0662':ur'2',ur'\u0663':ur'3',ur'\u0664':ur'4',
ur'\u0665':ur'5',ur'\u0666':ur'6',ur'\u0667':ur'7',ur'\u0668':ur'8',ur'\u0669':ur'9',
ur'\u06f0':ur'0',ur'\u06f1':ur'1',ur'\u06f2':ur'2',ur'\u06f3':ur'3',ur'\u06f4':ur'4',
ur'\u06f5':ur'5',ur'\u06f6':ur'6',ur'\u06f7':ur'7',ur'\u06f8':ur'8',ur'\u06f9':ur'9'}
letters = {ur'\u0622':ur'\u0627',ur'\u0623':ur'\u0627',ur'\u0625':ur'\u0627',ur'\u0624':ur'\u0648',ur'\u0626':ur'\u064a',ur'\06c0':ur'\u0674'}

#Normalize Farsi text string by removing diacritics, replacing diacriticized alef, he, ye, vav with standard versions
#and converting Arabic numerals to Western numerals
def norm_farsi(farsiString, ar=False, ellipsis=False):
	#Strip whitespace, ZWNJ, and non-break space from farsiString
	farsiString = farsiString.decode('utf-8').strip(u'\xa0\u200c \t\n\r\f\v')
	#Remove all diacritics
	farsiString = norm_accents.sub(ur'',farsiString)
	#Normalize Arabic numerals
	for num in numerals:
		farsiString = re.sub(num,numerals[num],farsiString,flags=re.U)	
	#Normalize Arabic letters (robust to diacritic removal)
	for letter in letters:
		farsiString = re.sub(letter,letters[letter],farsiString,flags=re.U)
	#Optional: normalize Arabic ya (ya -> alif maksura at end of word)
	if ar:
		farsiString = re.sub(ur'\u064a\b',ur'\u0649',farsiString,flags=re.U)
	#Normalize Farsi ye (Arabic ya and alif maksura --> Farsi ye)
	else:
		farsiString = re.sub(ur'\u064a',ur'\u06cc',farsiString,flags=re.U)
		farsiString = re.sub(ur'\u0649',ur'\u06cc',farsiString,flags=re.U)
		farsiString = re.sub(ur'\ufeef',ur'\u06cc',farsiString,flags=re.U)
	#Optional: normalize ellipsis (sequence of full stops becomes ellipsis)
	if ellipsis:
		farsiString = re.sub(ur'([\.\u06d4\u2026]+( )?[\.\u06d4\u2026]+)+',ur'\u2026',farsiString)
	#Re-encode as utf-8
	farsiString = farsiString.encode('utf-8')
	return farsiString

def main(args):
	output = []
	#Perform normalization on infile
	if type(args.infile) is file:
		#Input is stdin
		for line in args.infile:
				output.append(norm_farsi(line, args.arabic, args.ellipsis))
	else:
		#Input is list of files
		for f in args.infile:
			for line in f:
				output.append(norm_farsi(line, args.arabic, args.ellipsis))
	#Write output to filename specified by user
	for line in output:
		print line
	return 0

if __name__ == '__main__':
	#Get arguments from command line
	parser = argparse.ArgumentParser(description='Normalize Farsi or Arabic text.')
	parser.add_argument('-a', '--arabic', action='store_true',
		               help='input is Arabic text (default: input is Farsi text)')
	parser.add_argument('-e', '--ellipsis', action='store_true',
		               help='perform ellipsis normalization (default: no ellipsis normalization)')
	parser.add_argument('infile', nargs='*', type=argparse.FileType('r'), default=sys.stdin)
	args = parser.parse_args()
	#Run main function
	sys.exit(main(args))
