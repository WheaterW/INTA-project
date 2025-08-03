vrrp member-lbrg timer hello
============================

vrrp member-lbrg timer hello

Function
--------



The **vrrp member-lbrg timer hello** command configures an interval at which the master device in a load-balance redundancy group (LBRG) configured using a service VRRP group sends VRRP Advertisement packets.

The **undo vrrp member-lbrg timer hello** command restores the default interval.



By default, the interval is 120s.


Format
------

**vrrp member-lbrg timer hello** *hello-time*

**undo vrrp member-lbrg timer hello** [ *hello-time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *hello-time* | Specifies an interval at which the master device in an LBRG configured using a service VRRP group sends VRRP Advertisement packets. | The value is an integer ranging from 10 to 120, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a service VRRP group is configured as an LBRG, it does not periodically send gratuitous ARP packets (for VRRP4) or ND packets (for VRRP6) to update MAC entries on a downstream device. To prevent a master/backup switchover from occurring on the LBRG and ensure that the downstream device promptly updates MAC entries, the master device in the LBRG periodically sends VRRP Advertisement packets to update the MAC address of the downstream device.To ensure that the MAC entries on the downstream device can be promptly updated, you can configure an interval at which the master device in the LBRG sends VRRP Advertisement packets to meet requirements for network reliability.

**Precautions**

The command takes effect only for service VRRP load balancing groups in single-gateway load balancing scenarios and supports both service VRRP4 and VRRP6 LBRGs.


Example
-------

# Set an interval at which the master device in an LBRG configured using a service VRRP group sends VRRP Advertisement packets to 100s.
```
<HUAWEI> system-view
[~HUAWEI] vrrp member-lbrg timer hello 100

```