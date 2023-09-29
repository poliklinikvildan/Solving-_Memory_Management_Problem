# Solving_Memory_Management_Problem
**Summary:**

The provided Python code serves as a comprehensive tool for simulating memory management in a computer operating system. It takes input job data from two files, `input1.txt` and `input2.txt`, and conducts job processing based on different memory allocation algorithms, namely Random Fit, Best-Fit, First-Fit, and Worst-Fit, as outlined in the Assignment 1 prompt. After processing the jobs, the program reports the state of each job at the end of each interval.

**Key Features and Functionalities:**

* **Job Representation:**
  * The code defines a `Job` class that encapsulates essential attributes of a job, such as its ID, start time, size, execution interval, and state.

* **Data Reading:**
  * A function `read_table_data(filename)` is implemented to read job data from an input file and convert it into a list of tuples, where each tuple represents job information.

* **Job Execution Simulation:**
  * The core function, `run_jobs(jobs, memory_allocation)`, facilitates the execution simulation of jobs. It tracks the current time, memory usage, and memory limit while processing the jobs.

* **Memory Allocation Strategies:**
  * The code offers three distinct memory allocation strategy functions, namely `best_fit_allocation`, `first_fit_allocation`, and `worst_fit_allocation`. These functions determine which job should be allocated memory based on the chosen strategy.

* **Input Data Processing:**
  * The code reads data from `input1.txt` and `input2.txt`, creating instances of `Job` objects. It then simulates job execution for both datasets using specified memory allocation strategies.

* **Output Reporting:**
  * The program prints the state of each job at the conclusion of each interval, providing insights into job execution and memory allocation efficiency.

**Job States Explained:**

* **"Running"**: This state signifies that a job has successfully obtained memory resources and is actively executing its task. Jobs in this state are utilizing allocated memory and contributing to the system's memory utilization.

* **"Sleep"**: The "Sleep" state indicates that a job is waiting for available memory resources. In this state, the job is not actively executing and is essentially in a waiting or non-execution state.

* **"End"**: The "End" state denotes that a job has completed its memory allocation and execution phase.

**Additional Information:**

* An interval is the number of seconds.
* Total Memory size = 20 Kbytes.
* Page size = 1 Kbyte.

The provided code offers a powerful tool for studying memory management challenges and solutions within the context of an operating system. The output can be viewed in the editor's output console or saved to an `output.txt` file, which is appendable in the code development environment.
