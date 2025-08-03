display igmp snooping explicit-tracking
=======================================

display igmp snooping explicit-tracking

Function
--------



The **display igmp snooping explicit-tracking** command displays host tracking information of a VLAN.




Format
------

**display igmp snooping explicit-tracking** { **vlan** [ *vlan-id* [ **interface** { *interface-type* *interface-number* | *interface-name* } ] ] } [ [ **source-address** *source-address* ] **group-address** *group-address* ] [ [ **host-address** *host-address* ] **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Specifies a VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **interface** *interface-type* *interface-number* | Specifies an interface type and number. | - |
| *interface-name* | Specifies an interface name. | - |
| **source-address** *source-address* | Specifies a multicast source address. | The value can be a Class A, B, or C address, in dotted decimal notation. |
| **group-address** *group-address* | Specifies a multicast group address. | The value ranges from 224.0.1.0 to 239.255.255.255, in dotted decimal notation. |
| **host-address** *host-address* | Specifies a host address. | The value can be a Class A, B, or C address, in dotted decimal notation. |
| **verbose** | Displays detailed host tracking information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check host tracking information of a VLAN, run the display igmp snooping explicit-tracking command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief host tracking information of a VLAN.
```
<HUAWEI> display igmp snooping explicit-tracking vlan
Explicit-tracking information of Vlan: 10
100GE1/0/1(VLAN:10)                          
 -----------------------------------------------------------------------------------
(Source, Group)                                             INC/EXC Hosts    Forward
                                Host               Mode                             
 -----------------------------------------------------------------------------------
(192.168.3.2, 232.0.0.1)                                    1/0              Yes
                                10.1.12.2          include

```

# Display detailed host tracking information of a VLAN.
```
<HUAWEI> display igmp snooping explicit-tracking vlan verbose
Vlan: 10, Total 1 host(s), 1 entry(s), 1 group(s) reported
  100GE1/0/1, Total 1 host(s), 1 entry(s), 1 group(s) reported
    Host: 10.1.12.2, Total 1 entry(s), 1 group(s) reported
      (S, G) List:
      Group: 232.0.0.1
        Uptime: 00h00m18s
        Expires: --
        Mode: Include
        Source: 192.168.3.2
          Uptime: 00h00m18s
          Expires: 00h02m01s
          Time since last refresh: 00h00m09s

```

**Table 1** Description of the **display igmp snooping explicit-tracking** command output
| Item | Description |
| --- | --- |
| Explicit-tracking information of Vlan | VLAN ID of the host whose tracking information is displayed. |
| Vlan: 10, Total 1 host(s), 1 entry(s), 1 group(s) reported | Total number of hosts, entries, and multicast groups for a specific VLAN. |
| (Source, Group) | Multicast source and group addresses. |
| INC/EXC Hosts | Number of hosts that are included or excluded. |
| Forward | Whether multicast traffic is forwarded to the host:   * Yes. * No. |
| Host | IP address of the multicast host. |
| Mode | Mode in which the host joins a group:   * include. * exclude. |
| Host: 10.1.12.2, Total 1 entry(s), 1 group(s) reported | Host IP address and total number of entries and multicast groups for a specific host. |
| (S, G) List | List of (S, G) information. |
| Time since last refresh | Time since last refresh was performed. |
| Group | Multicast group IP address. |
| Uptime | Time since the entry was created. |
| Expires | Time after which the entry will expire. --: indicates that the parameter is invalid. |
| Source | Multicast source IP address. |
| 100GE1/0/1, Total 1 host(s), 1 entry(s), 1 group(s) reported | Total number of hosts, entries, and groups on the interface. |