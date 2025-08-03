flooding-control
================

flooding-control

Function
--------



The **flooding-control** command restricts the flooding of OSPF update LSAs.

The **undo flooding-control** command restores the default configuration.



By default, the flooding of update LSAs is not restricted.


Format
------

**flooding-control** [ **number** *number-value* | **timer-interval** *timer-interval-value* ] \*

**undo flooding-control** [ **number** *number-value* | **timer-interval** *timer-interval-value* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **number** *number-value* | Sets the maximum number of Update packets that can be sent at each interval during update LSA flooding. | The value is an integer ranging from 1 to 1000. The default value is 50. |
| **timer-interval** *timer-interval-value* | Sets the interval at which Update packets are sent during update LSA flooding. | The value is an integer ranging from 30 to 100000, in milliseconds. The default value is 30. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a local device has multiple neighbors or needs to flood a large number of update LSAs, an OSPF neighbor will receive a large number of Link State Update (LSU) packets within a short time. As a result, the established OSPF neighbor relationships may be terminated, because the neighbor may discard the Hello packets used to maintain neighbor relationships if it is busy processing the burst LSU packets. In this case, OSPF neighbors will exchange more packets to re-establish their neighbor relationships, exacerbating the problem of excessive packets.To resolve the problem, run the **flooding-control** command on the local device to set the maximum number of Update packets that can be sent at each interval during update LSA flooding.If the interval for sending Update packets during LSA flooding is less than 100 ms, LSAs are updated at the interval of 100 ms due to the timer limit.

**Precautions**

The parameter setting in this command directly affects the flooding speed. If the setting is improper, LSAs may fail to be synchronized in time, affecting network-wide routes. Therefore, you are not advised to use this function unless otherwise specified.


Example
-------

# Set the number of Update packets to be sent during update LSA flooding to 100 and the interval for sending Update packets to 150 ms.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] flooding-control number 100 timer-interval 150

```