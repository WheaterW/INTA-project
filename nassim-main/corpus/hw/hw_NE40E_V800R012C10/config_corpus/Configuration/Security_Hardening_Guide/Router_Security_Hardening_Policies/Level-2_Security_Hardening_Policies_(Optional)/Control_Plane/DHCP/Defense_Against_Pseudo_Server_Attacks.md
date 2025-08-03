Defense Against Pseudo Server Attacks
=====================================

Defense Against Pseudo Server Attacks

#### Security Policy

Trusted and untrusted interfaces can be configured for DHCP snooping to defend against bogus DHCP server attacks.

* Trusted and untrusted interfaces take effect in DHCP snooping.
* The configured trusted or untrusted interface records a maximum of 64 logs about the DHCP server. When 64 logs are generated on the interface, the later logs override the previous ones. In addition, the aging time of logs is 24 hours.
* The DHCP snooping function must have been globally enabled.


#### Attack Methods

An attacker pretends to be a DHCP server and replies to a DHCP client with an incorrect gateway address, DNS server address, and IP address to prevent the client from accessing networks.


#### Configuration and Maintenance Methods

Configure GE 0/1/0 as the trusted interface.

```
<HUAWEI> system-view
```
```
[~HUAWEI] interface gigabitethernet0/1/0
```
```
[~HUAWEI-Gigabitethernet0/1/0] dhcp snooping trusted
```
```
[*HUAWEI-Gigabitethernet0/1/0] commit
```

#### Configuration and Maintenance Suggestions

Configure the interface closest to the DHCP server as the trusted interface.


#### Verifying the Security Hardening Result

Run the **display dhcp snooping** **interface** *interface-type* *interface-number* command to check the DHCP snooping configuration.