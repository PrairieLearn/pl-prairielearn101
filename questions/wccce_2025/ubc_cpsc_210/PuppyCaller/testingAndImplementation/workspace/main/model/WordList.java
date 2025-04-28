package model;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

// represents a list of words that can be used to generate sets
public class WordList {
    private List<String> sortedWords;
    private Random random = new Random();

    // EFFECTS: Reads file at path and uses each line as a word for the list
    //          sorted by word length
    public WordList(Path wordFilePath) throws IOException {
        List<String> words = Files.readAllLines(wordFilePath);
        Collections.shuffle(words);
        words.sort(Comparator.comparingInt(String::length));
        sortedWords = words;
    }

    // REQUIRES: provided word count / maxDifficulty > 10 * count
    //           (in other words, there are sufficiently many words to choose from to create the set)
    // EFFECTS: creates a subset of count words from the total set by:
    //          by dividing the total set into fractions (maxDifficulty fractions)
    //          and using the difficulty'th subset as the word list to draw from
    //          then, picks count random words from the set.
    public Set<String> generateWordSet(int count, int difficulty, int maxDifficulty) {
        Set<String> generatedWords = new HashSet<>();
        int wordMaxIndex = (sortedWords.size() - 1) / maxDifficulty;
        int minIndex = difficulty == 0 ? 0 : wordMaxIndex * (difficulty - 1);

        // there should be more safeguards here against an infinite recursion, but whatever for now...
        while (generatedWords.size() < count) {
            int randomIndex = random.nextInt(wordMaxIndex);
            String word = sortedWords.get(minIndex + randomIndex);

            generatedWords.add(word);
        }

        return generatedWords;
    }
}
