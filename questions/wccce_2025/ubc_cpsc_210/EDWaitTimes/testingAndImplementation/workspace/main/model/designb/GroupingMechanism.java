package model.designb;

import model.WaitTimeRecord;

import java.util.Collection;
import java.util.List;

// represents a grouping mechanism for wait time records
public interface GroupingMechanism {
    // EFFECTS: returns the appropriate 'key' for this record based on the grouping
    String getGroupFor(WaitTimeRecord record);

    // EFFECTS: returns the label/name of this mechanism. e.g. "Day of the week" or "Hour of day"
    String getGroupingLabel();

    // EFFECTS: returns the set of groups that, if applicable, must always be shown even if values for that group
    //          are not present;
    //          returns null if only groups with values should be shown
    List<String> getRequiredGroups();
}
