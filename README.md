farsiNLPTools
=========

Open-source dependency parser, part-of-speech tagger, and text normalizer for Farsi (Persian).

(1) Dependency Parser:
Downloadable as TurboParser (www.ark.cs.cmu.edu/TurboParser) model file. Compatible with TurboParser v2.0.2. Please note this is *not* the current version of TurboParser; this dependency parser model is not tested with newer versions of TurboParser.

(2) Part-of-Speech Tagger:
Downloadable as TurboTagger (www.ark.cs.cmu.edu/TurboParser) model file. Compatiable with TurboTagger v2.0.2. Please note this is *not* the current version of TurboTagger; this part-of-speech tagger model is not tested with newer version of TurboTagger.

(3) Farsi Text Normalizer:
Downloadable as a python script.

Usage: python farsiNorm.py (-a for Arabic text) (-e for normalize ellipsis) infile > outfile

=========

Please also download our Farsi Verb Tokenizer here:
www.github.com/mehdi-manshadi/Farsi-Verb-Tokenizer

=========

Intended usage:
Pre-process your Farsi text using a sentence segmenter and tokenizer such as the Mojgan Seraji's SeTPer (http://stp.lingfil.uu.se/~mojgan/setper.html). Then, use our Farsi Verb Tokenizer (see above) and our Farsi Text Normalizer (see above) as two additional pre-processing steps. Finally, tag and parse your line-separated sentences using TurboTagger and TurboParser, with our dependency parser model file (see above, and use TurboParser documentation to learn how to tag and parse data).

For further information, please read our (forthcoming) LREC 2014 paper:
Weston Feely, Mehdi Manshadi, Robert Frederking and Lori Levin. “The CMU METAL Farsi NLP Approach.” In Proceedings of the Ninth Language Resources and Evaluation Conference (LREC). Reykjavik, Iceland. May, 2014. In Press.
