mac-address update arp enable
=============================

mac-address update arp enable

Function
--------



The **mac-address update arp enable** command enables the MAC address-triggered ARP entry update function. That is, the Switch is enabled to update outbound interfaces in ARP entries when outbound interfaces in MAC address entries change.

The **undo mac-address update arp enable** command disables the MAC address-triggered ARP entry update function.



By default, the MAC address-triggered ARP entry update function is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-address update arp enable**

**undo mac-address update arp enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On the Ethernet, MAC address entries are used to guide Layer 2 data forwarding. The ARP entries that define the mapping between IP addresses and MAC addresses guide communication between devices on different network segments.The outbound interface in a MAC address entry is updated by packets, whereas the outbound interface in an ARP entry is updated after the aging time is reached. In this case, the outbound interfaces in the MAC address entry and ARP entry may be different. To address this issue, run the mac-address update arp enable command to enable the Switch to update outbound interfaces in ARP entries when outbound interfaces in MAC address entries change.When the VM location is changed after MAC-ARP association is enabled and a gateway's MAC entries are updated upon receipt of Layer 2 user traffic, ARP entries and outbound interface information are updated as follows to accelerate Layer 3 traffic convergence:

* If ARP entries exist and the outbound interface of MAC entries is inconsistent with that of ARP entries, ARP entries are updated based on MAC entries, and outbound interface information is updated.
* If ARP entries do not exist, a broadcast suppression table is searched based on MAC entries and ARP probe is re-initiated to update ARP entries and outbound interface information.

**Precautions**

* This command takes effect only for dynamic ARP entries. Static ARP entries are not updated when the corresponding MAC address entries change.
* After the MAC address-triggered ARP entry update function is enabled, the device updates an ARP entry only if the outbound interface in the corresponding MAC address entry changes.
* If MAC address flapping occurs more than 10 times, the device disables the MAC address-triggered ARP entry update function. After MAC address flapping is eliminated, the device automatically enables the MAC address-triggered ARP entry update function.

Example
-------

# Enable the MAC address-triggered ARP entry update function.
```
<HUAWEI> system-view
[~HUAWEI] mac-address update arp enable

```