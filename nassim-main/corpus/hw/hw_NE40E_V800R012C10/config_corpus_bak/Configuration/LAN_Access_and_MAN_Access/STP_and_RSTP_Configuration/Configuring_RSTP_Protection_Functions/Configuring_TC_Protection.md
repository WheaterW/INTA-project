Configuring TC Protection
=========================

After Topology Change (TC) protection is enabled, you can set the number of times for a device to process TC Bridge Protocol Data Units (BPDUs) within a specified time. TC protection avoids frequent deletion of MAC address entries and ARP entries, thereby protecting devices.

#### Context

An attacker may send pseudo TC BPDUs to attack devices. Devices receive a large number of TC BPDUs in a short time and delete entries frequently, which burdens system processing and degrades network stability.

TC protection is used to suppress TC BPDUs. The number of times that TC BPDUs are processed by a device within a specified time is configurable. If the number of TC BPDUs that the device receives within a specified time exceeds the specified threshold, the device handles TC BPDUs only for the specified number of times. Excess TC-BPDUs are processed by the device as a whole for once after the specified time period expires. This protects the device from frequently deleting MAC entries and ARP entries, therefore avoiding overburden.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**stp tc-protection**](cmdqueryname=stp+tc-protection)
   
   
   
   TC protection is enabled for a device.
3. Run either or both of the following commands to configure TC protection parameters.
   
   
   * To set the time for a device to process the maximum number of TC BPDUs, run the [**stp tc-protection interval**](cmdqueryname=stp+tc-protection+interval) *interval-value* command.
   * To set the maximum number of TC BPDUs that a device processes within a specified period, run the [**stp tc-protection threshold**](cmdqueryname=stp+tc-protection+threshold) *threshold* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * There are two TC protection parameters: time needed to process the maximum number of TC BPDUs and the maximum number of TC BPDUs processed within a specified period. For example, if the time is set to 10 seconds and the maximum number is set to 5, when a device receives TC BPDUs, the device processes only the first 5 TC BPDUs within 10 seconds and processes the other TC BPDUs after the time expires.
   * The device processes only the maximum number of TC BPDUs specified in the [**stp tc-protection threshold**](cmdqueryname=stp+tc-protection+threshold) command within the time specified in the [**stp tc-protection interval**](cmdqueryname=stp+tc-protection+interval) command. The processing of other TC BPDUs is delayed, which may slow down spanning tree convergence.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.