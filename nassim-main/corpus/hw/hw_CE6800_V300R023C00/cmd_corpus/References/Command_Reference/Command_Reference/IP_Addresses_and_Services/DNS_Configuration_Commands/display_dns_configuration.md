display dns configuration
=========================

display dns configuration

Function
--------



The **display dns configuration** command displays the global DNS configurations.




Format
------

**display dns configuration**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view global DNS configurations, run the **display dns configuration** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the global DNS configurations.
```
<HUAWEI> display dns configuration
 -------------------------------------------------------------------------------
 Dns resolve                                 :  Disabled
 Dns-server-select-algorithm                 :  Auto
 Dns server source ip address/vpn-instance   :  1.1.1.1/vpn1
                                             :  2.2.2.2/-
 Dns server source ipv6 address/vpn-instance :  2001:db8:1::1/64/vpn1
                                             :  2001:db8:1::2/-
 Dns server source interface                 :  -
 Dns forward retry-number                    :  2
 Dns forward retry-timeout                   :  3
 Dns application cache ttl limit             :  600 ~ 86400
 Dns server vpn-instance                     :  -
 -------------------------------------------------------------------------------

```

**Table 1** Description of the **display dns configuration** command output
| Item | Description |
| --- | --- |
| Dns resolve | Whether dynamic DNS resolution is enabled. The value can be:   * Enabled: Dynamic DNS resolution is enabled. * Disabled: Dynamic DNS resolution is disabled.   To enable dynamic DNS resolution, run the dns resolve command. |
| Dns server source ip address/vpn-instance | Source IP address and VPN instance used by the local device for DNS communication.  To configure the parameter, run the dns server source-ip command. |
| Dns server source ipv6 address/vpn-instance | Source IPv6 address and VPN instance used by the local device for DNS communication.  To configure the parameter, run the dns server ipv6 source-ip command. |
| Dns server source interface | Whether the IP address of a specified interface is used as the source IP address for DNS communication on the local device.  To set the IP address of a specified interface as the source IP address, run the dns server source-interface command. |
| Dns forward retry-number | Number of times for retransmitting query messages to the destination DNS server.  To set the number of times for retransmitting query messages to the destination DNS server, run the dns forward retry-number command. |
| Dns forward retry-timeout | Retransmission timeout period that the device sends query messages to the destination DNS server.  To configure the parameter, run the dns forward retry-timeout command. |
| Dns application cache ttl limit | Limited TTL of the DNS application cache.  To configure the parameter, run the dns application cache ttl command. |
| Dns server vpn-instance | VPN instance used by the local device for DNS communication. |
| DNS-server-select-algorithm | Algorithm for selecting a destination DNS server. The value can be:   * Fixed: The destination DNS server is selected in fixed order. * Auto: The destination DNS server is selected in auto order.   To specify an algorithm for selecting a destination DNS server, run the dns-server-select-algorithm command. |