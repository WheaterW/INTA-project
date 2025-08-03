Configuring the Functions to Send Alarm Information on the Device Connected to an SNCP-Enabled SDH Device
=========================================================================================================

Configuring_the_Functions_to_Send_Alarm_Information_on_the_Device_Connected_to_an_SNCP-Enabled_SDH_Device

#### Usage Scenario

If the NE40E is connected to an SDH device to carry GSM-R services, perform the following configurations to enable the NE40E to convert PW-side faults into SDH channel-specific TU-AIS alarms and convert these alarms into LBit.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
   
   
   
   The view of a specific CPOS interface is displayed.
3. Run [**sdh-alarm uni-tuais ces-underrun enable**](cmdqueryname=sdh-alarm+uni-tuais+ces-underrun+enable)
   
   
   
   The CPOS interface is enabled to send TU-AIS bit streams to an AC-side device when the CES service is interrupted on the interface.
4. Run [**sdh-alarm nni-ais lrdi enable**](cmdqueryname=sdh-alarm+nni-ais+lrdi+enable)
   
   
   
   The CPOS interface is enabled to send AIS bit streams to a network-side device when an LRDI alarm is detected on the interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.