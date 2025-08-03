ospfv3 bfd block
================

ospfv3 bfd block

Function
--------



The **ospfv3 bfd block** command disables or blocks BFD on a specified OSPFv3 interface.

The **undo ospfv3 bfd block** command enables BFD on a specified OSPFv3 interface.



By default, BFD is enabled on OSPFv3 interfaces.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 bfd block** [ **instance** *instance-id* ]

**undo ospfv3 bfd block** [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Indicates the ID of the instance to which the interface belongs. | The value is an integer that ranges from 0 to 255. |
| **block** | Disables BFD from an OSPFv3 interface. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the **bfd all-interfaces enable** command is run in an OSPFv3 process, BFD sessions are created for all interfaces in the process that have OSPFv3 enabled and neighbors are in the Full state. If you do not want to enable BFD on some interfaces, disable the interfaces from dynamically establishing BFD sessions.

**Prerequisites**

BFD has been enabled on these interfaces.

**Precautions**



The ospfv3 bfd enable and ospfv3 bfd block commands are mutually exclusive. If both commands are run, the latest configuration overrides the previous one.




Example
-------

# Disable BFD on an interface.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 bfd enable
[*HUAWEI-100GE1/0/1] ospfv3 bfd block

```