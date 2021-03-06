## Command Line word searcher
Loads file contents on a given directory, and returns, given a set of input words, their presence ratio on each file 

## How to run it
1. Clone this repo.
2. cd to main folder.
3. Activate virtual environment (pipenv shell). If pipenv is not installed, run pip install pipenv
4. Sync to the venv - pipenv sync.
5. run python main.py

## Considerations
1. Any type of alphanumerical character, of any lenght, will be considered a word (yes, including numbers, so thing like years can be searched). Weird characters such as signs or symbols are removed.
2. Two words are equal if they are exact matches, but case (lower/upper) is not taken into account.
3. Data structure design: we read each file on the directory and save it into a dictionary, where the key is the file name and the value is the content. This works given there's a unique datastructure that, given a file name as the value, will automatically parse it (FileDict). This might be intensive on memory, but allows to parse the directory files just one time, and make multiple searches. We could just parse the files as we go, improving memory efficiency, but we'd lose on time if we want to search again on the same directory.
4. Ranking formula: Very simple for now, just a ratio between the amount of words that appear in the file and the total words. Some ideas for the future: consider repeated words as different instances and don't cut the loop short if a word matches, so more of the same word on the file would result in a higher score.
5. Simple unit testing of all modules is included in src/test/.
