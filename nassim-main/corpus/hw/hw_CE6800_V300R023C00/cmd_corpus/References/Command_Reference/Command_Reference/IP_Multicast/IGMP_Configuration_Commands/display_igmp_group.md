display igmp group
==================

display igmp group

Function
--------



The **display igmp group ssm-mapping** command displays information about multicast groups for which source-specific multicast (SSM) mapping rules are configured using the ssm-mapping command.

The **display igmp group** command displays information about IGMP groups, including multicast groups that hosts dynamically join by sending Report messages and multicast groups to which hosts are statically added by using commands.




Format
------

**display igmp group** [ *group-address* | **interface** { *interface-type* *interface-number* | *interface-name* } ] \* [ **ssm-mapping** ] [ **verbose** ]

**display igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **group** [ *group-address* | **interface** { *interface-type* *interface-number* | *interface-name* } ] \* [ **ssm-mapping** ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Displays configurations and running information about IGMP groups that have the specified group address.  group-address specifies a multicast group address. | The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. |
| **interface** *interface-type* *interface-number* | Displays configurations and running information about IGMP groups that a specified interface joins. | - |
| *interface-name* | Displays configurations and running information about IGMP groups that a specified interface joins. | - |
| **ssm-mapping** | Specifies information about multicast groups for which source-specific multicast (SSM) mapping rules are configured using the ssm-mapping command. | - |
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

**Usage Scenario**

If a host wants to receive multicast data for a multicast group, the host must join the multicast group. Either of the following modes can be used to enable a host to join a multicast group:

* Dynamic mode: Run the igmp enable command to enable IGMP on the interface connected to the network segment on which the host resides. Then, the network sends data to the host after the host joins the group and stops sending data after the host leaves the group.
* Static mode: Run the igmp static-group command to enable IGMP on the interface connected to the network segment on which the host resides. Then, the host becomes a static data receiver of this group, and the network keeps sending data to the host.To learn the status of or locate a fault in a dynamically joined multicast group, run the **display igmp group** command to view information about the multicast group. The information helps you analyze and locate the fault.

**Precautions**

Before using the **display igmp group** command, note the following:

* If neither vpn-instance nor all-instance is specified, the command displays information about multicast groups in the public network instance.
* If group-address is specified, the command displays information about the specified IGMP group.
* If interface is specified, the command displays information about IGMP groups that the specified interface joins.
* If verbose is specified, the command displays detailed information about IGMP groups.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about IGMP groups in the public network instance that hosts dynamically join.
```
<HUAWEI> display igmp group
Interface group report information of VPN Instance: public net
100GE1/0/1(10.1.6.2):
  Total 1 IGMP Group reported
   Group Address   Last Reporter   Uptime      Expires
   225.1.1.2       10.1.6.10       00:02:04    00:01:17

```

# Display information about multicast groups configured with SSM mapping rules in the public network instance.
```
<HUAWEI> display igmp group ssm-mapping
IGMP SSM mapping interface group report information of VPN Instance: public net
 Limited entry of this VPN Instance: -
 100GE1/0/1(192.168.101.1):
  Total 1 IGMP SSM-Mapping Group reported
   Group Address   Last Reporter   Uptime      Expires
   232.0.0.1       192.168.101.1   00:00:02    00:02:08

```

# Display detailed information about multicast groups configured with SSM mapping rules in the public network instance.
```
<HUAWEI> display igmp group ssm-mapping verbose
Interface group report information of VPN Instance: public net
 Limited entry of this VPN Instance: -
 100GE1/0/1(10.133.133.1):
  Total entry on this interface: 1
  Limited entries on this interface: -
  Total 1 IGMP SSM-Mapping Group reported
   Group: 232.0.0.1
     Uptime: 00:00:15
     Expires: 00:01:55
     Last reporter: 192.168.27.62
     Last-member-query-counter: 0
     Last-member-query-timer-expiry: off
     Source list:
       Source Address        Uptime
       10.11.0.4          00:00:08

```

# Display information about IGMP multicast groups that that hosts dynamically join through VLANIF interfaces in the public network instance.
```
<HUAWEI> display igmp group
Interface group report information of VPN instance: public net
 Vlanif1(10.1.6.2):
  Total 1 IGMP Group reported
   Group Address   Last Reporter   Uptime      Expires
   225.0.0.1       --              00:00:07    --

```

# Display detailed information about IGMP groups in the public network instance.
```
<HUAWEI> display igmp group verbose
Interface group report information of VPN instance: public net
 Limited entry of this VPN instance: -
 Vlanif10(10.1.10.1):
  Total entry on this interface: 1
  Limited entry on this interface: -
  Total IGMP Group reported:  1
   Group: 232.1.1.1
     Uptime: 00:00:46
     Expires: off
     Last reporter: --
     Last Member Query Counter: 0
     Last Member Query Timer Expiry: off
     Group mode: include
     Version1 Host Present Timer Expiry: off
     Version2 Host Present Timer Expiry: off
     Explicit-tracking state: valid
     Source list:
       Source: 100.1.1.1
          Uptime: 00:00:46
          Expires: 00:05:24
          Last-member-query-counter: 0
          Last-member-query-timer-expiry: off

```

**Table 1** Description of the **display igmp group** command output
| Item | Description |
| --- | --- |
| Interface group report information of VPN Instance | Instance to which information about IGMP groups belongs. |
| Total 1 IGMP Group reported | Number of multicast groups that an interface dynamically joins. |
| Total 1 IGMP SSM-Mapping Group reported | Number of reported IGMP groups with addresses in the SSM group address range. |
| Total IGMP Group reported | Number of multicast groups that an interface joins. |
| Total entry on this interface | Number of multicast groups that an interface is added to. |
| IGMP SSM mapping interface group report information of VPN Instance | Instance in which information about multicast groups configured with SSM mapping rules is displayed. |
| Group Address | Multicast group address. |
| Group | Multicast group address. |
| Group mode | Multicast group mode. The value can be:   * include: Include mode. * exclude: Exclude mode. |
| Last Reporter | Last host that sends a Report message. |
| Last Member Query Counter | Number of times that last-member query messages are sent. |
| Last Member Query Timer Expiry | Timeout period of the last member query message. The options are as follows:   * Time: The time format is hh:mm:ss. * off: indicates that the timer is not started. |
| Uptime | Time since a multicast group was created. The time format is as follows:   * If the time is shorter than or equal to 24 hours, the format is hours:minutes:seconds. * If the time is longer than 24 hours but shorter than or equal to one week, the format is days:hours. * If the time is longer than one week, the format is weeks:days. |
| Expires | Scheduled time when a group will be deleted from the IGMP group table. The time format is as follows:   * If the time is shorter than or equal to 24 hours, the format is hours:minutes:seconds. * If the time is longer than 24 hours but shorter than or equal to one week, the format is days:hours. * If the time is longer than one week, the format is weeks:days. |
| Limited entry on this interface | Maximum number of IGMP entries that can be created on an interface. |
| Limited entry of this VPN Instance | Maximum number of IGMP entries that can be created in an instance. |
| Limited entries on this interface | Maximum number of IGMP entries for an interface. |
| Source Address | Multicast source IP address. |
| Source list | Source list of SSM mapping. |
| Source | Source address. |
| Version1 Host Present Timer Expiry | Timeout period of an IGMPv1 host. The options are as follows:   * Time: The time format is hh:mm:ss. * off: indicates that the timer is not started. |
| Version2 Host Present Timer Expiry | Timeout period of an IGMPv2 host. The value can be:   * Actual time in the hours:minutes:seconds format. * off: indicates that the timer is not started. |
| Explicit-tracking state | State of host tracking. The value can be:   * valid: The function is valid. * invalid: The function is invalid. |
| Last-member-query-counter | Number of times that last-member query messages are sent. |
| Last-member-query-timer-expiry | Timeout period of the last member query message. The options are as follows:   * Time: The time format is hh:mm:ss. * off: indicates that the timer is not started. |
| 100GE1/0/1 | Interface name. |
| Vlanif10(10.1.10.1) | Interface type and number (IP address). |