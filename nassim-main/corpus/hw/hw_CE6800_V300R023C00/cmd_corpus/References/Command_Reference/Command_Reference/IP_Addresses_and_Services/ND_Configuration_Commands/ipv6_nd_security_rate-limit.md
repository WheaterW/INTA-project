ipv6 nd security rate-limit
===========================

ipv6 nd security rate-limit

Function
--------



The **ipv6 nd security rate-limit** command sets a rate limit for the system to compute or verify the RSA signature in a specified period (1s).

The **undo ipv6 nd security rate-limit** command deletes a rate limit.



By default, the rate limit for the system to compute or verify the RSA signature is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd security rate-limit** *ratelimit-value*

**undo ipv6 nd security rate-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ratelimit-value* | Specifies a rate limit for the system to compute or verify the RSA signature in a specified period (1s). | The value is an integer ranging from 1 to 100, in messages per second. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If an attacker keeps sending SEND messages to a device, the device will be busy verifying the RSA signature. To limit the rate at which the interface verifies the RSA signature of the SEND messages, you can run the ipv6 nd security rate-limit command. If the rate at which the interface verifies the RSA signature of the SEND messages is out of the allowed range, the device will regard these messages insecure and discard them.


Example
-------

# Configure the system to process a maximum of 10 received ND messages per second.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd security rate-limit 10

```