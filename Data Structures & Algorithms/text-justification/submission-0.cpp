class Solution {
public:
    /*
    approach 1
    for each line
        - start at the current word
        - keep adding words while the line can fit them
        - once adding the next word would exceed the maxWidhgt, stop
        - justify the selected words
        - repeat for the next line
    time complexity:
        - n = # of words
        - L = total number of characters in all output lines
        - O(L) -> since each otuput line has maxWidth characters, and there are at most n
    space complexity:
        - O(L) -> total space complexity
        - O(maxWidth) -> auxiliary space (extra/temporary space used on execution)
    */
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> justifiedLines;
        int numberOfWords = static_cast<int>(words.size());
        int lineStartIndex = 0;

        while (lineStartIndex < numberOfWords){
            int lineEndIndex = lineStartIndex;
            int totalWordCharacters = 0;

            while (lineEndIndex < numberOfWords){
                int candidateWordLength = static_cast<int>(words[lineEndIndex].length());
                int minimumSpacesNeeded = lineEndIndex - lineStartIndex;

                if(totalWordCharacters + candidateWordLength + minimumSpacesNeeded > maxWidth){
                    break;
                }

                totalWordCharacters += candidateWordLength;
                ++lineEndIndex;
                
            }
            int numberOfWordsInLine = lineEndIndex - lineStartIndex;
            int numberOfGaps = numberOfWordsInLine - 1;
            int totalSpacesNeeded = maxWidth - totalWordCharacters;

            string currentLine;

            bool isLastLine = lineEndIndex == numberOfWords;

            if (isLastLine || numberOfGaps == 0){
                for(int wordIndex = lineStartIndex; wordIndex < lineEndIndex; ++wordIndex){
                    currentLine += words[wordIndex];
                    if (wordIndex + 1 < lineEndIndex){
                        currentLine += ' ';
                    }
                }
                int remainingSpaces = maxWidth - static_cast<int>(currentLine.size());

                currentLine += string(remainingSpaces, ' ');
            } else {
                int spacesPerGap = totalSpacesNeeded / numberOfGaps;
                int extraSpaces = totalSpacesNeeded % numberOfGaps;

                for(int wordIndex = lineStartIndex; wordIndex < lineEndIndex; ++wordIndex){
                    currentLine += words[wordIndex];

                    if (wordIndex + 1 < lineEndIndex){
                        int currentGapIndex = wordIndex - lineStartIndex;
                        int spacesToInsert = spacesPerGap;

                        if (currentGapIndex < extraSpaces){
                            ++spacesToInsert;
                        }

                        currentLine += string(spacesToInsert, ' ');
                    }
                }
            }
            justifiedLines.push_back(currentLine);

            lineStartIndex = lineEndIndex;
        }
        return justifiedLines;
    }
};