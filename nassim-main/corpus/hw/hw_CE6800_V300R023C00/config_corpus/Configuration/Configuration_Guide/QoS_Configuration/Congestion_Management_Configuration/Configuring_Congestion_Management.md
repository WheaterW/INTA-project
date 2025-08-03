Configuring Congestion Management
=================================

Configuring Congestion Management

#### Context

Congestion management is a queue-based technology. With congestion management configured, if packets are buffered in queues due to congestion on a network, the device determines the sequence at which packets are forwarded according to the defined scheduling policy, thereby preferentially scheduling high-priority services.

There are eight queues on each interface, and each queue is able to use a different scheduling mode. During queue scheduling, PQ queues are scheduled first. Multiple PQ queues are scheduled in descending order of priority, with a larger queue index indicating a higher priority. After completing PQ scheduling, the device schedules the queues using WDRR scheduling. Finally, the device schedules the queues using LPQ scheduling.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-type interface-number | interface-name }
   ```
3. Configure a scheduling mode for queues on the interface.
   
   
   ```
   [qos](cmdqueryname=qos) { pq { start-queue-index [ to end-queue-index ] } &<1-8> | drr { start-queue-index [ to end-queue-index ] } &<1-8>* | lpq { start-queue-index [ to end-queue-index ] } &<1-8> }*
   ```
   
   LPQ scheduling is supported only by the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.
4. (Optional) Configure the queue weight in WDRR scheduling mode.
   
   
   ```
   [qos queue](cmdqueryname=qos+queue) queue-index drr weight weight-value
   ```
5. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. (Optional) Configure high-priority scheduling for queues 6 and 7 in the high-performance computing (HPC) scenario.
   
   
   ```
   [qos hpc enhanced](cmdqueryname=qos+hpc+enhanced)
   ```
   
   In the HPC scenario, if small packets are congested on multiple interfaces, packet loss may occur in queues 6 and 7. In this case, you can configure high-priority scheduling for queues 6 and 7.
   
   This function is supported only by the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display qos queue statistics**](cmdqueryname=display+qos+queue+statistics) { **slot** *slotid* | **interface** { *interface-type* *interface-number* | *interface-name* } } command to check queue-based traffic statistics.