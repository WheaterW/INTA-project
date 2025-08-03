display pim rp-info
===================

display pim rp-info

Function
--------



The **display pim rp-info** command displays information about rendezvous points (RPs).




Format
------

**display pim vpn-instance** *vpn-instance-name* **rp-info** [ *group-address* ]

**display pim** [ **all-instance** ] **rp-info** [ *group-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Displays information about the RP that serves a specified multicast group.  group-address specifies a group address. | The value ranges from 224.0.1.0 to 239.255.255.255, in dotted decimal notation. If this parameter is not specified, the command displays RP information of all multicast groups in the specified instance. |
| **all-instance** | Displays information about RPs in all instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays information about RPs in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view information about static RPs and bootstrap device (BSR) RPs, run the display pim rp-info command. The command output includes the RP address, RP priority, address of the group that the RP serves, and the length of time the RP has been Up.

**Precautions**

If neither vpn-instance nor all-instance is specified, the command displays information about RPs in the public network instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display RP information of all multicast groups in the public network instance.
```
<HUAWEI> display pim rp-info
 VPN-Instance: public net
 PIM-SM BSR RP Number:1
 Group/MaskLen: 224.0.0.0/4
     RP: 10.2.2.2 (local)
     Priority: 0
     Uptime: 03:01:36
     Expires: 00:02:29

```

**Table 1** Description of the **display pim rp-info** command output
| Item | Description |
| --- | --- |
| PIM-SM BSR RP Number | Number of PIM-SM BSR RPs. |
| RP | RP address. local indicates that the RP address is a local interface address.  All devices must be configured with the same RP address to serve a multicast group. If two or more different RP addresses exist, troubleshoot faults as follows:   * If static RPs are used on the network, run the static-rp command on all the devices to configure the same RP address for a multicast group. * In dynamic RP mode, see Step 4 in the section "An RPT on a PIM-SM Network Fails to Forward Data" in Troubleshooting - Multicast. |
| VPN-Instance | Instance in which information about RPs is displayed. |
| Group/MaskLen | Group address and mask length. |
| Priority | Priority of the RP. |
| Uptime | Length of time the RP has been Up. |
| Expires | Remaining time before the RP times out. |