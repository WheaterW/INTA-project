Configuring Automatic Tunnel Bandwidth Adjustment
=================================================

This section describes how to configure the automatic adjustment of the tunnel bandwidth.

#### Usage Scenario

Automatic bandwidth adjustment can be enabled to adjust the bandwidth of the tunnel automatically.

The system periodically collects the traffic rate on the outbound interface of a TE tunnel and obtains multiple sampled traffic rates within a certain period. The average value of the sampled values within this period is used as the bandwidth constraint to request the establishment of a new LSP. After the new LSP is established, traffic is switched to the new one. With make-before-break enabled, the old LSP is torn down after the new LSP is established.

The sampling interval is configured in the MPLS view and takes effect for all MPLS TE tunnels. The rate of the outbound interface on an MPLS TE tunnel is recorded at each sampling interval. In this manner, the actual average bandwidth sampled within a period of time can be obtained.

After automatic bandwidth adjustment is enabled, the [**mpls te timer auto-bandwidth**](cmdqueryname=mpls+te+timer+auto-bandwidth) command can be run to configure periodic sampling in order to obtain the bandwidth of the tunnel in a sampling interval. After multiple times of sampling within an automatic bandwidth adjustment period, the average bandwidth is calculated as the new bandwidth, and a new LSP is established based on the new bandwidth. If a new LSP is successfully established, traffic is switched to it, and the original LSP is torn down. If a new LSP fails to be established, traffic is still transmitted along the original LSP. The bandwidth is adjusted in the next automatic bandwidth adjustment period.


#### Pre-configuration Tasks

Before configuring the bandwidth automatic adjustment, [configure an RSVP-TE tunnel](dc_vrp_te-p2p_cfg_0003.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te timer auto-bandwidth**](cmdqueryname=mpls+te+timer+auto-bandwidth) [ *interval* ]
   
   
   
   The sampling interval for automatic bandwidth adjustment is configured. The larger value between the **mpls te timer auto-bandwidth** command setting and the **set flow-stat interval** command setting is used as the actual sampling interval for automatic bandwidth adjustment.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The **set flow-stat interval** command can be run in both the system view and tunnel interface view. If the command is not run in the tunnel interface view, the configuration in the system view is used. If no *interval* value is specified, the default interval is used.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   The tunnel interface view of the MPLS TE tunnel is displayed.
6. Run [**statistic enable**](cmdqueryname=statistic+enable)
   
   
   
   MPLS TE tunnel statistics can be collected.
7. To configure automatic bandwidth adjustment, run one of the following commands.
   
   
   * Run the [**mpls te auto-bandwidth**](cmdqueryname=mpls+te+auto-bandwidth) **adjustment** { [ **threshold** *percent* [ [ **or** ] **absolute-bw** *absolute-bw* ] ] | **frequency** *interval* | [ **max-bw** *max-bandwidth* | **min-bw** *min-bandwidth* ] \* | [ **overflow-limit** *overflow-limit-value* ] | [ **underflow-limit** *underflow-limit-value* ]  } \* command to enable automatic bandwidth adjustment and configure the interval at which automatic bandwidth adjustment is performed and the allowed bandwidth adjustment range.
     
     The following policies can be configured to control automatic bandwidth adjustment:
     
     + **frequency** *interval* sets the interval for bandwidth adjustment. After the [**mpls te auto-bandwidth**](cmdqueryname=mpls+te+auto-bandwidth) command is run, a device must sample bandwidth values for at least twice within a configured interval. If the device samples bandwidth values for less than twice within the specified interval, automatic bandwidth adjustment is not performed. The existing sampling times are counted in the next bandwidth adjustment interval.
     + You can run the **threshold** *percent*  [  [ **or** ] **absolute-bw** *absolute-bw* ] command to determine whether or not to adjust bandwidth.
       
       The system compares the average bandwidth calculated within the automatic bandwidth adjustment period with the actual bandwidth. The bandwidth will be automatically adjusted if the ratio of bandwidth change to the actual bandwidth is greater than the **threshold** value. If the absolute threshold is also set, the bandwidth will be automatically adjusted if the bandwidth change value is greater than the absolute threshold value.
       
       Therefore, if the network traffic changes frequently but frequent bandwidth adjustment is not needed, you can set a greater **threshold** value.
       
       If the **or** parameter is configured, the system performs a bitwise OR operation between the absolute bandwidth threshold and the threshold percentage for bandwidth adjustment. That is, if either the absolute bandwidth threshold or the threshold percentage meets the traffic adjustment condition, automatic bandwidth adjustment is triggered. If **or** is not configured, the bitwise AND operation is performed by default, so that automatic bandwidth adjustment can only be triggered after both the absolute bandwidth threshold and threshold percentage are reached.
     + Automatic bandwidth adjustment is performed if conditions are met in either of the following situations:
       - 1. If the **overflow-limit** *overflow-limit-value* and **underflow-limit** *underflow-limit-value* parameters are not specified and the interval for automatic bandwidth adjustment expires, bandwidth is automatically adjusted when the average bandwidth exceeds the upper or lower bandwidth adjustment threshold.
       - 2. If **overflow-limit** *overflow-limit-value* and **underflow-limit** *underflow-limit-value* are specified, the device checks whether the average bandwidth exceeds the upper or lower bandwidth adjustment threshold at an interval specified by **mpls te timer auto-bandwidth**. If the average bandwidth exceeds the upper or lower bandwidth adjustment threshold for n consecutive times (n is the value specified by **overflow-limit** *overflow-limit-value* or **underflow-limit** *underflow-limit-value*), the device automatically adjusts bandwidth without waiting for the timer to reach the interval for automatic bandwidth adjustment.The default **overflow-limit** *overflow-limit-value* and **underflow-limit** *underflow-limit-value* parameter values do not take effect. By default, after the configured interval expires, the device automatically adjusts bandwidth values if the average bandwidth exceeds the upper bandwidth adjustment threshold or falls below the lower bandwidth adjustment threshold.
   * Run the [**mpls te auto-bandwidth**](cmdqueryname=mpls+te+auto-bandwidth) **collect-bw** { [ **frequency** *interval* ] | [ **max-bw** *max-bandwidth* | **min-bw** *min-bandwidth* ] \*} \* command to configure the interval at which the bandwidth of the outbound interface is collected and the bandwidth range.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After completing the configuration, run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command on the ingress of the tunnel to check the tunnel configuration:

* Automatically adjusted bandwidth (Auto BW)
* Automatically adjusted frequency (Auto BW Freq)
* Minimum bandwidth that can be adjusted (Min BW)
* Maximum bandwidth that can be adjusted (Max BW)
* Current bandwidth that is collected (Current Collected BW)