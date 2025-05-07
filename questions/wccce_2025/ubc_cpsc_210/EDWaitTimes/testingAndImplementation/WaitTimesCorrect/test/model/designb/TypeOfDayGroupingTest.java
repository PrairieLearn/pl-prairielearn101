package model.designb;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Calendar;
import java.util.Date;
import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import model.WaitTimeRecord;

public class TypeOfDayGroupingTest {
    private TypeOfDayGrouping grouping;

    @BeforeEach
    public void beforeEach() {
        grouping = new TypeOfDayGrouping();
    }
    
    @Test
    public void testWeekdayGroup() {
        for (int i = 2; i < 7; i++) {
            testGroupWithDay(i, "Weekday");
        }
    }

    @Test
    public void testWeekendGroup() {
        testGroupWithDay(1, "Weekend");
        testGroupWithDay(7, "Weekend");
    }

    @Test
    public void testRequiredGroupsTypeOfDay() {
        assertEquals(List.of("Weekend", "Weekday"), grouping.getRequiredGroups());
    }

    @Test
    public void testGroupingLabelTypeOfDay() {
        assertEquals("Type of day", grouping.getGroupingLabel());
    }

    private void testGroupWithDay(int dayOfWeek, String expectedGroup) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.DAY_OF_WEEK, dayOfWeek);
        Date date = calendar.getTime();
        WaitTimeRecord record = new WaitTimeRecord("TestHospital", date, 123);

        assertEquals(expectedGroup, grouping.getGroupFor(record));
    }
}
