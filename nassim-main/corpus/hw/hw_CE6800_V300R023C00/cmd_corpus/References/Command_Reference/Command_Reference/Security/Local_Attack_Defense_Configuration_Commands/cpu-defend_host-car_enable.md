cpu-defend host-car enable
==========================

cpu-defend host-car enable

Function
--------



The **cpu-defend host-car enable** command enables user-level rate limiting.

The **undo cpu-defend host-car enable** command disables user-level rate limiting.



By default, user-level rate limiting is not enabled.


Format
------

**cpu-defend host-car enable**

**undo cpu-defend host-car enable**


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



User-side hosts are prone to virus attacks, and infected hosts can send a large number of protocol packets to devices, overloading device CPUs and deteriorating their performance, which ultimately impacting services. You can configure user-level rate limiting to address this issue. User-level rate limiting identifies users based on MAC addresses and limits the rate of specified packets. By default, the threshold for each user MAC address is 10 pps.Compared to CPCAR based on boards, rate limiting based on user MAC addresses can be accurate to each user and has little impact on normal users.



**Precautions**

* After you run the **undo cpu-defend host-car enable** command to disable user-level rate limiting, all configurations related to user-level rate limiting are deleted or restored to the default values.
* You are advised to disable user-level rate limiting on network-side ports of access devices and network interconnection ports of gateway devices.
* During user-level rate limiting, the system performs a hash calculation for the source MAC addresses of specified packets, and places the packets into different buckets. Therefore, multiple users may share the rate limit. When the traffic volume is heavy on the network, packets may be dropped. If you confirm that these users are authorized, run the **cpu-defend host-car mac-address** command to increase the rate threshold for the specified MAC addresses.

Example
-------

# Disable user-level rate limiting.
```
<HUAWEI> system-view
[~HUAWEI] undo cpu-defend host-car enable

```