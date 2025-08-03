ntp high-precision-time client enable
=====================================

ntp high-precision-time client enable

Function
--------



The **ntp high-precision-time client enable** command sets the interval at which a high-precision NTP client sends packets.

The **undo ntp high-precision-time client enable** command cancels the interval at which a high-precision NTP client sends packets.



By default, the interval at which a high-precision NTP client sends packets is not set.


Format
------

**ntp high-precision-time client enable poll-interval** [ *poll-interval-time* ]

**undo ntp high-precision-time client enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *poll-interval-time* | Specifies the polling interval for sending NTP packets. | The value is an integer ranging from 50 to 2500, in milliseconds. The default value is 200. |
| **poll-interval** | Specifies the polling interval for sending packets. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

For an NE client that requires high-precision time, you can run the command to enable the NTP high-precision client function and set the polling interval for sending packets.

**Precautions**



After the high-precision client function is configured on the device, the NTP packet sending rate is changed.




Example
-------

# Enable the NTP high-precision client function and set the packet sending interval to 100 ms.
```
<HUAWEI> system-view
[~HUAWEI] ntp high-precision-time client enable poll-interval 100
Info: The NTP High-precision function is only supported on unicast-server, unicast-peer and manycast modes.
Warning: After this configuration is committed, the polling interval of the client is subject to this configuration. Continue? [Y/N]:Y

```