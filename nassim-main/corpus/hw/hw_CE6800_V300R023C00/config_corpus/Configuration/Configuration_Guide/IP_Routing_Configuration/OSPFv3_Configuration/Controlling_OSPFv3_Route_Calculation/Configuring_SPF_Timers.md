Configuring SPF Timers
======================

Configuring SPF Timers

#### Prerequisites

Before configuring SPF timers, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

When the OSPFv3 LSDB changes, the shortest path needs to be recalculated. If the shortest path is calculated immediately after the LSDB changes each time, a large number of resources are consumed, and the device efficiency is adversely affected. Modifying the values of SPF timers can prevent exhaustion of bandwidth and routing resources caused by frequent network changes. You can adjust the interval (in milliseconds) for SPF calculation by modifying the parameters of the intelligent timer. Such adjustment can affect network convergence.


#### Procedure

* Configure a normal SPF timer.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the OSPFv3 view.
     
     
     ```
     [ospfv3](cmdqueryname=ospfv3) [ process-id ]
     ```
  3. Configure a normal SPF timer.
     
     
     ```
     [spf timers](cmdqueryname=spf+timers) delay-interval hold-interval
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure an intelligent SPF timer.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the OSPFv3 view.
     
     
     ```
     [ospfv3](cmdqueryname=ospfv3) [ process-id ]
     ```
  3. Configure an intelligent SPF timer.
     
     
     ```
     [spf-schedule-interval](cmdqueryname=spf-schedule-interval) { delay-interval hold-interval | intelligent-timer max-interval start-interval hold-interval-1 | millisecond interval2 }
     ```
     
     The default values of *delay-interval*, *hold-interval*, *max-interval*, *start-interval*, and *hold-interval-1* are 5s, 10s, 5s, 50 ms, and 200 ms, respectively.
     
     If the intelligent timer is enabled using **intelligent-timer**, the interval for SPF calculation is as follows:
     1. The initial interval for SPF calculation is specified by *start-interval*.
     2. The interval for SPF calculation for the nth (n â¥ 2) time equals *hold-interval-1* x 2(n â 2).
     3. After the interval specified by *hold-interval-1* x 2(n â 2) reaches the maximum interval specified by *max-interval*, OSPFv3 keeps using the maximum interval for SPF calculation.
     4. If no flapping occurs during the interval from the end of the last SPF calculation to the start of the next SPF calculation, and the interval exceeds the maximum interval specified by *max-interval*, the intelligent timer exits.
     5. If no flapping occurs in the previous interval but occurs in the current interval, SPF calculation is delayed for a period of *start-interval*. After the SPF calculation is complete, the current interval will be applied when waiting for the next SPF calculation.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     The normal SPF timer and intelligent SPF timer are mutually exclusive.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] command to check brief OSPFv3 information. The **SPF Intelligent Timer** field in the command output indicates the intelligent timer values used for SPF calculation.