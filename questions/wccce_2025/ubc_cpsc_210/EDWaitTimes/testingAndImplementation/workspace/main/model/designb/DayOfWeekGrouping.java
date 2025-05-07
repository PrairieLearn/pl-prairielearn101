package model.designb;

import model.WaitTimeRecord;

import java.util.*;

// represents the grouping for "by the day of the week of the record"
public class DayOfWeekGrouping implements GroupingMechanism {
    // EFFECTS: returns the day of the week (e.g. "Monday") that corresponds with the record's time
    @Override
    public String getGroupFor(WaitTimeRecord record) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(record.getRecordTime());
        int dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK);

        switch (dayOfWeek) {
            case 1: return "Sunday";
            case 2: return "Monday";
            case 3: return "Tuesday";
            case 4: return "Wednesday";
            case 5: return "Thursday";
            case 6: return "Friday";
            default: return "Saturday";
        }
    }

    // EFFECTS: returns a list of the days of the week starting from Sunday ("Sunday", "Monday", ...)
    @Override
    public List<String> getRequiredGroups() {
        return Arrays.asList(
                "Sunday",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday"
        );
    }

    // EFFECTS: returns the label/name of this mechanism. In this case, "Day of the week"
    @Override
    public String getGroupingLabel() {
        return "Day of the week";
    }
}
