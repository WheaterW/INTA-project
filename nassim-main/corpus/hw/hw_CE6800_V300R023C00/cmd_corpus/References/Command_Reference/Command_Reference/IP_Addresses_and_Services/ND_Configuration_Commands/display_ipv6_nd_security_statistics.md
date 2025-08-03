display ipv6 nd security statistics
===================================

display ipv6 nd security statistics

Function
--------



The **display ipv6 nd security statistics** command displays the statistics of IPv6 SEND messages on a specified interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 nd security statistics** { *interface-name* | *interface-type* *interface-num* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Displays statistics of IPv6 SEND messages based on a specified interface name. | - |
| *interface-type* *interface-num* | Displays statistics of IPv6 SEND messages based on a specified interface type and number. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check whether SEND functions properly, run the display ipv6 nd security statistics command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the statistics on SEND messages on 100GE 1/0/1.
```
<HUAWEI> display ipv6 nd security statistics 100ge 1/0/1
Received Packet Statistics:
------------------------------------------------------------------------------
Type                      NA         NS         RA         RS         Redirect
------------------------------------------------------------------------------
Total                     0          0          0          0          0
Secured                   0          0          0          0          0
Unsec: No CGA             0          0          0          0          0
Unsec: No RSA             0          0          0          0          0
Unsec: KeyLen Mismatch    0          0          0          0          0
Unsec: Others             0          0          0          0          0

Sent Packet Statistics:
------------------------------------------------------------------------------
Type                      NA         NS         RA         RS         Redirect
------------------------------------------------------------------------------
Sent                      0          0          0          0          0
Aborted                   0          0          0          0          0

Dropped Packet Statistics:
------------------------------------------------------------------------------
Type                      NA         NS         RA         RS         Redirect
------------------------------------------------------------------------------
No Nonce                  0          0          0          0          0
No TS                     0          0          0          0          0
CGA Verify Fail           0          0          0          0          0
RSA Verify Fail           0          0          0          0          0
Nonce Verify Fail         0          0          0          0          0
TS Verify Fail            0          0          0          0          0
RateLimit                 0          0          0          0          0
Fully Secured Mode        0          0          0          0          0

```

**Table 1** Description of the **display ipv6 nd security statistics** command output
| Item | Description |
| --- | --- |
| Received Packet Statistics | Statistics on received messages. |
| Type | Message type, including NA, NS, Router Advertisement (RA), Router Solicitation (RS), and Redirect messages. |
| Total | Total number of received ND messages, including secure and insecure messages. |
| Secured | Number of received secure ND messages that have passed the Nonce, Timestamp, CGA, and RSA authentication. |
| Unsec: No CGA | Number of received ND messages that carry some security options but are considered insecure due to the following reasons in non-strict security mode:   * The source addresses of received RS messages are not unspecified addresses and do not carry the CGA option. * The NS, NA, and RA message do not carry the CGA option. |
| Unsec: No RSA | Number of received ND messages that carry some security options but are considered insecure due to the following reasons in non-strict security mode:   * The source addresses of received RS messages are not unspecified addresses and do not carry the RSA option. * The NS, NA, and RA message do not carry the RSA option. |
| Unsec: KeyLen Mismatch | Number of received ND messages that carry the Nonce, Timestamp, CGA, or RSA options and pass the Nonce, Timestamp, and CGA authentication but are considered insecure because the key length exceeds the allowable range in non-strict security mode. |
| Unsec: Others | Number of ND messages that are considered insecure due to but not limited to the following reasons in non-strict security mode:   * The received ND messages do not carry any security option (Nonce, Timestamp, CGA, or RSA option). * The received ND messages carry some security options but not Nonce and Timestamp options. * The received ND messages carry the RSA option but not the Timestamp option. * The received RS/NS messages carry the RSA option but not the Nonce option. These four reasons are listed in sequence, and the statistics are collected only once for ND messages that are considered insecure due to any of these reasons. |
| No Nonce | Number of received RS/NS messages that carry the RSA option but not the Nonce option in strict security mode. |
| No TS | Number of received ND messages that carry the RSA option but not the Timestamp option in strict security mode. |
| CGA Verify Fail | Number of messages that fail CGA authentication in strict security mode. |
| RSA Verify Fail | Number of messages that fail RSA authentication and the RSA key length exceeds the allowable range in strict security mode. |
| Sent Packet Statistics | Statistics on sent messages. |
| Sent | Total number of sent ND messages. |
| Aborted | Total number of messages that are discarded before being sent. |
| Dropped Packet Statistics | Statistics about discarded packets in strict security mode. |
| Nonce Verify Fail | Number of messages that fail Nonce authentication in strict security mode. |
| TS Verify Fail | Number of messages that fail Timestamp authentication in strict security mode. |
| RateLimit | Number of messages that are discarded because the RSA signature computation and authentication rates exceed the upper limits in strict security mode. |
| Fully Secured Mode | Number of messages that are discarded because they are considered insecure due to any of the following reasons in strict security mode:   * The source addresses of received RS messages are not unspecified addresses and do not carry the CGA or RSA option. * The source addresses of received RS messages are not unspecified addresses. * The NS, NA, and RA message do not carry the CGA or RSA option. * The received ND messages carry some security options but not Nonce and Timestamp options. |