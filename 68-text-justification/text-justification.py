class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0
        
        # Loop through all words to process them into lines
        for word in words:
            # Check if adding the next word would exceed the maxWidth
            if current_length + len(word) + len(current_line) > maxWidth:
                # Distribute spaces evenly between words in the current line
                spaces = maxWidth - current_length
                if len(current_line) == 1:
                    # If there's only one word, all spaces go at the end
                    result.append(current_line[0] + ' ' * spaces)
                else:
                    # Distribute spaces evenly between words
                    space_between_words = spaces // (len(current_line) - 1)
                    extra_spaces = spaces % (len(current_line) - 1)
                    line = current_line[0]
                    
                    for i in range(1, len(current_line)):
                        # Add the normal spaces first
                        line += ' ' * (space_between_words)
                        if extra_spaces > 0:
                            line += ' '  # Distribute extra space to the leftmost gap
                            extra_spaces -= 1
                        line += current_line[i]
                    
                    result.append(line)
                
                # Reset current line for the next set of words
                current_line = [word]
                current_length = len(word)
            else:
                # Add the current word to the line
                current_line.append(word)
                current_length += len(word)
        
        # Handle the last line: left-justified and add spaces at the end
        last_line = ' '.join(current_line)
        result.append(last_line + ' ' * (maxWidth - len(last_line)))
        
        return result


        