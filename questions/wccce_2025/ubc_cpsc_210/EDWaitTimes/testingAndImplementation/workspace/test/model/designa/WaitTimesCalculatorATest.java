package model.designa;

import model.HourFormatter;
import model.WaitTimeRecord;
import model.ex.NoSuchGroupException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

public class WaitTimesCalculatorATest {
    private WaitTimesCalculatorA dayOfWeekCalculator;

    @BeforeEach
    public void beforeEach() {
        dayOfWeekCalculator = new WaitTimesCalculatorA(WaitTimesGrouping.DAY_OF_WEEK);
    }

    @Test
    public void testWaitTimeGroupingSunday() {
        testWaitTimeGroupingDay(1, "Sunday");
    }

    @Test
    public void testWaitTimeGroupingMonday() {
        testWaitTimeGroupingDay(2, "Monday");
    }

    @Test
    public void testWaitTimeGroupingTuesday() {
        testWaitTimeGroupingDay(3, "Tuesday");
    }

    @Test
    public void testWaitTimeGroupingWednesday() {
        testWaitTimeGroupingDay(4, "Wednesday");
    }

    @Test
    public void testWaitTimeGroupingThursday() {
        testWaitTimeGroupingDay(5, "Thursday");
    }

    @Test
    public void testWaitTimeGroupingFriday() {
        testWaitTimeGroupingDay(6, "Friday");
    }

    @Test
    public void testWaitTimeGroupingSaturday() {
        testWaitTimeGroupingDay(7, "Saturday");
    }

    private void testWaitTimeGroupingDay(int day, String expectedGroup) {
        WaitTimesCalculatorA calculator = dayOfWeekCalculator;
        WaitTimeRecord testRecord = new WaitTimeRecord("TestHospital", createDateWithDay(day), 123);

        // check the expected group is correct
        assertEquals(expectedGroup, calculator.getGroup(testRecord));

        calculator.addWaitTime(testRecord);

        // check it was added correctly
        List<Integer> waitTimes = calculator.getWaitTimesFor(expectedGroup);

        assertEquals(1, waitTimes.size());
        assertEquals(testRecord.getWaitTimeMinutes(), waitTimes.get(0));
    }

    @Test
    public void testAddMultipleGroups() {
        WaitTimesCalculatorA calculator = dayOfWeekCalculator;
        WaitTimeRecord firstRecord = new WaitTimeRecord("TestHospital", createDateWithDay(1), 1);
        WaitTimeRecord secondRecord = new WaitTimeRecord("TestHospital", createDateWithDay(2), 2);
        String firstGroup = calculator.getGroup(firstRecord);
        String secondGroup = calculator.getGroup(secondRecord);

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
        WaitTimesCalculatorA calculator = dayOfWeekCalculator;

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
        WaitTimesCalculatorA calculator = dayOfWeekCalculator;

        calculator.addWaitTime(new WaitTimeRecord("TestHospital", createDateWithDay(1), 4));
        calculator.addWaitTime(new WaitTimeRecord("TestHospital", createDateWithDay(1), 12));

        try {
            assertEquals(8, calculator.getAverageWaitTime("Sunday"));
        } catch (NoSuchGroupException ex) {
            fail("NoSuchGroupException thrown when data is available for group", ex);
        }
    }

    @Test
    public void testRequiredGroupsDayOfWeek() {
        List<String> requiredGroupsForDow = Arrays.asList(
                "Sunday",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday"
        );

        assertEquals(requiredGroupsForDow, dayOfWeekCalculator.getRequiredGroups());
    }

    @Test
    public void testGroupingLabelDayOfWeek() {
        WaitTimesCalculatorA calculator = dayOfWeekCalculator;

        assertEquals("Day of the week", calculator.getGroupingLabel());
    }

    // EFFECTS: creates a date with the provided day of the week
    private Date createDateWithDay(int dayOfWeek) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.DAY_OF_WEEK, dayOfWeek);
        return calendar.getTime();
    }

    // EFFECTS: creates a date with the provided hour of the day
    private Date createDateWithHourOfDay(int hourOfDay) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.HOUR_OF_DAY, hourOfDay);
        return calendar.getTime();
    }
}
