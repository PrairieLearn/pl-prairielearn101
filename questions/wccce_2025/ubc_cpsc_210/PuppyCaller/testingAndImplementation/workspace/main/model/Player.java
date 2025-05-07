package model;

// represents the player in the game
public class Player {
    public static final int HITBOX_RANGE = 5;

    private final int posX;
    private final int posY;

    // EFFECTS: creates a player in the middle left of the screen
    public Player(int maxX, int maxY) {
        this.posX = HITBOX_RANGE;
        this.posY = maxY / 2;
    }

    public int getX() {
        return posX;
    }

    public int getY() {
        return posY;
    }
}
