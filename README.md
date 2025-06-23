# Tokyo Olympics Data Analysis

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-green?logo=streamlit)](https://tokyo-olympics-data-analysis.streamlit.app/)

This repository contains an in-depth data analysis and interactive dashboard for the Tokyo Olympics. The project explores medal distributions, athlete performance, gender representation, and the impact of COVID-19 on the games using both a Jupyter notebook and a Streamlit dashboard.

## Table of Contents

- [Introduction](#introduction)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results and Findings](#results-and-findings)
- [Conclusion](#conclusion)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

The goal of this project is to perform a comprehensive analysis of the Tokyo Olympics data to uncover insights into athlete performance, medal distributions, and the overall impact of the pandemic on the event. The analysis is performed using Python and popular data analysis libraries such as pandas, matplotlib, seaborn, and plotly. An interactive dashboard is provided using Streamlit.

## Data Sources

The data used in this analysis includes:

- **Medals**: Information about the number of medals won by each country (`Medals (1).xlsx`).
- **Athletes**: Details about the athletes, including age, gender, and sports category (`Athletes (2).xlsx`).
- **Coaches**: Information about coaches for each country (`Coaches (1).xlsx`).
- **EntriesGender**: Gender distribution for each discipline (`EntriesGender (1).xlsx`).
- **Teams**: Team participation by country and event (`Teams (1).xlsx`).

## Project Structure

The repository is structured as follows:

```
Tokyo-Olympics-Data-Analysis/
│
├── Athletes (2).xlsx
├── Coaches (1).xlsx
├── EntriesGender (1).xlsx
├── Medals (1).xlsx
├── Teams (1).xlsx
├── Data_Analysis_on_the_Tokyo_Olympics.ipynb
├── streamlit_app.py
├── requirements.txt
└── README.md
```

- Excel files: Raw data used in the analysis.
- `Data_Analysis_on_the_Tokyo_Olympics.ipynb`: Jupyter notebook with the code, analysis, and visualizations.
- `streamlit_app.py`: Streamlit dashboard for interactive data exploration.
- `requirements.txt`: List of dependencies required to run the project.
- `README.md`: Description and documentation of the project.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Tokyo-Olympics-Data-Analysis.git
   cd Tokyo-Olympics-Data-Analysis
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Jupyter Notebook

Open the Jupyter notebook to explore the data analysis:

```bash
jupyter notebook Data_Analysis_on_the_Tokyo_Olympics.ipynb
```

Follow the steps in the notebook to reproduce the analysis and generate visualizations.

### Streamlit Dashboard

To launch the interactive dashboard locally, run:

```bash
streamlit run streamlit_app.py
```

This will open a web browser with the interactive dashboard, where you can explore all visualizations and insights in a scrollable format.

**Or try the hosted app here:**
[https://tokyo-olympics-data-analysis.streamlit.app/](https://tokyo-olympics-data-analysis.streamlit.app/)

## Results and Findings

Key findings from the analysis include:

- Medal distributions across different countries, with the USA, China, and Japan leading the tally.
- Performance analysis of athletes and coaches by country and discipline.
- Gender representation and distribution across disciplines and events.
- The impact of COVID-19 on athlete performance and event outcomes.
- Visualizations and detailed results are available in both the notebook and the dashboard.

## Conclusion

The analysis provides insights into the performance of athletes at the Tokyo Olympics, highlighting the achievements and challenges faced during the event. Recommendations for future improvements in sports development and athlete support are discussed.

## Contributing

Contributions are welcome! Please read the CONTRIBUTING.md file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
