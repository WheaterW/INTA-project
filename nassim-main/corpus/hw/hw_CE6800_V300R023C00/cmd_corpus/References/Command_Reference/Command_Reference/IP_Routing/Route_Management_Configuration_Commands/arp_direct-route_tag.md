arp direct-route tag
====================

arp direct-route tag

Function
--------



The **arp direct-route tag** command configures a tag for ARP Vlink direct routes.

The **undo arp direct-route tag** command restores the default configuration.



By default, the tag of ARP Vlink direct routes is 0.


Format
------

**arp direct-route tag** *tag-value*

**undo arp direct-route tag** [ *tag-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *tag-value* | Specifies a tag for ARP Vlink direct routes. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the tag of ARP Vlink direct routes is 0. To change the tag of ARP Vlink direct routes, run the **arp direct-route tag** command.

**Precautions**

The configuration of the **arp direct-route tag** command takes effect only if the **arp direct-route enable** command is run in the system view or interface view.


Example
-------

# Set the tag of ARP Vlink direct routes on a VBDIF interface to 100.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] quit
[*HUAWEI] interface vbdif 10
[*HUAWEI-Vbdif10] arp direct-route tag 100

```

# Set the tag of ARP Vlink direct routes on a VLANIF interface to 100.
```
<HUAWEI> system-view
[~HUAWEI] vlan 200
[*HUAWEI-Vlan200] quit
[*HUAWEI] interface vlanif 200
[*HUAWEI-Vlanif200] arp direct-route tag 100

```