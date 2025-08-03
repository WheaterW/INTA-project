Configuring Alarm Thresholds for other TE Resource
==================================================

Conditions that trigger TE resource threshold-reaching alarms can be configured. If the number of auto bypass tunnel interfaces, or the number of auto primary tunnels reaches the upper alarm threshold, the device can report an alarm, which facilitates operation and maintenance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run one or more of the following commands:
   * Run [**mpls autobypass-tunnel-number threshold-alarm**](cmdqueryname=mpls+autobypass-tunnel-number+threshold-alarm+upper-limit) **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value*
     
     The upper and lower alarm thresholds for the number of auto bypass tunnel interfaces are configured.
   * Run [**mpls autoprimary-tunnel-number threshold-alarm**](cmdqueryname=mpls+autoprimary-tunnel-number+threshold-alarm+upper-limit) **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value*
     
     The upper and lower alarm thresholds for the number of auto primary tunnels are configured.
   
   
   
   Note the following issues when configuring trigger conditions:
   
   * *upper-limit-value*: upper alarm threshold for the proportion of used TE resources to all TE resources supported by a device.
   * *lower-limit-value*: lower alarm threshold for the proportion of used TE resources to all TE resources supported by a device.
   * The upper alarm threshold must be greater than the lower alarm threshold.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Each command only configures the trigger conditions for an alarm and its clear alarm. Although trigger conditions are met, the alarm and its clear alarm can be generated only after the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name+mpls_lspm+trap-name) **mpls\_lspm** **trap-name** { **hwmplsresourcethresholdexceed** | **hwmplsresourcethresholdexceedclear** } command is run to enable the device to generate an MPLS resource insufficiency alarm and its clear alarm.
   * After the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name+mpls_lspm+trap-name) **mpls\_lspm** **trap-name** { **hwmplsresourcetotalcountexceed** | **hwmplsresourcetotalcountexceedclear** } command is run to enable the device to generate limit-reaching alarms and their clear alarms, the following situations occur:
     
     + If the number of used TE resources reaches the maximum number of TE resources supported by a device, a limit-reaching alarm is generated.
     + If the number of used TE resources falls below 95% of the maximum number of TE resources supported by a device, a clear alarm is generated.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.