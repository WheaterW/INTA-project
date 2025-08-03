arp fake timeout
================

arp fake timeout

Function
--------



The **arp fake timeout** command sets the aging expiry time of a fake dynamic Address Resolution Protocol (ARP) entry.

The **undo arp fake timeout** command restores the default aging expiry time of a fake dynamic ARP entry.



By default, the aging expiry time of a fake dynamic ARP entry is 5s.


Format
------

**arp fake timeout** *expire-time*

**undo arp fake timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *expire-time* | Specifies the aging expiry time of a fake dynamic ARP entry. | The value is an integer ranging from 1 to 36000 in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a new aging time is configured for fake ARP entries on an interface, this time takes effect only for newly generated fake ARP entries.


Example
-------

# Set the aging expiry time of fake dynamic ARP entries on interface to 10s.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] arp fake timeout 10

```