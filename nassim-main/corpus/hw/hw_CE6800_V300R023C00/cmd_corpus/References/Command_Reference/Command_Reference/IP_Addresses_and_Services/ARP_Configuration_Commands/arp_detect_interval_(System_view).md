arp detect interval (System view)
=================================

arp detect interval (System view)

Function
--------



The **arp detect interval** command sets the aging probe interval of dynamic ARP entries.

The **undo arp detect interval** command restores the default setting.



By default, the aging probe interval of dynamic ARP entries is 5 seconds.


Format
------

**arp detect interval** *interval-value*

**undo arp detect interval** [ *interval-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interval** *interval-value* | Specifies the aging probe interval of dynamic ARP entries. | The value is an integer ranging from 1 to 5, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To set the aging probe interval of dynamic ARP entries, run the **arp detect interval** command. Before aging a dynamic ARP entry, the system initiates detection. If the system does not receive any response within the detection interval, the system deletes the entry.



**Configuration Impact**



After the aging probe interval of dynamic ARP entries is set, the system detects dynamic ARP entries at this interval before aging the entries.



**Precautions**



The value obtained by multiplying the aging probe times by the aging probe interval must be smaller than the aging time of entries.




Example
-------

# Set the aging probe interval to 3 seconds for dynamic ARP entries on system-view.
```
<HUAWEI> system-view
[~HUAWEI] arp detect interval 3

```