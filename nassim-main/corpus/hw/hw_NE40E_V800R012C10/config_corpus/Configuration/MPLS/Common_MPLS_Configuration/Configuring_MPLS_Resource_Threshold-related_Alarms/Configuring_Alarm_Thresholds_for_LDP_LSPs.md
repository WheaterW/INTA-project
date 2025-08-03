Configuring Alarm Thresholds for LDP LSPs
=========================================

This section describes how to configure alarm thresholds for Label Distribution Protocol (LDP) label switched paths (LSPs).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls ldp-lsp-number threshold-alarm**](cmdqueryname=mpls+ldp-lsp-number+threshold-alarm+upper-limit+lower-limit) **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value*
   
   
   
   The upper and lower thresholds of alarms for LDP LSP usage are configured.
   
   
   
   The parameters in this command are described as follows:
   
   * *upper-limit-value* specifies the upper threshold of alarms for LDP LSP usage. An alarm is generated when the proportion of established LDP LSPs to total supported LDP LSPs reaches the upper limit.
   * *lower-limit-value* specifies the lower threshold of clear alarms for LDP LSP usage. A clear alarm is generated when the proportion of established LDP LSPs to total supported LDP LSPs falls below the lower limit.
   * The value of *upper-limit-value* must be greater than that of *lower-limit-value*.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * This command configures the alarm threshold for LDP LSP usage. The alarm that the number of LSPs reached the upper threshold is generated only when the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name+mpls_lspm+trap-name) **mpls\_lspm** **trap-name** { **hwmplslspthresholdexceed** } command is configured, and the actual LDP LSP usage reaches the upper limit of the alarm threshold. The alarm that the number of LSPs fell below the lower threshold is generated only when the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name+mpls_lspm+trap-name) **mpls\_lspm** **trap-name** { **hwmplslspthresholdexceedclear** } command is configured, and the actual LDP LSP usage falls below the lower limit of the clear alarm threshold.
   * After the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name+mpls_lspm+trap-name) **mpls\_lspm** **trap-name** { **hwmplslsptotalcountexceed** | **hwmplslsptotalcountexceedclear** } command is run to enable LSP limit-crossing alarm and LSP limit-crossing clear alarm, an alarm is generated in the following situations:
     
     + If the total number of LDP LSPs reaches the upper limit, a limit-crossing alarm is generated.
     + If the total number of LDP LSPs falls below 95% of the upper limit, a limit-crossing clear alarm is generated.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.