dscp (Subscription view)
========================

dscp (Subscription view)

Function
--------



The **dscp** command configures a DSCP value for data packets sent.

The **undo dscp** command restores the default DSCP value of data packets sent.



By default, the DSCP value of a data packet sent is 0.


Format
------

**dscp** *value*

**undo dscp**

**undo dscp** *value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the DSCP value for a data packet sent. | The value is an integer ranging from 0 to 63. |



Views
-----

Subscription view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



The DSCP value is designed to ensure the communication service quality. It is an 8-bit identifier contained in an IP packet header, and identifies service types and priorities.When network data transmission is stable, Telemetry does not need to change the DSCP value of the data packets sent. When packet loss occurs during data transmission, you can configure a DSCP value in the Telemetry view for the data packets sent. You can improve the priority of packet transmission to ensure the quality of network data transmission.



**Precautions**



The command is an overriding one, and only the last configuration takes effect.




Example
-------

# Set the DSCP value for data packets sent to 60.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] subscription test
[*HUAWEI-telemetry-subscription-test] dscp 60

```