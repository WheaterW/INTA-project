display vlan (All views)
========================

display vlan (All views)

Function
--------



The **display vlan** command displays information about all VLANs, including whether MAC address learning or the broadcast function is enabled.




Format
------

**display vlan** *vlan-id* [ **verbose** | **to** *vlan-id2* ]

**display vlan** [ **summary** ]

**display vlan vlan-name** *vlan-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Displays information about a specified VLAN.  If vlan-id is specified, interfaces in the VLAN are displayed. The interfaces can be tagged or untagged. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **verbose** | Displays detailed VLAN information. | - |
| **to** *vlan-id2* | Specifies the end VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **summary** | Displays VLAN summarized information. | - |
| **vlan-name** *vlan-name* | Specifies the name of a VLAN. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After VLANs are created on a device, you can run the display vlan command to check whether the configuration, name, and status of each VLAN are correct.

**Prerequisites**



VLANs have been created on a device. Otherwise, no command output is displayed.



**Precautions**

The following ports are displayed:

* Port (Tagged) that labels packets.
* Port (Untagged) that does not label packets.If a large number of VLAN information exists on a device, you are advised to specify the VLAN ID and VLAN name to filter the VLAN information. Otherwise, the following information may be displayed:
* The terminal screen keeps refreshing and cannot obtain the required information.
* The system does not respond when the system traverses and retrieves the information for a long time.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display VLAN summarized information.
```
<HUAWEI> display vlan summary
Number of static VLAN: 1
VLAN ID: 10

Number of dynamic VLAN: 0
VLAN ID: 
Number of service VLAN: 0
VLAN ID:

```

# Display brief information about a specified VLAN.
```
<HUAWEI> display vlan 10
--------------------------------------------------------------------------------
U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
MP: Vlan-mapping;               ST: Vlan-stacking;
#: ProtocolTransparent-vlan;    *: Management-vlan;
MAC-LRN: MAC-address learning;  STAT: Statistic;
BC: Broadcast; MC: Multicast;   UC: Unknown-unicast;
FWD: Forward;  DSD: Discard;
--------------------------------------------------------------------------------

VID          Ports
--------------------------------------------------------------------------------
  10         UT:100GE1/0/1(U)  100GE1/0/2(U)

VID  Type     Status  Property  MAC-LRN STAT    BC  MC  UC  Description
--------------------------------------------------------------------------------
 10  common   enable  default   enable  disable FWD FWD FWD VLAN 0010

```

# Display detailed information about a specified VLAN.
```
<HUAWEI> display vlan 10 verbose
* : Management-VLAN
---------------------
  VLAN ID      : 10
  VLAN Name    :
  VLAN Type    : Common
  Description  : VLAN 0010
  Status       : Enable
  Broadcast    : Enable
  MAC Learning : Enable
  Statistics   : Disable
  Property     : Default
  VLAN State   : Up
  ----------------
  Untagged      Port: 100GE1/0/2
  ----------------
  Active Untag  Port: 100GE1/0/2
---------------------
Interface                   Physical
100GE1/0/2                  UP

```

# Display information about all VLANs.
```
<HUAWEI> display vlan
The total number of vlans is : 7
VID  Type     Status  Property  MAC-LRN STAT    BC  MC  UC  Description
--------------------------------------------------------------------------------
1    common   enable  default   enable  disable FWD FWD FWD VLAN 0001
2    common   enable  default   enable  disable FWD FWD FWD VLAN 0002
3    common   enable  default   enable  disable FWD FWD FWD VLAN 0003
4    common   enable  default   enable  disable FWD FWD FWD VLAN 0004
5    common   enable  default   enable  disable FWD FWD FWD VLAN 0005
6    common   enable  default   enable  disable FWD FWD FWD VLAN 0006
7    common   enable  default   enable  disable FWD FWD FWD VLAN 0007

```

# Display information about a VLAN with the specified name.
```
<HUAWEI> display vlan vlan-name IPTV
--------------------------------------------------------------------------------
U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
MP: Vlan-mapping;               ST: Vlan-stacking;
#: ProtocolTransparent-vlan;    *: Management-vlan;
MAC-LRN: MAC-address learning;  STAT: Statistic;
BC: Broadcast; MC: Multicast;   UC: Unknown-unicast;
FWD: Forward;  DSD: Discard;
--------------------------------------------------------------------------------

VID          Ports
--------------------------------------------------------------------------------
 10          UT:100GE1/0/2(U)

VID  Type     Status  Property  MAC-LRN STAT    BC  MC  UC  Description
--------------------------------------------------------------------------------
 10  common   enable  default   enable  disable FWD FWD FWD VLAN 0010

```

**Table 1** Description of the **display vlan (All views)** command output
| Item | Description |
| --- | --- |
| Number of static VLAN | Static VLAN. |
| Number of dynamic VLAN | Dynamic VLAN. |
| Number of service VLAN | Service VLAN on the device. |
| VLAN ID | VLAN ID. |
| VLAN Name | Name of a VLAN. |
| VLAN state | Status of the VLAN:   * Up. * Down.   The status of a VLAN is determined by the status of interfaces in the VLAN. A VLAN is up only when at least one interface in the VLAN is up. If the corresponding VLANIF interface exists, the VLAN status is down only when the VLANIF interface is administratively down and all member interfaces in the VLAN are down. |
| VLAN Type | VLAN type:   * common: common VLAN. |
| #: ProtocolTransparent-vlan | Transparent transmission of VLAN tags. |
| \*: Management-vlan | Management VLAN. |
| VID | VLAN ID. |
| Type | VLAN type:   * common: common VLAN. |
| Status | Whether a VLAN is enabled:   * disable: The VLAN is disabled. (You can run the shutdown vlan command to disable a VLAN.). * enable: The VLAN is enabled. (You can run the undo shutdown vlan command to enable a VLAN.). |
| Property | VLAN attribute. The value default indicates that the VLAN is a common VLAN. |
| MAC-LRN | Whether MAC address learning is enabled:   * disable: MAC address learning is disabled. * enable: MAC addresses learning is enabled. |
| STAT | Whether VLAN packet statistics collection is enabled:   * disable. * enable. |
| BC | Whether broadcast packets are forwarded:   * forward. * discard. |
| MC | Whether multicast packets are forwarded:   * forward. * discard. |
| UC | Whether unknown unicast packets are forwarded:   * forward: Unknown unicast packets are forwarded. * discard: Unknown unicast packets are discarded. |
| Description | Description of a VLAN. |
| FWD | The packet is forwarded. |
| Broadcast | Whether broadcast packets are forwarded:   * forward. * discard. |
| MAC Learning | Whether MAC address learning is enabled:   * disable: MAC address learning is disabled. * enable: MAC addresses learning is enabled. |
| Statistics | Whether VLAN packet statistics collection is enabled:   * disable. * enable. |
| Interface | Interface added to a VLAN. |
| Physical | Physical status of the interface added to a VLAN. |
| The total number of vlans is | Total number of VLANs. |
| U | The interface status is up. |
| D | The interface status is down. |
| TG | Tagged packets. |
| UT | Untagged packets. |
| MP | VLAN mapping. |
| ST | VLAN stacking. |
| Ports/Port | Interfaces added to a VLAN. |
| DSD | Packets dropped. |