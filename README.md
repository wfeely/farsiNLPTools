farsiNLPTools
=========

Open-source dependency parser and text normalizer for Farsi (Persian).

(1) Dependency Parser:
Downloadable as TurboParser (www.ark.cs.cmu.edu/TurboParser) model file. Compatible with TurboParser v2.0.2. Please note this is *not* the current version of TurboParser; this dependency parser model is not tested with newer versions of TurboParser.

(2) Farsi Text Normalizer:
Downloadable as a python script.

Usage: python farsiNorm.py (-a for Arabic text) (-e for normalize ellipsis) infile > outfile

=========

Please also download our Farsi Verb Tokenizer here:
www.github.com/mehdi-manshadi/Farsi-Verb-Tokenizer

=========

Intended usage:
Pre-process your Farsi text using a sentence segmenter and tokenizer such as the Mojgan Seraji's SeTPer (http://stp.lingfil.uu.se/~mojgan/setper.html). Then, use our Farsi Verb Tokenizer (see above) and our Farsi Text Normalizer (see above) as two additional pre-processing steps. Finally, parse your line-separated sentences using TurboParser, with our dependency parser model file (see above, and use TurboParser documentation to learn how to parse data).
