
"""
postprocess the generator output
ex. i don ' t have a money . how about you ? => I don't have a money. How about you?

"""
def joint_sentence(s):
    """Split the string s into a list of sentences."""
    try: s+""
    except: raise TypeError( "s must be a string" )

    s = s.replace(" .", ".")
    s = s.replace(" ,", ",")
    s = s.replace(" !", "!")
    s = s.replace(" ?", "?")
    s = s.replace(" ' ", "'")
    s = s.replace(' " ', '"')

    pos = 0
    sentenceList = []
    l = len(s)
    while pos < l:
        try: p = s.index('.', pos)
        except: p = l+1
        try: q = s.index('?', pos)
        except: q = l+1
        try: e = s.index('!', pos)
        except: e = l+1
        end = min(p,q,e)
        if pos != end:
            sentenceList.append( s[pos:end+1].strip().capitalize() )
        pos = end+1
    # If no sentences were found, return a one-item list containing
    # the entire input string.
    if len(sentenceList) == 0: sentenceList.append(s.capitizalie())
    sentence = ' '.join(map(str, sentenceList))
    return sentence
