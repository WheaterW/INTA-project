display system tcam resource acl
================================

display system tcam resource acl

Function
--------



The **display system tcam resource acl** command displays TCAM resource information on a specified device.




Format
------

**display system tcam resource acl** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Displays TCAM resource information on a specified device. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display system tcam resource acl command displays TCAM resource information,which helps you learn about the resource usage of the device.If slot-id is not specified,all TCAM resource usages in different stages on the device are displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display TCAM resource information on a specified device.
```
<HUAWEI> system-view
[HUAWEI] display system tcam resource acl
--------------------------------------------------------------------------------                                                    
Slot  Chip TCAM     Resource Stage              Total     Used  Limited     Free                                                    
--------------------------------------------------------------------------------                                                    
1     0    Internal Banks    Ingress+Egress        56        2        2       52                                                    
1     0    Internal Rules    Ingress+Egress     28672      780      244    27648                                                    
1     0    Internal Meters   Ingress+Egress     32768      203        0    32565                                                    
1     0    Internal Counters Ingress+Egress     65536       75        0    65461                                                    
--------------------------------------------------------------------------------

```
```
<HUAWEI> system-view
[HUAWEI] display system tcam resource acl
-------------------------------------------------------------------------------------
Slot  Chip Pipe TCAM     Resource Stage              Total     Used  Limited     Free
-------------------------------------------------------------------------------------
1     0    0    Internal Banks    Ingress               30        6        0       24
1     0    0    Internal Rules    Ingress            30720      596     5548    24576
1     0    0    Internal Meters   Ingress            73656      612        0    73044
1     0    0    Internal Counters Ingress           196416      888        0   195528
1     0    2    Internal Banks    Ingress               30        6        0       24
1     0    2    Internal Rules    Ingress            30720      596     5548    24576
1     0    2    Internal Meters   Ingress            73656      612        0    73044
1     0    2    Internal Counters Ingress           196416      888        0   195528
-------------------------------------------------------------------------------------
1     0    0    Internal Banks    Egress                 6        2        0        4
1     0    0    Internal Rules    Egress              6144        4     2044     4096
1     0    0    Internal Meters   Egress             73656      612        0    73044
1     0    0    Internal Counters Egress            196416      888        0   195528
1     0    1    Internal Banks    Egress                 6        2        0        4
1     0    1    Internal Rules    Egress              6144        4     2044     4096
1     0    1    Internal Meters   Egress             73656      612        0    73044
1     0    1    Internal Counters Egress            196416      888        0   195528
1     0    4    Internal Banks    Egress                 6        2        0        4
1     0    4    Internal Rules    Egress              6144        4     2044     4096
1     0    4    Internal Meters   Egress             73656      612        0    73044
1     0    4    Internal Counters Egress            196416      888        0   195528
1     0    5    Internal Banks    Egress                 6        2        0        4
1     0    5    Internal Rules    Egress              6144        4     2044     4096
1     0    5    Internal Meters   Egress             73656      612        0    73044
1     0    5    Internal Counters Egress            196416      888        0   195528
-------------------------------------------------------------------------------------

```

**Table 1** Description of the **display system tcam resource acl** command output
| Item | Description |
| --- | --- |
| Slot | Device ID. |
| Chip | Chip ID. |
| TCAM | TCAM type:   * External. * Internal. |
| Resource | ACL resource type (the supported resource type depends on the device):   * Rules: rule resource. * Meters: CAR resource. * Counters: statistics collection resource. * Banks: slice resources. * Slices: slice resources.   The TCAM can be divided into several banks or slices, and rules are stored in the entries of banks or slices. |
| Stage | Stage during the packet forwarding process (the supported packet forwarding stages depend on the device):   * Pre-Ingress: inbound direction before MAC address table lookup. * Ingress: inbound direction. * Egress: outbound direction. * Ingress+Egress: inbound and outbound directions. |
| Total | Total number of resources. The number of resources differs according to device models. |
| Used | Number of used resources. |
| Limited | Number of reserved resources. |
| Free | Number of remaining resources. |
| Pipe | Pipeline No. |