package model.designb;

import ca.ubc.cs.autotest.AutoTest;
import ca.ubc.cs.autotest.Grader;
import ca.ubc.cs.autotest.Hint;
import model.WaitTimeRecord;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@AutoTest
public class DayOfWeekGroupingTest {
    private DayOfWeekGrouping grouping;

    @BeforeEach
    public void beforeEach() {
        grouping = new DayOfWeekGrouping();
    }

    @Test
    @Hint("Design B: Base functionality")
    @Grader
    public void testBaseFunctionality() {
        testGroupings();
        beforeEach();
        testRequiredGroupsDayOfWeek();
        beforeEach();
        testGroupingLabelDayOfWeek();
    }

    private void testGroupings() {
        testGroupWithDay(1, "Sunday");
        testGroupWithDay(2, "Monday");
        testGroupWithDay(3, "Tuesday");
        testGroupWithDay(4, "Wednesday");
        testGroupWithDay(5, "Thursday");
        testGroupWithDay(6, "Friday");
        testGroupWithDay(7, "Saturday");
    }

    private void testGroupWithDay(int dayOfWeek, String expectedGroup) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.DAY_OF_WEEK, dayOfWeek);
        Date date = calendar.getTime();
        WaitTimeRecord record = new WaitTimeRecord("TestHospital", date, 123);

        assertEquals(expectedGroup, grouping.getGroupFor(record));
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

        assertEquals(requiredGroupsForDow, grouping.getRequiredGroups());
    }

    private void testGroupingLabelDayOfWeek() {
        assertEquals("Day of the week", grouping.getGroupingLabel());
    }
}
