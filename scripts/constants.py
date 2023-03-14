# encoding:utf-8

"""
@author: Assem Chelli
@contact:  assem.ch [at] gmail.com
@license:  GPL
"""

#:buckwalter code
BUCKWALTER2UNICODE = {"'": u"\u0621",  # hamza-on-the-line
                      "|": u"\u0622",  # madda
                      ">": u"\u0623",  # hamza-on-'alif
                      "&": u"\u0624",  # hamza-on-waaw
                      "<": u"\u0625",  # hamza-under-'alif
                      "}": u"\u0626",  # hamza-on-yaa'
                      "A": u"\u0627",  # bare 'alif
                      "b": u"\u0628",  # baa'
                      "p": u"\u0629",  # taa' marbuuTa
                      "t": u"\u062A",  # taa'
                      "v": u"\u062B",  # thaa'
                      "j": u"\u062C",  # jiim
                      "H": u"\u062D",  # Haa'
                      "x": u"\u062E",  # khaa'
                      "d": u"\u062F",  # daal
                      "*": u"\u0630",  # dhaal
                      "r": u"\u0631",  # raa'
                      "z": u"\u0632",  # zaay
                      "s": u"\u0633",  # siin
                      "$": u"\u0634",  # shiin
                      "S": u"\u0635",  # Saad
                      "D": u"\u0636",  # Daad
                      "T": u"\u0637",  # Taa'
                      "Z": u"\u0638",  # Zaa' (DHaa')
                      "E": u"\u0639",  # cayn
                      "g": u"\u063A",  # ghayn
                      "_": u"\u0640",  # taTwiil
                      "f": u"\u0641",  # faa'
                      "q": u"\u0642",  # qaaf
                      "k": u"\u0643",  # kaaf
                      "l": u"\u0644",  # laam
                      "m": u"\u0645",  # miim
                      "n": u"\u0646",  # nuun
                      "h": u"\u0647",  # haa'
                      "w": u"\u0648",  # waaw
                      "Y": u"\u0649",  # 'alif maqSuura
                      "y": u"\u064A",  # yaa'
                      "F": u"\u064B",  # fatHatayn
                      "N": u"\u064C",  # Dammatayn
                      "K": u"\u064D",  # kasratayn
                      "a": u"\u064E",  # fatHa
                      "u": u"\u064F",  # Damma
                      "i": u"\u0650",  # kasra
                      "~": u"\u0651",  # shaddah
                      "o": u"\u0652",  # sukuun
                      "`": u"\u0670",  # dagger 'alif
                      "{": u"\u0671",  # waSla
                      # extended here
                      "^": u"\u0653",  # Maddah
                      "#": u"\u0654",  # HamzaAbove

                      ":": "\u06DC",  # SmallHighSeen
                      "@": "\u06DF",  # SmallHighRoundedZero
                      "\"": "\u06E0",  # SmallHighUprightRectangularZero
                      "[": "\u06E2",  # SmallHighMeemIsolatedForm
                      ";": "\u06E3",  # SmallLowSeen
                      ",": "\u06E5",  # SmallWaw
                      ".": "\u06E6",  # SmallYa
                      "!": "\u06E8",  # SmallHighNoon
                      "-": "\u06EA",  # EmptyCentreLowStop
                      "+": "\u06EB",  # EmptyCentreHighStop
                      "%": "\u06EC",  # RoundedHighStopWithFilledCentre
                      "]": "\u06ED"  #

                      }
ROOT2BUCK =           { "Alif":"A",
                        "Ayn":"E",
                        "Ba":"b",
                        "Dad":"D",
                        "Dal":"d",
                        "Fa":"f",
                        "Gh":"g",
                        "ha":"h",
                        "Ha":"H",
                        "Jiim":"j",
                        "Kaf":"k",
                        "Kh":"x",
                        "Lam":"l",
                        "Miim":"m",
                        "Nun":"n",
                        "Qaf":"q",
                        "Ra":"r",
                        "Sad":"S",
                        "Shiin":"$",
                        "Siin":"s",
                        "Ta":"t",
                        "Tay":"T",
                        "Tha":"v",
                        "Thal":"*",
                        "Waw":"w",
                        "Ya":"y",
                        "Za":"Z",
                        "Zay":"z",
                        "hamza":"#"
                       }
POS = {
    "N": (u"اسم", "Noun"),
    "PN": (u"اسم علم", "Proper noun"),
    "IMPN": (u"اسم فعل أمر", "Imperative verbal noun"),
    "PRON": (u"ضمير", "Personal pronoun"),
    "DEM": (u"اسم اشارة", "Demonstrative pronoun"),
    "REL": (u"اسم موصول", "Relative pronoun"),
    "ADJ": (u"صفة", "Adjective"),
    "NUM": (u"رقم", "Number"),
    "T": (u"ظرف زمان", "Time adverb"),
    "LOC": (u"ظرف مكان", "Location adverb"),
    "V": (u"فعل", "Verb"),
    "P": (u"حرف جر", "Preposition"),
    "EMPH": (u"لام التوكيد", "Emphatic lām prefix"),
    "IMPV": (u"لام الامر", "Imperative lām prefix"),
    "PRP": (u"لام التعليل", "Purpose lām prefix"),
    "CONJ": (u"حرف عطف", "Coordinating conjunction"),
    "SUB": (u"حرف مصدري", "Subordinating conjunction"),
    "ACC": (u"حرف نصب", "Accusative particle"),
    "AMD": (u"حرف استدراك", "Amendment particle"),
    "ANS": (u"حرف جواب", "Answer particle"),
    "AVR": (u"حرف ردع", "Aversion particle"),
    "CAUS": (u"حرف سببية", "Particle of cause"),
    "CERT": (u"حرف تحقيق", "Particle of certainty"),
    "COND": (u"حرف شرط", "Conditional particle"),
    "EQ": (u"حرف تسوية", "Equalization particle"),
    "EXH": (u"حرف تحضيض", "Exhortation particle"),
    "EXL": (u"حرف تفصيل", "Explanation particle"),
    "EXP": (u"أداة استثناء", "Exceptive particle"),
    "FUT": (u"حرف استقبال", "Future particle"),
    "INC": (u"حرف ابتداء", "Inceptive particle"),
    "INTG": (u"حرف استفهام", "Interogative particle"),
    "NEG": (u"حرف نفي", "Negative particle"),
    "PREV": (u"حرف كاف", "Preventive particle"),
    "PRO": (u"حرف نهي", "Prohibition particle"),
    "REM": (u"حرف استئنافية", "Resumption particle"),
    "RES": (u"أداة حصر", "Restriction particle"),
    "RET": (u"حرف اضراب", "Retraction particle"),
    "SUP": (u"حرف زائد", "Supplemental particle"),
    "SUR": (u"حرف فجاءة", "Surprise particle"),
    "VOC": (u"حرف نداء", "Vocative particle"),
    "INL": (u"حروف مقطعة", "Quranic initials"),
    "DET": ("_", "DET – determiner"),
    "CIRC":("حرف حال", "Circumstantial particle"),
    "RSLT":("حرف واقع في جواب الشرط", "Result particle"),
    "INT":("حرف تفسير", "Particle of interpretation"),
    "COM":("واو المعية", "Comitative particle")
    
}

POSclass = {
    "Nouns": ["N", "PN", "IMPN"],
    "Pronouns": ["DEM", "REL", "PRON"],
    "Nominals": ["ADJ", "NUM"],
    "Adverbs": ["T", "LOC"],
    "Verbs": ["V"],
    "Prepositions": ["P"],
    "lām Prefixes": ["EMPH", "IMPV", "PRP"],
    "Conjunctions": ["CONJ", "SUB"],
    "Particles": ["ACC", "AMD", "ANS", "AVR", "CAUS", "CERT", "COND", "EQ", "EXH", "EXL", "EXP", "FUT", "INC", "INTG",
                  "NEG", "PREV", "PRO", "REM", "RES", "RET", "SUP", "SUR", "VOC","CIRC","RSLT","INT","COM"],
    "Disconnected Letters": ["INL"]
}

PREFIXclass = {
    "determiner": ["Al+"],
    "preposition": ["bi+", "ka+", "ta+", "l:P+","w:P+"],
    "future particle": ["sa+"],
    "vocative particle": ["ya+", "ha+"],
    "interrogative particle": ["A:INTG+"],
    "equalization particle": ["A:EQ+"],
    "conjunction": ["wa:CONJ+", "f:CONJ+"],
    "resumption": ["w:REM+","f:REM+"],
    "circumstantial": ["w:CIRC+"],
    "supplemental": ["w:SUP+","f:SUP+"],
    "comitative" : ["w:COM+"],
    "result" : ["f:RSLT+"],
    "supplemental" : ["f:SUP+","w:SUP+"],
    "cause": ["f:CAUS+"],
    "emphasis": ["l:EMPH+"],
    "purpose": ["l:PRP+"],
    "imperative": ["l:IMPV+"],
    "--undefined--": ["A+", "fa+"]
}

PREFIX = {
    "Al+": (u"ال", u"al",'DET – determiner prefix ("the")'),
    "bi+": (u"ب", u"bi",'P – preposition prefix ("by", "with", "in")'),
    "ka+": (u"ك", u"ka",'P – preposition prefix ("like" or "thus")'),
    "ta+": (u"ت", u"ta",'P – particle of oath prefix used as a preposition ("by Allah")'),
    "sa+": (u"س", u"sa",'P – prefixed particle indicating the future ("they will")'),
    "ya+": (u"يا", u"yā",'VOC – a vocative prefix usually translated as "O"'),
    "ha+": (u"ها", u"hā",'VOC – a vocative prefix usually translated as "Lo!"'),
    
    "A+": (u"أ", u"alif"),
    "A:INTG+": (u"أ", u"alif",'INTG – prefixed interrogative particle ("is?", "did?", "do?")'),
    "A:EQ+": (u"أ", u"alif",'EQ – prefixed equalization particle ("whether")'),

    "wa+": (u"و", u"wa"),
    "w:CONJ+":(u"و", u"wa",'CONJ – conjunction prefix ("and")'),
    "w:REM+":(u"و", u"wa",'REM – resumption prefix ("then" or "so")'),
    "w:CIRC+":(u"و", u"wa",'CIRC – circumstantial prefix ("while")'),
    "w:SUP+":(u"و", u"wa",'SUP – supplemental prefix ("then" or "so")'),
    "w:P+": (u"و", u"wa",'P – particle of oath prefix used as a preposition ("by the pen")'),
    "w:COM+": (u"و", u"wa",'COM – comitative prefix ("with")'),

    "fa+": (u"ف", u"fa"),
    "f:CONJ+": (u"ف", u"fa",'CONJ – conjunction prefix ("and")'),
    "f:REM+": (u"ف", u"fa",'REM – resumption prefix ("then" or "so")'),
    "f:CAUS+": (u"ف", u"fa",'CAUS – cause prefix ("then" or "so")'),
    "f:RSLT+": (u"ف", u"fa",'RSLT – result prefix ("then")'),
    "f:SUP+": (u"ف", u"fa",'SUP – supplemental prefix ("then" or "so")'),

    "l:P+": (u"ل", u"lām",'P – the letter lām as a prefixed preposition'),
    "l:EMPH+": (u"ل", u"lām",'P – the letter lām as a prefixed particle used to give emphasis'),
    "l:PRP+": (u"ل", u"lām",'P – the letter lām as a prefixed particle used to indicate purpose'),
    "l:IMPV+": (u"ل", u"lām",'P – the letter lām as a prefixed particle used to form an imperative'),
}

PGNclass = {
    "person": ["1", "2", "3"],
    "number": ["S", "D", "P"],
    "gender": ["M", "F"]
}

PGN = {
    "1": u"متكلم",
    "2": u"مخاطب",
    "3": u"غائب",
    "M": u"مذّكر",
    "F": u"مؤنّث",
    "S": u"مفرد",
    "D": u"مثنّى",
    "P": u"جمع"
}

VERBclass = {
    "aspect": ["PERF", "IMPF", "IMPV"],
    "mood": ["IND", "SUBJ", "JUS", "ENG"],
    "voice": ["ACT", "PASS"],
    "form": ["(I)", "(II)", "(III)", "(IV)", "(V)", "(VI)", "(VII)", "(VIII)", "(IX)", "(X)", "(XI)", "(XII)"]
}

VERB = {
    "PERF": (u"فعل ماض", "Perfect verb"),
    "IMPF": (u"فعل مضارع", "Imperfect verb"),
    "IMPV": (u"فعل أمر", "Imperative verb"),
    "IND": (u"مرفوع", "Indicative mood"),
    "SUBJ": (u"منصوب", "Subjunctive mood"),
    "JUS": (u"مجزوم", "Jussive mood"),
    "ENG": (u"مؤكد", "Energetic mood"),
    "ACT": (u"مبني للمعلوم", "Active voice"),
    "PASS": (u"مبني للمجهول", "Passive voice"),
    "(I)": (u"", "First form"),
    "(II)": (u"", "Second form"),
    "(III)": (u"", "Third form"),
    "(IV)": (u"", "Fourth form"),
    "(V)": (u"", "Fifth form"),
    "(VI)": (u"", "Sixth form"),
    "(VII)": (u"", "Seventh form"),
    "(VIII)": (u"", "Eighth form"),
    "(IX)": (u"", "Ninth form"),
    "(X)": (u"", "Tenth form"),
    "(XI)": (u"", "Eleventh form"),
    "(XII)": (u"", "Twelfth form")
}

DERIVclass = {
    "derivation": ["ACT PCPL", "PASS PCPL", "VN"]
}

DERIV = {
    "ACT PCPL": (u"اسم فاعل", "Active participle"),
    "PASS PCPL": (u"اسم مفعول", "Passive participle"),
    "VN": (u"مصدر", "Verbal noun")
}

NOMclass = {
    "state": ["DEF", "INDEF"],
    "case": ["NOM", "ACC", "GEN"]
}

NOM = {
    "DEF": (u"معرفة", "Definite state"),
    "INDEF": (u"نكرة", "Indefinite state"),
    "NOM": (u"مرفوع", "Nominative case"),
    "ACC": (u"منصوب", "Accusative case"),
    "GEN": (u"مجرور", "Genitive case"),
}

PRON = {
    "*": {u"ني", u"نا", u"ك", u"كما", u"كم", u"ه", u"هما", u"هم", u"كن", u"ها", u"هن"},
    "1": {u"ني", u"نا"},
    "2": {u"ك", u"كما", u"كم", u"كن"},
    "3": {u"ه", u"ها", u"هما", u"هم", u"هن"},
    "M": {u"ني", u"نا", u"ك", u"كما", u"كم", u"ه", u"هما", u"هم"},
    "F": {u"ني", u"نا", u"ك", u"كما", u"كن", u"ها", u"هما", u"هن"},
    "S": {u"ني", u"ك", u"ه", u"ها"},
    "D": {u"نا", u"كما", u"هما"},
    "P": {u"نا", u"كم", u"هم", u"كن", u"هن"},
}