Configuring the Threshold Alarm Function for the Number of OSPFv3 Neighbors
===========================================================================

If the alarm function is configured for the number of OSPFv3 neighbors and the number of OSPFv3 neighbors exceeds the threshold, an alarm is generated.

#### Context

When the number of established OSPFv3 neighbor relationships exceeds the specifications of the device, establishing more OSPFv3 neighbor relationships may cause the neighbor status to be unstable. To prevent this problem, you can enable the alarm function for the number of OSPFv3 neighbor relationships so that an alarm is generated when the number of OSPFv3 neighbor relationships exceeds the upper alarm threshold.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3 peer alarm-threshold**](cmdqueryname=ospfv3+peer+alarm-threshold) *threshold-value* **upper-limit** *upper-value* **lower-limit** *lower-value*
   
   
   
   The threshold alarm function is configured for the number of OSPFv3 neighbors.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.