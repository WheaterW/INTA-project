tcp timer fin-timeout
=====================

tcp timer fin-timeout

Function
--------



The **tcp timer fin-timeout** command sets a TCP FIN-Wait timer.

The **undo tcp timer fin-timeout** command restores the default value.



By default, the value of the TCP FIN-Wait timer is 675 seconds.


Format
------

**tcp timer fin-timeout** *interval*

**undo tcp timer fin-timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the value of TCP FIN-Wait timer in seconds. | It is an integer ranging from 76 to 3600. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When the TCP connection status changes from FIN\_WAIT\_1 to FIN\_WAIT\_2, the FIN-Wait timer is enabled. If no FIN packet is received before the timeout of FIN-Wait timer, the TCP connection is terminated.



**Precautions**



If this command is configured for several times in the same view, only the last configuration takes effect.You are recommended to configure the parameter under the guidance of the technical personnel.




Example
-------

# Configure the TCP FIN-Wait timer value to 600 seconds.
```
<HUAWEI> system-view
[~HUAWEI] tcp timer fin-timeout 600

```