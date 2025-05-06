package model.designa;

import model.HourFormatter;
import model.WaitTimeRecord;
import model.ex.NoSuchGroupException;

import java.util.*;

// Represents a calculator that aggregates wait times for each grouping.
// Specifically, it will average the wait times provided
public class WaitTimesCalculatorA {
    // mapping some string 'key' representing the group to a list of wait times
    private Map<String, List<Integer>> groupValues = new HashMap<>();
    private WaitTimesGrouping group;

    // EFFECTS: initializes calculator with a specified grouping to be used
    public WaitTimesCalculatorA(WaitTimesGrouping group) {
        this.group = group;
    }

    // EFFECTS: returns the current wait times for each group
    public Map<String, List<Integer>> getGroupWaitTimes() {
        return groupValues;
    }

    // MODIFIES: this
    // EFFECTS: Adds the wait time to the provided date's group based on the calculator's grouping setting
    public void addWaitTime(WaitTimeRecord record) {
        String group = getGroup(record);

        if (!groupValues.containsKey(group)) {
            groupValues.put(group, new ArrayList<>());
        }

        List<Integer> waitTimes = groupValues.get(group);
        waitTimes.add(record.getWaitTimeMinutes());
    }

    // EFFECTS: Returns the current values for a given group
    public List<Integer> getWaitTimesFor(String group) {
        return groupValues.getOrDefault(group, Collections.emptyList());
    }

    // EFFECTS: Returns average wait time for a given group
    // throws NoSuchGroupException if there are no wait times for provided group
    public double getAverageWaitTime(String group) throws NoSuchGroupException {
        if (!groupValues.containsKey(group)) {
            throw new NoSuchGroupException();
        }

        List<Integer> waitTimes = getWaitTimesFor(group);
        double total = 0.0;

        for (int waitTime : waitTimes) {
            total += waitTime;
        }

        return total / waitTimes.size();
    }

    // EFFECTS: returns the appropriate group name for the provided date based on the grouping setting provided
    //          for day of week: returns the day of the week (e.g. "Monday") that corresponds with the record's time
    //          otherwise: returns the hour of the day (e.g. "9AM") corresponding to the record's time
    public String getGroup(WaitTimeRecord record) {
        Calendar calendar = Calendar.getInstance();

        calendar.setTime(record.getRecordTime());

        switch (this.group) {
            case DAY_OF_WEEK:
                int dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK);
                return getWeekdayGroupNames().get(dayOfWeek - 1);

            default:
                int hourOfDay = calendar.get(Calendar.HOUR_OF_DAY);
                return new HourFormatter(hourOfDay).formatHour();
        }
    }

    // EFFECTS: returns the set of groups that, if applicable, must always be shown even if values
    //          for that group are not present:
    //             for day of week: returns every day of the week
    //             otherwise: returns every hour string of the day "12AM", "1AM", ...
    public List<String> getRequiredGroups() {
        switch (this.group) {
            case DAY_OF_WEEK:
                return getWeekdayGroupNames();

            default:
                return HourFormatter.allHours();
        }
    }

    // EFFECTS: returns the display name / label of the grouping type. e.g. 'Average wait times by ...'
    //          for day of week: returns "Day of the week"
    //          otherwise: returns "Hour of day"
    public String getGroupingLabel() {
        switch (this.group) {
            case DAY_OF_WEEK:
                return "Day of the week";

            default:
                return "Hour of day";
        }
    }

    // EFFECTS: returns every day of the week, in order from Sunday to Saturday
    //          as a List of Strings.
    private List<String> getWeekdayGroupNames() {
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
}
