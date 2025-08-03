(Optional) Configuring a Limit on the Number of PIM-SM Entries
==============================================================

IPv6 PIM-SM allows you to limit the number of (S, G) and (\*, G) entries separately. After a specified limit is reached, new entries of the corresponding type cannot be created.

#### Context

Limit the number of PIM-SM entries to prevent a device from generating excessive multicast routing entries when attackers send numerous multicast data or MLD/PIM protocol messages. Therefore, this function helps prevent high memory and CPU usage and improve multicast service security.


#### Procedure

* In a public network scenario, configure a limit on the number of PIM-SM entries and alarm thresholds.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run 
     
     
     
     A limit on the maximum number of PIM-SM entries and alarm thresholds are configured.
     
     **star-group-number** indicates that the configuration takes effect for (\*, G) entries. **source-group-number** indicates that the configuration takes effect for (S, G) entries. After the command is run:
     
     
     
     + After the specified limit is reached, new entries cannot be created, and the alarm PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.23 routeExceed is generated.
     + If **threshold-alarm upper-limit** *upper-limit-value* is set, the alarm PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.21 routeThresholdExceed is generated when the percentage ratio of created PIM-SM entries to the specified limit reaches *upper-limit-value*.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After the specified limit is reached, new (\*, G) and (S, G) entries can be manually added, and ASM share-group entries for Rosen MVPN can be created.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* In a VPN instance, configure a limit on the number of PIM-SM entries and alarm thresholds.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
     
     
     
     The VPN instance IPv6 address family view is displayed.
  4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     An RD is configured for the VPN instance's IPv6 address family.
  5. Run [**multicast ipv6 routing-enable**](cmdqueryname=multicast+ipv6+routing-enable)
     
     
     
     IPv6 multicast routing is enabled.
  6. Run [**multicast ipv6 limit pim sm**](cmdqueryname=multicast+ipv6+limit+pim+sm) { **star-group-number** | **source-group-number** } *limit-count* [ **threshold-alarm upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value* ]
     
     
     
     A limit on the number of PIM-SM entries and alarm thresholds are set. **star-group-number** indicates that the configuration takes effect for (\*, G) entries. **source-group-number** indicates that the configuration takes effect for (S, G) entries. After the command is run:
     
     
     
     + If the number of PIM-SM entries in the IPv6 address family of a VPN instance reaches a configured limit, new entries fail to be created and the alarm PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.32 hwPimVrfTypeSGExceed is triggered.
     + If **upper-limit** *upper-limit-value* is specified and the number of PIM-SM entries in the IPv6 address family of a VPN instance reaches the configured alarm trigger threshold, the alarm PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.30 hwPimVrfTypeSGThresholdExceed is triggered.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Manually created (\*, G) and (S, G) entries are not affected by a limit on the maximum number of PIM-SM entries in the IPv6 address family of a VPN instance. The limit takes effect only on dynamic (\*, G) and (S, G) entries.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.