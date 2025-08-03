Defense Against Bogus Packets for Extending the IP Address Lease
================================================================

Defense Against Bogus Packets for Extending the IP Address Lease

#### Security Policy

An attacker keeps sending DHCP request packets for extending the IP address lease to prevent expired IP addresses from being reclaimed. You can configure the device to match received request packets against the binding table to defend against bogus packets for extending the IP address lease.


#### Attack Methods

An attacker sends a large number of DHCP request packets carrying incorrect source MAC address, source IP address, VLAN ID, or interface information to attack the DHCP server.


#### Configuration and Maintenance Methods

Configure an interface to check DHCP request packets for extending the IP address lease.

```
<HUAWEI> system-view
```
```
[~HUAWEI] interface gigabitethernet0/1/0
```
```
[~HUAWEI-Gigabitethernet0/1/0] dhcp snooping check dhcp-request enable
```
```
[*HUAWEI-Gigabitethernet0/1/0] commit
```

#### Configuration and Maintenance Suggestions

Note that configuring CHARDDR check affects user access.


#### Verifying the Security Hardening Result

Run the **display dhcp snooping** **interface** *interface-type* *interface-number* command to check the DHCP snooping configuration.