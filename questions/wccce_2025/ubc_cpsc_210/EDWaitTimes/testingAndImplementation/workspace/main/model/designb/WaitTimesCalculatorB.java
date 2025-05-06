package model.designb;

import model.WaitTimeRecord;
import model.ex.NoSuchGroupException;

import java.util.*;

// Represents a calculator that aggregates wait times for each grouping.
// Specifically, it will average the wait times provided
public class WaitTimesCalculatorB {
    // mapping some integer 'key' representing the group to a list of wait times
    private Map<String, List<Integer>> groupValues = new HashMap<>();
    private GroupingMechanism groupingMechanism;

    // EFFECTS: initializes calculator with a specified grouping to be used
    public WaitTimesCalculatorB(GroupingMechanism groupingMechanism) {
        this.groupingMechanism = groupingMechanism;
    }

    // EFFECTS: returns the current wait times for each group
    public Map<String, List<Integer>> getGroupWaitTimes() {
        return groupValues;
    }

    // MODIFIES: this
    // EFFECTS: Adds the wait time to the provided record based on the calculator's grouping setting
    public void addWaitTime(WaitTimeRecord record) {
        String group = groupingMechanism.getGroupFor(record);

        if (!groupValues.containsKey(group)) {
            groupValues.put(group, new ArrayList<>());
        }

        List<Integer> waitTimes = groupValues.get(group);
        waitTimes.add(record.getWaitTimeMinutes());
    }

    // EFFECTS: Returns the current values for a given group
    public List<Integer> getWaitTimesFor(String key) {
        return groupValues.getOrDefault(key, Collections.emptyList());
    }

    // EFFECTS: Returns average wait time for a given group
    // throws NoSuchGroupException if there are no wait times for provided group
    public double getAverageWaitTime(String key) throws NoSuchGroupException {
        if (!groupValues.containsKey(key)) {
            throw new NoSuchGroupException();
        }

        List<Integer> waitTimes = getWaitTimesFor(key);
        double total = 0.0;

        for (int waitTime : waitTimes) {
            total += waitTime;
        }

        return total / waitTimes.size();
    }
}
