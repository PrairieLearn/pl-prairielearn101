package model;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

// class to represent the workings of the whole 'game'
public class Game {
    public static final int TICKS_PER_SECOND = 40;

    private final Player player;
    private int levelIndex;
    private final List<Puppy> puppies = new ArrayList<>();
    private boolean endedGame = false;
    private boolean endedLevel = false;

    private final int maxY;
    private final int maxX;
    private final WordList wordList;

    // EFFECTS: creates a new instance of the game with a set width, size
    //          and potential word list. Starts game with the initial level,
    //          and the first set of puppies
    public Game(int maxX, int maxY, WordList wordList) {
        this.maxX = maxX;
        this.maxY = maxY;
        this.wordList = wordList;
        this.levelIndex = -1;
        this.player = new Player(maxX, maxY);

        advanceLevel();
    }

    // REQUIRES: endedLevel = true
    // MODIFIES: this
    // EFFECTS: clears the current puppies and advances to the next level
    //          if the current level was the last, ends the game
    //          otherwise, adds the next round of puppies
    public void advanceLevel() {
        puppies.clear();
        endedLevel = false;
        levelIndex++;

        if (levelIndex == GameLevel.values().length) {
            endedGame = true;
            return;
        }

        createPuppies();
    }

    // MODIFIES: this
    // EFFECTS: Adds puppies column-wise to the game
    //          Creates however many puppies corresponds to the current game level
    //          Generates names for puppies using the wordlist
    //          Attempts to center puppies that are in the last line
    private void createPuppies() {
        GameLevel currentLevel = GameLevel.values()[levelIndex];
        int difficulty = levelIndex + 1;
        List<String> puppyNames = new ArrayList<>(wordList.generateWordSet(
                currentLevel.getPuppyCount(),
                difficulty,
                GameLevel.values().length
        ));

        int minY = 10;
        int puppiesPerLine = Math.max(1, (maxY / Puppy.PUPPY_TOTAL_SIZE_PX) - 1);
        int lastLine = puppyNames.size() / puppiesPerLine;
        int wordBreakpoint = lastLine * puppiesPerLine;

        for (int i = 0; i < wordBreakpoint; i++) {
            int column = i % puppiesPerLine;
            int row = i / puppiesPerLine;

            createPuppy(minY + column * Puppy.PUPPY_TOTAL_SIZE_PX, row, currentLevel.getSpeed(), puppyNames.get(i));
        }

        createLastLinePuppies(puppyNames, wordBreakpoint, puppiesPerLine, minY, lastLine, currentLevel);
    }

    // MODIFIES: this
    // EFFECTS: places puppies on that are on the last 'line'/column
    //          evenly spacing them where possible
    private void createLastLinePuppies(List<String> puppyNames, int wordBreakpoint,
                                       int puppiesPerLine, int minY, int lastLine, GameLevel currentLevel) {
        int puppiesInLastLine = puppyNames.size() - wordBreakpoint;

        if (puppiesInLastLine == 0) {
            return;
        }

        int lastLineIncrements = (maxY - 10) / (puppiesInLastLine + 1);

        lastLineIncrements = Math.max(lastLineIncrements, 7);

        for (int i = wordBreakpoint; i < puppyNames.size(); i++) {
            int column = (i % puppiesPerLine) + 1;

            createPuppy(minY + column * lastLineIncrements, lastLine, currentLevel.getSpeed(), puppyNames.get(i));
        }
    }

    // MODIFIES: this
    // EFFECTS: adds a puppy with a given name, y position, and column
    //          where column representing how many 'puppies' are horizontally
    //          away the puppy is from the player
    private void createPuppy(int y, int column, int speed, String word) {
        int x = player.getX() + (column + 1) * Puppy.PUPPY_TOTAL_SIZE_PX;

        puppies.add(new Puppy(x, y, speed, word));
    }

    // MODIFIES: this
    // EFFECTS: Progresses the game in a given tick
    //          If any of the puppies have escaped, end the game (failed)
    //          If there are no puppies left to call, end the level
    //          Otherwise, move remaining puppies towards the fence
    public void tick() {
        if (hasAnyPuppiesEscaped()) {
            endedGame = true;
            return;
        }

        if (getPuppiesToCall().isEmpty()) {
            endedLevel = true;
        }

        this.movePuppies();
    }

    public int getMaxY() {
        return maxY;
    }

    public int getMaxX() {
        return maxX;
    }

    public int getLevelIndex() {
        return levelIndex;
    }

    public List<Puppy> getPuppies() {
        return puppies;
    }

    public List<Puppy> getPuppiesToCall() {
        return puppies.stream().filter(p -> !p.hasBeenCalled()).collect(Collectors.toList());
    }

    public Player getPlayer() {
        return player;
    }

    public boolean isEndedGame() {
        return endedGame;
    }

    public boolean isEndedLevel() {
        return endedLevel;
    }

    private boolean hasAnyPuppiesEscaped() {
        return puppies.stream().anyMatch(this::hasEscaped);
    }

    private boolean hasEscaped(Puppy puppy) {
        return puppy.getX() >= maxX;
    }

    public void movePuppies() {
        getPuppiesToCall().forEach(Puppy::moveTowardsFence);
    }
}
