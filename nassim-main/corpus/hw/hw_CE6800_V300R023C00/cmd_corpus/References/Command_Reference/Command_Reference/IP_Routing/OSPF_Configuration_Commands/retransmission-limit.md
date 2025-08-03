retransmission-limit
====================

retransmission-limit

Function
--------



The **retransmission-limit** command sets the maximum number of retransmissions.

The **undo retransmission-limit** command disables the retransmission limit.



By default, the number of retransmissions is not set.


Format
------

**retransmission-limit** *max-number*

**retransmission-limit**

**undo retransmission-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-number* | Specifies the maximum number of retransmissions. | The value is an integer ranging from 2 to 255. The default value is 30. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **retransmission-limit** command can be used to enable retransmission limit for OSPF (RL-for OSPF) to prevent dead loops caused by repeated transmissions when neighbors cannot receive packets.

**Configuration Impact**

The OSPF retransmission limit takes effect on the following packets:

* DD packets
* Update packets
* Request packetsIf the three types of packets cannot receive response packets, enable RL-for OSPF, limit the number of retransmissions, and disconnect the neighbor when the number of retransmissions exceeds the specified value.

Example
-------

# Enable OSPF retransmission limit and set the maximum number of retransmissions to 40.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] retransmission-limit 40

```