shutdown interface
==================

shutdown interface

Function
--------



The **shutdown interface** command shuts down sub-interfaces in a batch.

The **undo shutdown interface** command starts sub-interfaces in a batch.



By default, a sub-interface is started.


Format
------

**shutdown interface** { *ifname* | *beginIfType* *beginIfNum* } *to* { *endIfname* | *endIfType* *endIfNum* }

**undo shutdown interface** { *ifname* | *beginIfType* *beginIfNum* } *to* { *endIfname* | *endIfType* *endIfNum* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ifname* | Specifies a start interface name. | - |
| *beginIfType* | Specifies a start interface type. | The value is of the enumerated type. |
| *beginIfNum* | Specifies a start interface number. | - |
| *to* | The keyword to is used to connect two interfaces, indicating that the interface numbers are all interfaces between two interfaces (including these two interfaces). | - |
| *endIfname* | Specifies an end interface name. | - |
| *endIfType* | Specifies an end interface type. | The interfaces must support sub-interfaces. |
| *endIfNum* | Specifies an end interface number. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a main interface has a large number of sub-interfaces, to disable these interfaces, run the **shutdown** command on each sub-interface view. To release workloads, run the **shutdown interface** command to disable sub-interfaces in a batch. After the **shutdown interface** command is run, the sub-interface operating state changes to Down. If the sub-interface is in the disabled state, run the **undo shutdown interface** command to start sub-interfaces in a batch, after the **undo shutdown interface** command is run, the sub-interface operating state is synchronized with the link status.



**Prerequisites**



The sub-interfaces to be disabled or started in a batch must exist.



**Configuration Impact**



Running the **shutdown interface** command will interrupt services on the sub-interfaces. Therefore, exercise caution when running this command.If the **shutdown interface** command is run more than once, the latest configuration overrides the previous one.



**Precautions**

When you specify the interface range, note that:

* The end interface number must be greater than the start interface number.
* The types of the interfaces to which the end interface number and start interface number correspond must be the same
* The interfaces in the range must exist.


Example
-------

# Disable sub-interfaces 100GE1/0/1.1, 100GE1/0/1.2, and 100GE1/0/1.3 in a batch.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.1
[*HUAWEI-100GE1/0/1.1] quit
[*HUAWEI] interface 100GE 1/0/1.2
[*HUAWEI-100GE1/0/1.2] quit
[*HUAWEI] interface 100GE 1/0/1.3
[*HUAWEI-100GE1/0/1.3] quit
[*HUAWEI] shutdown interface 100GE 1/0/1.1 to 100GE 1/0/1.3

```