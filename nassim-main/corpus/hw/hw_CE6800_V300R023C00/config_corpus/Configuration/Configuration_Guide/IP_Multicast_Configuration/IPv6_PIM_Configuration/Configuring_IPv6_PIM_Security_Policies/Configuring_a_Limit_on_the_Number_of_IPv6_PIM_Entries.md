Configuring a Limit on the Number of IPv6 PIM Entries
=====================================================

Configuring a Limit on the Number of IPv6 PIM Entries

#### Context

If a large number of multicast routing entries are generated due to attacks on multicast data or MLD/IPv6 PIM messages, the memory or CPU usage of the device will be high. To prevent this problem, configure a limit on the number of IPv6 PIM entries (for IPv6 PIM-SM, the number of (S, G) and (\*, G) entries can be limited). If the number of entries exceeds the limit, no more entries can be created. In this way, multicast services can run properly.


#### Procedure

* In a public network scenario, configure a limit on the number of IPv6 PIM entries and alarm thresholds.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a limit on the number of IPv6 PIM entries and alarm thresholds.
     
     
     ```
     [multicast ipv6 global limit](cmdqueryname=multicast+ipv6+global+limit) pim sm { star-group-number | source-group-number } limit-count6 [ threshold-alarm upper-limit upper-limit-value lower-limit lower-limit-value ] 
     ```
     
     **star-group-number** indicates the limit on the number of (\*, G) entries. **source-group-number** indicates the limit on the number of (S, G) entries. After the command is run:
     
     
     
     + If the specified limit is reached, new entries cannot be created, and the alarm (routeExceed) is generated.
     + If an alarm threshold is set using the **threshold-alarm upper-limit** *upper-limit-value* command, the alarm (routeThresholdExceed) is generated when the number of entries reaches the alarm threshold.
     
     However, static (\*, G) and (S, G) entries are not limited by the configuration.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* In a VPN instance, configure a limit on the number of PIM entries and alarm thresholds.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VPN instance view.
     
     
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
  3. Enter the VPN instance IPv6 address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family)
     ```
  4. Configure an RD for the VPN instance IPv6 address family.
     
     
     ```
     [route-distinguisher](cmdqueryname=route-distinguisher) route-distinguisher
     ```
  5. Enable IPv6 multicast routing.
     
     
     ```
     [multicast ipv6 routing-enable](cmdqueryname=multicast+ipv6+routing-enable)
     ```
  6. Configure a limit on the number of IPv6 PIM entries and alarm thresholds.
     
     
     ```
     [multicast ipv6 limit pim sm](cmdqueryname=multicast+ipv6+limit+pim+sm) { star-group-number | source-group-number } limit-count [ threshold-alarm upper-limit upper-limit-value lower-limit lower-limit-value ]
     ```
     
     
     
     **star-group-number** indicates the limit on the number of (\*, G) entries. **source-group-number** indicates the limit on the number of (S, G) entries. After the command is run:
     
     
     
     + If the number of PIM entries in the VPN instance IPv6 address family reaches the configured limit, new entries fail to be created, and the alarm PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.32 hwPimVrfTypeSGExceed is triggered for the VPN instance IPv6 address family.
     + If **upper-limit** *upper-limit-value* is specified and the number of entries in the VPN instance IPv6 address family reaches the configured alarm threshold, the alarm PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.30 hwPimVrfTypeSGThresholdExceed is triggered.
     
     The entry limit in the VPN instance IPv6 address family does not take effect on static (\*, G) or (S, G) entries but takes effect only on dynamic entries.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```