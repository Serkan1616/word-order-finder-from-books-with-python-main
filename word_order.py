# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 21:25:35 2021

@author: Serkan
"""
def Word_Order_Frequency_One_Book (Book, Word_Order, File_Output):

    import operator #to sort the library
   
      
    while (Word_Order>2):
        print("Wrong number!!!")
        Word_Order=int(input("Please enter (1 or 2) "))
    
        
    try:
        with open(Book,"r",encoding='utf-8') as s:
          s_contents=s.read()
          s_contents=s_contents.lower()
          def remove_punch(s_contents): #to remove punctuation
           s_contents=s_contents.replace(".","")
           s_contents=s_contents.replace(",","")
           s_contents=s_contents.replace("-","")
           s_contents=s_contents.replace("’","")
           s_contents=s_contents.replace(":","")
           s_contents=s_contents.replace("!","")
           s_contents=s_contents.replace("?","")
           s_contents=s_contents.replace("*","")
           s_contents=s_contents.replace("/","")
           s_contents=s_contents.replace("+","")
           s_contents=s_contents.replace("(","")
           s_contents=s_contents.replace(")","")
           s_contents=s_contents.replace(";","")
           s_contents=s_contents.replace("”","")
           s_contents=s_contents.replace("“","")
           s_contents=s_contents.replace('"',"")
           s_contents=s_contents.replace('_',"")
           return (s_contents)
          contents=remove_punch(s_contents)
          words=contents.split()# I keep a list of words
          def stop_Words(): #words to be omitted
           stop_words = ['able', 'about', 'above', 'abroad', 'according', 'accordingly',
           'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
           'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
           'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
           'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
           'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
           'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
           'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
           'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
           'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
           'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
           'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
           'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
           'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
           'consequently', 'consider', 'considering', 'contain', 'containing',
           'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
           'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
           'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
           'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
           'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
           'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
           'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
           'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
           'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
           'following', 'follows', 'for', 'forever', 'former', 'formerly',
           'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
           'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
           'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
           'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
           'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
           'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
           'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
           'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
           'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
           'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
           'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
           'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
           'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
           'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
           'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
           'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
           'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
           'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
           'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
           'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
           'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
           'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
           'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
           'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
           'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
           'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
           'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
           'overall', 'own', 'particular', 'particularly', 'past', 'per',
           'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
           'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
           'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
           'regardless', 'regards', 'relatively', 'respectively', 'right',
           'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
           'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
           'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
           'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
           'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
           'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
           'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
           'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
           'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
           'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
           'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
           'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
           'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
           'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
           'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
           'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
           'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
           'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
           'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
           'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
           'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
           'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
           'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
           'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
           'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
           'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
           'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
           'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
           'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
           'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
           'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
           'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
           'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
           'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
           'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
           'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
           'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
           'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
           'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
           'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
           'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
           'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
           'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
           'importance', 'important', 'index', 'information', 'invention', 'itd',
           'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
           'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
           'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
           'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
           'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
           'readily', 'ref', 'refs', 'related', 'research', 'resulted',
           'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
           'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
           'similar', 'similarly', 'slightly', 'somethan', 'specifically',
           'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
           'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
           'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
           'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
           'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
           'world', 'youd', 'youre']
           return stop_words    
          stopwords=stop_Words()                    
          for word in range(0,len(words)): #finds stop words and translates them ""       
             for stop in range(0,len(stopwords)):
                 if(words[word]==stopwords[stop]):                  
                    words[word]=""                  
                    break                  
                 else:
                      pass
           
          if(Word_Order==1): #word order=1
             def count_for_one_words(words):
                words.sort()             
                while(words[0]==""):
                  words.remove("")          
                count_dic={}
                for word in range(0,len(words)):
                    if words[word] in count_dic.keys(): #zaten kütüphanede ise kelime 1 artır
                       count_dic[words[word]]=count_dic[words[word]]+1           
                    if words[word] not in count_dic.keys(): #değilse oluştur
                       count_dic[words[word]]=1
                    else:
                        pass                 
                return (count_dic)
             result_dic=count_for_one_words(words)
          elif(Word_Order==2): #word order=2
             def count_for_two_words(words):
                count_dic={}
                for word in range(0,len(words)-1):
                    if words[word]!="" and words[word+1]!="": #sort yapamadığımdan boşlukları sildiremedim o yüzden "" değilse
                       a="" 
                       a=words[word]+" "+words[word+1]
                       if a in count_dic.keys(): #eğer varsa kütüphanede 1 artırıyor
                         count_dic[a]=count_dic[a]+1
                       if a not in count_dic.keys(): #yoksa kütüphaneye ekliyor
                         count_dic[a]=1        
                return (count_dic)
             result_dic=count_for_two_words(words)
        
          #at the bottom it sorts the library by  values
          result_dic = dict( sorted(result_dic.items(), key=operator.itemgetter(1),reverse=True))
        
          with open(File_Output, 'w') as file: #writes the words to file
             count_for_sequance=0
             spaces=0
             file.write("| WORD          | WORD              |"+"\n")
             file.write("| ORDER         | ORDER             |"+"\n")
             file.write("| FREQUENCY     | SEQUENCE          |"+"\n")
             file.write("-------------------------------------"+"\n")
           
                                        
             for key,value in result_dic.items(): #stops when count is 100
                firstspace=" "*1
                spaces=0
                spacestwo=2
                if(value>9999): #to determine the number of spaces
                    c=5
                elif(value>999):
                    c=4
                elif(value>99):
                    c=3
                elif(value>9):
                    c=2
                else:
                    c=1
                for b in range(0,11):                   
                     if(c<=b):
                          spaces=spaces+1                                                      
                d=" "*spaces                          
                file.write("|"+firstspace+str(value))
                file.write(d+"   |")        
                d=" "*spacestwo             
                file.write(d)
                file.write(key+"\n")
              
              
                count_for_sequance +=1
                if(count_for_sequance==100):
                    break
    except IOError:
        print ("there is no such file to read")                
def Word_Order_Frequency_Two_Books(Book_1,Book_2,Word_Order,File_Output):
    import operator
    flag=True
    while (Word_Order>2):
        print("Wrong number!!!")
        Word_Order=int(input("Please enter (1 or 2) "))
   
    try:
        with open(Book_1,"r",encoding='utf-8') as s:
         s_contents=s.read()
         s_contents=s_contents.lower()
         def remove_punch(s_contents): #to remove punctuation
          s_contents=s_contents.replace(".","")
          s_contents=s_contents.replace(",","")
          s_contents=s_contents.replace("-","")
          s_contents=s_contents.replace("’","")
          s_contents=s_contents.replace(":","")
          s_contents=s_contents.replace(";","")
          s_contents=s_contents.replace("!","")
          s_contents=s_contents.replace("?","")
          s_contents=s_contents.replace("*","")
          s_contents=s_contents.replace("/","")
          s_contents=s_contents.replace("+","")
          s_contents=s_contents.replace("(","")
          s_contents=s_contents.replace(")","")
          s_contents=s_contents.replace(";","")
          s_contents=s_contents.replace("”","")
          s_contents=s_contents.replace("“","")
          s_contents=s_contents.replace('"',"")
          s_contents=s_contents.replace('_',"")
          return (s_contents)
         contents=remove_punch(s_contents)
         words=contents.split() # I keep a list of words
         def stop_Words(): #words to be omitted  
          stop_words = ['able', 'about', 'above', 'abroad', 'according', 'accordingly',
           'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
           'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
           'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
           'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
           'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
           'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
           'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
           'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
           'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
           'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
           'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
           'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
           'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
           'consequently', 'consider', 'considering', 'contain', 'containing',
           'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
           'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
           'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
           'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
           'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
           'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
           'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
           'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
           'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
           'following', 'follows', 'for', 'forever', 'former', 'formerly',
           'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
           'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
           'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
           'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
           'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
           'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
           'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
           'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
           'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
           'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
           'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
           'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
           'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
           'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
           'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
           'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
           'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
           'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
           'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
           'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
           'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
           'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
           'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
           'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
           'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
           'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
           'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
           'overall', 'own', 'particular', 'particularly', 'past', 'per',
           'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
           'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
           'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
           'regardless', 'regards', 'relatively', 'respectively', 'right',
           'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
           'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
           'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
           'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
           'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
           'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
           'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
           'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
           'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
           'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
           'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
           'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
           'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
           'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
           'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
           'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
           'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
           'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
           'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
           'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
           'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
           'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
           'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
           'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
           'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
           'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
           'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
           'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
           'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
           'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
           'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
           'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
           'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
           'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
           'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
           'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
           'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
           'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
           'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
           'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
           'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
           'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
           'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
           'importance', 'important', 'index', 'information', 'invention', 'itd',
           'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
           'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
           'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
           'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
           'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
           'readily', 'ref', 'refs', 'related', 'research', 'resulted',
           'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
           'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
           'similar', 'similarly', 'slightly', 'somethan', 'specifically',
           'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
           'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
           'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
           'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
           'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
           'world', 'youd', 'youre']
          return stop_words    
         stopwords=stop_Words()                    
         for word in range(0,len(words)):     #finds stop words and translates them ""    
            for stop in range(0,len(stopwords)):
                if(words[word]==stopwords[stop]):                  
                   words[word]=""                  
                   break                  
                else:
                     pass
           
         if(Word_Order==1): #word order=1
             def count_for_one_words(words):
                words.sort()             
                while(words[0]==""):
                  words.remove("")          
                count_dic={}
                for word in range(0,len(words)):
                    if words[word] in count_dic.keys():
                      count_dic[words[word]]=count_dic[words[word]]+1           
                    if words[word] not in count_dic.keys():
                       count_dic[words[word]]=1
                    else:
                        pass                 
                return (count_dic)
             result_dic_book1=count_for_one_words(words)
         elif(Word_Order==2): #word order=2
             def count_for_two_words(words):
                count_dic={}
                for word in range(0,len(words)-1):
                    if words[word]!="" and words[word+1]!="":
                       a="" 
                       a=words[word]+" "+words[word+1]
                       if a in count_dic.keys():
                         count_dic[a]=count_dic[a]+1
                       if a not in count_dic.keys():
                         count_dic[a]=1       
                return (count_dic)
             result_dic_book1=count_for_two_words(words)
        
            
        #at the bottom it sorts the library by  values
         result_dic_book1 = dict( sorted(result_dic_book1.items(), key=operator.itemgetter(1),reverse=True))
    except IOError:
        print("there is no such file to read")
        flag=False
    try:
        with open(Book_2,"r",encoding='utf-8') as s: #same operations as above
         s_contents=s.read()
         s_contents=s_contents.lower()
         def remove_punch(s_contents):
          s_contents=s_contents.replace(".","")
          s_contents=s_contents.replace(",","")
          s_contents=s_contents.replace("-","")
          s_contents=s_contents.replace("’","")
          s_contents=s_contents.replace(":","")
          s_contents=s_contents.replace(";","")
          s_contents=s_contents.replace("!","")
          s_contents=s_contents.replace("?","")
          s_contents=s_contents.replace("*","")
          s_contents=s_contents.replace("/","")
          s_contents=s_contents.replace("+","")
          s_contents=s_contents.replace("(","")
          s_contents=s_contents.replace(")","")
          s_contents=s_contents.replace(";","")
          s_contents=s_contents.replace("”","")
          s_contents=s_contents.replace("“","")
          s_contents=s_contents.replace('"',"")
          s_contents=s_contents.replace('_',"")
          return (s_contents)
         contents=remove_punch(s_contents)
         words=contents.split()
         def stop_Words():
          stop_words = ['able', 'about', 'above', 'abroad', 'according', 'accordingly',
           'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
           'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
           'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
           'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
           'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
           'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
           'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
           'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
           'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
           'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
           'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
           'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
           'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
           'consequently', 'consider', 'considering', 'contain', 'containing',
           'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
           'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
           'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
           'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
           'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
           'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
           'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
           'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
           'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
           'following', 'follows', 'for', 'forever', 'former', 'formerly',
           'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
           'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
           'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
           'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
           'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
           'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
           'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
           'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
           'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
           'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
           'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
           'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
           'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
           'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
           'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
           'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
           'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
           'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
           'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
           'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
           'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
           'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
           'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
           'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
           'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
           'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
           'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
           'overall', 'own', 'particular', 'particularly', 'past', 'per',
           'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
           'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
           'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
           'regardless', 'regards', 'relatively', 'respectively', 'right',
           'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
           'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
           'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
           'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
           'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
           'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
           'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
           'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
           'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
           'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
           'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
           'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
           'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
           'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
           'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
           'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
           'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
           'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
           'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
           'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
           'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
           'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
           'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
           'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
           'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
           'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
           'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
           'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
           'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
           'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
           'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
           'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
           'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
           'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
           'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
           'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
           'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
           'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
           'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
           'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
           'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
           'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
           'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
           'importance', 'important', 'index', 'information', 'invention', 'itd',
           'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
           'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
           'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
           'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
           'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
           'readily', 'ref', 'refs', 'related', 'research', 'resulted',
           'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
           'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
           'similar', 'similarly', 'slightly', 'somethan', 'specifically',
           'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
           'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
           'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
           'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
           'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
           'world', 'youd', 'youre']
          return stop_words    
         stopwords=stop_Words()                    
         for word in range(0,len(words)):       
            for stop in range(0,len(stopwords)):
               if(words[word]==stopwords[stop]):                  
                  words[word]=""                  
                  break                  
               else:
                    pass
           
        if(Word_Order==1):
            def count_for_one_words(words):
               words.sort()             
               while(words[0]==""):
                 words.remove("")          
               count_dic={}
               for word in range(0,len(words)):
                   if words[word] in count_dic.keys():
                      count_dic[words[word]]=count_dic[words[word]]+1           
                   if words[word] not in count_dic.keys():
                      count_dic[words[word]]=1
                   else:
                       pass                 
               return (count_dic)
            result_dic_book2=count_for_one_words(words)
        elif(Word_Order==2):
            def count_for_two_words(words):
               count_dic={}
               for word in range(0,len(words)-1):
                   if words[word]!="" and words[word+1]!="":
                      a="" 
                      a=words[word]+" "+words[word+1]
                      if a in count_dic.keys():
                        count_dic[a]=count_dic[a]+1
                      if a not in count_dic.keys():
                        count_dic[a]=1        
               return (count_dic)
            result_dic_book2=count_for_two_words(words)
                         
        result_dic_book2 = dict( sorted(result_dic_book2.items(), key=operator.itemgetter(1),reverse=True))
    except IOError:
        print("there is no such file to read")
        flag=False
   
    common_book1_words={}
    common_book2_words={}    
    result_dic_books={}
    
    if(flag):
        for k,v in result_dic_book1.items():
         for k2,v2 in result_dic_book2.items():
            if k==k2:
                result_dic_books[k]=v+v2
                common_book1_words[k]=v
                common_book2_words[k2]=v2
                break
            else:
                pass
        result_dic_books = dict( sorted(result_dic_books.items(), key=operator.itemgetter(1),reverse=True))                
        with open(File_Output,"w",encoding='utf-8') as f: #writes the words to file
          a=0
          count=0       
          first_line= '{:>0}  {:>8}  {:>8} {:>8} '.format("|  TOTAL    ","|  BOOK 1   ","|  BOOK 2   ","|  WORD                |")
          second_line='{:>0}  {:>8}  {:>8} {:>8} '.format("|  ORDER    ","|  ORDER    ","|  ORDER    ","|  ORDER               |",)
          third_line= '{:>0}  {:>8}  {:>8} {:>8} '.format("|  FREQUENCY","|  FREQUENCY","|  FREQUENCY","|  FREQUENCY           |",)
          f.write(first_line+"\n")
          f.write(second_line+"\n")
          f.write(third_line+"\n")
          f.write("-----------------------------------------------------------------"+"\n")
          for k,v in result_dic_books.items():
              line=""
              line='{:>0}  {:>6}  {:>4}  {:>6}  {:>4}  {:>4}  {:>5}  {:>6}  '.format("|",str(v),"|",str(common_book1_words[k]),"|", str(common_book2_words[k]),"|",k)
              f.write(line+"\n")
              count+=1
              a+=1
              if(count==100): #stops when count is 100
                  break
    else:
        pass
    
   
    
        
    