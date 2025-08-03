display arp anti-attack
=======================

display arp anti-attack

Function
--------



The **display arp anti-attack** command displays the configurations of Address Resolution Protocol (ARP) security functions.

The **display arp miss anti-attack** command displays configurations of anti-ARP Miss message attack functions.




Format
------

**display arp anti-attack** { **rate-limit** | **entry-check** }

**display arp miss anti-attack rate-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **rate-limit** | Displays the rate limit of ARP Miss messages or ARP packets. | - |
| **entry-check** | Displays configuration of fixed ARP modes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



After configuring ARP security functions, you can run the display arp anti-attack command to check whether the configurations of all ARP security functions are correct.After configuring anti-ARP Miss message attack functions, run the display arp miss anti-attack command to check whether the configurations of all anti-ARP Miss message attack functions are correct.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Displays fixed ARP modes.
```
<HUAWEI> display arp anti-attack entry-check
Vlanif      Mode
-------------------------------------------------------------------------------
   12       send-ack
   11       fix-mac
Other       fix-all
-------------------------------------------------------------------------------

```

# Display the rate limit of ARP packets.
```
<HUAWEI> display arp anti-attack rate-limit
Global ARP packet rate limit (pps)        : --
Suppress Rate of each destination IP (pps): --

Total number of rate-limit configuration for VLAN : 1
VLAN               Suppress Rate(pps)
-------------------------------------------------------------------------------
10                                22
-------------------------------------------------------------------------------

Total number of rate-limit configuration for source IP Address : 1
Source IP          Suppress Rate(pps)
-------------------------------------------------------------------------------
1.1.1.1                           20
Other                            111  
-------------------------------------------------------------------------------

Total number of rate-limit configuration for MAC Address : 1
Source MAC         Suppress Rate(pps)
-------------------------------------------------------------------------------
1-1-1                            20
Other                           111
-------------------------------------------------------------------------------

```

# Displays the rate limit of ARP Miss messages.
```
<HUAWEI> display arp miss anti-attack rate-limit
Global ARP miss rate limit (pps) : --

Total number of rate-limit configuration for VLAN : 0
VLAN               Suppress Rate(pps)
-------------------------------------------------------------------------------
10                                10
-------------------------------------------------------------------------------

Total number of rate-limit configuration for source IP Address : 0
Source IP          Suppress Rate(pps)
-------------------------------------------------------------------------------
All                               11
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display arp anti-attack** command output
| Item | Description |
| --- | --- |
| Vlanif | VLANIF interface on which fixed ARP is configured. |
| Mode | Specifies the fixed ARP mode.   * fix-all: specifies the fixed-all mode of fixed ARP. * fix-mac: specifies the fixed-mac mode of fixed ARP. * send-ack: specifies the send-ack mode of fixed ARP. |
| Global ARP miss rate limit (pps) | Globally set rate limit of ARP Miss messages. |
| Global ARP packet rate limit (pps) | Globally set rate limit of ARP packets. |
| Suppress Rate(pps) | Rate limit of ARP Miss messages or ARP packets. |
| Suppress Rate of each destination IP (pps) | Destination IP address based on which the rate limit of ARP packets is set. |
| VLAN | VLAN ID based on which the rate limit of ARP Miss messages or ARP packets is set. |
| Source IP | Source IP address based on which the rate limit of ARP Miss messages or ARP packets is set. |
| Source MAC | Source MAC address based on which the rate limit of ARP packets is set. |