Configuring an ETS Profile
==========================

Configuring an ETS Profile

#### Context

ETS provides two-level flow control:

* Flow control based on the priority group: congestion management and traffic shaping based on the priority group
* Flow control based on the priority: queue congestion management, queue shaping, and queue congestion avoidance


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an ETS profile and enter the ETS profile view.
   
   
   ```
   [dcb ets-profile](cmdqueryname=dcb+ets-profile) name
   ```
   
   The system provides a default ETS profile **default**. This profile can be modified but not deleted. You can create an ETS profile or modify the default ETS profile according to service requirements.
3. (Optional) Create a priority group.
   
   
   ```
   [priority-group](cmdqueryname=priority-group) pg-group-value
   ```
   
   By default, an ETS profile defines three priority groups: PG0, PG1, and PG15.
4. Add the specified interface queues to a priority group.
   
   
   ```
   [priority-group](cmdqueryname=priority-group) pg-group-value queue { start-queue-index [ to end-queue-index ] } &<1-8>
   ```
   
   By default, queues 0, 1, 2, 4, and 5 belong to PG0, queue 3 belongs to PG1, and queues 6 and 7 belong to PG15.
5. Configure flow control based on the priority group.
   
   
   * Set the DRR weight of a priority group.
     
     ```
     [priority-group](cmdqueryname=priority-group) pg-group-value drr weight weight-value
     ```
     
     For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM: The DRR weights of PG0 and PG1 are both 50 by default.
     
     For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855: By default, the scheduling mode of the CIR token bucket based on PG0 and PG1 is PQ, and the scheduling mode of the EIR token bucket based on PG0 and PG1 is DRR with the weight being 50.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     When there are more than three priority groups, multiple priority groups share system resources. When a priority group has the remaining bandwidth, scheduling of the remaining bandwidth may be inaccurate.
     
     For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:
     
     The default scheduling mode of the CIR token bucket based on priority groups is PQ and the rate is not limited by default. The priority groupâbased scheduling mode configured for the CIR token bucket does not take effect. The configured scheduling mode and the default configuration of PG0 and PG1 using DRR scheduling with their respective weight being 50 take effect only for the EIR (EIR = PIR â CIR) token bucket.
   * Enable traffic shaping for a priority group and set shaping parameters.
     
     ```
     [priority-group](cmdqueryname=priority-group) pg-value shaping cir cir-value { kbps | mbps | gbps } pir pir-value { kbps | mbps | gbps } [ cbs cbs-value { kbytes | mbytes} pbs pbs-value { kbytes | mbytes } ]
     ```
     
     By default, traffic shaping is disabled for a priority group.
6. Configure flow control based on the priority.
   
   
   * Set a scheduling mode for interface queues.
     
     ```
     [queue](cmdqueryname=queue) { start-queue-index [ to end-queue-index ] } &<1-8> { pq | lpq | drr  [ weight weight-value ] }
     ```
     
     By default, an interface queue uses PQ for scheduling.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     For the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:
     
     The default scheduling mode of the CIR token bucket based on interface queues is DRR scheduling and the default rate limit is 0. The interface queueâbased scheduling mode configured for the CIR token bucket does not take effect. The configured scheduling mode takes effect only for the EIR (EIR = PIR â CIR) token bucket.
   * Enable traffic shaping for interface queues and set shaping parameters.
     
     ```
     [queue](cmdqueryname=queue) { start-queue-index [ to end-queue-index ] } &<1-8> shaping cir cir-value { kbps | mbps | gbps } pir pir-value { kbps | mbps | gbps } [ cbs cbs-value { kbytes | mbytes } pbs pbs-value { kbytes | mbytes } ]
     ```
     
     By default, traffic shaping is disabled for an interface queue.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```