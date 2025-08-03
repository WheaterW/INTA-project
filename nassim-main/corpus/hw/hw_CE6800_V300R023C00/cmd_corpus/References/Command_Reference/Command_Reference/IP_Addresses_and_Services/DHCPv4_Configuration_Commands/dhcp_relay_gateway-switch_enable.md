dhcp relay gateway-switch enable
================================

dhcp relay gateway-switch enable

Function
--------



The **dhcp relay gateway-switch enable** command enables DHCP relay gateway switching.

The **undo dhcp relay gateway-switch enable** command disables DHCP relay gateway switching.



By default, DHCP relay gateway switching is disabled.


Format
------

**dhcp relay gateway-switch enable**

**undo dhcp relay gateway-switch enable**


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

The **dhcp relay gateway-switch enable** command is used on DHCP relay agents. This command allows a DHCP relay agent to use a secondary IP address as the gateway address to apply for IP addresses for users when it fails to use the primary IP address to apply for IP addresses.

**Prerequisites**

1. Global DHCP has been enabled by using the **dhcp enable** command in the system view.
2. DHCP relay has been enabled on an interface by using the **dhcp select relay** command.

**Precautions**

* After VRRP is configured, the gateway address for the DHCP relay agent switches among IP addresses of the VRRP groups.
* The gateway address switches from the primary IP address to a secondary IP address only when a user fails to obtain an IP address by using the primary IP address for at least three times and the interval between the last failure and first failure exceeds 24 seconds.
* Before running this command on an interface, ensure that the interface has a primary IP address and at least one secondary IP address.
* If a primary IP address and multiple secondary IP addresses are configured on an interface, the system tries the secondary IP addresses one by one until users successfully obtain IP addresses.

Example
-------

# Enable DHCP relay gateway switching on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 192.168.30.1 255.255.255.0
[*HUAWEI-100GE1/0/1] ip address 192.168.31.1 255.255.255.0 sub
[*HUAWEI-100GE1/0/1] dhcp select relay
[*HUAWEI-100GE1/0/1] dhcp relay server-ip 192.168.20.1
[*HUAWEI-100GE1/0/1] dhcp relay gateway-switch enable

```