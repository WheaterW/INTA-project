dhcp snooping trusted
=====================

dhcp snooping trusted

Function
--------



The **dhcp snooping trusted** command configures an interface as a trusted interface.

The **undo dhcp snooping trusted** command configures an interface as an untrusted interface.



By default, an interface is untrusted.


Format
------

**dhcp snooping trusted**

**undo dhcp snooping trusted**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable DHCP clients to obtain IP addresses from valid DHCP servers, the DHCP snooping security mechanism allows interfaces to be configured as trusted and untrusted interfaces. Trusted interfaces forward received DHCP messages normally. Untrusted interfaces receive DHCP ACK and DHCP Offer messages from DHCP servers, the discards the packet.The interface directly or indirectly connected to the DHCP server trusted by the administrator must be configured as a trusted interface, and other interfaces must be configured as untrusted interfaces. This ensures that DHCP clients can obtain IP addresses only from authorized DHCP servers. Bogus DHCP servers cannot allocate IP addresses to DHCP clients.If the interface connected to the DHCP client is configured as a trusted interface, the DHCP client does not need to be verified, and the device does not generate dynamic binding entries for the DHCP clients connected to the trusted interface.The trusted interface status is not affected by the **dhcp snooping enable** command. After the dhcp snooping disable command is run on the interface, the trusted interface status is not affected.The packet processing mode in this scenario is also applicable to DHCPv6 packets.

**Prerequisites**

DHCP snooping has been enabled using the **dhcp snooping enable** command in the system view.

**Precautions**

After an interface is configured as a DHCP trusted interface using the dhcp snooping trusted command, the device does not perform source tracing or attack defense for DHCP packets received by the interface.If you run the dhcp snooping trusted command in the VLAN view, the command takes effect only for the DHCP messages of the specified VLAN received on the interfaces that join this VLAN. If you run the dhcp snooping trusted command in the interface view, the command takes effect for all the DHCP messages received by the interface.You are advised not to configured more than 15 trusted interfaces in a VLAN.


Example
-------

# Configure 100GE1/0/1 as a trusted interface.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] dhcp snooping trusted

```