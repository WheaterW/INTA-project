(Optional) Configuring b1tca, b2tca, b3tca, sdbere, and sfbere Alarm Thresholds
===============================================================================

The b1tca, b2tca, b3tca, sdbere, and sfbere alarm thresholds can be configured. An alarm is reported only when the threshold is reached.

#### Context

Perform the following steps on the interface that is connected to the transmission device:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* or [**controller**](cmdqueryname=controller) *interface-type* *interface-number*
   
   
   
   The corresponding interface view is displayed.
3. Run [**transmission-alarm threshold**](cmdqueryname=transmission-alarm+threshold) { **b1tca** *b1tca* | **b2tca** *b2tca* | **b3tca** *b3tca* | **sdbere** *sdbere* | **sfbere** *sfbere* } \*
   
   
   
   The thresholds for reporting the b1tca, b2tca, b3tca, sdbere, and sfbere alarms are configured.
   
   
   
   The alarm thresholds are in the format of 10-n, where **n** is specified in the corresponding alarm parameter in the [**transmission-alarm threshold**](cmdqueryname=transmission-alarm+threshold) command. The value of *sdbere* must not be less than that of *sfbere*.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.