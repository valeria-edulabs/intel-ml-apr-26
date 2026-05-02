## Exercise 1: Extend `Sensor` with more logic

### Objective
Extend the `Sensor` class so it supports more realistic sensor behavior and analysis.

### Suggested extensions
- Add a method `count_by_quality()` that returns a dictionary with counts of each measurement quality value.
- Add a method `min_max_average()` that returns a tuple `(min_value, max_value, average_value)` using the sensor's current unit.
- Add a method `clean_data()` that removes measurements with `quality != "good"` and returns how many were removed.
- Add a method `summary()` that returns a friendly summary string for the sensor, including the number of measurements, average temperature, and number of anomalies.

### How to use GitHub Copilot
1. Open `python_refresher/05_object_oriented.py` and place your cursor inside the `Sensor` class.
2. Start by writing a short comment describing the method you want, for example:
   - `# TODO: compute counts of measurements by quality`
   - `# TODO: return min/max/average values in current sensor unit`
3. Ask Copilot to complete the method implementation.
4. Review the code it suggests.
5. Repeat for each new method.

### Tests and edge cases
- Ask Copilot to write tests for the new methods in a new file like `python_refresher/test_sensor.py`.
- Run the tests and confirm they pass.
- Think of an edge case that Copilot's tests may have missed, for example:
  - the sensor has no measurements,
  - all measurements are `quality="suspect"`,
  - measurements are mixed units when converting values,
  - `clean_data()` is called twice.
- Then ask Copilot to implement a new test for that edge case.
- Run the tests again and verify the result.

### Example prompt for Copilot
> "Add a `min_max_average` method to the `Sensor` class that returns the minimum, maximum, and average temperature in the sensor's unit. Then write tests for normal and empty measurement lists."


## Exercise 2: Refactor selection code into cleaner form

### Objective
Find a section of `05_object_oriented.py` or another file where the code is repetitive or hard to read, and use Copilot to make it cleaner.


### How to use GitHub Copilot
1. Highlight or select the block of code you want to improve.
2. Ask Copilot to rewrite it in a cleaner or more Pythonic way.
3. Compare the original and suggested versions.
4. Keep the version that is easier to read and still correct.


### Ask Copilot to test it
- After refactoring, ask Copilot to write a small test or a simple usage example that exercises the refactored code.
- Run it to make sure behavior is unchanged.

## Exercise 3: Create a Streamlit UI for the `Sensor` class

### Objective
Use GitHub Copilot to build a web-based dashboard using Streamlit to interact with your `Sensor` class and visualize its data.

### How to use GitHub Copilot
1. Create a new file `python_refresher/sensor_dashboard.py`.
2. Ask Copilot to:
   - Import `streamlit` and the `Sensor` class from `05_object_oriented.py`.
   - Create a user interface that allows you to interact with all the functionalities of the `Sensor` class.
   - Add inputs to create a sensor, add measurements, and view summaries.
3. **Customize the Design:**
   - Experiment with Copilot to change the **styling and colors** (e.g., "Make the dashboard look like a high-tech dark mode control panel").
   - Adjust the **positioning** of elements (e.g., "Use columns to show the sensor stats side-by-side").
   - Add visual elements like charts or status indicators for anomalies.

### Example prompt for Copilot
> "Use Streamlit to create a professional dashboard for my Sensor class. Include inputs to add measurements and use columns to display sensor stats. Make the styling modern with custom colors for anomalies and different quality levels."