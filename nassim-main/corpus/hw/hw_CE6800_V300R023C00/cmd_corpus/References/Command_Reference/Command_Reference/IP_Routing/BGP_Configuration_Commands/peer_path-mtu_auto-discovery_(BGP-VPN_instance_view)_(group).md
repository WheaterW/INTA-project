peer path-mtu auto-discovery (BGP-VPN instance view) (group)
============================================================

peer path-mtu auto-discovery (BGP-VPN instance view) (group)

Function
--------



The **peer path-mtu auto-discovery** command enables path MTU discovery.

The **undo peer path-mtu auto-discovery** command restores the default configuration.



By default, path MTU discovery is disabled.


Format
------

**peer** *group-name* **path-mtu** **auto-discovery**

**undo peer** *group-name* **path-mtu** **auto-discovery**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When hosts on the same network communicate, the MTU of the network is important to both communication ends. When hosts need to communicate across multiple networks, the smallest MTU on the communication path is most important to both ends. This is because different networks along the communication path have different link-layer MTUs. The minimum MTU on the communication path is called the path MTU.The path MTU has the following characteristics:

* Uncertainty: During communication, the path MTU of hosts depends on the selected path and thus may change.
* Inconsistency: The path MTUs in the inbound and outbound directions may be inconsistent because the path from the sender to the receiver may be different from the path from the receiver to the sender.

**Configuration Impact**

After this command is run, the peer learns the maximum number of bytes of a BGP data message on the transmission path, preventing message fragmentation. In addition, the local device sets the DF bit in the IP header of the message to be sent to the peer to 1.Enabling path MTU auto discovery affects TCP MSS calculation:

* When path MTU auto discovery is disabled:
  1. For the sender, the TCP MSS is calculated using the following formula: MSS = MIN { CFGMSS, MTU-40 }.
  2. For the receiver, if it supports SYN Cookie, the MSS is calculated using the following formula: MSS = MIN { MIN { CFGMSS, MTU-40 } , internally-defined MSS value }. If it does not support SYN Cookie, the MSS is calculated using the following formula: MSS = MIN { CFGMSS, MTU-40 }.
* After path MTU auto discovery is enabled:
  1. The sender updates the local MSS only when it sends a message with the MSS greater than the path MTU. The TCP MSS is calculated using the following formula: MSS = MIN { MIN { CFGMSS, MTU-40 } , PMTU-40 }.
  2. For the receiver, if it supports SYN Cookie, the TCP MSS is calculated using the following formula: MSS = MIN { MIN { MIN { CFGMSS, MTU-40 } , internally-defined MSS value } , PMTU-40 }. If it does not support SYN Cookie, the TCP MSS is calculated using the following formula: MSS = MIN { MIN { CFGMSS, MTU-40 } , PMTU-40 }.

The parameters in the formula are described as follows:

* CFGMSS: "MIN { APPMSS, CLICFGMSS}," where APPMSS indicates the MSS value configured using the **peer tcp-mss** command. CLICFGMSS specifies the maximum MSS value configured using the **tcp max-mss** command.
* MTU-40 indicates the MTU of the interface minus 40.
* PMTU-40 indicates the path MTU minus 40.
* internally-defined MSS value indicates the MSS value, which can be 216, 460, 952, 1400, 2900, 4900, 7900, or 9500. Upon receipt of a message, the receiver uses the MSS value which is smaller than but closest to the MSS of the received message.

**Precautions**

Enabling the path MTU requires extra costs. If the MTU is known during network planning, you do not need to enable the path MTU.


Example
-------

# Configure path MTU discovery for peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group test
[*HUAWEI-bgp-instance-vpn1] peer test path-mtu auto-discovery

```