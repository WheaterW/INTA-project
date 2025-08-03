Defense Against Invalid ARP Packets
===================================

Defense Against Invalid ARP Packets

#### Security Policy

The DHCP snooping ARP packet check function, also called DAI function on some products can be configured to defend against invalid ARP packets. The implementations of these two functions are similar.


#### Attack Methods

You can configure an interface to match received ARP packets against the binding table. To be specific, the device matches the source IP address, source MAC address, interface, and VLAN information of received ARP packets against the binding table. If they match, the device considers the ARP packets valid and forwards them. If they mismatch, the device considers the ARP packets invalid and drops them.


#### Configuration and Maintenance Methods

Configure the DHCP snooping ARP packet check function on an interface.

```
<HUAWEI> system-view
```
```
[~HUAWEI] interface gigabitethernet0/1/0
```
```
[~HUAWEI-Gigabitethernet0/1/0] dhcp snooping check arp enable
```
```
[*HUAWEI-Gigabitethernet0/1/0] commit
```

#### Configuration and Maintenance Suggestions

Note that configuring this function affects user access.


#### Verifying the Security Hardening Result

Run the **display dhcp snooping** **interface** *interface-type* *interface-number* command to check the DHCP snooping configuration.