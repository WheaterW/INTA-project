ospfv3
======

ospfv3

Function
--------



The **ospfv3** command creates and runs an OSPFv3 process.

The **undo ospfv3** command terminates an OSPFv3 process.



By default, OSPFv3 is disabled, that is, no OSPFv3 process runs.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3** *process-id* [ **vpn-instance** *vpn-instance-name* ]

**ospfv3** [ **vpn-instance** *vpn-instance-name* ]

**undo ospfv3** *process-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. The default value is 1. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

An OSPFv3 process can run normally only after a router ID is configured in the OSPFv3 view. Otherwise, the OSPFv3 process can be viewed but LSAs cannot be generated.Running the **undo ospfv3** command deletes all configurations in the OSPFv3 view. Exercise caution when running this command.


Example
-------

# Enable the OSPFv3 protocol.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance huawei
[*HUAWEI-vpn-instance-huawei] ipv6-family
[*HUAWEI-vpn-instance-huawei-af-ipv6] quit
[*HUAWEI-vpn-instance-huawei] quit
[*HUAWEI] ospfv3 1 vpn-instance huawei

```