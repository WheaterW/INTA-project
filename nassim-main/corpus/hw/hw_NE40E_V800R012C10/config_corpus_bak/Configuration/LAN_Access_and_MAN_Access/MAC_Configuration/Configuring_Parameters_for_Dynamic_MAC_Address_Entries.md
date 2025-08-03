Configuring Parameters for Dynamic MAC Address Entries
======================================================

Parameters that can be configured for dynamic MAC address entries include the aging time and MAC address learning limit rule.

#### Usage Scenario

[Table 1](#EN-US_TASK_0172362724__tab_dc_vrp_mac_cfg_000601) shows the usage scenario of the parameters of dynamic MAC address entries.

**Table 1** Parameters for dynamic MAC address entries
| Function | Usage Scenario |
| --- | --- |
| Aging time of dynamic MAC address entries | Dynamic MAC address entries are automatically generated on a device. They are not always valid. The system starts an aging timer for each MAC address entry. If a MAC address entry is not updated until its double aging time expires, the MAC address entry is deleted. If the MAC address entry is updated before the double aging time expires, the aging time will be recalculated. The shorter the aging time is, the more sensitive a device is to network changes.  As network topologies change constantly, a device learns more and more MAC addresses. To avoid the explosive growth of MAC address entries, set a proper aging time for dynamic MAC address entries to have invalid MAC address entries deleted regularly. |
| MAC address learning limit rule | As shown in [Figure 1](#EN-US_TASK_0172362724__fig_dc_vrp_mac_cfg_000601), networks with poor security management, such as community networks, are vulnerable to hackers' MAC address attacks. The capacity of a MAC address table is limited. When hackers forge a large number of packets with different source MAC addresses and send the packets to a device, the MAC address table of the device may be filled to its full capacity. After the MAC address table of the device is filled up, the device cannot learn the source MAC addresses of valid packets it receives.  After a MAC address learning limit rule is configured, the number of access users can be controlled. When the number of learned MAC address entries reaches the maximum number allowed by the system, the system cannot learn any additional MAC addresses. The packet discarding and alarm functions can be configured to prevent MAC address attacks and improve network security. **Figure 1** Networking for configuring a MAC address learning limit rule MAC address learning limit rules can be configured in the following modes:  * Configure a MAC address learning limit rule on an interface to control the number of users connected to the interface. * Configure a MAC address learning limit rule in a VLAN to control the number of users in the VLAN. * Configure a MAC address learning limit rule on an interface in a VLAN to control the number of VLAN users connected to the interface. * Configure a MAC address learning limit rule in a VSI to control the number of users in the VSI. |


#### Pre-configuration Tasks

Before configuring parameters for dynamic MAC address entries, connect interfaces and set their physical parameters to ensure that the interfaces are up.



[Configuring an Aging Time for Dynamic MAC Address Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mac_cfg_0005.html)

Dynamic MAC address entries do not need to be created manually and they will be aged automatically. An aging time can be configured for dynamic MAC address entries to prevent the explosive growth of MAC address entries.

[Configuring a MAC Address Learning Limit Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mac_cfg_0007.html)

Configuring a MAC address learning limit rule can control the number of access users. If the number of learned MAC addresses reaches the maximum number, no additional MAC addresses will be learned. In addition, the packet discarding and alarm functions can be configured to prevent MAC address attacks and improve network security.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mac_cfg_0011.html)

After parameters for dynamic MAC address entries are configured, you can check detailed information about the aging time and the MAC address learning limit rule.