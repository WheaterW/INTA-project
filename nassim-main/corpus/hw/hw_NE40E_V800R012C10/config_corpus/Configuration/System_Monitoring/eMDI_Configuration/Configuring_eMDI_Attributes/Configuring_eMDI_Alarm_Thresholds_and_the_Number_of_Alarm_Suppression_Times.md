Configuring eMDI Alarm Thresholds and the Number of Alarm Suppression Times
===========================================================================

This section describes how to configure alarm thresholds and the number of alarm suppression times when the frequency of reporting eMDI alarms needs to be changed.

#### Context

In addition to monitoring various indicators of video streams, the eMDI detection solution allows reporting of alarms to NMS. eMDI alarm triggering is determined by an alarm threshold and the number of alarm suppression times. If the alarm threshold is M and the number of alarm suppression times is N, when an indicator reaches M for N consecutive times, the device reports an eMDI alarm to the NMS. Therefore, to control the frequency at which eMDI alarms are reported, configure a proper alarm threshold and alarm suppression times.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If statistics are all below the threshold within 60 consecutive detection intervals, the alarm is automatically cleared.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**emdi**](cmdqueryname=emdi)
   
   
   
   The eMDI view is displayed.
3. Run [**emdi alarm**](cmdqueryname=emdi+alarm) { **rtp-lr** | **rtp-ser** } { **sd** | **hd** | **4k** } [**threshold**](cmdqueryname=threshold) *threshold-value*
   
   
   
   An alarm threshold for eMDI detection is configured.
4. Run [**emdi alarm suppress times**](cmdqueryname=emdi+alarm+suppress+times) *value*
   
   
   
   The number of eMDI alarm suppression times is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.