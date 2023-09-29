class Job:
    """
    Represents a job with attributes such as job ID, start time, job size, execution interval, and state.
    """
    def __init__(self, job_id, start_time, job_size, execution_interval, state):
        self.job_id = job_id
        self.start_time = start_time
        self.job_size = job_size
        self.execution_interval = execution_interval
        self.state = state

def read_table_data(filename):
    """
    Reads job data from a file and returns it as a list of tuples.
    
    Args:
        filename (str): The name of the file to read data from.

    Returns:
        list: A list of tuples containing job data.
    """
    table_data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) == 5:
                job_id, start_time, job_size, execution_interval, state = parts
                table_data.append((int(job_id), int(start_time), int(job_size), int(execution_interval), state))
    return table_data

def run_jobs(jobs, memory_allocation):
    """
    Simulates job execution for a list of jobs using a specified memory allocation strategy.
    
    Args:
        jobs (list): List of Job objects representing jobs to be executed.
        memory_allocation (function): Memory allocation strategy function.

    Returns:
        None
    """
    current_time = 0
    memory_used = 0
    memory_limit = 20 * 1024  # Total memory size in bytes (20 Kbytes)
    page_size = 1024  # Page size in bytes (1 Kbyte)

    for job in jobs:
        if job.start_time > current_time:
            current_time = job.start_time

        while current_time < job.start_time + job.execution_interval:
            if memory_allocation(jobs, memory_used, job, memory_limit, page_size):
                memory_used += job.job_size
                job.state = "Running"
            else:
                job.state = "Sleep"
                break

            current_time += 1  # 1 second

    for job in jobs:
        print(f"{job.job_id}: {job.state}")

def best_fit_allocation(jobs, memory_used, job, memory_limit, page_size):
    """
    Implements the Best-Fit memory allocation strategy.
    
    Args:
        jobs (list): List of Job objects representing jobs to be executed.
        memory_used (int): The current memory usage.
        job (Job): The job to allocate memory for.
        memory_limit (int): The total memory size limit.
        page_size (int): The size of memory pages.

    Returns:
        bool: True if memory allocation is successful, False otherwise.
    """
    best_fit_slot = None
    best_fit_size = float("inf")

    for j in jobs:
        if j.start_time <= job.start_time and j.state == "Sleep":
            if j.job_size >= job.job_size and j.job_size <= (memory_limit - memory_used):
                if j.job_size < best_fit_size:
                    best_fit_size = j.job_size
                    best_fit_slot = j

    if best_fit_slot:
        best_fit_slot.state = "Running"
        return True

    return False

def first_fit_allocation(jobs, memory_used, job, memory_limit, page_size):
    """
    Implements the First-Fit memory allocation strategy.
    
    Args:
        jobs (list): List of Job objects representing jobs to be executed.
        memory_used (int): The current memory usage.
        job (Job): The job to allocate memory for.
        memory_limit (int): The total memory size limit.
        page_size (int): The size of memory pages.

    Returns:
        bool: True if memory allocation is successful, False otherwise.
    """
    for j in jobs:
        if j.start_time <= job.start_time and j.state == "Sleep":
            if j.job_size >= job.job_size and j.job_size <= (memory_limit - memory_used):
                j.state = "Running"
                return True

    return False

def worst_fit_allocation(jobs, memory_used, job, memory_limit, page_size):
    """
    Implements the Worst-Fit memory allocation strategy.
    
    Args:
        jobs (list): List of Job objects representing jobs to be executed.
        memory_used (int): The current memory usage.
        job (Job): The job to allocate memory for.
        memory_limit (int): The total memory size limit.
        page_size (int): The size of memory pages.

    Returns:
        bool: True if memory allocation is successful, False otherwise.
    """
    worst_fit_slot = None
    worst_fit_size = -1

    for j in jobs:
        if j.start_time <= job.start_time and j.state == "Sleep":
            if j.job_size >= job.job_size and j.job_size <= (memory_limit - memory_used):
                if j.job_size > worst_fit_size:
                    worst_fit_size = j.job_size
                    worst_fit_slot = j

    if worst_fit_slot:
        worst_fit_slot.state = "Running"
        return True

    return False

# Read data from input1.txt
input1_data = read_table_data("input1.txt")

print("Table-1 Jobs (Best-Fit):")
table1_jobs = [Job(*data) for data in input1_data]
run_jobs(table1_jobs, lambda jobs, memory_used, job, memory_limit, page_size: memory_used + job.job_size <= memory_limit)

print("\nTable-1 Jobs (First-Fit):")
run_jobs(table1_jobs.copy(), lambda jobs, memory_used, job, memory_limit, page_size: first_fit_allocation(jobs, memory_used, job, memory_limit, page_size))

print("\nTable-1 Jobs (Worst-Fit):")
run_jobs(table1_jobs.copy(), lambda jobs, memory_used, job, memory_limit, page_size: worst_fit_allocation(jobs, memory_used, job, memory_limit, page_size))

# Read data from input2.txt
input2_data = read_table_data("input2.txt")

print("\nTable-2 Jobs (Best-Fit):")
table2_jobs = [Job(*data) for data in input2_data]
run_jobs(table2_jobs.copy(), lambda jobs, memory_used, job, memory_limit, page_size: best_fit_allocation(jobs, memory_used, job, memory_limit, page_size))

print("\nTable-2 Jobs (First-Fit):")
run_jobs(table2_jobs.copy(), lambda jobs, memory_used, job, memory_limit, page_size: first_fit_allocation(jobs, memory_used, job, memory_limit, page_size))

print("\nTable-2 Jobs (Worst-Fit):")
run_jobs(table2_jobs.copy(), lambda jobs, memory_used, job, memory_limit, page_size: worst_fit_allocation(jobs, memory_used, job, memory_limit, page_size))
