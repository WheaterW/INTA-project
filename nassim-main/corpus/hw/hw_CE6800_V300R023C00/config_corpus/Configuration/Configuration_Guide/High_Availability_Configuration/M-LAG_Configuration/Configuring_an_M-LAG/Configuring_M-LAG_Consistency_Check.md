Configuring M-LAG Consistency Check
===================================

Configuring M-LAG Consistency Check

#### 

#### Context

An M-LAG is composed of two devices that are virtualized into one device (a Layer 2 logical node), making the logical topology clear and requiring that certain configurations on the two devices must be consistent. If certain requirements are not satisfied, the M-LAG may fail to work or a loop may occur. In addition, manually configuring each of the two M-LAG member devices and comparing configuration inconsistencies is both time-consuming and error-prone.

To address this issue, M-LAG configuration consistency check is introduced to request the configuration of each module on the two devices. Based on the comparison result after an M-LAG configuration consistency check is complete, you can adjust the configurations of the devices to prevent problems such as network loops or data loss.

The M-LAG configuration falls into two types: key configuration (Type 1) and common configuration (Type 2), as described in [Table 1](#EN-US_TASK_0000001512849230__table176123353596). There are two M-LAG configuration consistency check modes available: strict and loose.

1. Key configuration (Type 1): If the configurations of the two M-LAG member devices are inconsistent, certain problems can occur, such as loops and long-period packet loss, even if the M-LAG status is normal. If the key configurations on the M-LAG member devices are inconsistent, the following apply:
   * In strict mode, the M-LAG member interface on the M-LAG backup device will enter the error-down state and an alarm that indicates key configuration inconsistencies will be generated.
   * In loose mode, an alarm that indicates key and common configuration inconsistencies will be generated.
2. Common configuration (Type 2): If the configurations of the two M-LAG member devices are inconsistent, the M-LAG status may be abnormal; however, this problem, compared to that of the key configuration, has less impact on the live network.
   
   Regardless of the chosen mode, if any common configuration inconsistencies are detected between the M-LAG member devices, an alarm that indicates key and common configuration inconsistencies will be generated.

In addition, you can enable or disable M-LAG configuration consistency check based on modules for Type 2 configurations. If M-LAG configuration consistency check is enabled but you do not want to perform consistency check on some Type 2 configurations, you can add the configurations of a specified module to the M-LAG consistency check whitelist. Consistency check will not be performed on the configurations in the whitelist.

![](../public_sys-resources/note_3.0-en-us.png) 

* Interfaces in error-down state cannot send or receive packets and their indicators are off. You can run the [**display error-down recovery**](cmdqueryname=display+error-down+recovery) command to view information about all interfaces in error-down state.
* If the M-LAG member interface on the M-LAG backup device enters the error-down state, you are advised to adjust the configuration of the M-LAG master and backup devices to make their configurations consistent, rather than manually restoring the interface to up or running the [**error-down auto-recovery**](cmdqueryname=error-down+auto-recovery) **cause** **m-lag** **interval** *interval-value* command in the system view to enable the interface to automatically go up. Otherwise, faults, such as excess service packets, packet loss, and service interruption, may occur. Exercise caution when performing this operation.
* If M-LAG consistency check in strict mode is configured and type 1 configuration inconsistencies are detected between the M-LAG master and backup devices, you are advised to adjust the configurations immediately, instead of restarting the devices. If you restart the M-LAG master device directly, the M-LAG member interface on the M-LAG backup device may enter the error-down state due to detected type 1 configuration inconsistencies when the two devices re-negotiate with each other. Due to the delay after which the M-LAG member interface on the M-LAG master device goes up, both the M-LAG master and backup devices fail to forward traffic, leading to service interruptions.
* If M-LAG configuration consistency check is disabled and configurations of M-LAG master and backup devices are inconsistent, traffic forwarding may be abnormal. In this case, you need to manually adjust the configurations of the M-LAG master and backup devices to make their configurations consistent and enable M-LAG configuration consistency check on them.

**Table 1** M-LAG configuration consistency check list
| View | Configuration | Type |
| --- | --- | --- |
| System view | Whether STP is enabled | Type 1 |
| Whether V-STP is enabled |
| STP working mode |
| Whether BPDU protection is enabled |
| Mappings between MSTIs and VLANs  NOTE:  By default, the device checks the mappings between MSTIs and VLANs only in process 0. |
| Whether VBST is enabled in a VLAN |
| M-LAG member interface view | M-LAG active/standby mode configuration |
| Whether STP is enabled |
| Whether root protection is enabled on an STP port |
| LACP mode of the M-LAG member interface |
| M-LAG LACP system priority and system ID |
| STP edge port |
| Peer-link interface view | Whether STP is enabled |
| LACP mode of the peer-link interface |
| System view | Type of packets for electing M-LAG master and backup member interfaces | Type2 |
| VLAN |
| Static MAC address entries:  * Static MAC address entries where the outbound interface is an M-LAG member interface * Static MAC address entry for a VXLAN tunnel   NOTE:  If the outbound interface in a static MAC address entry is a Layer 2 sub-interface on an M-LAG member interface, the device cannot check the static MAC address entry. |
| Aging time of dynamic MAC address entries |
| Static ARP entries:  * Short static ARP entries * Long static ARP entries   + If outbound interfaces are specified in static ARP entries, only the static ARP entries with the outbound interface being an M-LAG member interface are checked.   + If only VLANs are specified in static ARP entries, the VLAN IDs are compared.   + If both outbound interfaces and VLANs are specified in static ARP entries, only the entries with the outbound interface being an M-LAG member interface and the VLAN ID in the entries are compared.   + Static ARP entry for an IPv4 VXLAN tunnel   NOTE:  M-LAG member devices cannot check short static ARP entries with a specified VPN instance. If the outbound interface of a long static ARP entry is an M-LAG member interface and is bound to a VPN instance or the VLANIF interface corresponding to the VLAN to which the outbound interface belongs is bound to a VPN instance, the device cannot check the static ARP entry. |
| Aging time of dynamic ARP entries |
| Bridge domain (BD) configuration  * BD ID * VNI associated with the BD * Mapping VNI associated with the BD |
| VBDIF interface configuration  * BD ID * IPv4 address * M-LAG IPv4 address * IPv6 address * M-LAG IPv6 address * M-LAG link-local address * MAC address * Status   NOTE:  By default, only the virtual MAC addresses of VBDIF interfaces are checked.  The IPv6 configuration consistency check only takes effect when a VBDIF interface is up. If the VBDIF interface is down, the preceding configurations do not take effect on the interface.  When the VBDIF interface status changes, IPv6 address configuration inconsistency occurs. After services become stable, the configuration consistency check result is correct. |
| VLANIF interface configuration  * VLAN ID * IPv4 address * M-LAG IPv4 address * IPv6 address * M-LAG IPv6 address * M-LAG link-local address * VRRP4 group * MAC address * Status * Aging time of dynamic ARP entries   NOTE:  By default, only the virtual MAC addresses of VLANIF interfaces are checked.  For the IPv6 address configuration, the consistency check only takes effect when a VLANIF interface is up. If the VLANIF interface is down, the preceding configurations do not take effect on the interface.  When the VLANIF interface status changes, IPv6 address configuration inconsistency occurs. After services become stable, the configuration consistency check result is correct.  If a VRRP4 or VRRP6 IP address is configured on the VLANIF interface of the local M-LAG device, the system does not check whether the interface IP addresses are consistent or whether the virtual MAC addresses are consistent. |
| M-LAG member interface view | Port priority in a spanning tree protocol |
| VLAN ID |
| Other settings |
| Number of member interfaces in the Eth-Trunk interface which is configured as an M-LAG member interface NOTE:  Only the numbers of member interfaces in Eth-Trunk interfaces are compared. The physical up/down status or bandwidth of member interfaces is not checked. |
| Peer-link interface view | VLAN from which packets are not allowed to pass through the peer-link interface |


![](../public_sys-resources/note_3.0-en-us.png) 

An M-LAG consistency check fails if the M-LAG IPv4 addresses, M-LAG IPv6 addresses, and M-LAG link-local addresses of the M-LAG master and backup devices are the same, or if other configurations on the two devices are different.

For the CE6885-LL (low latency mode): VXLAN and IPv6-related configurations are not supported.




#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a DFS group and enter its view.
   
   
   ```
   [dfs-group](cmdqueryname=dfs-group) dfs-group-id
   ```
3. Enable M-LAG configuration consistency check, and specify a check mode.
   
   
   ```
   [consistency-check](cmdqueryname=consistency-check) enable mode { strict | loose }
   ```
   
   By default, M-LAG configuration consistency check is disabled.
4. (Optional) Configure the M-LAG consistency check whitelist for a specified module (supported only for Type 2 configurations).
   
   
   * Configure the M-LAG consistency check whitelist for the ARP module.
     ```
     [consistency-check whitelist module arp service-type](cmdqueryname=consistency-check+whitelist+module+arp+service-type) { arp-aging-time | static-arp } *
     ```
     
     By default, the M-LAG consistency check whitelist is not configured for the ARP module.
   * Configure the M-LAG consistency check whitelist for the M-LAG module.
     ```
     [consistency-check whitelist module m-lag service-type](cmdqueryname=consistency-check+whitelist+module+m-lag+service-type) { m-lag-member-num | m-lag-id | peer-link-exclude-vlan | m-lag-ipv4-address | m-lag-ipv6-address | m-lag-election-mode } *
     ```
     
     By default, the M-LAG consistency check whitelist is not configured for the M-LAG module.
     
     For the CE6885-LL (low latency mode): The **m-lag-ipv6-address** parameter cannot be configured.
   * Configure the M-LAG consistency check whitelist for the MAC module.
     ```
     [consistency-check whitelist module mac service-type](cmdqueryname=consistency-check+whitelist+module+mac+service-type) { mac-aging-time | static-mac } *
     ```
     
     By default, the M-LAG consistency check whitelist is not configured for the MAC module.
   * Configure the M-LAG consistency check whitelist for the STP module.
     ```
     [consistency-check whitelist module stp service-type](cmdqueryname=consistency-check+whitelist+module+stp+service-type) stp-m-lag-priority
     ```
     
     By default, the M-LAG consistency check whitelist is not configured for the STP module.
   * Configure the M-LAG consistency check whitelist for the VLAN module.
     ```
     [consistency-check whitelist module vlan service-type](cmdqueryname=consistency-check+whitelist+module+vlan+service-type) { vlan-configuration | port-vlan-relation } *
     ```
     
     By default, the M-LAG consistency check whitelist is not configured for the VLAN module.
   * Configure the M-LAG consistency check whitelist for the VLANIF module.
     ```
     [consistency-check whitelist module vlanif service-type](cmdqueryname=consistency-check+whitelist+module+vlanif+service-type) { vlanif-configuration | ipv4-address | ipv6-address | vrrp4 | virtual-mac | vlanif-status | vlanif-bypass | arp-timeout } *
     ```
     
     By default, the M-LAG consistency check whitelist is not configured for the VLANIF module.
     
     For the CE6820H, CE6820H-K, and CE6820S: The **vlanif-bypass** parameter cannot be configured.
     
     For the CE6885-LL (low latency mode): The **vlanif-bypass** and **ipv6-address** parameters cannot be configured.
   * Configure the M-LAG consistency check whitelist for the VXLAN module. (For the CE6820H, CE6820H-K, and CE6820S and CE6885-LL (low latency mode): This function is not supported.)
     ```
     [consistency-check whitelist module vxlan service-type](cmdqueryname=consistency-check+whitelist+module+vxlan+service-type) { bd-configuration | vbdif-configuration | ipv4-address | ipv6-address | virtual-mac | vbdif-status } *
     ```
     
     By default, the M-LAG consistency check whitelist is not configured for the VXLAN module.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The whitelist takes effect only on the local M-LAG device. When configuring the M-LAG consistency check whitelist, you are advised to configure the same whitelist on both devices in the M-LAG. Otherwise, the M-LAG device that is not configured with the whitelist still perform consistency check.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```