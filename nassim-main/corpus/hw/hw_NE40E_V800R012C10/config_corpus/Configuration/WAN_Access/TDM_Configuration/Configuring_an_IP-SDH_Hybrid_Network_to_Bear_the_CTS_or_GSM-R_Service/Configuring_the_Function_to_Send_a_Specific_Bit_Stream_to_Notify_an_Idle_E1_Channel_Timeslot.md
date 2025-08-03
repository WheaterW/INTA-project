Configuring the Function to Send a Specific Bit Stream to Notify an Idle E1 Channel Timeslot
============================================================================================

Configuring the Function to Send a Specific Bit Stream to Notify an Idle E1 Channel Timeslot

#### Usage Scenario

If the NE40E is connected to an SDH device to bear the GSM-R service, configure the function to send the 0xFF bit stream to notify the SDH device of an idle E1 channel timeslot on a subcard, so that the SDH device can learn network-side PW faults rapidly.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**idle-code-e1**](cmdqueryname=idle-code-e1) *idle-code-value*  [**card**](cmdqueryname=card) *card-id*
   
   
   
   The specified subcard is enabled to send the 0xFF bit stream to notify an idle E1 channel timeslot, so that the subcard can quickly and continuously send AIS bit streams to the AC-side device if network-side PW faults occur.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.