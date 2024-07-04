class RabinKarp:

    def __init__(self):
        pass

    

    def search(self, pattern, text):
        # TODO
        if (pattern == None or len(pattern) == 0) or (text == None or len(text) == 0):
            raise ValueError("Pattern or Text must contain characters")
        
        #print(len(text), text, ord(' '))

        interval = len(pattern)
        pattern_hash = self.get_rolling_hash_value(pattern, None, None)
        last_character = None
        previous_hash = None
        
        occurence_list = []
        #print(len(text)-len(pattern)+1)
        for starting_index in range(len(text)-len(pattern)+1):

            text_hash = self.get_rolling_hash_value(text[starting_index:starting_index+interval], last_character, previous_hash)

            if text_hash == pattern_hash:
                occurence_list.append(starting_index)
                previous_hash = text_hash
                last_character = text[starting_index]
            else: 
                previous_hash = text_hash
                last_character = text[starting_index]
        
        if len(occurence_list) == 0:
            return None
        return occurence_list

    """
        This method uses the RabinKarp algorithm to search a given pattern in a given input text.
        @ param pattern - The string pattern that is searched in the text.
        @ param text - The text string in which the pattern is searched.
        @ return a list with the starting indices of pattern occurrences in the text, or None if not found.
        @ raises ValueError if pattern or text is None or empty.
    """


    @staticmethod
    def get_rolling_hash_value(sequence, last_character, previous_hash):
        # TODO
        if previous_hash == None or previous_hash == 0:
            rolling_hash = 0
            for i in range(len(sequence)):
                rolling_hash += (ord(sequence[i])*(29**(len(sequence)-(i+1))))
            return rolling_hash
        
        rolling_hash = (previous_hash*29)-(ord(last_character)*(29**(len(sequence))))+(ord(sequence[-1]))
        return rolling_hash
        

    """
         This method calculates the (rolling) hash code for a given character sequence. For the calculation use the 
         base b=29.
         @ param sequence - The char sequence for which the (rolling) hash shall be computed.
         @ param last_character - The character to be removed from the hash when a new character is added.
         @ param previous_hash - The most recent hash value to be reused in the new hash value.
         @ return hash value for the given character sequence using base 29.
    """