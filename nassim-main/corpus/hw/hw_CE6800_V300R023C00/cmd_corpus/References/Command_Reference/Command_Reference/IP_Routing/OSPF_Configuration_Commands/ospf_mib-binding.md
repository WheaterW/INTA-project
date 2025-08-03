ospf mib-binding
================

ospf mib-binding

Function
--------



The **ospf mib-binding** command binds an OSPF process to SNMP and enables OSPF to respond to SNMP requests.

The **undo ospf mib-binding** command removes the binding.



By default, OSPF processes are not bound to SNMP.


Format
------

**ospf mib-binding** *process-id*

**undo ospf mib-binding**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The OSPF MIB is a virtual database of the device status maintained by the managed devices.When multiple OSPF processes are started, you can specify the OSPF process to be processed by the OSPF MIB by binding the OSPF MIB to a specified OSPF process.


Example
-------

# Bind an OSPF process to SNMP.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] quit
[*HUAWEI] ospf mib-binding 100

```