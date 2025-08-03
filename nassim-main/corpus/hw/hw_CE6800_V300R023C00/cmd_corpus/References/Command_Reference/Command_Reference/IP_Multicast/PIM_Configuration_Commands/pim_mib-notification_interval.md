pim mib-notification interval
=============================

pim mib-notification interval

Function
--------



The **pim mib-notification interval** command sets the interval for PIM to send trap messages about various events.

The **undo pim mib-notification interval** command restores the default interval for PIM to send various trap messages.



By default, an alarm is generated only when a neighbor loss event or a neighbor addition event occurs. No alarm is generated when the other events occur.


Format
------

**pim mib-notification interval** { **interface-election-dr** *election-value* | **invalid-join-prune** *jp-value* | **invalid-register** *register-value* | **neighbor-loss** *loss-value* | **new-neighbor** *new-value* | **rp-mapping-change** *change-value* }

**undo pim mib-notification interval all**

**undo pim mib-notification interval interface-election-dr**

**undo pim mib-notification interval invalid-join-prune**

**undo pim mib-notification interval invalid-register**

**undo pim mib-notification interval neighbor-loss**

**undo pim mib-notification interval new-neighbor**

**undo pim mib-notification interval rp-mapping-change**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface-election-dr** *election-value* | Specifies the minimum interval for sending trap messages about designated router (DR) election. | The value is an integer that ranges from 0 to 65535, in seconds. The default value is 65535 seconds. |
| **invalid-join-prune** *jp-value* | Specifies the minimum interval for sending trap messages about invalid Join/Prune messages. | The value is an integer that ranges from 10 to 65535, in seconds. The default value is 65535 seconds. |
| **invalid-register** *register-value* | Specifies the minimum interval for sending trap messages about invalid Register messages. | The value is an integer that ranges from 10 to 65535, in seconds. The default value is 65535 seconds. |
| **neighbor-loss** *loss-value* | Specifies the minimum interval for sending trap messages about neighbor loss. | The value is an integer that ranges from 0 to 65535, in seconds. The default value is 0 seconds. |
| **new-neighbor** *new-value* | Specifies the minimum interval for sending trap messages about neighbor addition. | The value is an integer that ranges from 0 to 65535, in seconds. The default value is 0 seconds. |
| **rp-mapping-change** *change-value* | Specifies the minimum interval for sending trap messages about the Rendezvous Point (RP)-mapping change. | The value is an integer that ranges from 0 to 65535, in seconds. The default value is 65535 seconds. |
| **all** | Specifies to undo all the minimum intervals for sending trap messages. | - |



Views
-----

Multicast MIB view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The pim mib-notification interval command sets the interval for sending trap messages. When an event occurs, if the period since the last time for sending the trap message is shorter than the configured interval, the system does not send any trap message.

* If the default interval is 0, it indicates that a trap message is sent immediately after an event occurs.
* If the default interval is 65535, it indicates that no trap message is sent after an event occurs. Then run this command to adjust the interval to a smaller value so that a trap message can be sent after an event occurs.

Example
-------

# Set the interval for PIM to send trap messages about invalid Join/Prune messages.
```
<HUAWEI> system-view
[~HUAWEI] multicast mib
[*HUAWEI-multicast-mib] pim mib-notification interval invalid-join-prune 50

```