peer timer (BGP multi-instance VPN instance IPv4 address family view) (group)
=============================================================================

peer timer (BGP multi-instance VPN instance IPv4 address family view) (group)

Function
--------



The **peer timer** command sets the Keepalive time and hold time for a peer group.

The **undo peer timer** command restores the default Keepalive time and hold time.



By default, the Keepalive time is 60s, and the hold time is 180s.


Format
------

**peer** *group-name* **timer** **keepalive** *keepalive-time* **hold** *hold-time*

**peer** *group-name* **timer** **keepalive** *keepalive-time* **hold** *hold-time* **min-holdtime** *min-hold-value*

**undo peer** *group-name* **timer** **keepalive** **hold** [ **min-holdtime** ]

**undo peer** *group-name* **timer** **keepalive** *keepalive-time* **hold** *hold-time*

**undo peer** *group-name* **timer** **keepalive** *keepalive-time* **hold** *hold-time* **min-holdtime** *min-hold-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **keepalive** *keepalive-time* | Specifies the Keepalive time. | The value is an integer in the range from 0 to 21845, in seconds. The default value is 60. |
| **hold** *hold-time* | Indicates the hold time. | The value is 0 or an integer ranging from 3 to 65535, in seconds. The default value is 180.  It is recommended that the configured hold time be related to the total number of BGP address family peers. For details, see the mapping between the total number of BGP peers in each address family and the recommended minimum hold time in the usage guide of the peer timer command. |
| **min-holdtime** *min-hold-value* | Specifies the minimum hold time. On the same device, min-hold-value must be less than hold-time. | The value is an integer ranging from 20 to 65535, in seconds. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After establishing a BGP connection, two peers periodically send Keepalive messages to each other to detect the status of the BGP connection. If a device receives no Keepalive message or any other type of message from its peer within the specified hold time, the device considers the BGP connection interrupted and closes the BGP connection.The keepalive-time and hold-time values are determined through negotiation between peers. The smaller value of hold-time contained in Open messages of both peers is used as the final value of hold-time. The smaller value of one third of hold-time and the locally configured keepalive-time is used as the final value of keepalive-time.You can run this command to set the Keepalive time and hold time of BGP.

* If short keepalive time and hold time are set, BGP can detect a link fault quickly. This speeds up link switchover, but increases the number of keepalive messages on the network and loads of devices, and consumes more network bandwidth resources.
* If long keepalive time and hold time are set, the number of keepalive messages on the network and loads of devices are reduced, and fewer network bandwidths are consumed. However, if the keepalive time is too long, BGP is unable to detect link status changes in time. This may cause a large amount of traffic loss.If the hold time configured on a remote device is less than the min-hold-value configured on the local device, no peer relationship can be established between the two devices. If the hold time configured on the local end is 0s, the rule does not take effect, and a peer relationship can still be established.

Mapping between the total number of peers in each BGP address family and the recommended minimum hold-time:

| Total Number of Peers | Recommended Minimum hold-time |
| --- | --- |
| 0 - 100 | 20 |
| 101 - 200 | 30 |
| 201 - 300 | 45 |
| 301 - 400 | 60 |
| 401 - 500 | 75 |
| 501 and above | 90 |


**Configuration Impact**



If the value of a timer changes, the BGP peer relationship between devices is disconnected. This is because the devices need to re-negotiate keepalive-time and hold-time. Therefore, exercise caution before changing the value of a timer.



**Precautions**

The Hold time must be at least three times the Keepalive time.When setting the values of Keepalive time and Hold time, avoid the following configurations:

* If the values of keepalive-time and hold-time are both set to 0, the BGP timers become invalid. That is, BGP does not detect link faults based on the timers, which may cause great traffic loss.
* The value of hold-time is much greater than the value of keepalive-time, for example, keepalive 1 hold 65535. In this case, there are a large number of Keepalive messages on the network, and BGP does not consider that the connection is interrupted even if it does not receive Keepalive messages for a long time.The Keepalive period and Holdtime can be configured globally, or on a particular peer or peer group. The Keepalive period and Holdtime configured on a specific peer or peer group takes precedence over the global Keepalive period and Holdtime. Using this command can still change the Keepalive period and Holdtime configured on a peer or peer group, although they were globally configured through the **timer** command.After the **keep-all-routes** command is run, the **undo peer timer keepalive** command does not take effect. In this case, you need to run the **undo keep-all-routes** command and then the **peer timer keepalive** command.


Example
-------

# Set the Keepalive time and hold time for peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] group test
[*HUAWEI-bgp-instance-a-vpna] peer test timer keepalive 10 hold 30

```