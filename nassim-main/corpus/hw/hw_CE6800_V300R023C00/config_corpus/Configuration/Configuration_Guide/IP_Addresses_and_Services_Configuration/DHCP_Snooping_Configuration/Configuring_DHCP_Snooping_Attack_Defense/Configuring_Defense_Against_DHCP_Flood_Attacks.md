Configuring Defense Against DHCP Flood Attacks
==============================================

Configuring Defense Against DHCP Flood Attacks

#### Context

On a DHCP network, if a DHCP client sends a large number of DHCP messages to the device within a short time, the device's performance may deteriorate, potentially to the point where the device fails to work normally. To address this issue and effectively prevent DHCP flood attacks, you can enable the device to check the rate of sending DHCP messages to the processing unit. Only the DHCP messages within the specified rate are sent to the processing unit, and those exceeding the specified rate are discarded. If the alarm function has been enabled and the number of discarded DHCP messages reaches a specified alarm threshold, an alarm is generated.

![](../public_sys-resources/note_3.0-en-us.png) 

* When configuring the maximum rate of sending DHCP messages, note:
  + If the configuration is performed in the system view, it takes effect for all interfaces of the device. If the configuration is performed in the interface view, it takes effect only for the specified interface. If the configuration is performed in the VLAN view, it takes effect for all interfaces belonging to the VLAN.
  + If the configuration is performed in the system, VLAN, and interface views, the maximum rate of sending DHCP messages is the smallest value among the three views.
* When configuring the alarm function, note:
  + If the configuration is performed in the system view, it takes effect for all interfaces of the device. If the configuration is performed in the interface view, it takes effect only for the specified interface.
  + If the configuration is performed in the system and interface views, the alarm threshold is the smallest value between the two views.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device to check the rate of sending DHCP messages to the processing unit, and configure the maximum allowable value for this rate.
   
   
   * In the system view, enable the device to check the rate of sending DHCP messages to the processing unit in multiple VLANs, and configure the maximum allowable value for this rate.
     ```
     [dhcp snooping check dhcp-rate](cmdqueryname=dhcp+snooping+check+dhcp-rate) { [enable](cmdqueryname=enable) | rate } [vlan](cmdqueryname=vlan) { vlan-id1 [ [to](cmdqueryname=to) vlan-id2 ] } &<1-10>
     ```
   * Enter the interface view, enable the device to check the rate of sending DHCP messages to the processing unit, and configure the maximum allowable value for this rate.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     portswitch
     [dhcp snooping check dhcp-rate enable](cmdqueryname=dhcp+snooping+check+dhcp-rate+enable)
     [dhcp snooping check dhcp-rate](cmdqueryname=dhcp+snooping+check+dhcp-rate) rate
     [quit](cmdqueryname=quit)
     ```
   * Enter the VLAN view, enable the device to check the rate of sending DHCP messages to the processing unit, and configure the maximum allowable value for this rate.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [dhcp snooping check dhcp-rate enable](cmdqueryname=dhcp+snooping+check+dhcp-rate+enable)
     [dhcp snooping check dhcp-rate](cmdqueryname=dhcp+snooping+check+dhcp-rate) rate
     [quit](cmdqueryname=quit)
     ```
   
   
   
   By default, the maximum allowable rate of sending DHCP messages to the processing unit is 5000 pps.
3. (Optional) Enable the device to report an alarm when the number of discarded DHCP messages reaches a specified alarm threshold.
   
   
   * In the system view, enable the device to report an alarm when the number of discarded DHCP messages reaches a specified alarm threshold.
     ```
     [dhcp snooping alarm dhcp-rate](cmdqueryname=dhcp+snooping+alarm+dhcp-rate) { [enable](cmdqueryname=enable) | threshold threshold } [vlan](cmdqueryname=vlan) { vlan-id1 [ [to](cmdqueryname=to) vlan-id2 ] } &<1-10>
     ```
   * Enter the interface view, and enable the device to report an alarm when the number of discarded DHCP messages reaches a specified alarm threshold.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     portswitch
     [dhcp snooping alarm dhcp-rate enable](cmdqueryname=dhcp+snooping+alarm+dhcp-rate+enable)
     [dhcp snooping alarm dhcp-rate](cmdqueryname=dhcp+snooping+alarm+dhcp-rate) [threshold](cmdqueryname=threshold) threshold
     [quit](cmdqueryname=quit)
     ```
   * Enter the VLAN view, and enable the device to report an alarm when the number of discarded DHCP messages reaches a specified alarm threshold.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [dhcp snooping alarm dhcp-rate enable](cmdqueryname=dhcp+snooping+alarm+dhcp-rate+enable)
     [dhcp snooping alarm dhcp-rate](cmdqueryname=dhcp+snooping+alarm+dhcp-rate) [threshold](cmdqueryname=threshold) threshold
     [quit](cmdqueryname=quit)
     ```
   
   By default, the alarm threshold for discarded DHCP messages is 100.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```