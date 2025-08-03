Configuring Thresholds for the Number of IPv6 Route Prefixes
============================================================

This section describes how to configure thresholds (one alarm threshold and one clear alarm threshold) for the number of IPv6 route prefixes on a device. After the thresholds are configured, an alarm is generated when the number of IPv6 route prefixes on the device exceeds the alarm threshold, and the alarm is cleared when the number of IPv6 route prefixes falls below the clear alarm threshold. Configuring these thresholds facilitates maintenance.

#### Context

The number of IPv6 route prefixes that can be added to a routing table is limited. If the number exceeds the limit, new prefixes cannot be added to the routing table, which may interrupt services. To address this problem, configure an alarm threshold for the number of IPv6 route prefixes.

An alarm is generated when the following conditions are met:

* The number of IPv6 route prefixes on the device exceeds the alarm threshold.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 prefix-limit system threshold-alarm**](cmdqueryname=ipv6+prefix-limit+system+threshold-alarm) **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value*
   
   
   
   Two thresholds (one alarm threshold and one clear alarm threshold) are configured for the number of IPv6 route prefixes on the device.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) When you configure *upper-limit-value* and *lower-limit-value*, note the following suggestions:
   * Set a value less than or equal to 95 for *upper-limit-value*.
   * *lower-limit-value* must be less than *upper-limit-value*. Set *lower-limit-value* to a value at least 10 less than *upper-limit-value* to prevent alarms from being frequently generated and cleared due to route flapping.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.