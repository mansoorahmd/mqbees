
"""
Morphology file loading to Pandas and assigning global ayah index from 1 to 6236
File is downloaded from corpus.quran.com
"""
import sqlite3
from constants import BUCKWALTER2UNICODE as b2u
from constants import ROOT2BUCK as r2b
import pandas as pd
import numpy as np



"""BuckWalter to Unicode Converter"""
def buckToUniString(buck):
    result=""
    for ch in buck:
        try:
            result += b2u[ch]
        except:
            return None
            
    return result
"""Load Root Words"""

def rootToUni(root):
    uni=""
    chList = root.split("-")
    for ch in chList:
        ch = ch.lstrip().rstrip()
        if ch in r2b:
            uni += buckToUniString(r2b[ch])
            uni += " "
        else:
            print(root)
    return uni

def rootToBck(root):
    bck=""
    chList = root.split("-")
    for ch in chList:
        ch = ch.lstrip().rstrip().lstrip()
        if ch in r2b:
            bck += r2b[ch]
        else:
            print(root)
    return bck


def featureRootExtract(f):
    if "ROOT:" in f:
        fts = f.split("|")
        for ft in fts:
            if "ROOT" in ft:
                r = ft.split(":")
                return [r[1],buckToUniString(r[1])]
    else:
        return [None,None]
def featureLemmaExtract(f):
    if "LEM:" in f:
        fts = f.split("|")
        for ft in fts:
            if "LEM" in ft:
                r = ft.split(":")
                return [r[1],buckToUniString(r[1])]
    else:
        return [None,None]






def loadMorphology(morphologyFilePath):
    df = pd.read_csv(morphologyFilePath,names=['LOCATION','FORM','TAG','FEATURES'],skiprows=57,sep='\t')
    df[['Surah','Ayah','Word','SubWord']] = df.LOCATION.map(lambda x: x.lstrip('()').rstrip(')')).str.split(':',expand=True)
    df[['Surah','Ayah','Word']] = df[['Surah', 'Ayah','Word']].apply(pd.to_numeric)
    df = df.set_index(['Surah','Ayah','Word'])
    df = df.sort_index()
    grouped  = df.groupby(['Surah','Ayah']).count()
    grouped['autoIndex'] = np.arange(1,grouped.shape[0]+1)
    df['globalAyah'] = grouped.autoIndex
    
    wgrouped  = df.groupby(['Surah','Ayah','Word']).count()
    wgrouped['autoIndex'] = np.arange(1,wgrouped.shape[0]+1)
    df['globalWord'] = wgrouped.autoIndex
    return df

def process_command(**kwargs):
    if 'filepath' in kwargs:
        print(f"Filepath: {kwargs['filepath']}")
    else:
        print("no File Path is specified. python parser.py filepath=/path/to/file.xml")
        return
    
    try:
        conn = sqlite3.connect('../data/tanzilquran.db')
        mor_df = loadMorphology(kwargs['filepath'])
        mor_df[['BUCKROOT','UNICODEROOT']]  =  mor_df.FEATURES.apply(lambda x: pd.Series(featureRootExtract(x)))
        
        mor_df[['BUCKLEMMA','UNICODELEMMA']]  =  mor_df.FEATURES.apply(lambda x: pd.Series(featureLemmaExtract(x)))
        
        
        mor_df.to_sql('morphology',conn,if_exists='replace',index=True)
        print(f"Morphology Databse table created! ")
    except Exception as ex:
        print (f"Error: {ex}")