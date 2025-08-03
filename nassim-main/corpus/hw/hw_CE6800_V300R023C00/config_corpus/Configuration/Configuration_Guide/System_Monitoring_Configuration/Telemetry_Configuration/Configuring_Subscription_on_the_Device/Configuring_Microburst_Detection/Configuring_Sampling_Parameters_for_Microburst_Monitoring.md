Configuring Sampling Parameters for Microburst Monitoring
=========================================================

Configuring Sampling Parameters for Microburst Monitoring

#### Prerequisites

You have created a static subscription for microburst monitoring. For details, see [Configuring Static Subscription](galaxy_telemetry_cfg_0008_c.html).


#### Context

After a static subscription is created for microburst monitoring, you can configure sampling parameters for microburst monitoring.

Sampling parameters for microburst monitoring include the upper and lower buffer thresholds and sampling interval.

* Upper and lower buffer thresholds:
  
  When any of the following conditions is met, the device considers that a microburst occurs and records the microburst information, including the occurrence time and corresponding queue buffer usage.
  
  If the obtained queue buffer usage is higher than the upper buffer threshold or the lower buffer threshold is set to 0, the conditions are as follows:
  + The difference between the obtained queue buffer usage and the last recorded queue buffer usage is greater than 2%.
  + The difference between the microburst occurrence time and the last recorded microburst occurrence time is greater than 1s.
  If the obtained queue buffer usage is between the upper and lower buffer thresholds, the conditions are as follows:
  + The difference between the obtained queue buffer usage and the last recorded queue buffer usage is greater than 2%, and a microburst occurred when the last queue buffer usage is recorded.
  + The difference between the microburst occurrence time and the last recorded microburst occurrence time is greater than 1s.
* Sampling interval:
  
  The sampling interval for microburst monitoring is specified by the *sample-interval* parameter in the [**sensor-group**](cmdqueryname=sensor-group) command.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the lower and upper buffer thresholds.
   1. Enter the interface view.
      
      
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   2. Configure the lower and upper buffer thresholds.
      
      
      ```
      [qos](cmdqueryname=qos) [ queue queue-index ] buffer-monitoring percent low low-percent high high-percent
      ```
      
      By default, the lower buffer threshold is 10% of the queue buffer size and the upper buffer threshold is 90% of the queue buffer size.
   3. Exit the interface view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
3. Configure the sampling interval.
   1. Enter the telemetry view.
      
      
      ```
      [telemetry](cmdqueryname=telemetry) [ openconfig ]
      ```
   2. Enter the view of the created static subscription.
      
      
      ```
      [subscription](cmdqueryname=subscription) subscription-name
      ```
   3. Configure the sampling interval for the associated sampling sensor group.
      
      
      ```
      [sensor-group](cmdqueryname=sensor-group) sensor-name sample-interval sample-interval
      ```
      
      By default, no sampling interval is configured for a sampling sensor group.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```