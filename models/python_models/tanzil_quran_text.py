import pandas as pd


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

def model(dbt, session):
    dbt.configure(materialized="table")
    AlQuranDF = getDFSurahAyahIndexed("seeds/quran-uthmani")
    # warm things up just a little
    #df = temps_df.withColumn("degree_plus_one", add_one(temps_df["degree"]))
    return AlQuranDF