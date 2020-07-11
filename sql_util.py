from sql import getSongByName,getSongByGenreName,getSongByAlbumName,getSongByArtistName,getSongByComposerName,getTopList,removeCount
def sql_util(requirement,name):
    if requirement=='song name':
        return getSongByName(name)
    elif requirement=='melody' or requirement=='pop' or requirement=='jazz':
        #print("YES CALLING")
        return getSongByGenreName(requirement)
    elif requirement=='singer name':
        return getSongByArtistName(name)
    elif requirement=='composer name':
        return getSongByComposerName(name)
    elif requirement=='movie name':
        return getSongByAlbumName(name)
    elif requirement=='top songs':
        return getTopList()
    elif requirement=='exit':
        return removeCount()
    return 'none'
