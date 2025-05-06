package model.designb;

import model.WaitTimeRecord;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class DayOfWeekGroupingTest {
    private DayOfWeekGrouping grouping;

    @BeforeEach
    public void beforeEach() {
        grouping = new DayOfWeekGrouping();
    }

    @Test
    public void testSundayGroup() {
        testGroupWithDay(1, "Sunday");
    }

    @Test
    public void testMondayGroup() {
        testGroupWithDay(2, "Monday");
    }

    @Test
    public void testTuesdayGroup() {
        testGroupWithDay(3, "Tuesday");
    }

    @Test
    public void testWednesdayGroup() {
        testGroupWithDay(4, "Wednesday");
    }

    @Test
    public void testThursdayGroup() {
        testGroupWithDay(5, "Thursday");
    }

    @Test
    public void testFridayGroup() {
        testGroupWithDay(6, "Friday");
    }

    @Test
    public void testSaturdayGroup() {
        testGroupWithDay(7, "Saturday");
    }

    private void testGroupWithDay(int dayOfWeek, String expectedGroup) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.DAY_OF_WEEK, dayOfWeek);
        Date date = calendar.getTime();
        WaitTimeRecord record = new WaitTimeRecord("TestHospital", date, 123);

        assertEquals(expectedGroup, grouping.getGroupFor(record));
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

        assertEquals(requiredGroupsForDow, grouping.getRequiredGroups());
    }

    @Test
    public void testGroupingLabelDayOfWeek() {
        assertEquals("Day of the week", grouping.getGroupingLabel());
    }
}
