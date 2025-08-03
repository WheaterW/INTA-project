dhcp relay giaddr outgoing-interface-address
============================================

dhcp relay giaddr outgoing-interface-address

Function
--------



The **dhcp relay giaddr outgoing-interface-address** command configures the relay agent address as the IP address of the outbound interface.

The **undo dhcp relay giaddr outgoing-interface-address** command deletes the configuration.



By default, a DHCP relay interface uses its primary IP address as the relay agent address.


Format
------

**dhcp relay giaddr outgoing-interface-address**

**undo dhcp relay giaddr outgoing-interface-address**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the primary IP address of the DHCP relay interface is used as the relay agent address, and the relay agent address is added to the GiAddr field of packets. The DHCP server then uses the relay agent address to identify the network segment where a user resides and allocates an appropriate IP address for the user to allow for communication with the DHCP relay.If the user and the DHCP server are located in different VPNs, the DHCP server fails to use this relay agent address to communicate with the DHCP relay, and DHCP reply packets are unreachable.To address this issue, run the **dhcp relay giaddr outgoing-interface-address** command to configure the relay agent address as the IP address of the outbound interface in DHCP request packets. In this manner, the DHCP reply packets sent by the DHCP server can be successfully forwarded to the DHCP relay.Generally, the DHCP server allocates IP addresses based on the GiAddr field. A modification of the GiAddr field may cause a user online failure.

* If the DHCP server supports the suboption link-selection of the Option 82 field, run the **dhcp option82** command on the DHCP relay so that the suboption link-selection can be added to the Option 82 field in DHCP request packets. As the suboption link-selection carries GiAddr information, the DHCP server can allocate IP addresses to users based on this suboption.
* If the DHCP server does not support the suboption link-selection of the Option 82 field, the **dhcp relay giaddr outgoing-interface-address** command cannot be run.

**Precautions**



When a distributed VXLAN gateway functions as a DHCPv4 relay agent, it selects the smallest local IP address in the same VPN as the DHCPv4 server as the relay agent address.




Example
-------

# On interface 100GE1/0/1, configure the relay agent address as the IP address of the outbound interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp relay giaddr outgoing-interface-address

```