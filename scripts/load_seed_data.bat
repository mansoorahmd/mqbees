@echo off

echo Parsing quran-simple-clean.xml
python parser.py mushaf filepath=../seeds/quran_text/quran-simple-clean.xml tblname=sc_loaded_quran-simple-clean

echo Parsing quran-simple-min.xml
python parser.py mushaf filepath=../seeds/quran_text/quran-simple-min.xml tblname=sc_loaded_quran-simple-min

echo Parsing quran-simple-plain.xml
python parser.py mushaf filepath=../seeds/quran_text/quran-simple-plain.xml tblname=sc_loaded_quran-simple-plain

echo Parsing quran-simple.xml
python parser.py mushaf filepath=../seeds/quran_text/quran-simple.xml tblname=sc_loaded_quran-simple

echo Parsing quran-uthmani-min.xml
python parser.py mushaf filepath=../seeds/quran_text/quran-uthmani-min.xml tblname=sc_loaded_quran-uthmani-min

echo Parsing quran-uthmani.xml
python parser.py mushaf filepath=../seeds/quran_text/quran-uthmani.xml tblname=sc_loaded_quran-uthmani


echo Loading Morphology
python parser.py mor filepath=../seeds/morphology/quranic-corpus-morphology-0.4.txt

echo Done
