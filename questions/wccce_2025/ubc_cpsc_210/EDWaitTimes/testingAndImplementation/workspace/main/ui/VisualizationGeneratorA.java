package ui;

import model.WaitTimeRecord;
import model.designa.WaitTimesCalculatorA;
import model.designa.WaitTimesGrouping;
import model.ex.NoSuchGroupException;
import org.knowm.xchart.CategoryChart;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

// visualization generator for Design A
public class VisualizationGeneratorA extends AbstractVisualizationGenerator {
    @Override
    public void generateVisualizations(List<WaitTimeRecord> recordStream) {
        generateVisualizations(recordStream, WaitTimesGrouping.DAY_OF_WEEK);
        // UNCOMMENT BELOW
//        generateVisualizations(recordStream, WaitTimesGrouping.HOUR_OF_DAY);
    }

    // EFFECTS: generates visualizations for a set of records with the provided grouping
    public void generateVisualizations(List<WaitTimeRecord> recordStream, WaitTimesGrouping grouping) {
        // setup calculator
        WaitTimesCalculatorA calculator = new WaitTimesCalculatorA(grouping);
        recordStream.forEach(calculator::addWaitTime);

        // create the chart
        String groupingLabel = calculator.getGroupingLabel();
        CategoryChart chart = createBaseChart(groupingLabel);

        Collection<String> groups = calculator.getRequiredGroups();

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

        saveChartToFile(chart, chart.getTitle());
    }
}
