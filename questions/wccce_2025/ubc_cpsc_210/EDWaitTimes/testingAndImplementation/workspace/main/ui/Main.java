package ui;

import model.WaitTimeRecord;

import java.io.IOException;
import java.nio.file.Path;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws Exception {
        Main main = new Main();
        main.run();
    }

    // EFFECTS: runs the application to generate visualizations from src/wait_times_data.csv
    public void run() throws IOException {
        DataParser parser = new DataParser(Path.of("src", "wait_time_data.csv"));
        List<WaitTimeRecord> recordStream = parser.readRecords().collect(Collectors.toList());
        // Update the line below to VisualizationGeneratorB to test out the new one
        AbstractVisualizationGenerator generator = new VisualizationGeneratorA();

        generator.generateVisualizations(recordStream);
    }

}
