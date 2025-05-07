package model;

import java.util.Date;

// represents a time when we recorded the current wait time
public class WaitTimeRecord {
    private final String hospital;
    private final Date recordTime;
    private final int waitTimeMinutes;

    // EFFECTS: creates a new record with the provided information
    public WaitTimeRecord(String hospital, Date recordTime, int waitTimeMinutes) {
        this.hospital = hospital;
        this.recordTime = recordTime;
        this.waitTimeMinutes = waitTimeMinutes;
    }

    public String getHospital() {
        return hospital;
    }

    public Date getRecordTime() {
        return recordTime;
    }

    public int getWaitTimeMinutes() {
        return waitTimeMinutes;
    }
}
