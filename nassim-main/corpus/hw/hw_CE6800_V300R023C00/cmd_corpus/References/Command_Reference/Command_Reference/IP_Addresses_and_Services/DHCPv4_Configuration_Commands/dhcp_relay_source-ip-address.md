dhcp relay source-ip-address
============================

dhcp relay source-ip-address

Function
--------



The **dhcp relay source-ip-address** command configures a DHCP relay source IP address.

The **undo dhcp relay source-ip-address** command restores the default DHCP relay source IP address.



By default, a DHCP relay interface uses its primary IP address as the source IP address.


Format
------

**dhcp relay source-ip-address** *ip-address*

**undo dhcp relay source-ip-address** [ *ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a DHCP relay source IP address. | The value is in dotted decimal notation. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The forwarding path of DHCP request packets may be inconsistent with that of DHCP reply packets. As a result, the DHCP relay fails to query user information during processing of DHCP reply packets and therefore discards these packets. Consequently, DHCP clients fail to go online. To address this problem, you can select DHCP Option 82 or change the source IP address of the DHCP packets. Third-party devices on the live network, however, may not support DHCP Option 82. In this case, run the **dhcp relay source-ip-address** command to change the source IP address of DHCP packets.After this command is run on the DHCP relay and the relay receives a DHCP request packet, the DHCP relay can add the IP address to the source address field of the IP header of the DHCP request packet. The DHCP server searches for routes based on this added IP address while giving a reply. This avoids path inconsistency.

**Precautions**

The DHCP relay source IP address must be the primary or secondary IP address of the relay interface. Configuring another address as the source IP address may cause the clients to fail to obtain IP addresses.


Example
-------

# Configure 10.1.1.1 as the DHCP relay source address on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.2.1.1 255.255.255.0
[*HUAWEI-100GE1/0/1] ip address 10.3.1.1 255.255.255.0 sub
[*HUAWEI-100GE1/0/1] dhcp select relay
[*HUAWEI-100GE1/0/1] dhcp relay server-ip 10.6.1.1
[*HUAWEI-100GE1/0/1] dhcp relay source-ip-address 10.1.1.1

```