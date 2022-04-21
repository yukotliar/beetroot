# Task 1
#
# Make a program that has some sentence (a string) on input
# and returns a dict containing all unique words as keys and the number of occurrences as values.
text = 'accusantibus aeternum aiebat alienae aliquem delectat dici appellant bonum confidam constituamus cubilia curiosi cyrenaicos ' \
       'declinare definiebas delectant delectat dici fortasse geometriaque divelli doctus dominos donec efficiendi eosque fabulis fastidii ' \
       'fierent filium iniuria interpretaris fortasse geometriaque homero i iactant illud impetus improbis inane inanitate inclusae individua' \
       ' iniuria interpretaris magistra malum mandamus iucunditatem iudicari laetitia laetitiam laudandis legemus leniat liberamur liquidae ' \
       'ludicra ludus luptatum magistra malum mandamus nominata ocurreret ornatus paranda perdiscere perpetuam perpetuis' \
       ' pertinax plura praeclaram reprehensiones sapientium servir praetermittenda praetor probet prospexit pueriliter quosdam rectas referta religionis ' \
       'relinqueret reprehensiones sapientium servire viros virtutes virtutu studiose sua tantis temeritas tria triarium turpius umbram utilior ' \
       'utinam utrumque venire videatur videri viros virtutes virtutum vituperatoribus viverra vix voluit'.split()
words_count = {}
text_without_duplicates = set(text)
if len(text) == len(text_without_duplicates):
    print('This text does\'nt have any duplicate words')
else:
    for word in text_without_duplicates:
        words_count[word] = text.count(word)
print(words_count)