dns resolve
===========

dns resolve

Function
--------



The **dns resolve** command enables dynamic DNS resolution.

The **undo dns resolve** command disables dynamic DNS resolution.



By default, dynamic DNS resolution is disabled.


Format
------

**dns resolve**

**undo dns resolve**


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

To obtain IP addresses mapping domain names from the DNS server, run the **dns resolve** command to enable dynamic DNS resolution on the device.

**Precautions**

The DNS module only checks the basic format of the IP address in the reply packet from the DNS server. The service module that processes the domain name resolution request determines whether the IP address is available. For the DNS module, the IP address resolved from the DNS server is valid as long as it complies with the basic address format.


Example
-------

# Enable dynamic DNS resolution.
```
<HUAWEI> system-view
[~HUAWEI] dns resolve

```