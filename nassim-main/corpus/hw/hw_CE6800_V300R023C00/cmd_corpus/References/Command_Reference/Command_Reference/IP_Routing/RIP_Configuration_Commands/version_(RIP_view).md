version (RIP view)
==================

version (RIP view)

Function
--------



The **version** command specifies a global RIP version.

The **undo version** command restores the default version.



By default, the RIP version is RIP-1.


Format
------

**version** *version-num*

**undo version**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *version-num* | Indicates a RIP version. | The value can be 1 or 2. |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If the RIP version number is set to 1, only RIP-1 packets are sent and accepted.If RIP version 2 is specified, RIP-2 packets are sent in multicast mode, and RIP-2 packets in multicast or broadcast mode are accepted.



**Configuration Impact**

If the version of RIP running on a device is changed, the routing information in a routing table is deleted and needs to be learned again.


Example
-------

# Enable RIP to send and receive RIP-2 packets.
```
<HUAWEI> system-view
[~HUAWEI] rip 100
[*HUAWEI-rip-100] version 2

```