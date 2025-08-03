ip address (interface view)
===========================

ip address (interface view)

Function
--------



The **ip address** command configures an IP address for an interface.

The **undo ip address** command deletes the IP address of an interface.



By default, no IP address is configured for interfaces.


Format
------

**ip address** *ip-address* { *mask* | *mask-length* } [ *sub* ] [ **tag** *tag-value* ]

**undo ip address** [ *ip-address* { *mask* | *mask-length* } [ *sub* ] [ **tag** *tag-value* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of an interface. | The value is in dotted decimal notation. |
| *mask* | Specifies a subnet mask.  The IP address with the subnet mask of 255.255.255.255 can be assigned only to a Loopback interface. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the length of the subnet mask.  The IP address with the subnet mask length of 32 can be assigned only to a Loopback interface. | The value is an integer ranging from 0 to 32. |
| *sub* | Indicates a secondary IP address. To implement communication between subnets on one interface, configure secondary IP addresses. | It is in dotted decimal notation. |
| **tag** *tag-value* | Specifies the administrative tag carried in a route imported from an interface. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure an IP address and its mask for an interface, run the **ip address** command. This configuration allows the interface to access a network. To connect an interface to several subnets, configure several IP addresses for the interface, one of which is the primary IP address and the others are secondary IP addresses. Each interface can have a maximum of one primary IP address and 255 secondary IP addresses configured.

**Configuration Impact**

* The **undo ip address** command deletes all IP addresses of an interface.
* The **undo ip address ip-address mask** command deletes the primary IP address.
* The **undo ip address ip-address mask sub** command deletes secondary IP addresses.
* When you configure a new primary IP address for an interface, the newly configured address overrides the previous one.
* After an interface is configured with an IP address, if the interface is Up, the system generates the host route and network segment route based on the IP address.

**Precautions**

The following configurations are not supported on different interfaces of the same device:

* The IP addresses are the same.
* The broadcast addresses corresponding to the IP addresses are the same. (In binary mode, the host ID field is all 1s.) For example, if the IP address of interface A is 10.1.1.1/16 and the corresponding broadcast address is 10.1.255.255, and the IP address of interface B is 10.1.1.2/24 and the corresponding broadcast address is 10.1.1.255, the broadcast addresses of interfaces A and B are different. In this case, the configuration is successful. If the IP address of interface B is 10.1.1.2/16 and the corresponding broadcast address is 10.1.255.255, the broadcast addresses of interfaces A and B are the same. As a result, the configuration fails.
* The IP address of an interface is the same as the broadcast address of another interface. For example, if the IP address of interface A is 1.1.1.1/28 and the corresponding broadcast address is 1.1.1.15, and the IP address of interface B is 1.1.1.15/26, the configuration fails because the broadcast address of interface A is the same as the IP address of interface B.
* The IP address cannot be a multicast or broadcast address. The Ethernet interface cannot be configured with a loopback address.
* Before deleting the primary IP address, you must delete all the secondary IP addresses.
* The configured IP address must be different from the network ID corresponding to the IP address. For example, if the IP address is 10.0.0.88 and the subnet mask is 255.255.255.248 (or the mask length is 29), the network ID corresponding to the IP address is 10.0.0.88. In this case, the configured IP address is the same as the network ID of the IP address. Therefore, the IP address is invalid and cannot be configured.
* If the address segments configured for different interfaces on the same device contain each other, exercise caution when running this command to prevent services from being affected. For example, if the IP address of interface A is 1.1.1.1/16 and the IP address of interface B is 1.1.2.1/24, the network segment addresses of interfaces A and B are included.
* The IP address configured on the interface cannot conflict with the IP address of the remote device. Otherwise, traffic may be incorrectly diverted to the current device, causing service interruption.

Example
-------

# Configure a primary IP address 10.102.0.1 and a secondary IP address 10.38.160.1 with the subnet mask 255.255.255.0 for 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.102.0.1 255.255.255.0
[*HUAWEI-100GE1/0/1] ip address 10.38.160.1 255.255.255.0 sub

```