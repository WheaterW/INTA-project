arp direct-route delay
======================

arp direct-route delay

Function
--------



The **arp direct-route delay** command sets a delay in advertising ARP Vlink direct routes on an interface.

The **undo arp direct-route delay** command deletes the delay in advertising ARP Vlink direct routes.



By default, no delay is set for advertising ARP Vlink direct routes.


Format
------

**arp direct-route delay** *delay-time*

**undo arp direct-route delay** [ *delay-time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-time* | Specifies a delay in advertising ARP Vlink direct routes on an interface. | The value is an integer ranging from 1 to 3600, in seconds. |



Views
-----

VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **arp direct-route delay** command sets a delay in advertising ARP Vlink direct routes on an interface.




Example
-------

# Set a delay in advertising ARP Vlink direct routes on a VLANIF interface.
```
<HUAWEI> system-view
[~HUAWEI] vlan 200
[*HUAWEI-Vlan200] quit
[*HUAWEI] interface vlanif 200
[*HUAWEI-vlanif200] arp direct-route delay 5

```