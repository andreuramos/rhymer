# Rhymer

This is a project to find words that rhyme with others, the expected API is to enter a word in a CLI and the result to be a list of words that rhyme*.

\* By rhyme is understood as the last syllabs are pronounced equal (consonant) or at least the vowels in them are pronounced equal (assonant)

## Approach

1) Generate a dataset: maybe from multiple sources, we need to build a database of words including nouns, adjectives, verbs along with conjugations, declinations, diminutives and other word modifications
2) A way to query this dataset: maybe a cli is enough. A word is entered, if found on the database, it returns a list of phonetically matching words. The result might be filtered by word type (noun, adjective etc) and verbal tense, etc