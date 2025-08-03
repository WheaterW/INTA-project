authentication trigger-condition (802.1X access profile view)
=============================================================

authentication trigger-condition (802.1X access profile view)

Function
--------



The **authentication trigger-condition** command configures the packet types that can trigger 802.1X authentication.

The **undo authentication trigger-condition** command restores the default configuration.



By default, DHCP, ARP, DHCPv6, and ND packets can trigger 802.1X authentication.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication trigger-condition** { **dhcp** | **arp** | **dhcpv6** | **nd** | **any-l2-packet** } \*

**undo authentication trigger-condition** [ **dhcp** | **arp** | **dhcpv6** | **nd** | **any-l2-packet** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dhcp** | Triggers 802.1X authentication through DHCP packets. | - |
| **arp** | Triggers 802.1X authentication through ARP packets. | - |
| **dhcpv6** | Triggers 802.1X authentication through DHCPv6 packets. | - |
| **nd** | Triggers 802.1X authentication through ND packets. | - |
| **any-l2-packet** | Triggers 802.1X authentication through any packet. For multicast packets, the corresponding protocol must be enabled. Otherwise, 802.1X authentication cannot be triggered. | If this parameter is configured but other optional parameters are not configured, DHCP, ARP, DHCPv6, and ND packets cannot trigger 802.1X authentication. |



Views
-----

802.1X access profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After 802.1X authentication is enabled, the device can trigger 802.1X authentication for users by default when receiving DHCP, DHCPv6, ND, or ARP packets. The administrator can adjust the packet types that can trigger 802.1X authentication based on user information on the actual network. For example, if all users on the network dynamically obtain IPv4 addresses, you can configure the device to trigger 802.1X authentication only through DHCP packets. This prevents unauthorized users from continuously sending ARP packets to trigger 802.1X authentication after static IPv4 addresses are configured for the users.

**Precautions**

* This function takes effect only for users who go online after the configuration is successful.
* To allow BPDUs to trigger 802.1X authentication, you must enable the corresponding function globally. For example, to allow LLDPDUs to trigger 802.1X authentication, run the lldp enable (system view) command to enable LLDP globally.
* When any-l2-packet is configured and 802.1X authentication is enabled on an interface, EAP packets sent from a client trigger 802.1X authentication first.


Example
-------

# In the 802.1X access profile d1, configure the device to trigger 802.1X authentication through DHCP packets.
```
<HUAWEI> system-view
[~HUAWEI] dot1x-access-profile name d1
[*HUAWEI-dot1x-access-profile-d1] authentication trigger-condition dhcp

```