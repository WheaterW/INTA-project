anti-attack tcp-syn car
=======================

anti-attack tcp-syn car

Function
--------



The **anti-attack tcp-syn car** command sets the rate limit at which TCP SYN packets are received.

The **undo anti-attack tcp-syn car** command restores the default rate limit at which TCP SYN packets are received.



By default, the rate limit at which TCP SYN packets are received is 155000000 bit/s.


Format
------

**anti-attack tcp-syn car cir** *cir-num*

**undo anti-attack tcp-syn car**


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

After defense against TCP SYN flood attacks is enabled, run the anti-attack tcp-syn car command to set the rate limit at which TCP SYN packets are received. If the rate of received TCP SYN attack packets exceeds the rate limit, the device discards excess TCP SYN flood attack packets to ensure that the device CPU works properly.This command takes effect only when defense against TCP SYN flood is enabled.


Example
-------

# Set the rate limit at which TCP SYN packets are received to 8000 bit/s.
```
<HUAWEI> system-view
[~HUAWEI] anti-attack tcp-syn enable
[*HUAWEI] anti-attack tcp-syn car cir 8000

```