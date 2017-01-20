# Hadoop Mapreduce Assignment 

### Problem Statement
**Find the number of spikes per website based on the user interaction time, using Mapreduce**
**Input file can be downloaded with onedrive below link**
https://1drv.ms/f/s!AmF05rpHfVsrkiah2L09vOxMBzLp

Input is a weblog stored in a tab-separated 3-column file. Each line represents a website, start_datetime & end_datetime, e.g., “199.72.81.55 1995-08-20 05:08:01 1995-08-20 05:11:08” represents a website, user interaction start time, and user interaction end time. Your job is to find the number of spikes per website based on the user interaction time.


**Spike:** If the average time spent on a website per day has at least doubled two times continuously over three consecutive days then it is called a spike.

 # **Solution**
**MapReduce Job 1:** Find average number of seconds users spent on each website, for each day.
**MapReduce Job 2:** Identify the spikes in this data.
**MapReduce Job 3:** Aggregate the counts to get number of spikes per website


