ip address bootp-alloc
======================

ip address bootp-alloc

Function
--------



The **ip address bootp-alloc** command enables the BOOTP client function on an interface.

The **undo ip address bootp-alloc** command disables the BOOTP client function from an interface.



By default, the BOOTP client function is disabled on an interface.


Format
------

**ip address bootp-alloc** [ **unicast** ]

**undo ip address bootp-alloc**


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

DHCP is developed based on the BOOTP protocol. The device supports both DHCP and BOOTP and allows hosts to obtain IP addresses by BOOTP.To enable an interface to obtain IP addresses using BOOTP, you can enable the BOOTP client function on the interface. A BOOTP client requests for an IP address from the server using BOOTP. The BOOTP client has two functions:

* Sends BOOTP Request messages to the server.
* Processes BOOTP Reply messages from the server.To obtain an IP address, the BOOTP client sends a BOOTP Request message to the server. When the server receives the BOOTP Request message, it sends a BOOTP response message to the BOOTP client. The BOOTP client obtains the assigned IP address from the response message.

**Precautions**

* Interfaces of the device can have IP addresses statically configured using the **ip address** command or dynamically obtain IP addresses using the **ip address bootp-alloc** command. A static IP address takes precedence over a dynamic IP address. If the interface has dynamically obtained an IP address after the **ip address bootp-alloc** command is executed, running the **undo ip address** command deletes the IP address and the **ip address bootp-alloc** command. If the interface does not obtain an IP address after the **ip address bootp-alloc** command is executed, running the **undo ip address** command does not delete the **ip address bootp-alloc** command.
* The maximum total length of the options that a BOOTP client's request message can carry is 60 bytes. For example, if the length of the hostname configured using the dhcp client hostname command exceeds 57 bytes, the total length of all options exceeds 60 bytes. In this case, the request message does not carry the configured hostname.
* After an IP address is obtained using the **ip address bootp-alloc** command, resources fail to be deleted on the server if the client goes offline. As a result, the user address is not released. If the user goes offline and does not go online again, you are advised to manually delete the user on the server.

Example
-------

# Enable the BOOTP client function on interface 100GE1/0/1 to obtain an IP address.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address bootp-alloc

```