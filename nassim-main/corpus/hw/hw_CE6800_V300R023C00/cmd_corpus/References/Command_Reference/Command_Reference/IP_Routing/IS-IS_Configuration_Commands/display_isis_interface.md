display isis interface
======================

display isis interface

Function
--------



The **display isis interface** command displays information on IS-IS interfaces.




Format
------

**display isis interface** { *interface-name* | *interface-type* *interface-number* } [ **verbose** ]

**display isis** *process-id* **interface** [ **verbose** ]

**display isis interface** [ **verbose** ] [ **vpn-instance** *vpn-instance-name* ]

**display isis** *process-id* **interface** { *interface-name* | *interface-type* *interface-number* } [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Displays detailed information about interfaces. | - |
| *process-id* | Specifies the ID of an IS-IS process. | The value is an integer ranging from 1 to 4294967295.  If no IS-IS process is specified, information about interfaces in all local IS-IS processes is displayed. |
| **interface** *interface-type* *interface-number* | Specifies the interface type and interface number. | - |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| **vpn-instance** *vpn-instance-name* | Displays interface information about an IS-IS multi-instance process in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information on IS-IS interfaces, including the interface name, IP address, link status of each interface, run the display isis interface command. If verbose is specified, the output of this command also covers IS-IS parameter configurations for each interface, such as the CSNP broadcast interval, hello packet broadcast interval, and the number of IS-IS Hello packets sent by the neighbor before IS-IS should declare the neighbor Down.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information on IS-IS interfaces.
```
<HUAWEI> display isis interface verbose

Interface Information for ISIS(1)
--------------------------------------------------------------------------------

 Interface         ID      IPV4 State          IPV6 State      MTU  Type  DIS
 100GE1/0/1         001 Mtu:Dn/Lnk:Dn/IP:Up Mtu:Dn/Lnk:Dn/IP:Dn 1497 L1/L2 No/No
  Description                 :
  SNPA Address                : 00e0-fc12-3456
  IP Address                  : 10.2.3.4
  IPV6 Link Local Address     :
  IPV6 Global Address(es)     :
  Csnp Timer Value            :  L1    10  L2    10
  Hello Timer Value           :  L1    10  L2    10
  DIS Hello Timer Value       :  L1     3  L2     3
  Hello Multiplier Value      :  L1     3  L2     3
  LSP-Throttle Timer          :  L12    50 <ms>
  Cost                        :  L1    10  L2    10
  Ipv6 Cost                   :  L1     0  L2     0
  Priority                    :  L1    64  L2    64
  Retransmit Timer Value      :  L1     5  L2     5
  Bandwidth-Value             :  Low  100000000  High          0
  Static BFD                  :  NO
  Dynamic BFD                 :  NO
  Static IPv6 BFD             :  NO
  Dynamic IPv6 BFD            :  NO
  Suppress Base               :  NO
  IPv6 Suppress Base          :  NO
  Extended-Circuit-Id Value   :  0000000000
  Circuit State               :  OSI:UP     IP:UP     MTU:DOWN   SNPA:UP
                                 BandWidth:UP     IsEnable:UP     Interface:DOWN
  Circuit Ipv6 State          :  OSI:UP     IP:DOWN   MTU:DOWN   SNPA:UP
                                 BandWidth:UP     IsEnable:DOWN   Interface:DOWN
  Link quality adjust cost    :  NO
  IPv6 Link quality cost      :  NO
  Link quality                :  0x0(GOOD)
  CRC-ERR State               :  0x1(UP)
  Effective Link Quality      :  0x0(GOOD)
  Suppress flapping peer      :  YES(flapping-count: 0, threshold: 10)

```

**Table 1** Description of the **display isis interface** command output
| Item | Description |
| --- | --- |
| Interface | Type and number of an interface. |
| IPV6 Link Local Address | IPv6 Link-local address. |
| IPV6 Global Address(es) | Circuit IPv6 address. |
| MTU | MTU size. |
| Type | Interface type:   * L1: Level-1 interface. * L2: Level-2 interface. * L1/L2: Level-1 and Level-2 interfaces. |
| DIS | Whether the interface is a Designated Intermediate System (DIS):   * No/No: The interface is not a DIS either in the Level-1 or Level-2 area. * Yes/Yes: The interface is a DIS in both Level-1 and Level-2 areas. * Yes/No: The interface is a DIS in the Level-1 area. * No/Yes: The interface is a DIS in the Level-2 area. * --: The interface is P2P, and it cannot be a DIS. |
| DIS Hello Timer Value | Indicates the interval for the DIS to send Hello packets. The value of this field is one third of Hello Timer Value. This field is valid only when the interface is a DIS. |
| Description | Interface description. |
| SNPA Address | MAC address of a DHCP client. |
| SNPA | SNPA status. |
| IP Address | Primary IPv4 address of the interface. |
| Link quality adjust cost | Whether bit-error-triggered interface cost adjustment is effective:   * NO. * YES.   The prerequisites for the function to take effect are as follows:   * The cost specified in the isis link-quality low incr-cost cost command is not 0. * The link quality is 0x4 (Low). For details, see the description of the Link quality field. * LDP-IS-IS synchronization is not in HoldMaxCost state. To check the state, run the display isis ldp-sync interface command. * Neighbor relationship flapping suppression is not in hold-max-cost state. For details, see the description of the Suppress flapping peer field. |
| Link quality | Link quality. The bit error rate is: LOW > MEDIUM > HIGH > GOOD.   * 0x0(GOOD). * 0x1(HIGH). * 0x2(MEDIUM). * 0x4(LOW). |
| Csnp Timer Value | Interval at which the intermediate system sends CSNPs, which can be set using the isis timer csnp command. Modifying the interval affects IS-IS route convergence. |
| Hello Timer Value | Interval at which the IS sends Hello packets, which can be set using the isis timer hello command. |
| Hello Multiplier Value | Number of sent IS-IS Hello packets that are not replied by a neighbor before the local device declares the neighbor Down. The value can be set using the isis timer holding-multiplier command. Because the value determines the hold time of IS-IS neighbor relationships, referring the usage guideline of the command before configuring the value is recommended. |
| LSP-Throttle Timer | Minimum interval at which LSPs are sent, which can be set using the isis timer lsp-throttle command. |
| Cost | Cost of an IPv4 interface. The value of this field affects route selection in an IPv4 topology. |
| Ipv6 Cost | IPv6 cost on an interface. The value is decisive in route selection. |
| Priority | DIS priority of an interface, which can be set using the isis dis-priority command. The interface with the highest DIS priority is selected as the DIS. |
| Retransmit Timer Value | LSP retransmission timer, which is set using the isis timer lsp-retransmit command. |
| Bandwidth-Value | Bandwidth of an interface. The value can be calculated using the following formula:  Bandwidth-Value = 4294967296 x high + low. For example, if the value of high is 1 and the value of low is 705032704, Bandwidth-Value = 1 x 4294967296 + 705032704 = 5000000000.   * low: The maximum value is 4294967295. * high: The maximum value is 4294967295. |
| Static Bfd | Whether static BFD is enabled:   * NO. * YES. |
| Static IPv6 Bfd | Whether static BFD for IPv6 is enabled.   * NO. * YES. |
| Static BFD | Whether static BFD is enabled:   * NO. * YES. |
| Static IPv6 BFD | Whether IPv6 static BFD is enabled:   * NO. * YES. |
| Dynamic Bfd | Whether dynamic BFD is enabled:   * NO. * YES. |
| Dynamic IPv6 Bfd | Whether dynamic IPv6 BFD is enabled.   * NO. * YES. |
| Dynamic BFD | Whether dynamic BFD is enabled:   * NO. * YES. |
| Dynamic IPv6 BFD | Whether dynamic IPv6 BFD is enabled:   * NO. * YES. |
| IPv6 Link quality cost | Whether bit-error-triggered interface cost adjustment is effective:   * NO. * YES.   The prerequisites for the function to take effect are as follows:   * The cost specified in the isis ipv6 link-quality low incr-cost cost command is not 0. * The link quality is 0x4 (Low). For details, see the description of the Link quality field. * Neighbor relationship flapping suppression is not in hold-max-cost state. For details, see the description of the Suppress flapping peer field. |
| IPv6 Suppress Base | Whether an interface belongs to an IPv6 base topology: - NO - YES. |
| Suppress flapping peer | Status of IS-IS neighbor relationship flapping suppression:   * NO: IS-IS neighbor relationship flapping suppression is disabled. * YES (flapping-count: 3, threshold: 10): IS-IS neighbor relationship flapping suppression is enabled and IS-IS neighbor relationship is not suppressed. The flapping-count and threshold value. * Hold-down(start: UTC 10:20:30, remain-interval: 7): IS-IS neighbor relationship flapping suppression works in Hold-down mode. The starting and remaining time of the flapping suppression. * Hold-max-cost(start: UTC 10:20:30, remain-interval: 7): IS-IS neighbor relationship flapping suppression works in Hold-max-cost mode. The starting and remaining time of the flapping suppression.   In the flapping suppression state, remain-interval is reset each time when the device detects a valid neighbor flapping event. |
| Suppress Base | Whether an interface belongs to an IPv4 base topology:   * NO. * YES. |
| Extended-Circuit-Id Value | Link ID of an interface. |
| Circuit State | Interface state. |
| Circuit Ipv6 State | IPv6 protocol status on the interface. |
| CRC-ERR State | CRC-error state of an interface.   * 0x0(DOWN). * 0x1(UP). |
| Effective Link Quality | Link quality that takes effect. The value is obtained based on the Link quality and CRC-ERR state fields. If Link quality is LOW or CRC-ERR state is DOWN, the value of this field is LOW.   * 0x0(GOOD). * 0x1(HIGH). * 0x2(MEDIUM). * 0x4(LOW). |
| Id | ID of a link. |
| BandWidth | BandWidth status. |
| IsEnable | ISIS circuit status. |
| OSI | Indicates the OSI status. |