package ui;

import model.WaitTimeRecord;
import org.knowm.xchart.BitmapEncoder;
import org.knowm.xchart.CategoryChart;
import org.knowm.xchart.CategoryChartBuilder;
import org.knowm.xchart.CategorySeries;

import java.io.File;
import java.io.IOException;
import java.util.List;

// represents a visualization generator for wait times
public abstract class AbstractVisualizationGenerator {
    // EFFECTS: creates a base bar/stick chart for wait times
    static CategoryChart createBaseChart(String groupingLabel) {
        CategoryChart chart = new CategoryChartBuilder()
                .title("Average wait times by " + groupingLabel.toLowerCase())
                .xAxisTitle(groupingLabel)
                .yAxisTitle("Average Wait Time in Minutes")
                .width(1200)
                .height(600)
                .build();

        // set it to a bar chart
        chart.getStyler().setDefaultSeriesRenderStyle(CategorySeries.CategorySeriesRenderStyle.Stick);

        return chart;
    }

    // EFFECTS: generates all the available visualizations for the provided records
    public abstract void generateVisualizations(List<WaitTimeRecord> recordStream);

    // EFFECTS: saves provided chart to file
    protected static void saveChartToFile(CategoryChart chart, String title) {
        try {
            File file = new File("charts", title + ".png");
            file.getParentFile().mkdirs(); // create parent if not already exists
            BitmapEncoder.saveBitmapWithDPI(chart, file.getCanonicalPath(), BitmapEncoder.BitmapFormat.PNG, 300);
        } catch (IOException ex) {
            System.out.println("Could not save chart to file!");
            ex.printStackTrace();
        }
    }
}
