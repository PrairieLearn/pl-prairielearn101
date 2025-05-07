package model;

import java.util.ArrayList;
import java.util.List;

// A utility class that aids in the formatting of time strings
public class HourFormatter {
    private int hour;

    // REQUIRES: hour is in [0, 23]
    // EFFECTS: constructs a formatter for hour;
    //          0 is midnight (12AM), 12 is noon (12PM)
    public HourFormatter(int hour) {
        this.hour = hour;
    }

    // EFFECTS: for a time like 0 (12AM), 3 (3AM), or 19 (7PM),
    //          produces only the "AM" or "PM" part.
    public String hourToAMOrPMPart() {
        if (hour < 12) {
            return "AM";
        } else {
            return "PM";
        }
    }

    // EFFECTS: for a time like 0 (12AM), 3 (3AM), or 19 (7PM),
    //          produces only the numerical (12, 3, 7) part.
    public int hourToNumberPart() {
        // x % 12 is in the range [0, 11]
        // Adding 11 beforehand and adding 1 after
        // gives the range [1, 12] as desired.
        return ((hour + 11) % 12) + 1;
    }

    // EFFECTS: produces the hour as a string like 12AM (for 0),
    //          3AM (for 3), or 7PM (for 19)
    public String formatHour() {
        return hourToNumberPart() + hourToAMOrPMPart();
    }

    // EFFECTS: returns a list of the hours in a day, formatted as strings:
    //          ["12AM", "1AM", ... , "10PM", "11PM"]
    public static List<String> allHours() {
        List<String> result = new ArrayList<>();
        for (int i = 0; i < 24; i++) {
            result.add(new HourFormatter(i).formatHour());
        }
        return result;
    }
}
