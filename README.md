farsiNLPTools
=========

Open-source dependency parser, part-of-speech tagger, and text normalizer for Farsi (Persian).

(1) Dependency Parser:
Downloadable as TurboParser model file from www.ark.cs.cmu.edu/TurboParser. Compatible with TurboParser v2.0.2. Please note this is *not* the current version of TurboParser; this dependency parser model is not tested with newer versions of TurboParser.

(2) Part-of-Speech Tagger:
farsi_tagger.model file downloadable here. Please see www.ark.cs.cmu.edu/TurboParser for instructions on how to use this POS tagger. Compatible with TurboTagger v2.0.2. Please note this is *not* the current version of TurboTagger; this part-of-speech tagger model is not tested with newer version of TurboTagger.

(3) Farsi Text Normalizer:
Downloadable as a python script.

Usage: python farsiNorm.py (-a for Arabic text) (-e for normalize ellipsis) infile > outfile

=========

Please also download our Farsi Verb Tokenizer here:
www.github.com/mehdi-manshadi/Farsi-Verb-Tokenizer

=========

Intended usage:

Pre-process your Farsi text using a sentence segmenter and tokenizer such as the Mojgan Seraji's SeTPer (http://stp.lingfil.uu.se/~mojgan/setper.html). Then, use our Farsi Verb Tokenizer (see above) and our Farsi Text Normalizer (see above) as two additional pre-processing steps. Finally, tag and parse your line-separated sentences using TurboTagger and TurboParser, with our POS tagger model file (see above) and dependency parser model file (see above). Use the TurboParser documentation (http://www.cs.cmu.edu/~afm/TurboParser/README) to learn how to tag and parse data.

If you use the resources contained in this repo, cite the following paper:

Weston Feely, Mehdi Manshadi, Robert Frederking and Lori Levin. “The CMU METAL Farsi NLP Approach.” In Proceedings of the Ninth Language Resources and Evaluation Conference (LREC). Reykjavik, Iceland. May, 2014.

PDF of the paper here: http://www.lrec-conf.org/proceedings/lrec2014/pdf/596_Paper.pdf
