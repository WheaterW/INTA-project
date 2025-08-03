Configuring Conditions That Trigger LDP Resource Threshold-Reaching Alarms
==========================================================================

Conditions that trigger LDP resource threshold-reaching alarms can be configured. If the number of remote LDP adjacencies or the number of outsegment entries reaches a specified upper alarm threshold, the device can report an alarm to an NMS.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run one or more of the following commands:
   * Run [**mpls remote-adjacency-number threshold-alarm**](cmdqueryname=mpls+remote-adjacency-number+threshold-alarm+upper-limit) **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value*
     
     The upper and lower alarm thresholds for the number of remote LDP adjacencies are configured.
   * Run [**mpls outsegment-number threshold-alarm**](cmdqueryname=mpls+outsegment-number+threshold-alarm+upper-limit+lower-limit) **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value*
     
     The upper and lower alarm thresholds for the number of outsegment entries are configured.
   * Run [**mpls mldp-tree-number threshold-alarm**](cmdqueryname=mpls+mldp-tree-number+threshold-alarm+upper-limit+lower-limit) **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value*
     
     The upper and lower alarm thresholds for the number of mLDP LSPs are configured.
     
     Configure conditions that trigger threshold-reaching alarms and the corresponding clear alarms for other LDP resources.
   * Run [**mpls mldp-branch-number threshold-alarm**](cmdqueryname=mpls+mldp-branch-number+threshold-alarm+upper-limit+lower-limit) **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value*
     
     The upper and lower alarm thresholds for the number of mLDP sub-LSPs are configured.
   
   
   
   Configure the following parameters in the preceding command:
   
   * *upper-limit-value*: specifies the upper alarm threshold of the proportion of used LDP resources to all LDP resources supported by a device.
   * *lower-limit-value*: specifies the lower alarm threshold for the proportion of used LDP resources to all LDP resources supported by a device.
   * *upper-limit-value* must be greater than *lower-limit-value*.
   
   By default, the upper threshold for alarms is 80% and the lower threshold for clear alarms is 75%.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Each command only configures the trigger conditions for an alarm and its clear alarm. Although trigger conditions are met, the alarm and its clear alarm can be generated only after the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name+mpls_lspm+trap-name) **mpls\_lspm** **trap-name** { **hwmplsresourcethresholdexceed** | **hwmplsresourcethresholdexceedclear** } command is run to enable the device to generate an LDP resource insufficiency alarm and its clear alarm.
   * After the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name+mpls_lspm+trap-name) **mpls\_lspm** **trap-name** { **hwmplsresourcetotalcountexceed** | **hwmplsresourcetotalcountexceedclear** } command is run to enable the device to generate an LDP resource insufficiency alarm and its clear alarm, note the following issues:
     
     + If the number of used LDP resources reaches the maximum number of LDP resources supported by a device, a maximum number-reaching alarm is generated.
     + If the number of used LDP resources falls to 95% or below of the maximum number of LDP resources supported by a device, a clear alarm is generated.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.