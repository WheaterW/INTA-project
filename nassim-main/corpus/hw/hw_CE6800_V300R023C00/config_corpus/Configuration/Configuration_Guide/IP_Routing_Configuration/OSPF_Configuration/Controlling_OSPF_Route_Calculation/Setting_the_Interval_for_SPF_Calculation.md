Setting the Interval for SPF Calculation
========================================

Setting the Interval for SPF Calculation

#### Prerequisites

Before setting the interval for SPF calculation, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

When the OSPF LSDB changes, the shortest path needs to be recalculated. If a network changes frequently, the shortest path is calculated accordingly, resulting in excessive consumption of system resources, affecting device efficiency. Using the intelligent timer to set a proper interval for SPF calculation prevents excessive consumption of device memory and bandwidth resources.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
   
   The *process-id* parameter specifies the ID of a process, and the default value is 1.
3. Set the interval for SPF calculation.
   
   
   ```
   [spf-schedule-interval](cmdqueryname=spf-schedule-interval) { interval1 | intelligent-timer max-interval start-interval hold-interval [ conservative ] | millisecond interval2 }
   ```
   If the intelligent timer is enabled using **intelligent-timer**, the interval for SPF calculation is as follows:
   1. The initial interval for SPF calculation is specified by *start-interval*.
   2. The interval for SPF calculation for the nth (n â¥ 2) time equals *hold-interval* x 2(n â 2).
   3. After the interval specified by *hold-interval* x 2(n â 2) reaches the maximum interval specified by *max-interval*, OSPF keeps using the maximum interval for SPF calculation.
   4. If no flapping occurs during the interval from the end of the last SPF calculation to the start of the next SPF calculation, and the interval exceeds the maximum interval specified by *max-interval*, the intelligent timer exits.
   5. If no flapping occurs in the previous interval but occurs in the current interval, SPF calculation is delayed for a period of *start-interval*. After the SPF calculation is complete, the current interval will be applied when waiting for the next SPF calculation.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **brief** command to check brief OSPF information. The **Spf-schedule-interval** field in the command output indicates the interval for SPF calculation.