anti-attack fragment car
========================

anti-attack fragment car

Function
--------



The **anti-attack fragment car** command limits the rate of packet fragments.

The **undo anti-attack fragment car** command restores the rate limit of packet fragments.



By default, the rate of packet fragments is limited and the maximum rate is 155000000 bit/s.


Format
------

**anti-attack fragment car cir** *cir-num*

**undo anti-attack fragment car**


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

After defense against packet fragment attacks is enabled, run the anti-attack fragment car command to set the rate limit of packet fragments. If the rate of received packet fragments exceeds the rate limit, the device discards excess packet fragments to ensure that the device CPU works properly.This command takes effect only when defense against packet fragment attacks is enabled.


Example
-------

# Set the rate limit of packet fragments to 8000 bit/s.
```
<HUAWEI> system-view
[~HUAWEI] anti-attack fragment enable
[*HUAWEI] anti-attack fragment car cir 8000

```