import sqlite3
import pandas as pd
import xml.etree.ElementTree as ET



"""Surah Ayah Text From Tanzil Quran"""
def getDFSurahAyahIndexed(xmlFile):
    # create element tree object 
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    SurahAyahTouples = []
    SurahAyahText = []
    for item in root.findall("./sura"):
        for child in item:
            SurahAyahTouples.append((int(item.attrib['index']),int(child.attrib['index'])))
            if('bismillah' not in child.attrib):
                SurahAyahText.append([item.attrib['name'],child.attrib['text'],0])
            else:
                SurahAyahText.append([item.attrib['name'],child.attrib['text'],child.attrib['bismillah']])
    index = pd.MultiIndex.from_tuples(SurahAyahTouples)
    index.set_names(['SurahNumber','AyahNumber'], inplace=True)
    return (pd.DataFrame(SurahAyahText,columns=['SurahName','Ayah','Bismillah'],index=index))





"""Tanzil XML Suras Meta Parser"""  
def getTanzilMetaDataSuras(xmlFile):
    # create element tree object 
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    SurahByIndex = []
    SurahByIndexAttribs = []
    for item in root.findall("./suras"):
        for child in item:
            SurahByIndex.append(child.attrib['index'])
            SurahByIndexAttribs.append((child.attrib['ayas'],
                                        child.attrib['start'],
                                        child.attrib['name'],
                                        child.attrib['tname'],
                                        child.attrib['ename'],
                                        child.attrib['type'],
                                        child.attrib['order'],
                                        child.attrib['rukus']))
    columns = ['ayas','start','name','tname','ename','type','order','rukus']
    return (pd.DataFrame(SurahByIndexAttribs,columns=columns,index=pd.Index(SurahByIndex).astype('int32')))




def process_command(**kwargs):
    if 'filepath' in kwargs:
        print(f"Filepath: {kwargs['filepath']}")
        #print(getDFSurahAyahIndexed(kwargs['filepath']).head(5))
    else:
        print("no File Path is specified. python parser.py filepath=/path/to/file.xml")
        return
    if 'tblname' in kwargs:
        print(f"Sqllite Table: {kwargs['tblname']}")
    else:
        print("no table name is specified. python parser.py filepath=/path/to/file.xml tblname=quran-simple-clean.xml")
        return
    try:
        conn = sqlite3.connect('../data/tanzilquran.db')
        getDFSurahAyahIndexed(kwargs['filepath']).to_sql(kwargs['tblname'],conn,if_exists='replace',index=True)
        print("Databse table created! ")
    except Exception as ex:
        print (f"Error: {ex}")
        
    