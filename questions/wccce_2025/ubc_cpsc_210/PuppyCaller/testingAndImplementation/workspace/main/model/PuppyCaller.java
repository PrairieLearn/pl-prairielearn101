package model;

import java.util.List;

/**
 * Handles input from the player and calls puppies based on their input.
 * For your convenience, the description of the problem has been provided below.
 *
 * <br> <br>
 * In the game, each puppy has a name and are running away from their owner.
 * In order to stop the puppies from running away, the owner has to 'call' them by typing their name.
 * <br> <br>
 * The game runs under the following sequence: <br>
 * 1. The player starts calling a puppy by typing the first letter of its name. This 'selects' the puppy. <br>
 * 2. The player must type the rest of its name to call it. Any incorrect input (e.g. typing 'a' when the next letter is
 *    'c' is ignored) <br>
 * 3. Once the player has typed the last character, the puppy is now 'called' and will stop running away. This also
 *      unselects the puppy, returning back to step 1.
 * <br> <br>
 * This logic has been broken down into a few methods in this class: <br>
 * - Getting and setting the current selected puppy (useful for tests!) <br>
 * - Typing the name for the current puppy - corresponding to step 2 and 3 above. <br>
 * - Finding a puppy whose next character starts with an input character c - helpful for step 1. <br>
 * <br> <br>
 * These pieces are finally put together in the handleInput method, where you can use your work earlier
 * to handle the full logic of the game! As you write this method, think about where and how the other
 * helper methods might be useful.
 */
public class PuppyCaller {

    // EFFECTS: creates an instance of this class with no current puppy selected.
    public PuppyCaller() {
    }

    // EFFECTS: returns the current selected puppy, null if none is selected
    public Puppy getCurrentPuppy() {
        return null;
    }

    // REQUIRES: !currentPuppy.hasBeenCalled()
    // MODIFIES: this
    // EFFECTS: sets the current puppy to the provided puppy
    public void setCurrentPuppy(Puppy currentPuppy) {
    }

    // REQUIRES: getCurrentPuppy() != null and !getCurrentPuppy().hasBeenCalled()
    // MODIFIES: this
    // EFFECTS: Types one character of the current puppy's name if c is the next character to be typed for that puppy
    //          If the puppy has been called after typing that character, current puppy will be null
    //          Returns whether progress was made on calling the puppy
    public boolean typeNameForCurrentPuppy(char c) {
        return true;
    }

    // REQUIRES: currentPuppies.size() > 0 AND for all puppies in the list, puppy has not been called
    // EFFECTS: returns any puppy in the list whose next character is c
    //          returns null if none was found
    public Puppy findPuppy(List<Puppy> currentPuppies, char c) {
        return currentPuppies.get(0);
    }

    // REQUIRES: currentPuppies.size() > 0 AND for all puppies in the list, puppy has not been called
    // MODIFIES: this
    // EFFECTS: Handles the given input for the player, where:
    //          If there is a current puppy selected:
    //              type its name according to typeNameForCurrentPuppy
    //              return whether progress was made on calling the puppy
    //          If there is no current puppy:
    //              Find the puppy who matches the input character c
    //              Set this puppy as the current and if one was found, 
    //              type its name according to typeNameForCurrentPuppy
    //              Return whether progress was made on calling the puppy
    public boolean handleInput(List<Puppy> currentPuppies, char c) {
        return false;
    }
}
