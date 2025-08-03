anti-attack icmp-flood car
==========================

anti-attack icmp-flood car

Function
--------



The **anti-attack icmp-flood car** command sets the rate limit of ICMP flood attack packets.

The **undo anti-attack icmp-flood car** command restores the default rate limit of ICMP flood attack packets.



By default, the rate limit of ICMP flood attack packets is 155000000 bit/s.


Format
------

**anti-attack icmp-flood car cir** *cir-num*

**undo anti-attack icmp-flood car**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cir** *cir-num* | Specifies the CIR. | Integer type. Range: 8000-155000000. The default value is 155000000, in bit/s. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After defense against ICMP flood attacks is enabled, run the anti-attack icmp-flood car command to set the rate limit of ICMP flood attack packets. If the rate of received ICMP flood attack packets exceeds the rate limit, the device discards excess ICMP flood attack packets to ensure that its CPU works properly.


Example
-------

# Set the rate limit of ICMP flood attack packets to 8000 bit/s.
```
<HUAWEI> system-view
[~HUAWEI] anti-attack icmp-flood enable
[*HUAWEI] anti-attack icmp-flood car cir 8000

```