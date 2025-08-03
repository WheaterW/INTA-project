display cpu-defend configuration
================================

display cpu-defend configuration

Function
--------



The **display cpu-defend configuration** command displays CAR configurations.




Format
------

**display cpu-defend configuration** [ **packet-type** *packet-type* ] { **all** | **slot** *slot-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **packet-type** *packet-type* | Displays the configuration of rate limiting for packets of a specified type. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ: The value can be acl-logging, arn, arn-logging, arp-miss, arp-mlagpeer, arp-reply, arp-request, arp-request-uc, bfd, bgp, bgp4plus, bgp4plus-overlay, bgp-overlay, buffer-drop, cdp, dhcp-reply, dhcp-request, dhcpv6-discovery, dhcpv6-reply, dhcpv6-request, dldp, dns-reply, dpfr-downlink-outbound, dpfr-notification, dpfr-uplink-sampling, fib-hit, fib-miss, ftp, gre-keepalive, headroom-detect, hw-tacacs, icmp, icmpv6, ifit, igmp, inof-rpfr, ipv4-multicast-registration, ip-option, isis, isis-overlay, lacp, ldap, lldp, macsec, mld, mtu, m-lag, m-lag-heart, m-lag-sync, nd, nd-dad, nd-mlagpeer, netstream, ntp, ospf, ospf-hello, ospf-hello-overlay, ospf-overlay, ospfv3, ospfv3-overlay, pim, pimv6, pimv6-mc, pim-mc, ptp-1588, ptp-ann-change, ptp-ann-timeout, radius, rip, ripng, rip-terminated, sampling, scnp, snmp, ssh, ssm, stp, tcp, telnet, ttl-expired, udp, unknown-multicast, vbst, vrrp, vrrp6 or vxlan-detect.  The macsec parameter is supported only after the MACsec feature package is installed on the device.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM: The value can be acl-logging, any-flow, arn, arn-logging, arp-miss, arp-mlagpeer, arp-reply, arp-request, arp-request-uc, bfd, bgp, bgp4plus, bgp4plus-overlay, bgp-overlay, buffer-drop, cdp, cnp, dhcp-reply, dhcp-request, dhcpv6-discovery, dhcpv6-reply, dhcpv6-request, dldp, dns-reply, fib-hit, fib-miss, forward-drop, ftp, gre-keepalive, headroom-detect, hw-tacacs, icmp, icmpv6, igmp, inof-rpfr, ioam, ipv4-multicast-registration, ip-option, iqcn-sync, isis, isis-overlay, lacp, latency, ldap, lldp, macsec, mld, mtu, m-lag, m-lag-heart, m-lag-sync, nd, nd-dad, nd-mlagpeer, netstream, npcc-roce, ntp, ospf, ospf-hello, ospf-hello-overlay, ospf-overlay, ospfv3, ospfv3-overlay, pim, pimv6, pimv6-mc, pim-mc, ptp-1588, ptp-ann-change, ptp-ann-timeout, radius, rip, ripng, rip-terminated, sampling, scnp, snmp, ssh, ssm, stp, tcp, telnet, traffic-analysis, ttl-expired, udp, unknown-multicast, vbst, vrrp, vrrp6 or vxlan-detect.  The macsec parameter is supported only after the MACsec feature package is installed on the device.  For the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S:The value can be 8021x, 8021x-ident, 8021x-start, acl-logging, arp-miss, arp-malgpeer, arp-reply, arp-request, arp-request-uc, bfd, bgp, bgp4plus, bgp4plus-overlay, bgp-overlay, buffer-drop, cdp, dhcp-discovery, dhcp-reply, dhcp-request, dhcpv6-discovery, dhcpv6-reply, dhcpv6-request, dldp, dns-reply, erps, fib-hit, fib-miss, forward-drop, ftp, gre-keepalive, headroom-detect, hw-tacacs, icmp, icmpv6, igmp, ipv4-multicast-registration, ip-option, isis, isis-overlay, l2pt, lacp, ldap, lldp, mac-miss, mice-elephant-flow, mice-elephant-flow-statistics, mld, m-lag, m-lag-heart, m-lag-sync, mtu, nac-arp-reply, nac-arp-request, nac-dhcp, nac-dhcpv6, nac-nd, nd, nd-dad, nd-miss, nd-mlagpeer, ntp, ospf, ospf-hello, ospf-hello-overlay, ospf-overlay, ospfv3, ospfv3-overlay, pim, pim-mc, ptp-ann-change, ptp-ann-timeout, pimv6, pimv6-mc, radius, rip, ripng, rip-terminated, said-ping, smart-link, snmp, ssh, stp, tcp, telnet, ttl-expired, udp, unknown-multicast, vbst, vrrp, vrrp6 or vxlan-detect.  For the CE6885-LL (low latency mode):The value can be acl-logging, arn, arn-logging, arp-miss, arp-mlagpeer, arp-reply, arp-request, arp-request-uc, bfd, bgp, buffer-drop, cdp, dhcp-reply, dhcp-request, dldp, dns-reply, fib-hit, fib-miss, ftp, hw-tacacs, icmp, igmp, ipv4-multicast-registration, ip-option, isis, lacp, ldap, lldp, mac-learning, m-lag, m-lag-heart, m-lag-sync, netstream, ntp, ospf, pim, pim-mc, ptp-1588, ptp-ann-change, ptp-ann-timeout, radius, rip, sampling, scnp, snmp, ssh, ssm, stp, tcp, telnet, traffic-analysis, ttl-expired, udp, unknown-multicast, vbst or vrrp. |
| **all** | Displays CAR configurations of all slots. | - |
| **slot** *slot-id* | Displays CAR configurations of a specified slot. | The value must be set according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the display cpu-defend configuration command to view the rate limit of protocol packets sent to the CPU. By default, the rate limit of protocol packets in the default policy is displayed.After the device is initialized, for protocols whose status is disabled in the command output, you need to deliver service configurations to change their status to enabled first, so that the protocol packets can be sent to the CPU and their rate limits can take effect.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the CAR configurations of all devices.
```
<HUAWEI> display cpu-defend configuration all
Car configurations on slot 1 :      
----------------------------------------------------------------------                                                              
PacketType            Status      Current(pps) Default(pps)      Queue                                                              
----------------------------------------------------------------------                                                              
......
arp-miss              Enabled             1536         1536          1                                                              
arp-reply             Enabled             2048         2048          2                                                              
arp-request           Enabled             2048         2048          2                                                              
arp-request-uc        Enabled             2048         2048          2                                                              
bfd                   Enabled              512          512          6                                                              
bgp                   Enabled             1024         1024          3                                                              
......
----------------------------------------------------------------------                                                              
Car all-packets (pps) : 10000                                                                                                       
----------------------------------------------------------------------

```

**Table 1** Description of the **display cpu-defend configuration** command output
| Item | Description |
| --- | --- |
| Car configurations on slot 1 | CAR configurations on the device. |
| Car all-packets (pps) | Rate limit for packets sent to the CPU. To set the rate limit for packets sent to the CPU, run the car all-packets pps command. |
| PacketType | Packet type. |
| Status | Protocol packet status.   * Enabled: indicates that the protocol is enabled. * Disabled: indicates that the protocol is disabled.   When the protocol is disabled, the device cannot limit the rate of packets. |
| Current(pps) | Current rate limit for packets in use, in pps. To set the rate limit for packets, run the car command. |
| Default(pps) | Rate limit for packets by default, in pps. |
| Queue | Queue ID of packets. |