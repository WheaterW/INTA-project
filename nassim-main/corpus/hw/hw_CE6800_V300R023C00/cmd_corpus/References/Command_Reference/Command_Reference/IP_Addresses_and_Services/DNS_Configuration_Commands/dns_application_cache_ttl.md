dns application cache ttl
=========================

dns application cache ttl

Function
--------



The **dns application cache ttl** command sets the maximum and minimum of the TTL of the cache of application domain name resolution.

The **undo dns application cache ttl** command sets the maximum and minimum of the TTL of the cache of application domain name resolution to the default value.



By default, the maximum of the ttl of the DNS application cache is 86400 seconds, and the minimum of the ttl is 600 seconds.


Format
------

**dns application cache ttl maximum** *max-seconds* **minimum** *min-seconds*

**undo dns application cache ttl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **minimum** *min-seconds* | Specify the minimum of the TTL of the cache of application domain name resolution. | The value is an integer ranging from 60 to 4294967295, in second. The default value is 600. |
| **maximum** *max-seconds* | Specify the maximum of the TTL of the cache of application domain name resolution. | The value is an integer ranging from 60 to 4294967295, in second. The default value is 86400. The value of max-seconds must be larger than or equal to that of min-seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The device sends requests of domain name resolution to the DNS server according to the TTL of the cache of application domain name resolution. If the TTL is too short, the CPU occupancy can increase. If the TTL is too long, the updates cannot be performed in time. The administrator can properly set the maximum and minimum of the TTL of the cache of application domain name resolution by running this command. If the default TTL of application domain names is less than the minimum TTL configured on the device, the device periodically resolves domain names to the DNS server based on the configured minimum TTL. If the default TTL of application domain names is between the minimum and maximum TTLs configured on the device, the default TTL is retained. If the default TTL of application domain names is greater than the maximum TTL configured on the device, the device periodically resolves domain names based on the configured maximum TTL.


Example
-------

# Set the maximum and minimum of the TTL of the cache of application domain name resolution to 10 minutes and 1 minute respectively.
```
<HUAWEI> system-view
[~HUAWEI] dns application cache ttl maximum 600 minimum 60

```