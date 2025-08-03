display igmp explicit-tracking
==============================

display igmp explicit-tracking

Function
--------



The **display igmp explicit-tracking** command displays tracking information of IGMPv3 hosts.




Format
------

**display igmp explicit-tracking** [ **interface** { *interface-type* *interface-number* | *interface-name* } [ **group** *group-address* [ **source** *source-address* ] ] ] [ [ **host-address** *host-address* ] **verbose** ]

**display igmp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **explicit-tracking** [ **interface** { *interface-type* *interface-number* | *interface-name* } [ **group** *group-address* [ **source** *source-address* ] ] ] [ [ **host-address** *host-address* ] **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies an interface type and number. | - |
| *interface-name* | Specifies the name of an interface. | - |
| **group** *group-address* | Specifies a multicast group address. | The value ranges from 224.0.1.0 to 239.255.255.255, in dotted decimal notation. |
| **source** *source-address* | Specifies a multicast source address. | The value can be a Class A, B, or C address, in dotted decimal notation. |
| **host-address** *host-address* | Specifies a host address. | The value can be a Class A, B, or C address, in dotted decimal notation. |
| **verbose** | Displays detailed host tracking information. | - |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Indicates all instances. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check host tracking information of interfaces, run the display igmp explicit-tracking command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed host tracking information on Layer 3 multicast interfaces.
```
<HUAWEI> display igmp explicit-tracking verbose
Explicit-tracking information of VPN-Instance: public net
  Total 1 host, 1 entry, 1 group reported
  VLANIF 200 (10.1.1.1), Total 1 host, 1 entry, 1 group reported
    Host: 10.1.12.2, Total 1 entry, 1 group reported
      (S, G) List:
      Group: 232.0.0.1
        Uptime: 00h00m12s
        Expires: --
        Mode: Include
        Source: 192.168.3.2
          Uptime: 00h00m12s
          Expires: 00h02m07s
          Time since last refresh: 00h00m03s

```

# Display brief host tracking information on Layer 3 multicast interfaces.
```
<HUAWEI> display igmp explicit-tracking
Explicit-tracking information of VPN-Instance: public net

Interface VLANIF 200
 -----------------------------------------------------------------------------------
(Source, Group)                                             INC/EXC Hosts    Forward
                                Host               Mode                             
 -----------------------------------------------------------------------------------
(192.168.3.2, 232.0.0.1)                                    1/0              Yes
                                10.1.12.2          include

```

**Table 1** Description of the **display igmp explicit-tracking** command output
| Item | Description |
| --- | --- |
| Explicit-tracking information of VPN-Instance | VPN instance name of the host whose tracking information is displayed. |
| Total 1 host, 1 entry, 1 group reported | Total number of hosts, entries, and multicast groups for a specific VPN instance. |
| VLANIF 200 (10.1.1.1), Total 1 host, 1 entry, 1 group reported | IP address of the interface, total number of hosts on the interface, number of records, and number of record groups. |
| Host: 10.1.12.2, Total 1 entry, 1 group reported | Total number of entries and multicast groups for a specific host. |
| (S, G) List | List of (S, G) information. |
| Time since last refresh | Time since last refresh was performed. |
| (Source, Group) | Multicast source and group addresses. |
| INC/EXC Hosts | Number of hosts that are included or excluded. |
| Forward | Whether multicast traffic is forwarded to the host:   * Yes. * No. |
| Host | IP address of the multicast host. |
| Mode | Mode in which the host joins a group:   * include. * exclude. |
| Group | Multicast group IP address. |
| Uptime | Time since the entry was created. |
| Expires | Time after which the entry will expire. --: indicates that the parameter is invalid. |
| Source | Multicast source IP address. |