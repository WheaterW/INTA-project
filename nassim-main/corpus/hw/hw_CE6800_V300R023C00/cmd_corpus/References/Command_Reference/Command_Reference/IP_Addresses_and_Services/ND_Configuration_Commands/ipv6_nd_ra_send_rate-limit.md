ipv6 nd ra send rate-limit
==========================

ipv6 nd ra send rate-limit

Function
--------



The **ipv6 nd ra send rate-limit** command sets a limit on the rate at which router advertisement (RA) messages are sent.

The **undo ipv6 nd ra send rate-limit** command restores the default rate limit.



The default rate limit for sending RA messages is 550 per second.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd ra send rate-limit** *rate-limit*

**undo ipv6 nd ra send rate-limit** *rate-limit*

**undo ipv6 nd ra send rate-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rate-limit* | Specifies a limit on the rate at which RA messages are sent. | The value is an integer ranging from 1 to 1000, representing RA messages per second. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the remote device has a limited capability of receiving RA messages or the local device has a limited capability of processing router solicitation (RS) messages, run the **ipv6 nd ra send rate-limit** command on the local device to set a limit on the rate at which RA messages are sent. This prevents a host from failing to update the default routing information.

**Configuration Impact**

If the rate limit is set to a small value, the rate at which a host updates the default routing information becomes slow.


Example
-------

# Set a limit on the rate at which RA messages are sent to 500 in the system view.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd ra send rate-limit 500

```