ip address unnumbered (interface view)
======================================

ip address unnumbered (interface view)

Function
--------



The **ip address unnumbered** command enables an interface to borrow an IP address from another interface.

The **undo ip address unnumbered** command disables an interface from borrowing an IP address from another interface.



By default, an interface is disabled from borrowing an IP address from another interface.


Format
------

**ip address unnumbered interface** { *interface-name* | *interface-type* *interface-number* }

**undo ip address unnumbered**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface whose IP address is borrowed. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface whose IP address is borrowed. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To save IP address resources, run the ip address unnumbered command to configure an interface to borrow an IP address from another interface. If an interface is only occasionally used, it is unnecessary to configure an IP address for the interface. Instead, configure the interface to borrow an IP address from another interface.The following interfaces support IP borrowing from other interfaces such as Ethernet and loopback interfaces:

* Interfaces encapsulated with PPP
* Tunnel interfaces

**Prerequisites**

The numbered interface has been configured with an IP address using the **ip address** command or has obtained an IP address through negotiation.

**Configuration Impact**

After an unnumbered interface borrows an IP address, the interface can use this IP address to communicate with other devices. The **display interface** command displays the borrowed IP address and its subnet mask.

**Precautions**

Because an interface with a borrowed IP address does not have its own IP address, the system cannot generate any route for the interface. Therefore, you need to manually configure a dynamic or static route to implement interconnection between devices.When configuring IP address unnumbered on an interface, note the following:

* The IP address of the numbered interface cannot be a borrowed IP address.
* The IP address of the numbered interface can be lent to multiple interfaces.
* If the numbered interface has multiple IP addresses, only the primary IP address can be lent.
* If the numbered interface is not configured with any IP address, the IP address 0.0.0.0 is borrowed.
* The IP address of the virtual loopback interface can be lent to other interfaces, but the virtual loopback interface cannot borrow an IP address from another interface.If a tunnel interface is not configured to borrow IP addresses of other interfaces, the tunnel interface does not have an IP address by default.

Example
-------

# Configure Tunnel 10 to borrow the IP address of Loopback 0.
```
<HUAWEI> system-view
[~HUAWEI] interface LoopBack 0
[*HUAWEI-LoopBack0] ip address 1.1.1.1 24
[*HUAWEI-LoopBack0] quit
[*HUAWEI] interface Tunnel 10
[*HUAWEI-Tunnel10] ip address unnumbered interface loopback 0

```