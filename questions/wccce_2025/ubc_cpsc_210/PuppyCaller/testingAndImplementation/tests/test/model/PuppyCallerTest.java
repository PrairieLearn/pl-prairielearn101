package model;

import ca.ubc.cs.autotest.AutoTest;
import ca.ubc.cs.autotest.Grader;
import ca.ubc.cs.autotest.Hint;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@AutoTest
public class PuppyCallerTest {
    private PuppyCaller puppyCaller;
    private List<Puppy> puppyList;

    @BeforeEach
    public void beforeEach() {
        puppyCaller = new PuppyCaller();
        puppyList = new ArrayList<>();

        // use numbers as the word for no conflicts
        puppyList.add(new Puppy("123"));
        puppyList.add(new Puppy("421"));
        puppyList.add(new Puppy("246"));
        // next character for longWordProgress is m

    }

    @Hint("PuppyCaller: a test for the constructor")
    @Grader
    @Test
    public void constructorTest() {
        assertNull(puppyCaller.getCurrentPuppy());
    }

    @Hint("PuppyCaller: a test for findPuppy with a single puppy with a puppy matched")
    @Grader()
    @ParameterizedTest()
    @CsvSource(value = {
            // single character, no progress
            "a,0,a",
            // long word, no progress
            "feature,0,f",
            // long word, progress
            "computer,2,m",
            // long word, just at end
            "testing,6,g"
    })
    public void findPuppySingleSuccess(String word, int progress, char input) {
        Puppy puppy = createPuppy(word, progress);
        Puppy foundPuppy = puppyCaller.findPuppy(Collections.singletonList(puppy), input);

        assertEquals(puppy, foundPuppy);
    }

    private static Puppy createPuppy(String word, int progress) {
        Puppy puppy = new Puppy(word);

        for (int i = 0; i < progress; i++) {
            puppy.typeName();
        }
        return puppy;
    }

    @Hint("PuppyCaller: a test for findPuppy with a single puppy with no puppy matched")
    @Grader()
    @ParameterizedTest
    @CsvSource(value = {
            // single character, no progress
            "a,0,b",
            // long word, no progress
            "feature,0,e",
            // long word, progress
            "computer,2,p",
            // long word, just at end
            "testing,6,n"
    })
    public void findPuppySingleFail(String word, int progress, char input) {
        Puppy puppy = createPuppy(word, progress);
        Puppy foundPuppy = puppyCaller.findPuppy(Collections.singletonList(puppy), input);

        assertNull(foundPuppy);
    }

    @Hint("PuppyCaller: a test for findPuppy with multiple puppies with a puppy matched")
    @Grader()
    @ParameterizedTest()
    @CsvSource(value = {
            // single character, no progress
            "a,0,a",
            // long word, no progress
            "feature,0,f",
            // long word, progress
            "computer,2,m",
            // long word, just at end
            "testing,6,g"
    })
    public void findPuppyMultipleSuccess(String word, int progress, char input) {
        Puppy puppy = createPuppy(word, progress);

        puppyList.add(puppy);
        Collections.shuffle(puppyList);

        Puppy foundPuppy = puppyCaller.findPuppy(puppyList, input);

        assertEquals(puppy, foundPuppy);
    }

    @Hint("PuppyCaller: a test for findPuppy with multiple puppies with no puppies matched")
    @Grader()
    @ParameterizedTest()
    @CsvSource(value = {
            // single character, no progress
            "a,0,b",
            // long word, no progress
            "feature,0,e",
            // long word, progress
            "computer,2,p",
            // long word, just at end
            "testing,6,n"
    })
    public void findPuppyMultipleFail(String word, int progress, char input) {
        puppyList.add(createPuppy(word, progress));
        Collections.shuffle(puppyList);

        Puppy foundPuppy = puppyCaller.findPuppy(puppyList, input);

        assertNull(foundPuppy);
    }

    @Hint("PuppyCaller: a test for typeNameForCurrentPuppy with the correct input")
    @Grader()
    @ParameterizedTest()
    @CsvSource(value = {
            // long word, no progress
            "feature,0,f",
            // long word, progress
            "computer,2,m"
    })
    public void callAtCurrentPuppy(String word, int progress, char input) {
        Puppy puppy = createPuppy(word, progress);

        puppyCaller.setCurrentPuppy(puppy);

        assertTrue(puppyCaller.typeNameForCurrentPuppy(input));
        // ensure the puppy was called
        assertEquals(word.charAt(progress + 1), puppy.getNextChar());
        // ensure the puppy has not changed
        assertEquals(puppy, puppyCaller.getCurrentPuppy());
    }

    @Hint("PuppyCaller: a test for typeNameForCurrentPuppy completing the name")
    @Grader()
    @ParameterizedTest()
    @CsvSource(value = {
            // single character, no progress
            "a,0,a",
            // long word, just at end
            "testing,6,g"
    })
    public void typeNameComplete(String word, int progress, char input) {
        Puppy puppy = createPuppy(word, progress);

        puppyCaller.setCurrentPuppy(puppy);

        assertTrue(puppyCaller.typeNameForCurrentPuppy(input));
        assertTrue(puppy.hasBeenCalled());
        assertNull(puppyCaller.getCurrentPuppy());
    }

    @Hint("PuppyCaller: a test for typeNameForCurrentPuppy with an incorrect input")
    @Grader()
    @ParameterizedTest()
    @CsvSource(value = {
            // single character, no progress
            "a,0,b",
            // long word, no progress
            "feature,0,e",
            // long word, progress
            "computer,2,p",
            // long word, just at end
            "testing,6,n"
    })
    public void typeNameForCurrentPuppyMiss(String word, int progress, char input) {
        Puppy puppy = createPuppy(word, progress);
        char nextChar = puppy.getNextChar();

        puppyCaller.setCurrentPuppy(puppy);

        assertFalse(puppyCaller.typeNameForCurrentPuppy(input));
        assertFalse(puppy.hasBeenCalled());
        assertEquals(nextChar, puppy.getNextChar());
        assertEquals(puppy, puppyCaller.getCurrentPuppy());
    }

    @Hint("PuppyCaller: a test for handleInput with a current puppy selected")
    @Grader()
    @ParameterizedTest()
    @CsvSource(value = {
            // single character, no progress
            "a,0,true",
            // long word, no progress
            "feature,0,false",
            // long word, progress
            "computer,2,false",
            // long word, just at end
            "testing,6,true"
    })
    public void handleInputCurrentPuppyCall(String word, int progress, boolean called) {
        Puppy puppy = createPuppy(word, progress);
        char nextChar = puppy.getNextChar();

        puppyList.add(puppy);
        Collections.shuffle(puppyList);
        puppyCaller.setCurrentPuppy(puppy);

        boolean result = puppyCaller.handleInput(puppyList, nextChar);
        Puppy expectedTarget = called ? null : puppy;

        assertTrue(result);
        assertEquals(expectedTarget, puppyCaller.getCurrentPuppy());
        assertEquals(called, puppy.hasBeenCalled());

        if (!called) {
            assertEquals(word.charAt(progress + 1), puppy.getNextChar());
        }
    }

    @Hint("PuppyCaller: a test for handleInput with a current puppy selected")
    @Grader()
    @ParameterizedTest()
    @CsvSource(value = {
            // single character, no progress
            "a,0,b",
            // long word, no progress
            "feature,0,e",
            // long word, progress
            "computer,2,u",
            // long word, just at end
            "testing,6,n"
    })
    public void handleInputCurrentPuppyMiss(String word, int progress, char input) {
        Puppy puppy = createPuppy(word, progress);

        puppyList.add(puppy);
        Collections.shuffle(puppyList);
        puppyCaller.setCurrentPuppy(puppy);

        boolean result = puppyCaller.handleInput(puppyList, input);

        assertFalse(result);
        assertEquals(puppy, puppyCaller.getCurrentPuppy());
    }

    @Hint("PuppyCaller: a test for handleInput with no current puppy before and the input matches a puppy whose name is a single character")
    @Grader()
    @ParameterizedTest()
    @ValueSource(strings = {
            "a",
            "@"
    })
    public void handleInputNoCurrentCallSingle(String word) {
        handleInputNoCurrent(word, true);
    }

    @Hint("PuppyCaller: a test for handleInput with no current puppy before and the input matches a puppy")
    @Grader()
    @ParameterizedTest()
    @ValueSource(strings = {
            "feature",
            "computer",
    })
    public void handleInputNoCurrentCall(String word) {
        handleInputNoCurrent(word, true);
    }

    @Hint("PuppyCaller: a test for handleInput with no current puppy before and no matched puppy")
    @Grader()
    @ParameterizedTest()
    @ValueSource(strings = {
            "a",
            "feature",
            "computer",
    })
    public void handleInputNoCurrentMiss(String word) {
        handleInputNoCurrent(word, false);
    }

    private void handleInputNoCurrent(String word, boolean match) {
        Puppy puppy = createPuppy(word, 0);

        puppyList.add(puppy);
        Collections.shuffle(puppyList);

        char input = match ? puppy.getNextChar() : '9';
        boolean result = puppyCaller.handleInput(puppyList, input);
        boolean matchAndNotCalled = match && !puppy.hasBeenCalled();
        Puppy expectedTarget = matchAndNotCalled ? puppy : null;

        assertEquals(match, result);
        assertEquals(expectedTarget, puppyCaller.getCurrentPuppy());

        if (matchAndNotCalled) {
            assertEquals(word.charAt(1), puppy.getNextChar());
        }
    }
}
