package model;

import java.util.List;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class HourFormatterTest {
    private HourFormatter formatter;

    @Test
    public void testHourToAMOrPMPartAM() {
        for (int hour = 0; hour < 12; hour++) {
            formatter = new HourFormatter(hour);
            assertEquals("AM", formatter.hourToAMOrPMPart());
        }
    }

    @Test
    public void testHourToAMOrPMPartPM() {
        for (int hour = 12; hour < 24; hour++) {
            formatter = new HourFormatter(hour);
            assertEquals("PM", formatter.hourToAMOrPMPart());
        }
    }

    @Test
    public void testHourToNumberPartMidnight() {
        formatter = new HourFormatter(0);
        assertEquals(12, formatter.hourToNumberPart());
    }

    @Test
    public void testHourToNumberPartMorning() {
        for (int hour = 1; hour < 13; hour++) {
            formatter = new HourFormatter(hour);
            assertEquals(hour, formatter.hourToNumberPart());
        }
    }

    @Test
    public void testHourToNumberPartEvening() {
        for (int hour = 13; hour < 24; hour++) {
            formatter = new HourFormatter(hour);
            assertEquals(hour - 12, formatter.hourToNumberPart());
        }
    }

    @Test
    public void testAllHours() {
        assertEquals(
            List.of("12AM", "1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", "9AM", "10AM", "11AM",
                "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM"),
            HourFormatter.allHours());
    }
}
