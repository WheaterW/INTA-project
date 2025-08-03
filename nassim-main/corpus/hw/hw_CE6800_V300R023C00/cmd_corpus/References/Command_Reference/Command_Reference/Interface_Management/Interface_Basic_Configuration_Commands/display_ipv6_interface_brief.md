display ipv6 interface brief
============================

display ipv6 interface brief

Function
--------



The **display ipv6 interface brief** command displays IPv6 information about an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 interface brief**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

If an interface is assigned an IPv6 address, run the **display ipv6 interface** command to view the IPv6 status and configuration on this interface.

**Follow-up Procedure**

You can run the **display interface description** command to view the description of the interface.You can run the **display interface** command to view detailed information about the operation and statistics of the interface.

**Precautions**

Ensure that the designated interfaces are assigned IPv6 addresses; otherwise, you cannot view information on the interfaces.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief IPv6 information of all interfaces.
```
<HUAWEI> display ipv6 interface brief
*down: administratively down
!down: FIB overload down
(l): loopback
(s): spoofing
Interface                    Physical              Protocol VPN
100GE1/0/1                   up                    up       --
[IPv6 Address/Prefix Length] 2001:db8:3c4d::/48
100GE1/0/2                   up                    up       --
[IPv6 Address/Prefix Length] 2001:db8:3c4d:15::/64

```

**Table 1** Description of the **display ipv6 interface brief** command output
| Item | Description |
| --- | --- |
| (l): loopback | The loopback function is configured on the interface. |
| (s): spoofing | The spoofing feature of the link protocol status of the interface. That is, the link protocol status of the interface is always Up.  This is the build-in attribute of an interface. When this interface is assigned an IP address, (s) is still displayed. |
| Interface | Interface name. |
| Physical | Physical status of the interface:   * up. * down. * administratively down. |
| Protocol | Status of the link protocol:   * up. * down. * \*down. |
| VPN | Status of a virtual private network (VPN) configured on the interface:   * -: No VPN is configured. * ifm: Specifies the name of a VPN instance. |
| IPv6 Address | IP address of the interface. |
| \*down | Reason that interface is physically Down.  administratively down: The network administrator runs the shutdown command on the interface. |
| !down | The interface goes Down because the number of route prefixes in the FIB exceeds the upper limit. |
| Prefix Length | Prefix length of an interface address. |