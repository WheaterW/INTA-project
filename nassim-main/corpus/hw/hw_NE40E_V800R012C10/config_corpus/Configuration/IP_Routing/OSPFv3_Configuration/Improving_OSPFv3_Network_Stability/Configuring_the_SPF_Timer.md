Configuring the SPF Timer
=========================

By setting the interval for Shortest Path First (SPF) calculation, you can reduce resource consumption caused by frequent network changes.

#### Context

Whenever the Link-state Database (LSDB) of OSPFv3 changes, the shortest path should be recalculated. Calculating the shortest path each time the LSDB changes consumes enormous resources and lowers the efficiency of the device. In this case, you can adjust values of *delay-interval* and *hold-interval* to prevent bandwidth exhaustion and route consumption caused by frequent network changes. You can use the **intelligent-timer** parameter to configure the device to perform SPF calculation at an interval (at the millisecond level) based on an intelligent timer. This speeds up network convergence.


#### Procedure

* Configure an SPF normal timer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
     
     
     
     The OSPFv3 view is displayed.
  3. Run [**spf timers**](cmdqueryname=spf+timers) *delay-interval* *hold-interval*
     
     
     
     An SPF normal timer is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an SPF intelligent timer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
     
     
     
     The OSPFv3 view is displayed.
  3. Run [**spf-schedule-interval**](cmdqueryname=spf-schedule-interval) { *delay-interval* *hold-interval* | **intelligent-timer** *max-interval* *start-interval* *hold-interval-1* | **millisecond** *interval2* }
     
     
     
     The SPF intelligent timer is set.
     
     
     
     The interval for SPF calculation based on the intelligent timer is described as follows:
     1. The initial interval for SPF calculation is specified by *start-interval*.
     2. The interval for SPF calculation for the nth (n â¥ 2) time equals *hold-interval* x 2(n â 2).
     3. After the interval specified by *hold-interval* x 2(n â 2) reaches the maximum interval specified by *max-interval*, OSPFv3 keeps using the maximum interval for SPF calculation.
     4. If no flapping occurs during the interval from the end of the last SPF calculation to the start of the next SPF calculation, and the interval exceeds the maximum interval specified by *max-interval*, the intelligent timer exits.
     5. If no flapping occurs in the previous interval but occurs in the current interval, SPF calculation is delayed for a period of *start-interval*. After the SPF calculation is complete, the current interval will be applied when waiting for the next SPF calculation.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The normal SPF timer and intelligent SPF timer are mutually exclusive.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.