package model.designb;

import java.util.Calendar;
import java.util.List;

import model.WaitTimeRecord;

// Note to graders: This is an example of one (simple) possible grouping mechanism.
// Students are encouraged to get creative and come up with their own mechanisms!

// represents a grouping which separates days by "type": weekend or weekday
public class TypeOfDayGrouping implements GroupingMechanism {
    // EFFECTS: returns the type of day ("Weekend" or "Weekday") corresponding to the record's day
    @Override
    public String getGroupFor(WaitTimeRecord record) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(record.getRecordTime());
        int dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK);
        if (dayOfWeek == 1 || dayOfWeek == 7) {
            return "Weekend";
        }
        return "Weekday";
    }

    // EFFECTS: returns the label/name of this mechanism. In this case, "Type of day"
    @Override
    public String getGroupingLabel() {
        return "Type of day";
    }

    // EFFECTS: returns a list of all "types" of days
    @Override
    public List<String> getRequiredGroups() {
        return List.of("Weekend", "Weekday");
    }
}
