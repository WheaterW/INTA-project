Configuring Transmission Alarm Suppression
==========================================

This section describes the usage scenario, pre-configuration tasks, and configuration procedure for transmission alarm suppression. If a transmission alarm suppression threshold is configured, an alarm is reported only when the threshold is reached.

#### Usage Scenario

In the scenario where a router is connected to a transmission device, if the network is unstable, a large number of burr alarms may be generated. As a result, the physical status of interfaces will frequently change between up and down. To prevent these alarms from frequently flapping or configure the device to ignore these burr alarms, you need to enable transmission alarm suppression.


#### Pre-configuration Tasks

Before configuring transmission alarm suppression, complete the following tasks:

* Power on the Router and ensure that the Router passes the self-check.
* Configure transmission alarm customization on the Router's interface connected to the transmission device by referring to [Configuring Transmission Alarm Customization](dc_ne_transalarm_cfg_0004.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Transmission alarm suppression takes effect on an interface only after transmission alarm customization is configured on the interface.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run the following commands as required:
   1. To enter the POS or 10GE WAN interface view, run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command.
   2. To enter the CPOS interface view, run the [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number* command.
   3. To enter the WDM interface view, run the [**controller**](cmdqueryname=controller) *wdm* *interface-number* command.
   4. To enter the E1 interface view, run the [**controller**](cmdqueryname=controller) **e1** *controller-number* command.
   5. To enter the E3 interface view, run the [**controller**](cmdqueryname=controller) **e3** *controller-number* command.
3. Run [**transmission-alarm damping**](cmdqueryname=transmission-alarm+damping) [ **ceiling** *ceiling* | **reuse** *reuse* | **suppress** *suppress* | **decay-ok** *decay-ok* | **decay-ng** *decay-ng* ] \*
   
   
   
   Transmission alarm suppression is enabled, and suppression parameters are set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring transmission alarm suppression, verify the configuration.

Run the [**display transmission-alarm configuration**](cmdqueryname=display+transmission-alarm+configuration) command to check the transmission alarm configuration on an interface.