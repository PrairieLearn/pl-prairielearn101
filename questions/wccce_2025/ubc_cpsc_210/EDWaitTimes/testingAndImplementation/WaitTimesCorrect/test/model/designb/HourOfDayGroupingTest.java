package model.designb;

import model.WaitTimeRecord;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.*;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class HourOfDayGroupingTest {
    private HourOfDayGrouping grouping;

    @BeforeEach
    public void beforeEach() {
        grouping = new HourOfDayGrouping();
    }

    @Test
    public void testAMHours() {
        for (int i = 1; i < 12; i++) {
            assertEquals(i + "AM", grouping.getGroupFor(createRecordWithHour(i)));
        }
    }

    @Test
    public void testNoon() {
        assertEquals("12PM", grouping.getGroupFor(createRecordWithHour(12)));
    }


    @Test
    public void testPMHours() {
        for (int i = 1; i < 12; i++) {
            assertEquals(i + "PM", grouping.getGroupFor(createRecordWithHour(i + 12)));
        }
    }

    @Test
    public void testGroupingLabel() {
        assertEquals("Hour of day", grouping.getGroupingLabel());
    }

    @Test
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