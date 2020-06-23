import regex

def censor(word):
    '''helper function to censor words with asterisks. Input: string'''
    
    # test if function input is string
    try: 
        if not isinstance(word, str):
            raise TypeError('Function censor takes in string type as parameter')

    except TypeError:
        print('Function censor takes in string type as parameter')
        return False   

    new_word = '*' * len(word)
    
    return new_word


def email_classifier(classified_words, email_text): 
    """Input: words TYPE list and email TYPE string 
    Replaces any found "classified" words in email string with astericks 
    Returns: Tuple with Boolean flag signaling if classified words found, and new censored email"""

    # test if function inputs are list and string type
    try: 
        if not (isinstance(classified_words, list) and isinstance(email_text, str)):
            raise TypeError('Function email_classifier takes in list, string as parameters')

    except TypeError:
        print('Function email_classifier takes in list, string as parameters')
        return False    

    ### init return variables
    classified_flag = False
    censored_text = []

    # create new list of words by splitting original email by special characters and space characters so we can match words 
    email_word_list = regex.findall(r"\s+|\W+|\w+", email_text)
   
    # create dictionary from classified words for faster lookup resulting in average time complexity of O(1) 
    classified_words_dict = { classified_words[i].lower() : i for i in range(0, len(classified_words)) }

    # for each word in email, if it matches classified word, censor word and append to new text array.  
    for word in email_word_list:
        if word.lower() in classified_words_dict:
            classified_flag = True
            censored_word = censor(word)
            censored_text.append(censored_word)
        else:
            censored_text.append(word)
           
    # join new censored text array together to result in original text with any classified words censored
    censored_text = ''.join(censored_text)

    # Boolean, String
    return classified_flag, censored_text

