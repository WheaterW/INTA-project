Checking Statistics About Protocol Packets on the Local Device
==============================================================

You can run the corresponding **display** command to check statistics about received or sent protocol packets on a device.

#### Prerequisites

Packet statistics collection has been enabled globally or on the specified interface, and historical packet statistics have been cleared.


#### Procedure

1. Enable packet statistics collection globally or on the specified interface.
   * To globally enable the function of collecting statistics about sent and received packets, run the [**ip host packet statistics protocol all**](cmdqueryname=ip+host+packet+statistics+protocol+all) command in the system view.
   * To enable the function of collecting statistics about sent and received packets on the specified interface, run the [**ip host packet statistics protocol enable**](cmdqueryname=ip+host+packet+statistics+protocol+enable) command in the interface view.
2. Check statistics about protocol packets on the device.
   * To check global statistics about received protocol packets, run the [**display ip host packet statistics receive protocol**](cmdqueryname=display+ip+host+packet+statistics+receive+protocol+arp+stp+lacp) { **arp** | **stp** | **lacp** | **lldp** | **isis** | **icmp** | **ospf** | **pim** | **igmp** | **vrrp** | **snmp** | **dhcp** | **bgp** | **ldp** | **icmpv6** | **ospfv3** | **pimv6** | **mld** | **vrrpv6** | **snmpv6** | **dhcpv6** | **bgp4plus** | **ldpv6** } command.
   * To check global statistics about sent protocol packets, run the [**display ip host packet statistics send protocol**](cmdqueryname=display+ip+host+packet+statistics+send+protocol+arp+stp+lacp) [ **arp** | **stp** | **lacp** | **lldp** | **isis** | **icmp** | **ospf** | **pim** | **igmp** | **vrrp** | **snmp** | **dhcp** | **bgp** | **ldp** | **icmpv6** | **ospfv3** | **pimv6** | **mld** | **vrrpv6** | **snmpv6** | **dhcpv6** | **bgp4plus** | **ldpv6** ] command.
   * To check statistics about packets received by interfaces that rank top 10 in the number of received packets, run the [**display ip host packet statistics receive**](cmdqueryname=display+ip+host+packet+statistics+receive) command.
   * To check statistics about sent protocol packets on the specified board, run the [**display ip host packet statistics send protocol**](cmdqueryname=display+ip+host+packet+statistics+send+protocol+arp+stp+lacp) { **arp** | **stp** | **lacp** | **lldp** | **isis** | **icmp** | **ospf** | **pim** | **igmp** | **vrrp** | **snmp** | **dhcp** | **bgp** | **ldp** | **icmpv6** | **ospfv3** | **pimv6** | **mld** | **vrrpv6** | **snmpv6** | **dhcpv6** | **bgp4plus** | **ldpv6** } **slot** [ *slot-id* ] command.
   * To check statistics about sent protocol packets on the specified interface, run the [**display ip host packet statistics send protocol interface**](cmdqueryname=display+ip+host+packet+statistics+send+protocol+interface) { *ifType* *ifNum* | *ifName* } command.
   * To check statistics about received protocol packets on the specified interface, run the [**display ip host packet statistics receive protocol interface**](cmdqueryname=display+ip+host+packet+statistics+receive+protocol+interface) { *ifType* *ifNum* | *ifName* } command.