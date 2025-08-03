ospfv3 mib-binding
==================

ospfv3 mib-binding

Function
--------



The **ospfv3 mib-binding** command binds an OSPFv3 process to SNMP and enables OSPFv3 to respond to SNMP requests.

The **undo ospfv3 mib-binding** command removes the binding.



By default, OSPFv3 processes are not bound to SNMP.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 mib-binding** *process-id*

**undo ospfv3 mib-binding**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

OSPFv3 supports the network management function. You can bind the OSPFv3 MIB to a certain OSPFv3 process, and configure the trap function and log function.When multiple OSPFv3 processes are started, you can specify the OSPFv3 process to be processed by the OSPFv3 MIB by binding the OSPFv3 MIB to a specified OSPFv3 process.


Example
-------

# Bind an OSPFv3 process to SNMP.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 100
[*HUAWEI-ospfv3-100] quit
[*HUAWEI] ospfv3 mib-binding 100

```

# Unbind the OSPFv3 process from SNMP.
```
<HUAWEI> system-view
[~HUAWEI] undo ospfv3 mib-binding

```