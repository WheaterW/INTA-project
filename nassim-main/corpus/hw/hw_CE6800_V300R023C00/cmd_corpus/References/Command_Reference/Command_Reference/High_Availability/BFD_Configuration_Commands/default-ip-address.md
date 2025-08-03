default-ip-address
==================

default-ip-address

Function
--------



The **default-ip-address** command configures the default multicast address for a BFD session.

The **undo default-ip-address** command restores the default multicast address for a BFD session.



By default, the default multicast address for a BFD session is 224.0.0.184.


Format
------

**default-ip-address** *default-ip-value*

**undo default-ip-address** [ *default-ip-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *default-ip-value* | Specifies the multicast address for a BFD session. | The value ranges from 224.0.0.107 to 224.0.0.250, in dotted decimal notation. |



Views
-----

BFD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the physical status of a link is to be monitored and the peer IP address is unavailable (for example, when no peer IP address exists on an Eth-Trunk member link), you can bind a BFD session to a multicast address and enable BFD control packets to be sent to the multicast address before BFD monitors the physical status.You must change the default multicast address in either of the following situations:

* Other protocols use this multicast address on a live network.
* Multiple BFD sessions detect faults in a specified path. If BFD detects faults in a link between Layer 3 interfaces and these Layer 3 interfaces are connected by BFD-capable Layer 2 switching devices, multiple BFD sessions function. These BFD sessions must be configured with different default multicast addresses.

**Prerequisites**

BFD has been globally enabled using the **bfd** command in the system view.

**Configuration Impact**

All established BFD sessions associated with multicast will use this configured multicast address.

**Follow-up Procedure**

Run the **bfd bind peer-ip default-ip** command to configure a BFD session before using the BFD session to detect the physical status.

**Precautions**

* If a BFD session bound to a default multicast address has been configured, the default multicast address cannot be changed.
* A default multicast address can be deleted only after all BFD sessions using this default multicast address have been deleted.


Example
-------

# Set the default multicast address to 224.0.0.150 for a BFD session.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] default-ip-address 224.0.0.150

```