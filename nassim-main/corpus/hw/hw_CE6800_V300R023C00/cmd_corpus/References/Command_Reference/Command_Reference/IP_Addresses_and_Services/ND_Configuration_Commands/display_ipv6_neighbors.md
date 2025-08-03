display ipv6 neighbors
======================

display ipv6 neighbors

Function
--------



The **display ipv6 neighbors** command displays information about ND entries.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 neighbors** [ *ipv6-address* | **vpn-instance** *vpn-instance-name* | { *interface-name* | *interface-type* *interface-number* } ]

**display ipv6 neighbors brief**

**display ipv6 neighbors vlan** *vlan-id* { *interface-name* | *interface-type* *interface-number* }

**display ipv6 neighbors slot** *slot-num*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address. If this parameter is specified, information about ND entries of the specified IPv6 address is displayed. | The value is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of an IPv6 VPN instance. If this parameter is specified, information about ND entries of the specified IPv6 VPN instance is displayed. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name cannot be \_public\_. If the string is enclosed in double quotation marks (" "), the string can contain spaces.. |
| *interface-name* | Displays neighbor entries on a specified interface. | - |
| *interface-type* *interface-number* | Displays neighbor entries on a specified interface. | - |
| **brief** | Specifies brief information about neighbor entries. | - |
| **vlan** *vlan-id* | Specifies a VLAN ID. | An integer ranging from 1 to 4094. |
| **slot** *slot-num* | Specifies the slot ID. If this parameter is specified, information about neighbor entries on the specified slot ID is displayed. | The value is an integer. You can enter the question mark (?) and select the value as prompted. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Through the output of the **display ipv6 neighbors** command displays information about dynamic and static ND entries and check the following:

* Whether the local Router has learnt MAC addresses from neighbors
* Status of the neighbors of the local Router, including neighbor unreachable, neighbor reachable, or unknown

**Precautions**

If no parameter is specified when the **display ipv6 neighbors** command is run, information about all ND entries is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display contents in the neighbor cache.
```
<HUAWEI> display ipv6 neighbors 100ge 1/0/1
-----------------------------------------------------------------------------
IPv6 Address : 2001:DB8::1                                         
Link-layer   : 00e0-fc12-3456                     State     : INCMP               
Interface    : 100GE1/0/1                         Age       : -                   
VLAN         : -                                  CEVLAN    : -                   
VPN name     : vpn1                               Is Router : TRUE               
Secure FLAG  : SECURE Nickname : -
Source IP    : -          
Destination IP: -                                 
VNI          : -                                  BD        : -

-----------------------------------------------------------------------------
Total: 1        Dynamic: 0      Static: 1      Remote:0

```

# Display neighbor entries of the IPv6 VPN instance named vpnA.
```
<HUAWEI> display ipv6 neighbors vpn-instance vpnA
-----------------------------------------------------------------------------
IPv6 Address : 2001:DB8::2                                         
Link-layer   : 00e0-fc12-3456                     State     : INCMP               
Interface    : 100GE1/0/1                          Age       : -
VLAN         : -                                  CEVLAN    : -                   
VPN name     : vpnA                               Is Router : TRUE               
Secure FLAG  : SECURE Nickname : -
Destination IP: -                                 Source IP : -           VNI          : -                                  BD        : -
-----------------------------------------------------------------------------
Total: 1        Dynamic: 0      Static: 1      Remote:0

```

# Display contents in the neighbor cache of the VLANIF interface 1.
```
<HUAWEI> display ipv6 neighbors Vlanif 1
-----------------------------------------------------------------------------
IPv6 Address : 2001:DB8::1                                                          
Link-layer   : 00e0-fc12-3456                     State     : INCMP               
Interface    : 100GE1/0/1                         Age       : -                   
VLAN         : 1                                  CEVLAN    : -                   
VPN name     : -                                  Is Router : TRUE               
Secure FLAG  : SECURE Nickname : -
Source IP    : -          
Destination IP: -                                 
VNI          : -                                  BD        : -

-----------------------------------------------------------------------------
Total: 1        Dynamic: 0      Static: 1      Remote:0

```

# Display contents in the neighbor cache with the IPv6 address of 2001:db8::2.
```
<HUAWEI> display ipv6 neighbors 2001:db8::2
-----------------------------------------------------------------------------
IPv6 Address : 2001:DB8::2                                         
Link-layer   : 00e0-fc12-3456                     State     : STALE               
Interface    : 100GE1/0/1                         Age       : -                   
VLAN         : -                                  CEVLAN    : -                   
VPN name     : -                                  Is Router : TRUE               
Secure FLAG  : SECURESource IP    : -          
Destination IP: -                                 
VNI          : -                                  BD        : -

-----------------------------------------------------------------------------
Total: 1        Dynamic: 0      Static: 1      Remote:0

```

# Display brief information about neighbor entries.
```
<HUAWEI> display ipv6 neighbors brief
D-Dynamic,S-Static,R-Remote
I-INCMP,R-REACH,S-STALE,D-DELAY,P-PROBE
-----------------------------------------------------------------
IPv6 Address         Link-layer       State Type Interface 
-----------------------------------------------------------------
2001:DB8::3         00e0-fc12-3456   I     S     100GE1/0/1                                                               
                                                         
2001:DB8::4         00e0-fc12-3457   I     S    100GE1/0/2                                                                                                                             
-----------------------------------------------------------------
Total: 2        Dynamic: 0      Static: 2      Remote:0

```

**Table 1** Description of the **display ipv6 neighbors** command output
| Item | Description |
| --- | --- |
| IPv6 Address | IPv6 address of the neighbor. |
| Link-layer | Link layer address (MAC address of the neighbor). |
| State | Status of ND entries.   * INCMP: indicates that the neighbor is unreachable. When the address is being resolved, the link layer address of the neighbor is not detected. If resolution succeeds, the neighbor enters the REACH state. * REACH: indicates that the neighbor is reachable within a specified period. By default, the period is 20 minutes. If the period expires and this entry is unused, the entry enters the Stale state. * STALE: indicates that whether the neighbor is reachable is unknown. That is, the entry is unused within a specified period. By default, the period is 20 minutes. In this case, reachability of the neighbor is not detected unless a packet is sent to the neighbor. * DELAY: indicates that whether the neighbor is reachable is unknown. An NS packet has been sent to the neighbor. If no response is received within the specified period, the neighbor entry enters the Probe state. By default, the period is 5 seconds. If an NA Reply message is received, the neighbor entry enters the Reach state. * PROBE: indicates that whether the neighbor is reachable is unknown. The ND entry sends a unicast NS packet according to the interval Retrans Timer at which the RA packet is sent (or the configured value on the host). If no response is received, the ND entry is deleted. If a Reply message is received, the ND entry enters the Reach state. |
| Interface | Interface to which the ND entry belongs. |
| Age | Elapsed time after an ND entry is created, including the following situations:   * The elapsed time after a static entry is created is "-". * The elapsed time after a dynamic entry is created includes the following types:   + The elapsed time of a proactively created dynamic entry is the time that the REACH state lasts, in minutes.   + The elapsed time of a passively learned dynamic entry is the time that elapsed after the entry is created (in minutes) if the entry is in the STALE state. When the state of the entry is changed to REACH, the elapsed time is the time that the REACH state lasts, in minutes. |
| VLAN | Neighbors in the specified VLAN. |
| CEVLAN | Neighbors in the specified VLAN ID of CE. |
| VPN name | Name of the VPN instance to which the neighbor belongs. |
| Is Router | Dynamic entries:  Whether the NA packet sent by the neighbor carries the R flag:   * If the NA packet carries an R flag, TRUE is displayed.   In this case, the neighbor is a routing device.   * If the NA packet does not carry an R flag, "FALSE" is displayed.   In this case, the neighbor may be a PC or a routing device that sends an NA packet without the R flag.  Remote entry:  If remote entries are added through the control plane, TRUE is displayed. |
| Secure FLAG | Secure flag of a neighbor entry.   * UN-SECURE. * SECURE. |
| Nickname | Nickname of an ND entry. |
| Source IP | Source IP address. |
| Destination IP | Destination IP address. |
| VNI | network identifier. |
| BD | Bridge domain. |
| Type | Type of neighbor entries:   * Dynamic: dynamic neighbor entry. * Static: static neighbor entry. * Remote: neighbor entries sent by the remote end. |
| Total | Total number of ND entries. |
| Dynamic | Total number of dynamic ND entries. |
| Static | Total number of static ND entries. |
| Remote | Total number of ND entries sent by the remote end. |