package model;

// Represents a puppy in the game with a name
// Puppies are 'called' when the entire name has been typed
// Puppies' names are typed character by character using the typeName method.
public class Puppy {
    public static final int PUPPY_TOTAL_SIZE_PX = 10;
    private static final int MAX_SPEED = 30;

    private int posX;
    private int posY;
    private int nextToTypeIndex;

    private final String name;
    private final int speed;
    private int moveCounter = 0;

    // EFFECTS: instantiates a puppy at a starting x,y position
    //          with a given name and no current progression
    public Puppy(int x, int y, int speed, String name) {
        this.posX = x;
        this.posY = y;
        this.name = name;
        this.speed = speed;
        this.nextToTypeIndex = 0;
    }

    // EFFECTS: creates a puppy with no position with a given name for test purposes
    Puppy(String name) {
        this.name = name;
        this.speed = 0;
    }

    // REQUIRES: !hasBeenCalled()
    // EFFECTS: returns the next character to be typed by the player for this puppy
    public char getNextChar() {
        return name.charAt(nextToTypeIndex);
    }

    // EFFECTS: returns whether the puppy has been called
    public boolean hasBeenCalled() {
        return nextToTypeIndex >= name.length();
    }

    // EFFECTS: 'types' the next character in the word, getting closer to calling the puppy
    public void typeName() {
        nextToTypeIndex++;
    }

    // EFFECTS: resets this puppy's progress to 0 and players have to type the puppy's name
    public void resetProgress() {
        nextToTypeIndex = 0;
    }

    public void moveTowardsFence() {
        moveCounter++;

        if (moveCounter != (MAX_SPEED - speed)) {
            return;
        }

        moveCounter = 0;
        this.posX++;
    }

    public boolean isStriding() {
        return this.moveCounter >= (MAX_SPEED - speed) / 2;
    }

    public int getX() {
        return posX;
    }

    public int getY() {
        return posY;
    }

    public String getName() {
        return this.name;
    }

    public String getTypedPortion() {
        return this.name.substring(0, nextToTypeIndex);
    }

    public String getUntypedPortion() {
        return this.name.substring(nextToTypeIndex);
    }
}
