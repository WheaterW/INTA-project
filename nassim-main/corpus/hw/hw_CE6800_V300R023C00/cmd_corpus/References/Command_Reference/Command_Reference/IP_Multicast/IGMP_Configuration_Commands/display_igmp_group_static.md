display igmp group static
=========================

display igmp group static

Function
--------



The **display igmp group static** command displays information about IGMP groups, including multicast groups that hosts dynamically join by sending Report messages and multicast groups to which hosts are statically added by using commands.




Format
------

**display igmp group** [ *group-address* | **interface** { *interface-type* *interface-number* | *interface-name* } ] \* **static** [ **verbose** ]

**display igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **group** [ *group-address* | **interface** { *interface-type* *interface-number* | *interface-name* } ] \* **static** [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Displays configurations and running information about IGMP groups that have the specified group address.  group-address specifies a multicast group address. | The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. |
| **interface** *interface-type* *interface-number* | Displays configurations and running information about IGMP groups that a specified interface joins.  interface-type interface-number specifies the type and number of an interface. | - |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **verbose** | Displays detailed configurations and running information about IGMP groups that hosts dynamically join or the IGMP groups to which hosts are statically added. | - |
| **vpn-instance** *vpn-instance-name* | Displays configurations and running information about IGMP groups in a specified VPN instance.  vpn-instance-name specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Displays configurations and running information about IGMP groups in all instances. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If a host wants to receive multicast data for a multicast group, the host must join the multicast group. Either of the following modes can be used to enable a host to join a multicast group:

* Dynamic mode: Run the igmp enable command to enable IGMP on the interface connected to the network segment on which the host resides. Then, the network sends data to the host after the host joins the group and stops sending data after the host leaves the group.
* Static mode: Run the igmp static-group command to enable IGMP on the interface connected to the network segment on which the host resides. Then, the host becomes a static data receiver of this group, and the network keeps sending data to the host.To learn the status of or locate a fault in a dynamically joined multicast group, run the **display igmp group** command to view information about the multicast group. The information helps you analyze and locate the fault.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about IGMP groups on GE 1/0/1 in the public network instance.
```
<HUAWEI> display igmp group interface Eth-Trunk 0 static
Static join group information of VPN Instance: public net
 Eth-Trunk 0:
Total: 2
   Group Address   Source Address  Expires
   226.0.0.1       10.1.6.4      never
   226.0.0.2       0.0.0.0         never

```

**Table 1** Description of the **display igmp group static** command output
| Item | Description |
| --- | --- |
| Eth-Trunk 0 | Type and number of an interface. |
| Static join group information of VPN Instance | Instance in which information about IGMP groups is displayed. |
| Group Address | Multicast group address. |
| Source Address | Multicast source address. |
| Expires | Scheduled time when a group will be deleted from the IGMP group table. The time format is as follows:   * If the time is shorter than or equal to 24 hours, the format is hours:minutes:seconds. * If the time is longer than 24 hours but shorter than or equal to one week, the format is days:hours. * If the time is longer than one week, the format is weeks:days. |
| Total | Number of multicast groups that an interface is added to. |