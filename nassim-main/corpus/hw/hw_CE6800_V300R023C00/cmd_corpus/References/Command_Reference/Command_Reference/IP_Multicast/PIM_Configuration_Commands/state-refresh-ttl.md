state-refresh-ttl
=================

state-refresh-ttl

Function
--------



The **state-refresh-ttl** command configures the TTL of State-Refresh messages to be sent.

The **undo state-refresh-ttl** command restores the default TTL.



By default, the TTL of State-Refresh messages to be sent is 255.


Format
------

**state-refresh-ttl** *ttl-value*

**undo state-refresh-ttl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ttl-value* | Specifies the TTL of State-Refresh messages to be sent from an interface. | The value is an integer ranging from 1 to 255. The default value is recommended. |



Views
-----

PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a PIM-DM network, a Router deducts 1 from the TTL of a received State-Refresh message, and then sends the message to the downstream device. When the TTL is decreased to 0, the message is not forwarded. On a small-scale network, State-Refresh messages are transmitted circularly. You can modify the TTL according to the network scale by running the **state-refresh-ttl** command.

**Precautions**

The command applies only to routers directly connected to the source.


Example
-------

# In a public network instance, set the TTL to 45s for State-Refresh messages to be sent.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] state-refresh-ttl 45

```