package model.designb;

import model.WaitTimeRecord;
import model.ex.NoSuchGroupException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

public class WaitTimesCalculatorBTest {
    private WaitTimesCalculatorB calculator;

    @BeforeEach
    public void beforeEach() {
        /*
         * Treat an example grouping that places records into two groups for testing the calculator.
         *
         * In the future, you'll learn about mocks are regularly used in large software projects to
         * accomplish this very thing! We don't have to rely on any specific mechanism, we can use a
         * "fake"/mocked one that does something very simple.
         */
        GroupingMechanism exampleMechanism = new GroupingMechanism() {
            // puts in group "Test" if the hospital name starts with "Test", otherwise "Not test"
            @Override
            public String getGroupFor(WaitTimeRecord record) {
                if (record.getHospital().startsWith("Test")) {
                    return "Test";
                } else {
                    return "Not test";
                }
            }

            // not relevant for test, unused
            @Override
            public String getGroupingLabel() {
                return null;
            }

            // not relevant for test, unused
            @Override
            public List<String> getRequiredGroups() {
                return null;
            }
        };
        calculator = new WaitTimesCalculatorB(exampleMechanism);
    }

    // EFFECTS: creates a record whose group will be "Test"
    private WaitTimeRecord createRecordInTestGroup(int waitTime) {
        return new WaitTimeRecord("TestHospital", new Date(), waitTime);
    }

    // EFFECTS: creates a record whose group will be "Not test"
    private WaitTimeRecord createRecordNotInTestGroup(int waitTime) {
        return new WaitTimeRecord("NotInTest", new Date(), waitTime);
    }

    @Test
    public void testAddWaitTimeGrouping() {
        WaitTimeRecord testRecord = createRecordInTestGroup(12);

        calculator.addWaitTime(testRecord);

        // check it was added correctly
        List<Integer> waitTimes = calculator.getWaitTimesFor("Test");

        assertEquals(1, waitTimes.size());
        assertEquals(testRecord.getWaitTimeMinutes(), waitTimes.get(0));
    }

    @Test
    public void testAddWaitMultipleGroups() {
        WaitTimeRecord firstRecord = createRecordInTestGroup(1);
        WaitTimeRecord secondRecord = createRecordNotInTestGroup(2);
        String firstGroup = "Test";
        String secondGroup = "Not test";

        calculator.addWaitTime(firstRecord);
        calculator.addWaitTime(secondRecord);

        // check the first record went into its group
        List<Integer> firstWaitTimes = calculator.getWaitTimesFor(firstGroup);

        assertEquals(1, firstWaitTimes.size());
        assertEquals(firstRecord.getWaitTimeMinutes(), firstWaitTimes.get(0));

        // check the second record went into its group
        List<Integer> secondWaitTimes = calculator.getWaitTimesFor(secondGroup);

        assertEquals(1, secondWaitTimes.size());
        assertEquals(secondRecord.getWaitTimeMinutes(), secondWaitTimes.get(0));

        // make sure the map is built correctly
        Map<String, List<Integer>> waitTimesMap = calculator.getGroupWaitTimes();

        assertEquals(2, waitTimesMap.size());
        assertEquals(firstWaitTimes, waitTimesMap.get(firstGroup));
        assertEquals(secondWaitTimes, waitTimesMap.get(secondGroup));
    }

    @Test
    public void testGetAverageNoGroup() {
        // add some data just to make sure the average is not checking for ANY data
        calculator.addWaitTime(new WaitTimeRecord("TestHospital", new Date(), 1));

        try {
            calculator.getAverageWaitTime("ImpossibleGroup");
            fail("Expected getAverageWaitTime for a group with no values to throw exception");
        } catch (NoSuchGroupException ex) {
            // pass
        }
    }

    @Test
    public void testGetAverageWithGroup() {
        calculator.addWaitTime(createRecordInTestGroup(4));
        calculator.addWaitTime(createRecordInTestGroup(12));

        try {
            // 4 + 12 = 16 / 2 = 8
            assertEquals(8, calculator.getAverageWaitTime("Test"));
        } catch (NoSuchGroupException ex) {
            fail("NoSuchGroupException thrown when data is available for group", ex);
        }
    }
}
