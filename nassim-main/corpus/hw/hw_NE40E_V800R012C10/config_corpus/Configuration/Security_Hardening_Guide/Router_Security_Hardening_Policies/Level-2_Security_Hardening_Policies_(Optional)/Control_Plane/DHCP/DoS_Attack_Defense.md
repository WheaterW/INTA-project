DoS Attack Defense
==================

DoS Attack Defense

#### Security Policy

An attacker keeps applying for IP addresses by changing the CHADDR value in DHCP packets to exhaust DHCP server address resources. You can configure the device to check the CHADDR value in DHCP request packets to defend against such DoS attacks.


#### Attack Methods

You can configure MAC restriction to defend attacks that an attacker keeps changing the source MAC address in frame headers. However, if an attacker changes the CHADDR value instead of the source MAC address in packets, MAC restriction cannot suppress such attacks because a device determines whether a packet is valid based on its source MAC address. Attack packets can be forwarded.


#### Configuration and Maintenance Methods

Enable CHADDR check on an interface.

```
<HUAWEI> system-view
```
```
[~HUAWEI] interface gigabitethernet0/1/0
```
```
[~HUAWEI-Gigabitethernet0/1/0] dhcp check chaddr enable
```
```
[*HUAWEI-Gigabitethernet0/1/0] commit
```

#### Configuration and Maintenance Suggestions

Note that configuring CHARDDR check affects user access.


#### Verifying the Security Hardening Result

Run the **display dhcp snooping** **interface** *interface-type* *interface-number* command to check the DHCP snooping configuration.