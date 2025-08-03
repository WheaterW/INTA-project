Configuring Transmission Alarm Filtering Intervals
==================================================

This section describes the usage scenario of transmission alarm filtering intervals, and the pre-configuration tasks and operation procedure for configuring the transmission alarm filtering intervals. If the lifetime (interval between alarm generation and alarm clearance) of an alarm is less than the generation alarm filtering interval, the alarm is filtered out as a burr. Otherwise, the alarm is considered as a normal alarm.

#### Usage Scenario

In the scenario where a router is connected to a transmission device, if the network is unstable, a large number of burr alarms may be generated. As a result, the physical status of interfaces will frequently change between up and down. If a transmission alarm filtering interval is configured, the alarms whose lifetime is shorter than the interval will be ignored.

Transmission alarm filtering intervals can be configured globally or on an interface. The global configuration takes effect on interfaces supporting the function. The relationship is as follows:

* If a transmission alarm filtering interval is configured globally and a non-default transmission alarm filtering interval is configured on an interface, the configuration on the interface preferentially takes effect.
* If no transmission alarm filtering interval is configured in the interface view, the global configuration takes effect.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, global transmission alarm filtering intervals are supported only by the admin VS.



#### Pre-configuration Tasks

Before configuring transmission alarm filtering intervals, complete the following tasks:

* Power on the Router and ensure that the Router passes the self-check.
* Configure transmission alarm customization on the Router's interface connected to the transmission device by referring to [Configuring Transmission Alarm Customization](dc_ne_transalarm_cfg_0004.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The alarm filtering function on an interface takes effect only after transmission alarm customization is configured on the interface.



#### Procedure

* Enable the global alarm filtering function and set global generation and clearance alarm filtering intervals.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**transmission-alarm holdoff-timer**](cmdqueryname=transmission-alarm+holdoff-timer) *holdoff-time*
     
     
     
     Generation alarm filtering is enabled globally, and an interval for filtering generation alarms is configured globally.
  3. Run [**transmission-alarm holdup-timer**](cmdqueryname=transmission-alarm+holdup-timer) *holdup-time*
     
     
     
     Clearance alarm filtering is enabled globally, and an interval for filtering clearance alarms is configured globally.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the alarm filtering function on an interface and set generation and clearance alarm filtering intervals for the interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run the following commands as required:
     
     
     + To enter the POS or 10GE WAN interface view, run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command.
     + To enter the CPOS interface view, run the [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number* command.
     + To enter the WDM interface view, run the [**controller wdm**](cmdqueryname=controller+wdm) *controller-number* command.
     + To enter the E1 interface view, run the [**controller e1**](cmdqueryname=controller+e1) *controller-number* command.
     + To enter the E3 interface view, run the [**controller e3**](cmdqueryname=controller+e3) *controller-number* command.
  3. Run [**transmission-alarm holdup-timer**](cmdqueryname=transmission-alarm+holdup-timer) [ *holdup-time* ]
     
     
     
     The clearance alarm filtering function is configured on the interface, and a clearance alarm filtering interval is set for the interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display transmission-alarm**](cmdqueryname=display+transmission-alarm) command to check the interface configuration.