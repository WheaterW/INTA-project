ipv6 nd na anti-attack rate-limit
=================================

ipv6 nd na anti-attack rate-limit

Function
--------



The **ipv6 nd na anti-attack rate-limit** command configures the rate at which Neighbor Advertisement (NA) messages are sent, that is, the number of ND messages allowed to be processed per second.

The **undo ipv6 nd na anti-attack rate-limit** command restores the default configuration.



By default, 2000 NA messages are sent per second.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd na anti-attack rate-limit** *limit-number*

**undo ipv6 nd na anti-attack rate-limit** *limit-number*

**undo ipv6 nd na anti-attack rate-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit-number* | Specifies the rate at which NA messages are sent. | The value is an integer in the range of 1 to 5000, in packets per second. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a device is under an attack, a large number of NA messages are received within a short period of time. As a result, lots of CPU resources are used in neighbor entry learning and response, which affects the processing of other services. To resolve this problem, run the ipv6 nd na anti-attack rate-limit command to configure the rate at which NA messages are sent. With this configuration, when the number of NA messages received exceeds the specified threshold, the device discards the excess NA messages.


Example
-------

# Configure the rate at which NA messages are sent as 3000.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd na anti-attack rate-limit 3000

```