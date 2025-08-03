Setting the Interval for the SPF Calculation
============================================

By setting the interval for the SPF calculation, you can save resources consumed by frequent network changes.

#### Context

When the OSPF LSDB changes, the shortest path needs to be recalculated. If a network changes frequently, the shortest path is calculated accordingly, which consumes a large number of system resources degrades system performance. By configuring an intelligent timer and a proper interval for the SPF calculation, you can prevent excessive system memory and bandwidth resources from being occupied.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**spf-schedule-interval**](cmdqueryname=spf-schedule-interval) { *interval1* | **intelligent-timer** *max-interval* *start-interval* *hold-interval* [ **conservative** ] | **millisecond** *interval2* }
   
   
   
   The interval for SPF calculation is set.
   
   
   
   The interval for SPF calculation based on the intelligent timer is described as follows:
   1. The initial interval for SPF calculation is specified by *start-interval*.
   2. The interval for SPF calculation for the nth (n â¥ 2) time equals *hold-interval* x 2(n â 2).
   3. After the interval specified by *hold-interval* x 2(n â 2) reaches the maximum interval specified by *max-interval*, OSPF keeps using the maximum interval for SPF calculation.
   4. If no flapping occurs during the interval from the end of the last SPF calculation to the start of the next SPF calculation, and the interval exceeds the maximum interval specified by *max-interval*, the intelligent timer exits.
   5. If no flapping occurs in the previous interval but occurs in the current interval, SPF calculation is delayed for a period of *start-interval*. After the SPF calculation is complete, the current interval will be applied when waiting for the next SPF calculation.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.