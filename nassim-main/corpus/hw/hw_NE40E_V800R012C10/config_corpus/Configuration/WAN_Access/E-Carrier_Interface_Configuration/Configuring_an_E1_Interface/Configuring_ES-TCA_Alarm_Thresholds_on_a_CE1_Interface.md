Configuring ES-TCA Alarm Thresholds on a CE1 Interface
======================================================

If the threshold for triggering an ES-TCA alarm is set
and the number of E1 code errors exceeds the threshold, an alarm will
be generated.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view
   is displayed.
2. Run [**controller e1**](cmdqueryname=controller+e1) *controller-number*
   
   
   
   The view
   of a specific CE1 interface is displayed.
3. Run [**trap-threshold es-tca**](cmdqueryname=trap-threshold+es-tca) **trigger-threshold** *trigger-threshold* **resume-threshold** *resume-threshold*
   
   
   
   The thresholds for
   triggering and clearing an ES-TCA alarm are set.