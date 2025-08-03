network (RIP view)
==================

network (RIP view)

Function
--------



The **network** command enables RIP for a specified network segment on an interface.

The **undo network** command disables RIP from a specified network segment on an interface.



By default, RIP is disabled for the specified network segment on an interface.


Format
------

**network** *network-address*

**undo network** *network-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *network-address* | Specifies the address of the network segment for which RIP is enabled. | The value is in dotted decimal notation. |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **network** command enables RIP for the interface on the specified network segment.

**Prerequisites**

An IP has been configured for the interface whose network segment is to be enabled with RIP.ProcedureIn RIP, the network segments of the same physical interface must be specified for the same RIP process.

**Implementation Procedure**

In RIP, the network segments of the same physical interface must be specified for the same RIP process.


Example
-------

# Enable RIP on network 10.0.0.0.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1] network 10.0.0.0

```