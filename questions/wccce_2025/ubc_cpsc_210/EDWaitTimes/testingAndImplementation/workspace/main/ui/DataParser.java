package ui;

import model.WaitTimeRecord;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Date;
import java.util.stream.Stream;

// represents a parser that reads wait times from files and parses them into WaitTimeRecords
public class DataParser {
    private Path dataPath;

    // EFFECTS: initializes data parser with provided path
    public DataParser(Path dataPath) {
        this.dataPath = dataPath;
    }

    // EFFECTS: Reads all the records from path and provides them as wait time records
    public Stream<WaitTimeRecord> readRecords() throws IOException {
        return Files.readAllLines(dataPath)
                .stream()
                .map(this::createWaitTimeRecord);
    }

    // EFFECTS: parses a line into a wait time record
    private WaitTimeRecord createWaitTimeRecord(String line) {
        String[] columns = line.split(",");
        Date recordTime = new Date(Long.parseLong(columns[0]) * 1000);
        String hospital = columns[1];

        String[] waitTimeString = columns[2].split(":");
        int waitTimeMinutes = Integer.parseInt(waitTimeString[0]) * 60 + Integer.parseInt(waitTimeString[1]);

        return new WaitTimeRecord(hospital, recordTime, waitTimeMinutes);
    }
}
