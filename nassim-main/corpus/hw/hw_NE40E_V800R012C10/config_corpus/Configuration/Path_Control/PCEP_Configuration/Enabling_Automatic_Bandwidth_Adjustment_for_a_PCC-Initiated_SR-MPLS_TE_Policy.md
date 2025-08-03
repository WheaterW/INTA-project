Enabling Automatic Bandwidth Adjustment for a PCC-Initiated SR-MPLS TE Policy
=============================================================================

You can enable automatic bandwidth adjustment for a PCC-initiated SR-MPLS TE Policy in order to better respond to service requirement changes.

#### Context

After configuring automatic bandwidth adjustment for a PCC-initiated SR-MPLS TE Policy, you can perform sampling at fixed interval A (for example, 5 minutes) to obtain the maximum bandwidth of the traffic forwarded over the SR-MPLS TE Policy within the automatic bandwidth adjustment period B (for example, 24 hours). According to the requested bandwidth sent to the controller based on the sampling value, the controller re-computes an SR-MPLS TE Policy path and then delivers the new path.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The device is configured as a PCE client, and the PCE client view is displayed.
3. Run [**capability auto-bandwidth**](cmdqueryname=capability+auto-bandwidth)
   
   
   
   The PCE client is enabled to support automatic bandwidth adjustment.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**segment-routing**](cmdqueryname=segment-routing)
   
   
   
   Segment Routing is enabled globally, and the Segment Routing view is displayed.
6. Run [**sr-te-policy auto-bandwidth adjustment enable**](cmdqueryname=sr-te-policy+auto-bandwidth+adjustment+enable)
   
   
   
   Automatic bandwidth adjustment is enabled for SR-MPLS TE Policies.
7. Run [**sr-te-policy auto-bandwidth sample interval**](cmdqueryname=sr-te-policy+auto-bandwidth+sample+interval)[ *sample-interval-value* ]
   
   
   
   The automatic bandwidth adjustment function is enabled to sample the outbound traffic rate of SR-MPLS TE Policies, and a global sampling interval is specified.
8. Run [**sr-te policy**](cmdqueryname=sr-te+policy) *policy-name*[ **endpoint** *ipv4-address* **color** *color-value* ]
   
   
   
   The SR-MPLS TE Policy view is displayed.
9. Run [**auto-bandwidth adjustment**](cmdqueryname=auto-bandwidth+adjustment)
   
   
   
   The automatic bandwidth adjustment function is enabled for the PCC-Initiate SR-MPLS TE Policy, and the SR-MPLS TE Policy automatic bandwidth adjustment view is displayed.
   
   
   
   1. Run the [**adjustment threshold**](cmdqueryname=adjustment+threshold){ **absolute-bw***absolute-bw-value* | **percent** *percent-value* [ **minimum-bw** *minimum-bw-value* ]}\* [ **downadjustment** { **down-absolute-bw** *down-absolute-bw-value* | **down-percent** *down-percent-value* [ **down-minimum-bw** *down-minimum-bw-value* ]}\* ] command to configure periodic bandwidth adjustment parameters for the SR-MPLS TE Policy.
   2. Run the [**bandwidth**](cmdqueryname=bandwidth){ **minimum** *min-bandwidth-value* | **maximum** *max-bandwidth-value* } \* command to configure the upper and lower bandwidth limits for automatic bandwidth adjustment of the SR-MPLS TE Policy.
      
      
      
      This command configures the maximum and minimum bandwidth that can be reserved for automatic bandwidth adjustment. When the maximum traffic rate is not within the bandwidth range configured using this command (that is, when the maximum traffic rate is lower than the configured minimum bandwidth or higher than the configured maximum bandwidth), bandwidth is requested based on the configured minimum and maximum bandwidth.
   3. Run the [**overflow-limit**](cmdqueryname=overflow-limit){ **absolute-bw** *absolute-bw-value***count** *count-value* | **percent** *percent-value***count** *percent-count-value* [ **minimum-bw** *minimum-bw-value* ] } \* command to configure thresholds for automatic upward bandwidth adjustment of the SR-MPLS TE Policy.
      
      
      
      Perform this step to implement fast automatic bandwidth adjustment. If the difference between the continuously sampled value and the reserved bandwidth is greater than or equal to a specified fast adjustment threshold, the system adjusts the bandwidth to the sampled maximum traffic rate immediately, without waiting for the automatic upward bandwidth adjustment interval to be reached. This command sets the minimum threshold for fast automatic bandwidth adjustment, absolute upward adjustment threshold, relative upward adjustment threshold, and overflow count. This command can be used together with the command that sets the periodic bandwidth adjustment threshold. After either fast bandwidth adjustment or periodic bandwidth adjustment is triggered, all bandwidth statistics are cleared, bandwidth statistic collection is restarted, and automatic bandwidth adjustment is restarted.
   4. Run the [**underflow-limit**](cmdqueryname=underflow-limit){ **absolute-bw** *absolute-bw-value***count** *count-value* | **percent***percent-value***count** *percent-count-value* [ **minimum-bw** *minimum-bw-value* ] } \* command to configure thresholds for automatic downward bandwidth adjustment of the SR-MPLS TE Policy.
      
      
      
      Perform this step to implement fast automatic downward bandwidth adjustment. If the difference between the continuously sampled value and the reserved bandwidth is greater than or equal to a specified fast adjustment threshold, the system adjusts the bandwidth to the sampled maximum traffic rate immediately, without waiting for the automatic downward bandwidth adjustment interval to be reached. This command sets the minimum threshold for fast downward automatic bandwidth adjustment, absolute downward adjustment threshold, relative downward adjustment threshold, and overflow count. If this command is not run, the thresholds for fast upward bandwidth adjustment are used. This command can be used together with the command that sets the periodic bandwidth adjustment threshold. After either fast bandwidth adjustment or periodic bandwidth adjustment is triggered, all bandwidth statistics are cleared, bandwidth statistic collection is restarted, and automatic bandwidth adjustment is restarted.
10. (Optional) Run [**adjustment interval**](cmdqueryname=adjustment+interval)*adjustment-interval-value* [ **down** **adjustment** **interval** *down-adjustment-interval-value* ]
    
    
    
    An automatic bandwidth adjustment interval is configured for the SR-MPLS TE Policy.
    
    
    
    By default, the automatic bandwidth adjustment interval is 86400 seconds (1 day).
    
    If the global bandwidth sampling interval configured using the [**sr-te-policy auto-bandwidth sample interval**](cmdqueryname=sr-te-policy+auto-bandwidth+sample+interval) command is longer than the automatic bandwidth adjustment interval configured using this command, automatic bandwidth adjustment does not take effect.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

After configuring automatic bandwidth adjustment for the PCC-initiated SR-MPLS TE Policy, verify the configuration.

* Run the [**display sr-te policy auto-bandwidth adjustment**](cmdqueryname=display+sr-te+policy+auto-bandwidth+adjustment) [ **policy-name** *policy-name*| **endpoint** *ipv4-address* **color** *color-value* | **binding-sid** *sid-value* ] command to check detailed information about automatic bandwidth adjustment of the SR-MPLS TE Policy.
* Run the [**display pce protocol session**](cmdqueryname=display+pce+protocol+session)**verbose** command to check the congestion status of PCEPv4 automatic bandwidth adjustment and the remaining time of involved timers.