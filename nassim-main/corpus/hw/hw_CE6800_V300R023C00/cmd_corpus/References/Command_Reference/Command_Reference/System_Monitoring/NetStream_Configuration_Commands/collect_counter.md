collect counter
===============

collect counter

Function
--------



The **collect counter** command allows the flexible flow statistics exported to the NetStream Collector (NSC) to contain the number of bytes and packets.

The **undo collect counter** command restores the default setting.



By default, the flexible flow statistics exported to the NSC do not contain the number of bytes or packets.


Format
------

**collect counter** { **bytes** | **packets** }

**undo collect counter** { **bytes** | **packets** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bytes** | Indicates that the flexible flow statistics exported to NSC contain the number of bytes. | - |
| **packets** | Indicates that the flexible flow statistics exported to NSC contain the number of packets. | - |



Views
-----

IPv4 flexible flow statistics template view,IPv6 flexible flow statistics template view,VXLAN flexible flow statistics template view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To obtain richer flow statistics, configure whether flexible flow statistics contain the number of bytes and packets.

**Prerequisites**

A flexible flow statistics template has been created.

**Precautions**

If a flexible flow statistics template has been applied to an interface, the template configuration cannot be modified or deleted.


Example
-------

# Configure the flexible flow statistics template record1 to export the flexible flow statistics containing the number of packets to the NSC.
```
<HUAWEI> system-view
[~HUAWEI] netstream record record1 ip
[*HUAWEI-netstream-record-ipv4-record1] collect counter packets

```