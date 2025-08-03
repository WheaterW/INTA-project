timer recover-time
==================

timer recover-time

Function
--------



The **timer recover-time** command sets the WTR time of a Monitor Link group.

The **undo timer recover-time** command restores the default value.



By default, the WTR time of a Monitor Link group is 3s.


Format
------

**timer recover-time** *recover-time*

**undo timer recover-time** [ *recover-time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *recover-time* | Specifies the WTR time of a Monitor Link group. | The value is an integer in the range 0 to 3600, in seconds.  If this parameter is set to 0, the switchback is performed immediately. |



Views
-----

Monitor link group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If downlink interfaces go Up and Down constantly due to intermittent uplink disconnections, packet forwarding and system performance will be affected. To address this problem, run the timer recover-time command to set the WTR time of the Monitor Link group. When the uplink recovers, Monitor Link does not recover downlink interfaces until the WTR time expires, reducing the impact on system performance due to constant changes of the downlink interface status.



**Prerequisites**



A Monitor Link has been created using the **monitor-link group** command.




Example
-------

# Set the WTR time of Monitor Link group 1 to 6s.
```
<HUAWEI> system-view
[~HUAWEI] monitor-link group 1
[*HUAWEI-mtlk-group1] timer recover-time 6

```