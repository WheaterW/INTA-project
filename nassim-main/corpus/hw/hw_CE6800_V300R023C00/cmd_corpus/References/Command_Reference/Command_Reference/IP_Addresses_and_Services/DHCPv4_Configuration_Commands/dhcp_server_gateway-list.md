dhcp server gateway-list
========================

dhcp server gateway-list

Function
--------

The **dhcp server gateway-list** command sets the default gateway IP address that a DHCP server pre-allocates to DHCP clients.

The **undo dhcp server gateway-list** command deletes the configured default gateway IP address.

By default, the default gateway IP address that a DHCP server pre-allocates to DHCP clients is not configured.



Format
------

**dhcp server gateway-list** *ip-address* &<1-8>

**undo dhcp server gateway-list** { *ip-address* | **all** }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies an IP address. You can configure a maximum of eight gateway addresses, which are separated by spaces. | The value is in dotted decimal notation. |
| **all** | Indicates all IP addresses. | - |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

To load balance traffic and improve network reliability, you can configure multiple default gateway addresses.

**Prerequisites**

1. IP addresses in the interface address pool have been configured using the **ip address** command.
2. The DHCP server function has been enabled on the interface using the **dhcp select interface** command.

**Precautions**

The default gateway address allocated to the DHCP client can only be a class A, B, or C address, and cannot be a broadcast address, a host address, or a class A address whose network address is 0.

If the VRRP virtual IP address is configured on the interface and no gateway address is pre-allocated to the DHCP client using the
**dhcp server gateway-list** command, the DHCP server uses the first VRRP virtual IP address as the gateway address to be allocated to the client. If no VRRP virtual IP address is configured on the interface, the DHCP server uses the physical IP address of the interface as the gateway address to be allocated to the client.If the
**dhcp server gateway-list** command is not configured, the gateway address allocated by the DHCP server to the DHCP client may fail to be displayed in information during fault diagnosis. Therefore, you are advised to configure this command if the DHCP server function based on an interface address pool is used.

Example
-------

# Enable a DHCP server on
100GE
1/0/1 to pre-allocate default gateway address 10.1.1.1 to DHCP clients.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server gateway-list 10.1.1.1

```