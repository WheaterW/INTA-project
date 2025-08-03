ospfv3 flush-source-trace block
===============================

ospfv3 flush-source-trace block

Function
--------



The **ospfv3 flush-source-trace block** command disables OSPFv3 flush LSA source tracing on an interface.

The **undo ospfv3 flush-source-trace block** command enables OSPFv3 flush LSA source tracing on an interface.



By default, OSPFv3 flush LSA source tracing is enabled on all interfaces.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 flush-source-trace block** [ **instance** *instance-id* ]

**undo ospfv3 flush-source-trace block** [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Specifies an interface instance ID. | The value is an integer ranging from 0 to 255. The default value is 0. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the OSPFv3 flush LSA source tracing function is enabled on all interfaces of a specified OSPFv3 process. To disable this function on an interface, run the **ospfv3 flush-source-trace block** command.

**Prerequisites**

OSPFv3 has been enabled using the **ospfv3 area** command in the interface view.


Example
-------

# Disable OSPFv3 flush LSA source tracing on a specified interface.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 flush-source-trace block

```