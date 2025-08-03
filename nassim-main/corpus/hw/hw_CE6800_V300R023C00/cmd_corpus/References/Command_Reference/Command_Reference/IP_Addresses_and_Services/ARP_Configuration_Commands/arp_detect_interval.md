arp detect interval
===================

arp detect interval

Function
--------



The **arp detect interval** command sets the aging probe interval of dynamic Address Resolution Protocol (ARP) entries.

The **undo arp detect interval** command restores the default setting.



By default, the aging probe interval of dynamic ARP entries is 5 seconds.


Format
------

**arp detect interval** *detect-interval*

**undo arp detect interval** [ *detect-interval* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *detect-interval* | Specifies the aging probe interval of dynamic ARP entries. | The value is an integer ranging from 1 to 5, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Interface group view,Management interface view


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

# Set the aging probe interval to 3 seconds for dynamic ARP entries on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] arp detect interval 3

```