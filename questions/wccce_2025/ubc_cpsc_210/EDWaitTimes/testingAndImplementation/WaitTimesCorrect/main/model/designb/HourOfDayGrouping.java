package model.designb;

import model.HourFormatter;
import model.WaitTimeRecord;

import java.util.Calendar;
import java.util.Collection;
import java.util.List;

// represents the grouping for "by the hour of day of the record"
public class HourOfDayGrouping implements GroupingMechanism {
    // EFFECTS: returns the hour of the day (e.g. "9AM") corresponding to the record's time
    @Override
    public String getGroupFor(WaitTimeRecord record) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(record.getRecordTime());
        int hourOfDay = calendar.get(Calendar.HOUR_OF_DAY);
        return new HourFormatter(hourOfDay).formatHour();
    }

    // EFFECTS: returns the label/name of this mechanism. In this case, "Hour of day"
    @Override
    public String getGroupingLabel() {
        return "Hour of day";
    }

    // EFFECTS: returns a list of all hours of the day starting from "12AM" ("12AM", "1AM", "...")
    @Override
    public List<String> getRequiredGroups() {
        return HourFormatter.allHours();
    }
}
