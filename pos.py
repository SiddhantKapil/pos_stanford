from nltk.tag.stanford import StanfordPOSTagger
st = StanfordPOSTagger('english-bidirectional-distsim.tagger')
print(st.tag('What is the airspeed of an unladen swallow ?'.split()))
