package model.designb;

import ca.ubc.cs.autotest.AutoTest;
import ca.ubc.cs.autotest.Grader;
import ca.ubc.cs.autotest.Hint;
import model.WaitTimeRecord;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.*;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@AutoTest
public class HourOfDayGroupingTest {
    private HourOfDayGrouping grouping;

    @BeforeEach
    public void beforeEach() {
        grouping = new HourOfDayGrouping();
    }

    @ParameterizedTest
    @MethodSource("testAMHoursCaseProvider")
    @Hint("Design B: Test of grouping for AM Hours for hour of day")
    @Grader
    public void testAMHours(int hour, String expectedGroup) {
        assertEquals(expectedGroup, grouping.getGroupFor(createRecordWithHour(hour)));
    }

    public static Object[][] testAMHoursCaseProvider() {
        Object[][] cases = new Object[12][2];

        cases[0][0] = 0;
        cases[0][1] = "12AM";

        for (int i = 1; i < 12; i++) {
            cases[i][0] = i;
            cases[i][1] = i + "AM";
        }

        return cases;
    }

    @Test
    @Hint("Design B: Test of grouping for noon for hour of day")
    @Grader
    public void testNoon() {
        assertEquals("12PM", grouping.getGroupFor(createRecordWithHour(12)));
    }

    @ParameterizedTest
    @MethodSource("testPMHoursCaseProvider")
    @Hint("Design B: Test of grouping for PM Hours for hour of day")
    @Grader
    public void testPMHours(int hour, String expectedGroup) {
        assertEquals(expectedGroup, grouping.getGroupFor(createRecordWithHour(hour)));
    }

    public static Object[][] testPMHoursCaseProvider() {
        Object[][] cases = new Object[11][2];

        for (int i = 1; i < 12; i++) {
            cases[i - 1][0] = 12 + i;
            cases[i - 1][1] = i + "PM";
        }

        return cases;
    }

    @Test
    @Grader
    @Hint("Design B: Test for getGroupingLabel for hour of day")
    public void testGroupingLabel() {
        assertEquals("Hour of day", grouping.getGroupingLabel());
    }

    @Test
    @Grader
    @Hint("Design B: Test for getRequiredGroups for hour of day")
    public void testRequiredGroups() {
        List<String> expectedGroups = Arrays.asList(
                "12AM", "1AM", "2AM", "3AM", "4AM", "5AM",
                "6AM", "7AM", "8AM", "9AM", "10AM", "11AM",
                "12PM", "1PM", "2PM", "3PM", "4PM", "5PM",
                "6PM", "7PM", "8PM", "9PM", "10PM", "11PM"
        );
        Collection<String> actualGroups = grouping.getRequiredGroups();

        assertEquals(24, actualGroups.size());
        expectedGroups.forEach(group -> assertTrue(actualGroups.contains(group)));
    }


    private WaitTimeRecord createRecordWithHour(int hour) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.HOUR_OF_DAY, hour);
        Date date = calendar.getTime();

        return new WaitTimeRecord("TestHospital", date, 123);
    }
}
