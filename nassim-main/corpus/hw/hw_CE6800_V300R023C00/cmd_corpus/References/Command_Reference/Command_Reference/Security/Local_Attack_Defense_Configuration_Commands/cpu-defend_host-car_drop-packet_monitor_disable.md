cpu-defend host-car drop-packet monitor disable
===============================================

cpu-defend host-car drop-packet monitor disable

Function
--------



The **cpu-defend host-car drop-packet monitor disable** command disables packet loss monitoring for user-level rate limiting.

The **undo cpu-defend host-car drop-packet monitor disable** command enables packet loss monitoring for user-level rate limiting.



By default, packet loss monitoring for user-level rate limiting is enabled.


Format
------

**cpu-defend host-car drop-packet monitor disable**

**undo cpu-defend host-car drop-packet monitor disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After user-level rate limiting is enabled, if the number of packets with the same source MAC address received by the device within a specified period exceeds the rate limit, the device discards the excess packets. To check which packets are discarded, enable packet loss monitoring for user-level rate limiting.

**Prerequisites**

User-level rate limiting has been enabled using the **cpu-defend host-car enable** command.

**Precautions**

After you run the **cpu-defend host-car drop-packet monitor disable** command to disable packet loss monitoring for user-level rate limiting, the **cpu-defend host-car drop-packet pps** command configuration will be deleted.


Example
-------

# Enable monitoring for packets discarded due to user-level rate limiting.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend host-car enable
[*HUAWEI] undo cpu-defend host-car drop-packet monitor disable

```