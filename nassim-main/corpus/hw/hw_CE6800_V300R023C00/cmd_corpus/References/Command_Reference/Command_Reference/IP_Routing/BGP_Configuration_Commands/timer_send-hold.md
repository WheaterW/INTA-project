timer send-hold
===============

timer send-hold

Function
--------



The **timer send-hold** command sets the holdtime of a BGP session on the sender.

The **undo timer send-hold** command restores the default value.



By default, the session holdtime is 86400 seconds.


Format
------

**timer send-hold** *send-hold-time*

**undo timer send-hold** *send-hold-time*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **send-hold** *send-hold-time* | Specifies the interval for holding a session when the local end fails to send messages. | The value is 0 or an integer ranging from 360 to 172800, in seconds. The default value is 86400. The value 0 indicates that the function is disabled. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After establishing a BGP connection, peers periodically send Keepalive messages to each other to maintain the validity of the BGP connection.If both BGP Update and Keepalive messages fail to be sent within twice the hold-time, an alarm is reported. If the alarm is not cleared within the period specified by send-hold-time, the BGP connection is reset.

**Precautions**

BGP messages are sent to peers through an update peer-group. When there is only one peer in the update peer-group or there is no message in the update peer-group, the session hold time does not take effect.When the keeplive-time negotiated between peers is 0, the keepalive timer is not started and the session hold time does not take effect.


Example
-------

# Set the BGP session hold time to 720 seconds.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] timer send-hold 720

```