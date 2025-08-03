Configuring Fast Alarm Detection
================================

Configuring Fast Alarm Detection

#### Usage Scenario

In TDM dual feed and selective
receiving scenarios, to enable a local serial interface to rapidly
notify an AC-side device of PW faults, enable fast alarm detection
on the serial interface. The AC-side device can then quickly learn
the fault information and switch to a normal link for data receiving.


#### Pre-configuration Tasks

Before configuring
fast alarm detection on a serial interface, run the [**link-protocol**](cmdqueryname=link-protocol) **tdm** command to enable TDM for the
interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface serial**](cmdqueryname=interface+serial) *interface-number*
   
   
   
   The view of the specified serial interface is displayed.
3. Run [**fast-alarm-detect enable**](cmdqueryname=fast-alarm-detect+enable)
   
   
   
   Fast alarm detection is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.