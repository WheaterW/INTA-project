Configuring Alarm and Clear Alarm Thresholds for IP FPM Performance Counters
============================================================================

After you configure the alarm threshold and its clear alarm threshold for packet loss or delay, the device generates an alarm when the packet loss rate or delay reaches the alarm threshold and clears the alarm when the packet loss rate or delay falls below the clear alarm threshold. The alarm functions help network operation and maintenance.

#### Context

If the packet loss rate or delay on a network is detected high but left unattended, the packet loss rate or delay may increase and potentially affect user experience. To help network operation and maintenance, configure the alarm threshold and its clear alarm threshold for packet loss or delay.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa ipfpm mcp**](cmdqueryname=nqa+ipfpm+mcp)
   
   
   
   The IPFPM-MCP view is displayed.
3. Run [**instance**](cmdqueryname=instance) *instance-id*
   
   
   
   The IP FPM instance view is displayed.
4. Run [**loss-measure ratio-threshold**](cmdqueryname=loss-measure+ratio-threshold) **upper-limit** *upper-limit* **lower-limit** *lower-limit*
   
   
   
   The packet loss alarm threshold and its clear alarm threshold are configured.
5. Run either of the following commands to configure the delay alarm threshold and its clear alarm threshold.
   
   
   * When the target flow is unidirectional, run the [**delay-measure one-way delay-threshold**](cmdqueryname=delay-measure+one-way+delay-threshold) **upper-limit** *upper-limit* **lower-limit** *lower-limit* command to configure the one-way delay alarm threshold and its clear alarm threshold.
   * When the target flow is bidirectional, run the [**delay-measure two-way delay-threshold**](cmdqueryname=delay-measure+two-way+delay-threshold) **upper-limit** *upper-limit* **lower-limit** *lower-limit* command to configure the two-way delay alarm threshold and its clear alarm threshold.