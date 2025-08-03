tcp timer syn-timeout
=====================

tcp timer syn-timeout

Function
--------



The **tcp timer syn-timeout** command sets the TCP SYN-Wait timer.

The **undo tcp timer syn-timeout** command restores the default value of the timer.



By default, the value of the TCP SYN-Wait timer is 75 seconds.


Format
------

**tcp timer syn-timeout** *interval*

**undo tcp timer syn-timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the value of TCP SYN-Wait timer in seconds. | The value ranges from 2 to 600 seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When a SYN packet is sent, TCP enables the SYN-Wait timer. If no response packet is received before SYN-Wait is timeout, the TCP connection is terminated.



**Configuration Impact**



The SYN-Wait timer starts when an SYN packet is sent. A TCP connection is torn down if no response packet is received before the SYN-Wait timer expires.



**Precautions**



If this command is configured for several times in the same view, only the last configuration takes effect.You are recommended to configure the parameters under the guidance of the technical personnel.




Example
-------

# Set the TCP SYN-Wait timer to 100 seconds.
```
<HUAWEI> system-view
[~HUAWEI] tcp timer syn-timeout 100

```