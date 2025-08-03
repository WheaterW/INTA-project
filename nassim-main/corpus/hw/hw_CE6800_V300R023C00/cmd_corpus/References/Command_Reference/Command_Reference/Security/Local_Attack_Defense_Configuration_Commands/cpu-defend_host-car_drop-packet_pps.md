cpu-defend host-car drop-packet pps
===================================

cpu-defend host-car drop-packet pps

Function
--------



The **cpu-defend host-car drop-packet pps** command sets the rate limit for the packets that are discarded during user-level rate limiting and are sent to the CPU.

The **undo cpu-defend host-car drop-packet pps** command restores the default rate limit.



By default, the rate limit for packets discarded in user-level rate limiting is 64 pps.


Format
------

**cpu-defend host-car drop-packet pps** *pps-value*

**undo cpu-defend host-car drop-packet pps**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pps-value* | Rate limit for the packets that are discarded because the user-level rate limit is exceeded and sent to the CPU. | The value is an integer that ranges from 1 to 256, in pps. The default value is 64. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After you run the **undo cpu-defend host-car drop-packet monitor disable** command to enable packet loss monitoring for user-level rate limiting, the packets discarded due to user-level rate limiting are sent to the CPU. In this case, you can run the **cpu-defend host-car drop-packet pps** command to adjust the rate limit for these packets to be sent to the CPU.

**Prerequisites**

Packet loss monitoring for user-level rate limiting has been enabled using the **undo cpu-defend host-car drop-packet monitor disable** command.


Example
-------

# Set the rate limit for packets discarded due to user-level rate limiting to 100 pps.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend host-car enable
[*HUAWEI] undo cpu-defend host-car drop-packet monitor disable
[*HUAWEI] cpu-defend host-car drop-packet pps 100

```