cpu-defend host-car pps
=======================

cpu-defend host-car pps

Function
--------



The **cpu-defend host-car pps** command sets the rate limit for the user-level rate limiting.

The **undo cpu-defend host-car** command restores the default rate limit for the user-level rate limiting.



By default, the rate limit for the user-level rate limiting is 10 pps.


Format
------

**cpu-defend host-car** [ **mac-address** *mac-address* | **car-id** *car-id* ] **pps** *pps-value*

**undo cpu-defend host-car** [ **mac-address** *mac-address* | **car-id** *car-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mac-address** *mac-address* | Sets the rate limit for the specified MAC address. | The value is in the format of H-H-H. |
| **car-id** *car-id* | Sets the rate limit for the specified bucket. | The value is an integer that ranges from 0 to 8191. |
| **pps** *pps-value* | Indicates the rate limit, in pps. | The value is an integer that ranges from 1 to 128. The default value is 10. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



User-level rate limiting identifies users based on user MAC addresses and rate-limits specified user packets (ARP, ND, DHCP Request, and DHCPv6 Request packets). By default, the user-level rate limit is 10 pps. You can set different rate limits for different users.



**Precautions**

* Before using this command, run the **cpu-defend host-car enable** command to enable user-level rate limiting.
* If the rate limit is too high, attacks cannot be prevented and CPU may be overloaded.
* If both the **cpu-defend host-car mac-address** <*mac-address*> **pps** <*pps-value*> and **cpu-defend host-car pps** <*pps-value*> commands are run, the rate limit for the specified MAC address is determined by the former command, and the rate limit for other MAC addresses is determined by the latter command.
* The user-level rate limiting performs a hash calculation for the source MAC addresses of specified packets, and places the packets into different buckets. When two user MAC addresses are mapped to the same bucket index, the two users share the same rate limit (in pps mode). If the two users modify the rate limit for the bucket simultaneously, the setting will be overwritten. To avoid this situation, the rate limit for the specified MAC address cannot be set upon hash conflict.
* When the **cpu-defend host-car mac-address** <*mac-address*> **pps** <*pps-value*> and **cpu-defend host-car pps** <*pps-value*> commands are run to configure the rate limit for multiple MAC addresses, the settings are displayed in the alphabetic order in the configuration file.

Example
-------

# Set the rate limit for the user with MAC address 00e0-fc12-3456 to 30 pps.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend host-car enable
[~HUAWEI] cpu-defend host-car mac-address 00e0-fc12-3456 pps 30

```