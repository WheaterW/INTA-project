(Optional) Configuring a Priority for Protocol Packets
======================================================

You can set the differentiated services code point (DSCP) value of management or control protocol packets sent by the local device, and enable the protocol packets to enter the specified internal priority queue and obtain the corresponding colors based on the DSCP values.

#### Context

Currently, when the NE40E performs internal scheduling on protocol packets, by default, it places the protocol packets in the CS6 queue without colors, and the priority of the packets is fixed. If you use the CS6 queue for another purpose or not for service forwarding, services are affected. In addition, on the downstream device, scheduling requirements of specified protocol packets may fail to be met because these packets may enter the low-priority QoS queue. Therefore, to allow for flexible packet scheduling, allow these packets to enter other queues.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure the DSCP value of management or control protocol packets based on the packet type.
   * Run the [**host-packet type**](cmdqueryname=host-packet+type) { **management-protocol** | **control-protocol** } **dscp** *dscp-value* command to configure the DSCP value of IPv4 management or control protocol packets.
   * Run the [**host-packet ipv6 type**](cmdqueryname=host-packet+ipv6+type) { **management-protocol** | **control-protocol** } **dscp** *dscp-value* command to configure the DSCP value of IPv6 management or control protocol packets.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Generally, each protocol has a default DSCP value, and the DSCP values of some protocols can be configured using the **host-packet type** command or the corresponding commands for changing the DSCP values of the protocols. In this case, the rules for the DSCP values to take effect as follows:
   
   * If a protocol has its own command for changing the DSCP value, the DSCP value configured using its own command takes effect regardless of whether the DSCP value is controlled by the **host-packet type** command.
   * If a protocol does not have its own command for changing the DSCP value and the DSCP value is controlled by the **host-packet type** command, the DSCP value configured using the command takes effect.
   * If a protocol does not have its own command for changing the DSCP value and the DSCP value is not controlled by the **host-packet type** command, the default DSCP value takes effect.
   
   For details about the DSCP value and meaning corresponding to each PHB, see [DSCP and PHB](feature_0021577549.html).
   
   [Table 1](#EN-US_TASK_0172371290__table16936823201416) and [Table 2](#EN-US_TASK_0172371290__table478194617114) describe how to change the ToS/DSCP value of the IPv4 protocol and the traffic class/DSCP value of the IPv6 protocol, respectively.
   
   **Table 1** ToS/DSCP value of IPv4 and its modification method
   | Protocol | Default ToS/DSCP Value | Controlled by the **host-packet type** Command | Modification Command for Each Protocol |
   | --- | --- | --- | --- |
   | ICMP\_ECHO | 0 | No | **ping** **-dscp** *dscp-value* |
   | ICMP\_ECHO\_REPLY | 0 | No | N/A |
   | ICMP Error | 48 | No | N/A |
   | DNS | 0 | No | N/A |
   | FTP | 48 | Yes (**host-packet type** **management-protocol dscp**) | N/A |
   | TFTP | 48 | Yes (**host-packet type** **management-protocol dscp**) | N/A |
   | SNMP | 48 | Yes (**host-packet type** **management-protocol dscp**) | **snmp-agent packet-priority** **snmp** *priority-level* |
   | SSH | 48 | Yes (**host-packet type** **management-protocol dscp**) | **ssh server dscp** *value* |
   | Telnet | 48 | Yes (**host-packet type** **management-protocol dscp**) | **telnet server dscp** *value* |
   | Syslog (UDP) | 0 | Yes (**host-packet type** **management-protocol dscp**) | **info-center syslog packet-priority** *priority-level*  The **info-center syslog packet-priority** *priority-level* command takes precedence over the **host-packet type** **management-protocol dscp** command. |
   | Syslog (TCP) | 0 | No | **info-center syslog packet-priority** *priority-level* |
   | HWTACACS | 48 | Yes (**host-packet type** **management-protocol dscp**) | N/A |
   | RADIUS | 48 | No | N/A |
   | NTP | 48 | Yes (**host-packet type** **control-protocol dscp**) | N/A |
   | BFD | 56 | No | **tos-exp** *tos-value* (BFD session view)  **tos-exp** *tos-value* { **dynamic** | **static** } (BFD view) |
   | IGMP | 48 | No | N/A |
   | PIM | 48 | No | N/A |
   | CUSP | 48 | Yes (**host-packet type** **control-protocol dscp**) | N/A |
   | BGP | 48 | Yes (**host-packet type** **control-protocol dscp**) | N/A |
   | LDP | 48 | Yes (**host-packet type** **control-protocol dscp**) | N/A |
   | OSPF | 48 | Yes (**host-packet type** **control-protocol dscp**) | N/A |
   | DHCP Server/DHCP Relay | 48 | No | **dhcp dscp-outbound** *value* |
   | DHCP Snooping | 0 | No | N/A |
   | GRE | If the inner IP ToS is valid, the ToS/DSCP value of the inner IP packet is inherited. Otherwise, it is set to 48. | No | N/A |
   | IKE | 48 | No | N/A |
   | VXLAN | If the inner IP ToS is valid, the ToS/DSCP value of the inner IP packet is inherited. Otherwise, it is set to 48. | No | N/A |
   | RSVP-TE | 48 | No | N/A |
   | MSDP | 48 | No | N/A |
   | PCEPv4 | 48 | No | **dscp** *dscp-val* |
   
   
   **Table 2** Traffic class/DSCP value of IPv6 and its modification method
   | Protocol | Default Traffic Class/DSCP Value | Controlled by the **host-packet type** Command | Modification Command for Each Protocol |
   | --- | --- | --- | --- |
   | ICMP6\_ECHO | 0 | No | **ping ipv6** **-tc** *traffic-class-value* |
   | ICMP6\_ECHO\_REPLY | Copied from the TC/DSCP value of an ICMP6\_ECHO message | No | N/A |
   | ICMP6 Error | Copied from the TC/DSCP value of an ICMP6\_ECHO message | No | N/A |
   | ND (NS/NA/RS/RA) | 48 | No | N/A |
   | TNL6 (IPv6 over IPv4) | 0 | No | N/A |
   | TNL6 (IPv4 over IPv6) | 0 | No | **tunnel ipv4-ipv6 traffic-class** *class-value* |
   | DNSv6 | 0 | No | N/A |
   | FTPv6 | 0 | Yes ([**host-packet ipv6 type management-protocol dscp**](cmdqueryname=host-packet+ipv6+type+management-protocol+dscp)) | N/A |
   | TFTPv6 SERVER | NA | No | NA |
   | TFTPv6 CLIENT | 0 | Yes ([**host-packet ipv6 type management-protocol dscp**](cmdqueryname=host-packet+ipv6+type+management-protocol+dscp)) | NA |
   | SNMPv6 | 48 | No | **snmp-agent packet-priority** **snmp** *priority-level* |
   | SSHv6 | 0 | Yes ([**host-packet ipv6 type management-protocol dscp**](cmdqueryname=host-packet+ipv6+type+management-protocol+dscp)) | N/A |
   | Telnetv6 | 0 | Yes ([**host-packet ipv6 type management-protocol dscp**](cmdqueryname=host-packet+ipv6+type+management-protocol+dscp)) | N/A |
   | Syslog (UDP) | 0 | Yes ([**host-packet ipv6 type management-protocol dscp**](cmdqueryname=host-packet+ipv6+type+management-protocol+dscp)) | **info-center syslog packet-priority** *priority-level* |
   | Syslog (TCP) | 0 | No | **info-center syslog packet-priority** *priority-level* |
   | HWTACACS | 48 | No | N/A |
   | RADIUS | 48 | No | N/A |
   | NTPv6 | 0 | Yes ([**host-packet ipv6 type management-protocol dscp**](cmdqueryname=host-packet+ipv6+type+management-protocol+dscp)) | N/A |
   | BFDv6 | 56 | No | **tos-exp** *tos-value* (BFD session view) |
   | **tos-exp** *tos-value* { **dynamic** | **static** } (BFD view) |
   | MLD | 48 | No | N/A |
   | PIMv6 | 48 | No | N/A |
   | BGP4+ | 48 | Yes ([**host-packet ipv6 type control-protocol dscp**](cmdqueryname=host-packet+ipv6+type+control-protocol+dscp)) | N/A |
   | OSPFv3 | 48 | Yes ([**host-packet ipv6 type control-protocol dscp**](cmdqueryname=host-packet+ipv6+type+control-protocol+dscp)) | N/A |
   | DHCPv6 | 48 | No | N/A |
   | GRE | If the inner IP TC is valid, the TC/DSCP value of the inner IP packet is inherited. Otherwise, it is set to 48. | No | N/A |
   | VXLAN | If the inner IP TC is valid, the TC/DSCP value of the inner IP packet is inherited. Otherwise, it is set to 48. | No | N/A |
3. Run [**host-packet dscp**](cmdqueryname=host-packet+dscp) *dscp-value* **map local-service** *cos-value* [ **color** *color* ]
   
   
   
   Mappings between DSCP values of protocol packets and internal priorities and between DSCP values and colors are configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The DSCP value in the [**host-packet type**](cmdqueryname=host-packet+type) command only indicates the priority of protocol packets. 802.1p priorities of Layer 2 protocol packets are mapped from the DSCP value based on the DS domain configured on the outbound interface. EXP priorities of MPLS packets are the leftmost 3 bits of the DSCP value. If this command is not used, sent protocol packets carry the preconfigured priority.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.