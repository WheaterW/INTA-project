Setting Alarm Thresholds for the Number of IPv6 Route Prefixes Supported by a Device
====================================================================================

Setting Alarm Thresholds for the Number of IPv6 Route Prefixes Supported by a Device

#### Context

The number of IPv6 route prefixes that can be added to a routing table is limited on a device. If the number of added IPv6 route prefixes exceeds a specified limit, new prefixes cannot be added to the routing table, which may interrupt services. To help address this problem, set an alarm threshold for the proportion of added IPv6 route prefixes to all IPv6 route prefixes allowed on a device.

After an alarm threshold is configured for IPv6 route prefixes, an alarm is generated only when the following condition is met:

* The alarm function is enabled using the [**snmp-agent trap enable feature-name rm**](cmdqueryname=snmp-agent+trap+enable+feature-name+rm) command.
* The proportion of added IPv6 route prefixes to all IPv6 route prefixes allowed on a device exceeds the alarm threshold.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set two alarm thresholds (one alarm threshold and one clear alarm threshold) for the proportion of added IPv6 route prefixes to all IPv6 route prefixes allowed on a device.
   
   
   ```
   [ipv6 prefix-limit system threshold-alarm](cmdqueryname=ipv6+prefix-limit+system+threshold-alarm) upper-limit upper-limit-value lower-limit lower-limit-value
   ```
   
   
   
   By default, the alarm threshold is 80%, and the clear alarm threshold is 70%.
   
   ![](public_sys-resources/note_3.0-en-us.png) When setting *upper-limit-value* and *lower-limit-value*, consider the following recommendations:
   * Set a value less than or equal to 95 for *upper-limit-value*.
   * *lower-limit-value* must be less than *upper-limit-value*. Set *lower-limit-value* less than *upper-limit-value* at least by 10 to prevent alarms from being frequently generated and cleared due to route flapping.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```