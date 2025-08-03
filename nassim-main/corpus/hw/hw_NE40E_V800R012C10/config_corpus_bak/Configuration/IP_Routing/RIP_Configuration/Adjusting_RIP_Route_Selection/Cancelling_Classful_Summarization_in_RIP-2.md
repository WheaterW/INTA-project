Cancelling Classful Summarization in RIP-2
==========================================

On a network where subnets are incontiguous, you can cancel classful summarization in RIP-2 to obtain routing information that is more accurate.

#### Context

Although IP address summarization reduces the routing table size, it shields the routing information of subnets. As a result, routing information may be incorrectly calculated.

On a network where subnets are incontiguous, classful summarization needs to be disabled in RIP-2. On the network shown in [Figure 1](#EN-US_TASK_0172365842__fig_dc_vrp_rip_cfg_002401), classful summarization needs to be disabled on the interfaces of DeviceA and DeviceC.

Because classful summarization is enabled in RIP-2 by default, both DeviceB and DeviceC send a route 10.0.0.0/8 to DeviceA. DeviceA cannot differentiate 10.1.0.0/16, 10.2.0.0/16, 10.4.0.0/16, and 10.5.0.0/16 from each other. As a result, routing information is incorrect.

**Figure 1** Cancelling classful summarization in RIP-2  
![](images/fig_dc_vrp_rip_cfg_002401.png)  


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**rip**](cmdqueryname=rip) [ *process-id*] command to create a RIP process and enter the RIP view.
3. Run the [**undo summary**](cmdqueryname=undo+summary) command to cancel classful summarization in RIP-2.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.