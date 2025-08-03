display stp vlan abnormal-interface
===================================

display stp vlan abnormal-interface

Function
--------



The **display stp vlan abnormal-interface** command displays information about abnormal interfaces running the Spanning Tree Protocol (STP).




Format
------

**display stp vlan** [ *vlan-id* ] **abnormal-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Displays information about abnormal ports running STP in a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If a device has many interfaces and the **display stp brief** command output displays vast information, viewing information about abnormal interfaces running STP is difficult.You can use the **display stp vlan abnormal-interface** command to view information about abnormal interfaces running STP.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about abnormal ports running VBST in VLAN 5.
```
<HUAWEI> display stp vlan 5 abnormal-interface
VLANID    Interface          Status          Reason                   
     5    100GE1/0/1         DISCARDING      LOOP-Protected           
     5    100GE1/0/2         DOWN            BPDU-Protected           
     5    100GE1/0/3         DISCARDING      ROOT-Protected           
     5    100GE1/0/4         DISCARDING      LOOP-Detected

```

**Table 1** Description of the **display stp vlan abnormal-interface** command output
| Item | Description |
| --- | --- |
| VLANID | Identity VLAN ID. |
| Interface | Identity interface name. |
| Status | Status of an interface after the VBST protection takes effect.   * DOWN: indicates that the physical status of the interface is Down (including error-down). * DISCARDING: indicates the blocked interface after the topology of the spanning tree becomes stable. |
| Reason | An interface running STP becomes abnormal due to one of the following:   * ROOT-Protected: indicates that the root protection takes effect. * LOOP-Protected: indicates that the loop protection takes effect. * BPDU-Protected: indicates that the BPDU protection takes effect. * LOOP-Detected: indicates that the loop detection takes effect. * PVID-Inconsistency: The PVID of the directly connected interface is inconsistent. |