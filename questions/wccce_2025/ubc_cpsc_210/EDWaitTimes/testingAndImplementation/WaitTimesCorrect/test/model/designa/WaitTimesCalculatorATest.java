package model.designa;

import model.WaitTimeRecord;
import model.ex.NoSuchGroupException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

public class WaitTimesCalculatorATest {
    private WaitTimesCalculatorA dayOfWeekCalculator;
    private WaitTimesCalculatorA hourOfDayCalculator;

    @BeforeEach
    public void beforeEach() {
        dayOfWeekCalculator = new WaitTimesCalculatorA(WaitTimesGrouping.DAY_OF_WEEK);
        hourOfDayCalculator = new WaitTimesCalculatorA(WaitTimesGrouping.HOUR_OF_DAY);
    }

    @Test
    public void testRequiredGroupsHourOfDay() {
        List<String> expectedGroups = Arrays.asList(
                "12AM", "1AM", "2AM", "3AM", "4AM", "5AM",
                "6AM", "7AM", "8AM", "9AM", "10AM", "11AM",
                "12PM", "1PM", "2PM", "3PM", "4PM", "5PM",
                "6PM", "7PM", "8PM", "9PM", "10PM", "11PM"
        );
        Collection<String> actualGroups = hourOfDayCalculator.getRequiredGroups();

        assertEquals(24, actualGroups.size());
        expectedGroups.forEach(group -> assertTrue(actualGroups.contains(group)));
    }

    @Test
    public void testGroupingLabelHourOfDay() {
        WaitTimesCalculatorA calculator = hourOfDayCalculator;

        assertEquals("Hour of day", calculator.getGroupingLabel());
    }

    @Test
    public void testAMHours() {
        for (int i = 1; i < 12; i++) {
            testWaitTimeGroupingHour(i, i + "AM");
        }
    }

    @Test
    public void testNoon() {
        testWaitTimeGroupingHour(12, "12PM");
    }


    @Test
    public void testPMHours() {
        for (int i = 1; i < 12; i++) {
            testWaitTimeGroupingHour(i + 12, i + "PM");
        }
    }

    private void testWaitTimeGroupingHour(int hour, String expectedGroup) {
        WaitTimesCalculatorA calculator = hourOfDayCalculator;
        WaitTimeRecord testRecord = new WaitTimeRecord("TestHospital", createDateWithHour(hour), 123);

        // check the expected group is correct
        assertEquals(expectedGroup, calculator.getGroup(testRecord));

        calculator.addWaitTime(testRecord);

        // check it was added correctly
        List<Integer> waitTimes = calculator.getWaitTimesFor(expectedGroup);

        assertEquals(1, waitTimes.size());
        assertEquals(testRecord.getWaitTimeMinutes(), waitTimes.get(0));
    }

    private Date createDateWithHour(int hour) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.HOUR_OF_DAY, hour);
        return calendar.getTime();
    }

    @Test
    public void testBaseFunctionality() {
        testWaitTimeGroupingSunday();
        beforeEach();
        testWaitTimeGroupingMonday();
        beforeEach();
        testWaitTimeGroupingTuesday();
        beforeEach();
        testWaitTimeGroupingWednesday();
        beforeEach();
        testWaitTimeGroupingThursday();
        beforeEach();
        testWaitTimeGroupingFriday();
        beforeEach();
        testWaitTimeGroupingSaturday();
        beforeEach();
        testAddMultipleGroups();
        beforeEach();
        testGetAverageNoGroup();
        beforeEach();
        testGetAverageWithGroup();
        beforeEach();
        testRequiredGroupsDayOfWeek();
        beforeEach();
        testGroupingLabelDayOfWeek();
    }

    private void testWaitTimeGroupingSunday() {
        testWaitTimeGroupingDay(1, "Sunday");
    }

    private void testWaitTimeGroupingMonday() {
        testWaitTimeGroupingDay(2, "Monday");
    }

    private void testWaitTimeGroupingTuesday() {
        testWaitTimeGroupingDay(3, "Tuesday");
    }

    private void testWaitTimeGroupingWednesday() {
        testWaitTimeGroupingDay(4, "Wednesday");
    }

    private void testWaitTimeGroupingThursday() {
        testWaitTimeGroupingDay(5, "Thursday");
    }

    private void testWaitTimeGroupingFriday() {
        testWaitTimeGroupingDay(6, "Friday");
    }

    private void testWaitTimeGroupingSaturday() {
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

    private void testAddMultipleGroups() {
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

    private void testGetAverageNoGroup() {
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

    private void testGetAverageWithGroup() {
        WaitTimesCalculatorA calculator = dayOfWeekCalculator;

        calculator.addWaitTime(new WaitTimeRecord("TestHospital", createDateWithDay(1), 4));
        calculator.addWaitTime(new WaitTimeRecord("TestHospital", createDateWithDay(1), 12));

        try {
            assertEquals(8, calculator.getAverageWaitTime("Sunday"));
        } catch (NoSuchGroupException ex) {
            fail("NoSuchGroupException thrown when data is available for group", ex);
        }
    }

    private void testRequiredGroupsDayOfWeek() {
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

    private void testGroupingLabelDayOfWeek() {
        WaitTimesCalculatorA calculator = dayOfWeekCalculator;

        assertEquals("Day of the week", calculator.getGroupingLabel());
    }

    private Date createDateWithDay(int dayOfWeek) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.DAY_OF_WEEK, dayOfWeek);
        return calendar.getTime();
    }
}
