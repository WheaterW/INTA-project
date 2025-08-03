Configuring Alarm Thresholds for Dynamic Labels
===============================================

This section describes how to set the dynamic label thresholds for triggering an alarm. If the number of dynamic labels that the system uses reaches a specific threshold, the system generates an alarm, which facilitates operation and maintenance.

#### Context

If dynamic labels run out but the system receives new dynamic label requests, the system fails to satisfy the requests because the dynamic labels are insufficient. The module that fails to be assigned labels works abnormally. The modules that apply for labels include MPLS TE, MPLS LDP, BGP, L3VPN and L2VPN.

To help facilitate operation and maintenance, you can set dynamic label thresholds for triggering alarms to alert users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls dynamic-label-number threshold-alarm**](cmdqueryname=mpls+dynamic-label-number+threshold-alarm+upper-limit) **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value*
   
   
   
   The thresholds for triggering dynamic label alarms are set.
   
   You can set the following parameters:
   
   * *upper-limit-value*: a percent indicating the upper limit of dynamic labels. If dynamic label usage reaches the upper limit, an alarm is generated. An upper limit less than or equal to 95% is recommended.
   * *lower-limit-value*: a percent indicating the lower limit of dynamic labels. If dynamic label usage falls below the lower limit, an alarm is generated.
   * The *upper-limit-value* must be greater than the *lower-limit-value*.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Each command only configures the trigger conditions for an alarm and its clear alarm. Although trigger conditions are met, the alarm and its clear alarm can be generated only after the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name+mpls_lspm+trap-name) **mpls\_lspm** **trap-name** { **hwMplsDynamicLabelThresholdExceed** | **hwMplsDynamicLabelThresholdExceedClear** } command is run to enable the device to generate a dynamic label insufficiency alarm and its clear alarm.
   * After the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name+mpls_lspm+trap-name) **mpls\_lspm** **trap-name** { **hwMplsDynamicLabelTotalCountExceed** | **hwMplsDynamicLabelTotalCountExceedClear** } command is run to enable the device to generate limit-reaching alarms and their clear alarms, the following situations occur:
     
     + If the number of dynamic labels reaches the maximum number of dynamic labels supported by a device, a limit-reaching alarm is generated.
     + If the number of dynamic labels falls below 95% of the maximum number of dynamic labels supported by the device, a clear alarm is generated.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.