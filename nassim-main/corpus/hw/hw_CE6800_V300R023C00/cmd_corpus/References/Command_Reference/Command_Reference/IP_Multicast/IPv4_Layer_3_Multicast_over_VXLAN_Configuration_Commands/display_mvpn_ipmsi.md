display mvpn ipmsi
==================

display mvpn ipmsi

Function
--------



The **display mvpn ipmsi** command displays multicast virtual private network (MVPN) inclusive-provider multicast service interface (I-PMSI) tunnel configurations.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mvpn** { **all-instance** | **vpn-instance** *vpn-instance-name* } **ipmsi** [ **verbose** [ *grpAddr* | *srcAddr* ] \* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all-instance** | Displays I-PMSI tunnel configurations of all instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays I-PMSI tunnel configurations of a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **verbose** | Displays detailed I-PMSI tunnel configurations. | - |
| *grpAddr* | Displays I-PMSI tunnel configurations of a specified multicast group address.  group-address specifies a multicast group address. | The value ranges from 224.0.1.0 to 239.255.255.255, in dotted decimal notation. |
| *srcAddr* | Displays I-PMSI tunnel configurations of a specified multicast source address.  source-address specifies a multicast source address. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After an MVPN is configured, run the **display mvpn ipmsi** command to check MVPN I-PMSI tunnel configurations of a specified VPN instance so that you can determine whether the MVPN is working properly.

**Precautions**

If an I-PMSI tunnel is not established, no command output is displayed for the **display mvpn ipmsi** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed I-PMSI tunnel information of a specified VPN instance.
```
<HUAWEI> display mvpn vpn-instance mcast1 ipmsi verbose
MVPN local I-PMSI information for VPN-Instance: mcast1
Tunnel type: vxlan static
Vxlan vni id: 5010
Total number of (S, G): 2
    1. (192.168.10.9, 232.1.1.1)
    2. (192.168.10.9, 232.3.1.1)

```

# Display basic I-PMSI tunnel information of a specified VPN instance.
```
<HUAWEI> display mvpn vpn-instance mcast1 ipmsi
MVPN local I-PMSI information for VPN-Instance: mcast1
Tunnel type: vxlan static
Vxlan vni id: 5010

```

**Table 1** Description of the **display mvpn ipmsi** command output
| Item | Description |
| --- | --- |
| MVPN local I-PMSI information for VPN-Instance | VPN instance to which MVPN I-PMSI tunnel information belongs. |
| Tunnel type | I-PMSI tunnel type, which can only be vxlan static. |
| Vxlan vni id | VNI. |
| Total number of (S, G) | Total number of (S, G) entries that use this I-PMSI tunnel to forward multicast data. |