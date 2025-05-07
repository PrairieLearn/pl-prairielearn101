package model;

// represents a game level
public enum GameLevel {
    R1_1(3, 15),
    R1_2(3, 20),
    R1_3(3, 25),
    R2_1(6, 15),
    R2_2(6, 20),
    R2_3(6, 25),
    R3_1(8, 15),
    R3_2(8, 20),
    R3_3(8, 25),
    R4_1(10, 15),
    R4_2(10, 20),
    R4_3(10, 25),
    R5_1(12, 20),
    R5_2(12, 25),
    R6_1(14, 20),
    R6_2(14, 25);

    private final int puppyCount;
    private final int speed;

    // EFFECTS: creates a game level with a given amount of puppies and speed
    GameLevel(int puppyCount, int speed) {
        this.puppyCount = puppyCount;
        this.speed = speed;
    }

    public int getPuppyCount() {
        return puppyCount;
    }

    public int getSpeed() {
        return speed;
    }
}
