
"""
Morphology file loading to Pandas and assigning global ayah index from 1 to 6236
File is downloaded from corpus.quran.com
"""
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