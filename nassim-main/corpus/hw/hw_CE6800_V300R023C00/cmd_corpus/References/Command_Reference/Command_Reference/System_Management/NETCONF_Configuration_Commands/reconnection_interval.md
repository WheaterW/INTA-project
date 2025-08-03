reconnection interval
=====================

reconnection interval

Function
--------



The **reconnection interval** command configures an interval at which a device firstly sends NETCONF connection requests to the NMS.

The **undo reconnection interval** command restores the default interval at which a device sends NETCONF connection requests to the NMS.



By default, a device firstly sends NETCONF connection requests to the NMS at an interval of 5s.


Format
------

**reconnection interval** *interval*

**undo reconnection interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which the device firstly sends NETCONF connection requests to the NMS. | The value is an integer ranging from 5 to 300, in seconds. The default value is 5. |



Views
-----

Callhome view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When configuring proactive NETCONF registration, you can configure an interval at which the device sends NETCONF connection requests firstly to the NMS using the **reconnection interval** command.The subsequent reconnection interval is exponentially backoff by multiplying two. A maximum of five backoffs are performed. Then, the reconnection interval returns to the initial value and performs cyclic backoff again according to the preceding policy. If the intermediate backoff time is greater than 300s, 300s is used as the retry time to perform this backoff. Then, the system returns to the initial value and performs cyclic backoff again.The formula is as follows: s = t\*2^(n â 1), s is the current backoff time, the maximum value of s is 300s, t is the first backoff time, n is the number of reconnections, and the maximum value of n is 5.


Example
-------

# Set the interval at which the device firstly sends NETCONF connection requests to the NMS to 30s.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] callhome root
[*HUAWEI-netconf-callhome-root] reconnection interval 30

```