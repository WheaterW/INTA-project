ipv4 reassembling timeout
=========================

ipv4 reassembling timeout

Function
--------



The **ipv4 reassembling timeout** command sets the reassembly timeout period of IPv4 fragments.

The **undo ipv4 reassembling timeout** command restores the reassembly timeout period to the default value.



By default, the reassembly timeout period of IPv4 fragments is 30s.


Format
------

**ipv4 reassembling timeout** *time*

**undo ipv4 reassembling timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time* | Specifies the reassembly timeout period of IPv4 fragments. | The value is an integer ranging from 5 to 120, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To improve device performance and prevent attacks, set a proper reassembly timeout period to ensure that IPv4 fragments that have waited for reassembly for a long time are aged in time.



**Configuration Impact**



If time is set too long, it is probable that a large number of fragments are stored on the device, waiting to be reassembled. This wastes resources, reduces device performance, and may cause network attacks. Therefore, you are not recommended to set time too long.



**Precautions**



Packet fragmentation is performed on outbound interfaces, and inbound interfaces do not fragment packets.




Example
-------

# Set the reassembly timeout period of IPv4 fragments to 20s in the system view.
```
<HUAWEI> system-view
[~HUAWEI] ipv4 reassembling timeout 20

```