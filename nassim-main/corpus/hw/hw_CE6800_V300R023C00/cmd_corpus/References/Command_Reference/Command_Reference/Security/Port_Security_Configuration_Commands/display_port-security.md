display port-security
=====================

display port-security

Function
--------



The **display port-security** command displays security information of interfaces.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display port-security** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |



Views
-----

All views,System view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After port security is enabled on an interface of a device, you can run the **display port-security** command to check whether the port security function is correctly configured. If the port security function is incorrectly configured, authorized users cannot communicate with each other.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display port security information on a specified interface.
```
<HUAWEI> display port-security interface eth-trunk 1
Port Security              : Enabled
Port Status                : Secure-up
Protect Action             : Restrict
Aging Time(minutes)        : -
Aging Type                 : -
Maximum MAC Addresses      : 100
Total MAC Addresses        : 0
Configured MAC Addresses   : 2
Sticky MAC Addresses       : 0
Last Source MAC Address    : 00e0-fc12-3456
Last Source VLAN ID        : -
Security Violation Count   : 0

```

# Display port security information on all interfaces.
```
<HUAWEI> display port-security
--------------------------------------------------------------------------------
SecurePort           MaxSecureAddr CurrentAddr SecurityViolation ProtectAction
                           (count)     (count)           (count)
--------------------------------------------------------------------------------
Eth-Trunk11                      1           0                 0 Restrict         
Eth-Trunk12                      1           0                 0 Restrict         
Eth-Trunk13                      1           0                 0 Restrict         
Eth-Trunk14                      1           0                 0 Restrict         
Eth-Trunk15                      1           0                 0 Restrict                  
--------------------------------------------------------------------------------
Total Secured MAC Addresses in System: 0

```

**Table 1** Description of the **display port-security** command output
| Item | Description |
| --- | --- |
| Port Security | Whether interface security is enabled on the interface:   * Enabled. * Disabled. |
| Port Status | Interface status:   * Secure-up. * Secure-down. |
| Security Violation Count | Number of times an interface learns the maximum number of dynamic secure MAC addresses. |
| Protect Action | Security protection action taken by an interface:   * Protect: When the number of MAC addresses learned on an interface reaches the maximum, the interface discards the packets whose source MAC addresses are not in the MAC table. * Restrict: When the number of MAC addresses learned on an interface reaches the maximum, the interface discards the packets whose source MAC addresses are not in the MAC table and reports an alarm. * Error-down: When the number of MAC addresses learned on an interface reaches the maximum, the interface becomes Error-Down and reports an alarm. |
| Aging Time(minutes) | Aging time (in minutes) of the dynamic secure MAC addresses learned on the interface. |
| Aging Type | Aging type of the dynamic secure MAC addresses learned on the interface:   * Absolute: absolute time aging. Specifically, after an aging time is configured for dynamic secure MAC addresses on an interface, the system detects whether there is traffic carrying these MAC addresses at an interval of the set aging time. If no such traffic exists, the system immediately ages these MAC addresses. * Inactivity: relative time aging. Specifically, after an aging time is configured for dynamic secure MAC addresses on an interface, the system detects whether there is traffic carrying these MAC addresses every 1 minute. If no such traffic exists, the system ages these MAC addresses after the time specified by Aging Time(minutes) elapses. * -: No aging type is configured for dynamic secure MAC addresses. |
| Maximum MAC Addresses | Maximum number of dynamic secure MAC addresses that can be learned on an interface. |
| Total Secured MAC Addresses in System | Total number of dynamic secure MAC addresses and sticky MAC addresses on all interfaces. |
| Total MAC Addresses | Total number of dynamic secure MAC addresses that are learned on the interface. |
| Configured MAC Addresses | Number of sticky MAC addresses configured on the interface. |
| Sticky MAC Addresses | Number of sticky MAC addresses converted from learned MAC addresses on the interface. |
| Last Source MAC Address | Dynamic secure MAC address that was last learned on the interface. |
| Last Source VLAN ID | VLAN to which the dynamic secure MAC address that was last learned on the interface belongs. |
| SecurePort | Interfaces that have the interface security function enabled. |
| MaxSecureAddr | Maximum number of dynamic secure MAC addresses that can be learned on an interface. |
| CurrentAddr | Number of dynamic secure MAC addresses that are learned on an interface. |
| SecurityViolation | Number of times an interface learns the maximum number of dynamic secure MAC addresses. |
| ProtectAction | Security protection action taken by an interface:   * Protect: When the number of MAC addresses learned on an interface reaches the maximum, the interface discards the packets whose source MAC addresses are not in the MAC table. * Restrict: When the number of MAC addresses learned on an interface reaches the maximum, the interface discards the packets whose source MAC addresses are not in the MAC table and reports an alarm. * Error-down: When the number of MAC addresses learned on an interface reaches the maximum, the interface becomes Error-Down and reports an alarm. |