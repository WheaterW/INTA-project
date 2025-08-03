Defense Against Invalid IP Packets
==================================

Defense Against Invalid IP Packets

#### Security Policy

After receiving an IP packet, a device checks whether the source IP address, source MAC address, interface information, and VLAN ID carried in the packet match an entry in the DHCP snooping binding table. If a matching entry exists, the device considers the packet valid and forwards it. If no matching entry exists, the device considers the packet invalid and drops it.

The DHCP snooping IP packet check function, also called IP source guard (IPSG) function in some products can be configured to defend against invalid IP packets. The implementations of these two functions are similar.


#### Attack Methods

An attacker sends a large number of IP packets carrying incorrect source MAC address, source IP address, VLAN ID, or interface information to attack the DHCP server.


#### Configuration and Maintenance Methods

Configure the DHCP snooping IP packet check function on an interface.

```
<HUAWEI> system-view
```
```
[~HUAWEI] interface gigabitethernet0/1/0
```
```
[~HUAWEI-Gigabitethernet0/1/0] dhcp snooping check ip enable
```
```
[*HUAWEI-Gigabitethernet0/1/0] commit
```

#### Configuration and Maintenance Suggestions

Note that configuring this function affects user access.


#### Verifying the Security Hardening Result

Run the **display dhcp snooping** **interface** *interface-type* *interface-number* command to check the DHCP snooping configuration.