(Optional) Configuring Attack Detection Parameters
==================================================

If attack event reports present incorrect or missing decisions on attack events, adjust attack detection parameters to allow attack detection to function precisely.

#### Context

The security Operating Center (SOC) determines whether the system is being attacked based on the statistics analysis. To correctly obtain these statistics on a live network, you must set proper alarm thresholds for security attack events. The traffic models vary with different networkings in different scenarios.

* On small-scale networks where the traffic rate is low, router bandwidth is low, and the number of users is small, setting a low alarm threshold is recommended.
* On large-scale networks where the traffic rate is high, router bandwidth is high, and the number of users is great, setting a high alarm threshold is recommended.

Additionally, you can also adjust the threshold based on the security attack event reports. If false alarms are frequently reported, you can increase the alarm threshold. However, if some security attacks are ignored (the security attacks are detected by other monitoring systems but not reported by the SOC), you can lower the alarm threshold.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**soc**](cmdqueryname=soc)
   
   
   
   The SOC view is displayed.
3. Configure thresholds for determining attack events.
   * Run the [**attack-detect protocol**](cmdqueryname=attack-detect+protocol) *protocol-name* **car** { **min-rate** *rate-value* | **drop-packet-percent** *percentage* } \* command to set the rate threshold for sending protocol packets to the CPU and the packet loss percentage threshold for attack detection.
   * Run the [**attack-detect cpu-usage-threshold**](cmdqueryname=attack-detect+cpu-usage-threshold) *threshold-value* command to set the CPU usage threshold for attack detection.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.