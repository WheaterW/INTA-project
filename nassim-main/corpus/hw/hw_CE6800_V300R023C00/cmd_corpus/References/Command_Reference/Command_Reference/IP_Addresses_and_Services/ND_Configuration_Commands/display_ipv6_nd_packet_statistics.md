display ipv6 nd packet statistics
=================================

display ipv6 nd packet statistics

Function
--------



The **display ipv6 nd packet statistics** command displays statistics about ND messages.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 nd packet statistics** [ **slot** *slot-id* | **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Displays ND message statistics based on a specified slot ID. | The value is an integer. You can enter a question mark (?) and select a value from the displayed value range. |
| **interface** *interface-type* *interface-number* | Displays ND message statistics based on a specified interface type and number. | - |
| **interface** *interface-name* | Displays ND message statistics based on a specified interface name. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view ND message statistics for troubleshooting of ND-related issues, run the **display ipv6 nd packet statistics** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display ND message statistics.
```
<HUAWEI> display ipv6 nd packet statistics
Sent Packet Statistics:
-------------------------------------------------------------------------------
Type                               NS         NA         RS         RA

-------------------------------------------------------------------------------
Total                              0          0          0          0
Source IP
    Unspecified                    0          -          -          -
Destination IP
    Unicast                        0          0          -          0
    Multicast                      0          0          0          0
Target IP
    Linklocal                      0          0          -          -
    Global                         0          0          -          -
-------------------------------------------------------------------------------

Received Packet Statistics:
--------------------------------------------------------------------------------------
Type                               NS         NA         RS         RA         ND_MISS
--------------------------------------------------------------------------------------
Recv Total                         0          0          0          0          0
Valid Total                        0          0          0          0          0
Source IP
    Unspecified                    0          -          -          -          -
Destination IP
    Unicast                        0          0          0          0          -
    Multicast                      0          0          0          0          -
Target IP
    Linklocal                      0          0          -          -          -
    Global                         0          0          -          -          -
--------------------------------------------------------------------------------------

Dropped Packet Statistics:
--------------------------------------------------------------------------------------
Type                               NS         NA         RS         RA         ND_MISS
--------------------------------------------------------------------------------------
Total                              0          0          0          0          0
Packet Check
    Checksum error                 0          0          0          0          -
    Bad length                     0          0          0          0          -
    Bad code                       0          0          0          0          -
    Bad hoplimit                   0          0          0          0          -
    Bad source mac                 0          0          0          0          -
    Bad destination mac            0          0          0          0          -
    Bad target mac                 0          0          0          0          -
    Bad source ip                  0          0          0          0          -
    Bad destination ip             0          0          0          0          -
    Bad target ip                  0          0          -          -          -
    Bad option                     0          0          0          0          -
    Local address                  0          0          0          0          -
Anti-attack
    Nd validate mac-check          0          0          0          0          -
    Nd source mac check            0          0          0          0          -
    Global rate-limit              0          0          0          0          0
    Source mac rate-limit          0          0          0          0          -
    Source ip rate-limit           0          0          0          0          0
    Destination ip rate-limit      0          0          0          0          -
    Target ip rate-limit           0          0          -          -          -
    Interface source ip rate-limit 0          0          0          0          0
    Interface rate-limit           0          0          0          0          0
    LR rate-limit                  0          0          0          0          0
--------------------------------------------------------------------------------------

```

**Table 1** Description of the **display ipv6 nd packet statistics** command output
| Item | Description |
| --- | --- |
| Sent Packet Statistics | Statistics about sent packets. |
| Packet Check | Packet check. |
| Type | Type of statistics collection. |
| NS | Number of NS messages. |
| NA | Number of NA messages. |
| RS | Number of RS messages. |
| RA | Number of RA messages. |
| Total | Total number of packets. |
| Source mac rate-limit | Source MAC anti-attack rate limit. |
| Source ip rate-limit | Source IP anti-attack rate limit. |
| Source IP | Source address of ND messages, which is used for neighbor discovery. |
| Unspecified | Number of packets with unspecified source addresses. |
| Destination IP | Outer destination address of ND messages, which is used for packet forwarding. |
| Destination ip rate-limit | Destination IP anti-attack rate limit. |
| Unicast | Unicast address. |
| Multicast | Multicast address. |
| Target IP | Inner destination address of ND messages, which is used for neighbor discovery. |
| Target ip rate-limit | Target IP anti-attack rate limit. |
| Linklocal | Link-local address. |
| Global | Global unicast address. |
| Global rate-limit | Rate limit for packet receiving. |
| Received Packet Statistics | Statistics about received packets. |
| ND\_MISS | Number of ND Miss messages. |
| Recv Total | Number of received packets.  The value of Recv Total is the sum of Valid Total and Total in Dropped Packet Statistics. |
| Valid Total | Number of valid packets.  In the scenario where rate limiting is based on ND Miss messages, if ND entries (incomplete entries) exist, the device continues to send ND Miss messages. These messages are received but not processed, and are counted into Valid Total. |
| Dropped Packet Statistics | Statistics about dropped packets. |
| Checksum error | Checksum error. |
| Bad length | Incorrect packet length. |
| Bad code | Incorrect packet code. |
| Bad hoplimit | Incorrect hop limit. |
| Bad source mac | Incorrect source MAC address in the Layer 2 header. |
| Bad destination mac | Incorrect destination MAC address in the Layer 2 header. |
| Bad source ip | Incorrect source IP address. |
| Bad destination ip | Incorrect destination IP address. |
| Bad target ip | Incorrect target IP address. |
| Bad option | Incorrect packet option. |
| Bad target mac | Incorrect target mac address in the ND message option. |
| Anti-attack | Attack defense check. |
| Nd validate mac-check | Source MAC address consistency check on ND messages. |
| Nd source mac check | Nd source mac check. |
| Interface source ip rate-limit | Interface source IP anti-attack rate limit. |
| Interface rate-limit | Interface ND packet type or ND Miss message anti-attack rate limit. |
| LR rate-limit | LR ND packet type or ND Miss message anti-attack rate limit. |