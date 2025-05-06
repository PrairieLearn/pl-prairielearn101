package ui;

import model.designb.*;
import model.WaitTimeRecord;
import model.ex.NoSuchGroupException;
import org.knowm.xchart.CategoryChart;
import org.knowm.xchart.style.AxesChartStyler;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

// visualization generator for Design B
public class VisualizationGeneratorB extends AbstractVisualizationGenerator {
    @Override
    public void generateVisualizations(List<WaitTimeRecord> recordStream) {
        generateVisualizations(recordStream, new DayOfWeekGrouping());
        // UNCOMMENT BELOW
//        generateVisualizations(recordStream, new HourOfDayGrouping());
    }

    // EFFECTS: generates visualizations for a set of records with the provided grouping
    private void generateVisualizations(List<WaitTimeRecord> recordStream, GroupingMechanism adapter) {
        WaitTimesCalculatorB calculator = new WaitTimesCalculatorB(adapter);
        recordStream.forEach(calculator::addWaitTime);

        // create the chart
        String groupingLabel = adapter.getGroupingLabel();
        CategoryChart chart = createBaseChart(groupingLabel);

        Collection<String> groups = adapter.getRequiredGroups();

        if (groups == null) {
            groups = calculator.getGroupWaitTimes().keySet();
        }

        List<String> xAxis = new ArrayList<>();
        List<Double> yAxis = new ArrayList<>();

        for (String group : groups) {
            double averageWaitTime = 0;

            try {
                averageWaitTime = calculator.getAverageWaitTime(group);
            } catch (NoSuchGroupException ex) {
                System.out.println("No data found for group " + group + "!");
            }

            xAxis.add(group);
            yAxis.add(averageWaitTime);
        }

        chart.addSeries("Wait Times", xAxis, yAxis);

        int totalChars = groups.stream()
                .mapToInt(String::length)
                .sum();

        // if total chars won't fit across chart, tilt them 90 degrees
        if (totalChars > 80) {
            chart.getStyler().setXAxisLabelAlignment(AxesChartStyler.TextAlignment.Right);
            chart.getStyler().setXAxisLabelRotation(90);
        }

        saveChartToFile(chart, chart.getTitle());
    }
}
