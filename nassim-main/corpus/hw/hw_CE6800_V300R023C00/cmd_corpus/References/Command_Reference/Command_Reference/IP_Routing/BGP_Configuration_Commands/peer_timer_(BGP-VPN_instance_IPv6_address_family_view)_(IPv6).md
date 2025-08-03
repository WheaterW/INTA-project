peer timer (BGP-VPN instance IPv6 address family view) (IPv6)
=============================================================

peer timer (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer timer** command sets the Keepalive time and hold time for a peer.

The **undo peer timer** command restores the default Keepalive time and hold time.



By default, the keepalive time is 60s, the hold time is 180s, and the session hold time is 86400s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **timer** **keepalive** *keepalive-time* **hold** *hold-time*

**peer** *ipv6-address* **timer** **keepalive** *keepalive-time* **hold** *hold-time* **min-holdtime** *min-hold-value*

**peer** *ipv6-address* **timer** **send-hold** *send-hold-time*

**undo peer** *ipv6-address* **timer** **keepalive** **hold** [ **min-holdtime** ]

**undo peer** *ipv6-address* **timer** **keepalive** *keepalive-time* **hold** *hold-time*

**undo peer** *ipv6-address* **timer** **keepalive** *keepalive-time* **hold** *hold-time* **min-holdtime** *min-hold-value*

**undo peer** *ipv6-address* **timer** **send-hold** *send-hold-time*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies an IPv6 peer address. | The format is X:X:X:X:X:X:X:X. |
| **keepalive** *keepalive-time* | Specifies the Keepalive time. | The value is an integer ranging from 0 to 21845, in seconds. The default value is 60 seconds. |
| **hold** *hold-time* | Indicates the hold time. | The value is 0 or an integer ranging from 3 to 65535, in seconds. The default value is 180.  It is recommended that the configured hold time be related to the total number of BGP address family peers. For details, see the mapping between the total number of BGP peers in each address family and the recommended minimum hold time in the usage guide of the peer timer command. |
| **min-holdtime** *min-hold-value* | Specifies the minimum hold time. On the same device, min-hold-value must be less than or equal to hold-time. | The value is an integer ranging from 20 to 65535, in seconds. |
| **send-hold** *send-hold-time* | Specifies the interval for holding a session when the local end fails to send messages. | The value is 0 or an integer ranging from 360 to 172800, in seconds. The default value is 86400. The value 0 indicates that the function is disabled. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After establishing a BGP connection, two peers periodically send Keepalive messages to each other to detect the status of the BGP connection. If a device receives no Keepalive message or any other type of message from its peer within the specified hold time, the device considers the BGP connection interrupted and closes the BGP connection.In addition, if the device fails to send BGP Update and Keepalive messages within twice the hold time, an alarm is reported. If the alarm is not cleared within the specified send hold time, the BGP connection is reset.

The keepalive-time and hold-time values are determined through negotiation between peers. The smaller value of hold-time contained in Open messages of both peers is used as the final value of hold-time. The smaller value of one third of hold-time and the locally configured keepalive-time is used as the final value of keepalive-time.You can run this command to set the Keepalive time and hold time of BGP.

* If short keepalive time and hold time are set, BGP can detect a link fault quickly. This speeds up link switchover, but increases the number of keepalive messages on the network and loads of devices, and consumes more network bandwidth resources.
* If long keepalive time and hold time are set, the number of keepalive messages on the network and loads of devices are reduced, and fewer network bandwidths are consumed. However, if the keepalive time is too long, BGP is unable to detect link status changes in time. This may cause a large amount of traffic loss.If the hold time configured on a remote device is less than the min-hold-value configured on the local device, no peer relationship can be established between the two devices. If the hold time configured on the local end is 0s, the rule does not take effect, and a peer relationship can still be established.

Mapping between the total number of peers in each BGP address family and the recommended minimum hold-time:

| Total Number of Peers | Recommended Minimum hold-time |
| --- | --- |
| 0â100 | 20 |
| 101â200 | 30 |
| 201â300 | 45 |
| 301â400 | 60 |
| 401â500 | 75 |
| Greater than or equal to 501 | 90 |

**Configuration Impact**



If the value of a timer changes, the BGP peer relationship between devices is disconnected. This is because the devices need to re-negotiate keepalive-time and hold-time. Therefore, exercise caution before changing the value of a timer.



**Precautions**

In actual configuration, the hold time must be at least three times the Keepalive time.Avoid the following situations when setting the values for the timers:

* Both keepalive-time and hold-time are set to 0. In this case, BGP timers become invalid. That is, BGP does not detect link faults based on the timers, which may cause heavy traffic loss.
* The value of hold-time is much greater than the value of keepalive-time, for example, keepalive 1 hold 65535. In this case, there are a large number of Keepalive messages on the network. In addition, BGP does not consider the connection interrupted even if it does not receive Keepalive messages for a long time.
* Keepalive-time is set to 0. In this case, the keepalive timer is not started, and the send-hold timer function does not take effect.The Keepalive time and hold time can be configured for a single peer, a peer group, or globally. The Keepalive time and Holdtime of a single peer take precedence over those of a peer group, and those of a peer group take precedence over the global configurations. If the global Keepalive time and hold time have been set using the **timer** command, you can still run this command to change the Keepalive time and hold time of a single peer or peer group.After the **keep-all-routes** command is run, the **undo peer timer keepalive** command does not take effect. To configure this function, run the **undo keep-all-routes** command and then the **peer timer keepalive** command.BGP messages are sent to peers through an update peer-group. When there is only one peer in the update peer-group or there is no message in the update peer-group, the session hold time does not take effect.


Example
-------

# Set the session hold time for a peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 timer send-hold 720

```

# Configure the Keepalive time, hold time, and minimum hold time for the BGP peer relationship with peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 timer keepalive 10 hold 30 min-holdtime 20

```