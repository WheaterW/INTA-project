Configuring Alarm Thresholds for RSVP LSPs
==========================================

This section describes how to configure alarm thresholds for RSVP LSPs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls rsvp-lsp-number threshold-alarm**](cmdqueryname=mpls+rsvp-lsp-number+threshold-alarm+upper-limit+lower-limit) **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value*
   
   
   
   The upper and lower thresholds of alarms for RSVP LSP usage are configured.
   
   
   
   The parameters in this command are described as follows:
   
   * *upper-limit-value* specifies the upper threshold of alarms for RSVP LSP usage. An alarm is generated when the proportion of established RSVP LSPs to total supported RSVP LSPs reaches the upper limit.
   * *lower-limit-value* specifies the lower threshold of clear alarms for RSVP LSP usage. A clear alarm is generated when the proportion of established RSVP LSPs to total supported RSVP LSPs falls below the lower limit.
   * The value of *upper-limit-value* must be greater than that of *lower-limit-value*.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.