Configuring Alarm Thresholds for the Number of PCE-Initiated SRv6 TE Policies
=============================================================================

You can configure upper and lower thresholds for the number of PCE-initiated SRv6 TE Policies, enabling a PCE client to generate alarms when the number of received PCE-initiated SRv6 TE Policies reaches the thresholds. This facilitates O&M.

#### Context

If the number of PCE-initiated LSPs in the system reaches a specified limit, new LSPs may fail to be established due to insufficient resources. To facilitate O&M, enable the device to generate an alarm when the number of PCE-initiated LSPs reaches the limit.

* If the percentage of PCE-initiated LSPs reaches the upper threshold, a threshold alarm is generated.
* If the percentage of PCE-initiated LSPs falls below the lower threshold, the threshold alarm is cleared.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The PCE client view is displayed.
3. Run [**pcep pce-initiated lsp-number threshold-alarm**](cmdqueryname=pcep+pce-initiated+lsp-number+threshold-alarm) **upper-limit** *upper-limit-value***lower-limit** *lower-limit-value*
   
   
   
   The upper and lower thresholds for the number of PCE-initiated SRv6 TE Policies are configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.