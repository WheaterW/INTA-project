info-center syslog packet-priority
==================================

info-center syslog packet-priority

Function
--------



The **info-center syslog packet-priority** command configures an output priority for Syslog packets.

The **undo info-center syslog packet-priority** command restores the default output priority of Syslog packets.



The default output priority of Syslog packets is 0.


Format
------

**info-center syslog packet-priority** *priority-level*

**undo info-center syslog packet-priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority-level* | Specifies an output priority for Syslog packets. | The value is an integer ranging from 0 to 7. A larger value indicates a higher priority. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Network packets have different priorities, and high-priority packets will be transmitted first. The default output priority of Syslog packets is 0. To output Syslog packets first, run the **info-center syslog packet-priority** command to increase the output priority of the packets based on service traffic conditions on the network.


Example
-------

# Set the output priority of Syslog packets to 3.
```
<HUAWEI> system-view
[~HUAWEI] info-center syslog packet-priority 3

```