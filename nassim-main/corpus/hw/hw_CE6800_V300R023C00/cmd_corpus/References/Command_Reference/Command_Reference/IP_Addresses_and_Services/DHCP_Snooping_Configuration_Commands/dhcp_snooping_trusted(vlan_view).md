dhcp snooping trusted(vlan view)
================================

dhcp snooping trusted(vlan view)

Function
--------



The **dhcp snooping trusted** command configures an interface as a trusted interface.

The **undo dhcp snooping trusted** command configures an interface as an untrusted interface.



By default, an interface is untrusted.


Format
------

**dhcp snooping trusted interface** { *interface-type* *interface-number* | *interface-name* }

**undo dhcp snooping trusted interface** { *interface-type* *interface-number* | *interface-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-number* | Specifies the interface number. | - |
| *interface-name* | Specifies the interface name. | - |
| **interface** *interface-type* | Specifies the interface type. | - |



Views
-----

VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable DHCP clients to obtain IP addresses from authorized DHCP servers, the DHCP snooping security mechanism allows you to configure trusted and untrusted interfaces. The trusted interface forwards DHCP messages, and untrusted interfaces discard DHCP ACK messages and DHCP Offer messages from DHCP servers.The interface directly or indirectly connected to the DHCP server trusted by the administrator needs to be configured as the trusted interface, and other interfaces are configured as untrusted interfaces. This ensures that DHCP clients can obtain IP addresses only from authorized DHCP servers and prevents bogus DHCP servers from assigning IP addresses to DHCP clients.The message processing method in this scenario also applies to DHCPv6 messages.

**Prerequisites**

DHCP snooping has been enabled using the **dhcp snooping enable** command in the system view.

**Precautions**

After an interface is configured as a DHCP trusted interface using the dhcp snooping trusted command, the device does not perform source tracing or attack defense for DHCP packets received by the interface.If you run the dhcp snooping trusted command in the VLAN view, the command takes effect only for the DHCP messages of the specified VLAN received on the interfaces that join this VLAN. If you run the dhcp snooping trusted command in the interface view, the command takes effect for all the DHCP messages received by the interface.You are advised not to configured more than 15 trusted interfaces in a VLAN.


Example
-------

# Configure 100GE1/0/1 in VLAN 100 as a trusted interface.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan 100
[*HUAWEI-vlan100] dhcp snooping trusted interface 100GE 1/0/1

```