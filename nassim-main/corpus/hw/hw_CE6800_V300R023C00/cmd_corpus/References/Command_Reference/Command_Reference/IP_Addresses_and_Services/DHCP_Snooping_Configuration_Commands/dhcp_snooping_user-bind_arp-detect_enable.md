dhcp snooping user-bind arp-detect enable
=========================================

dhcp snooping user-bind arp-detect enable

Function
--------



The **dhcp snooping user-bind arp-detect enable** command enables the association between ARP and DHCP snooping.

The **undo dhcp snooping user-bind arp-detect enable** command disables the association between ARP and DHCP snooping.



By default, association between ARP and DHCP snooping is disabled.


Format
------

**dhcp snooping user-bind arp-detect enable**

**undo dhcp snooping user-bind arp-detect enable**


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

After receiving a DHCPRELEASE message for releasing the IP address from a DHCP client, the DHCP snooping-enabled device immediately deletes the client's binding entry. However, if the client cannot send a DHCPRELEASE message because it is unexpectedly disconnected, the DHCP snooping-enabled device cannot immediately delete the client's binding entry.After association between ARP and DHCP snooping is enabled, the DHCP snooping-enabled device performs ARP probe on the IP address if it cannot find the ARP entry corresponding to the IP address in the DHCP snooping entry. If no client is detected after four consecutive ARP probes are performed, the DHCP snooping-enabled device deletes the DHCP snooping binding entry corresponding to the IP address. (The probe interval is 20 seconds; this interval and the number of probes are fixed values and cannot be changed.) If the DHCP snooping-enabled device supports the DHCP relay function, it then sends a DHCPRELEASE message on behalf of the DHCP client, instructing the DHCP server to release the IP address.

**Precautions**

Before association between ARP and DHCP snooping is enabled, ensure that an IP address configured on the device is on the same network segment as the IP address of the client for ARP probe.This function depends on ARP entries on the device. When the number of dynamic DHCP snooping binding entries on the device exceeds the maximum number of ARP entries, after this function is enabled, some user binding entries that do not have corresponding ARP entries are deleted.


Example
-------

# Enable association between ARP and DHCP snooping on the device.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] dhcp snooping user-bind arp-detect enable

```