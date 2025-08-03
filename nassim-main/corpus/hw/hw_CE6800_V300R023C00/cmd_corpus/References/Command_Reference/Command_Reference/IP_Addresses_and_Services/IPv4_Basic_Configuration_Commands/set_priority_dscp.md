set priority dscp
=================

set priority dscp

Function
--------



The **set priority dscp** command sets a DSCP value for protocol packets.

The **undo set priority dscp** command cancels the DSCP value configured for protocol packets.



By default, the DSCP value is not configured for protocol packets.


Format
------

**set priority dscp** *dscp-value*

**undo set priority dscp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dscp-value* | Specifies the DSCP value of protocol packets. A larger value indicates a higher priority. | The value is an integer ranging from 0 to 63. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



During network planning and deployment, if the DSCP value of a device is determined, configure the device to send protocol packets carrying this DSCP value. After the upstream device receives the protocol packets, it can schedule the packets into different queues based on the DSCP values in the packets. This allows packets sent from devices of higher priorities to be scheduled preferentially.



**Precautions**



The **set priority dscp** command configures a DSCP priority for host protocol packets. The configuration takes effect only for IP packets sent to hosts.




Example
-------

# Set the DSCP value of all host protocol packets to 10.
```
<HUAWEI> system-view
[~HUAWEI] set priority dscp 10

```