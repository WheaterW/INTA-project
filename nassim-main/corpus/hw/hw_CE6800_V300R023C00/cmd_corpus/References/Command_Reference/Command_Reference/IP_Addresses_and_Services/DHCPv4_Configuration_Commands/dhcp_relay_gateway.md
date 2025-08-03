dhcp relay gateway
==================

dhcp relay gateway

Function
--------



The **dhcp relay gateway** command configures a gateway address on a DHCP relay interface.

The **undo dhcp relay gateway** command deletes a gateway address configured on a DHCP relay interface.



By default, no gateway address is configured on a DHCP relay interface.


Format
------

**dhcp relay gateway** *ip-address*

**undo dhcp relay gateway** [ *ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies an IP address. | The value is in dotted decimal notation. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, you can configure the gateway address of an interface based on its primary/secondary IP address. By default, the primary IP address of an interface is used as the gateway address. If VRRP is enabled on an interface, run the dhcp relay gateway command on the interface to forcibly set the gateway address to the virtual IP address of the VRRP group.

**Prerequisites**

DHCP relay has been enabled using the **dhcp select relay** command in the interface view.


Example
-------

# Set the relay agent address to 10.1.1.1 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 255.255.255.0
[*HUAWEI-100GE1/0/1] dhcp select relay
[*HUAWEI-100GE1/0/1] dhcp relay server-ip 10.1.1.6
[*HUAWEI-100GE1/0/1] dhcp relay gateway 10.1.1.1

```