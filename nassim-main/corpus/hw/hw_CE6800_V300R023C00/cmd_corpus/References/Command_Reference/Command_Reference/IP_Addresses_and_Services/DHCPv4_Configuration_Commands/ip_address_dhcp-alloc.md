ip address dhcp-alloc
=====================

ip address dhcp-alloc

Function
--------



The **ip address dhcp-alloc** command enables the DHCP client function on an interface.

The **undo ip address dhcp-alloc** command disables the DHCP client function on an interface.



By default, the DHCP client function is disabled on an interface.


Format
------

**ip address dhcp-alloc** [ **unicast** ]

**undo ip address dhcp-alloc**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **unicast** | Indicates that the client requests the server to unicast response packets to the client. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable an interface of the device to obtain IP addresses using DHCP, enable the DHCP client function on the interface. A BOOTP client applies for an IP address from the server using DHCP. The DHCP client has two functions:- Sends DHCP Request messages to the server.- Processes DHCP Reply messages from the server.To obtain an IP address, the DHCP client sends a DHCP Request message to the server. After the server receives the DHCP Request message, it sends a DHCP response message to the DHCP client. The DHCP client obtains the assigned IP address from the response message.

**Precautions**

Interfaces of the device can have IP addresses statically configured using the **ip address** command or dynamically obtain IP addresses using the **ip address dhcp-alloc** command. A static IP address takes precedence over a dynamic IP address. If the interface has dynamically obtained an IP address after the **ip address dhcp-alloc** command is executed, running the **undo ip address** command deletes the IP address and the **ip address dhcp-alloc** command. If the interface does not obtain an IP address after the **ip address dhcp-alloc** command is executed, running the **undo ip address** command does not delete the **ip address dhcp-alloc** command.


Example
-------

# Enable the DHCP client function on interface 100GE1/0/1 to obtain an IP address.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address dhcp-alloc

```