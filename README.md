# Log-Monitoring-Application

The goal of this application is to read logs files, measures how long each job takes from start to finish and generates warnings or errors if the processing time exceeds certain thresholds.

## Features

1. Parse the log file.
2. Identify each job or task and track its start and finish times.
3. Calculate the duration of each job from the time it started to the time it finished.
4. Produce a report with warning/error logs when a job takes longer than certain threshold value (e.g. 5 minutes, 10 minutes)

## Usage

Clone the GitHub Repository [Log Monitoring App](https://github.com/daniel-marius/Log-Monitoring-Application)

```bash
git clone https://github.com/daniel-marius/Log-Monitoring-Application.git
``` 

Navigate to the root folder of the repository cloned

```bash
cd Log-Monitoring-Application
```

Before running the application, make sure that you have [Python](https://www.python.org/downloads/) installed on your machine

Run the application with the following command (depending on your python version)

```bash
python3 main.py
```