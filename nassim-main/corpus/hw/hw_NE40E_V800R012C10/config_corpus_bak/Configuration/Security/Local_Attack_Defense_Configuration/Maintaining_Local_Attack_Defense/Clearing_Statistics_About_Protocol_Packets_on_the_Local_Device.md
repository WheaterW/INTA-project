Clearing Statistics About Protocol Packets on the Local Device
==============================================================

Before collecting statistics about received or sent protocol packets, you need to clear the existing packet statistics.

#### Context

After the function of collecting statistics about protocol packets is enabled, you can run the corresponding **display** command to check statistics about protocol packets received by the specified interface. To clear such statistics, run the corresponding **reset** command. The **reset** and **display** commands can be used together to determine whether protocol packets are abnormal.


#### Procedure

1. To clear global statistics about received packets of a specified protocol, run the [**reset ip host packet statistics receive protocol**](cmdqueryname=reset+ip+host+packet+statistics+receive+protocol+arp+stp+lacp) { **arp** | **stp** | **lacp** | **lldp** | **isis** | **icmp** | **ospf** | **pim** | **igmp** | **vrrp** | **snmp** | **dhcp** | **bgp** | **ldp** | **icmpv6** | **ospfv3** | **pimv6** | **mld** | **vrrpv6** | **snmpv6** | **dhcpv6** | **bgp4plus** | **ldpv6** } command in the user view.
2. To clear global statistics about sent packets of a specified protocol, run the [**reset ip host packet statistics send protocol**](cmdqueryname=reset+ip+host+packet+statistics+send+protocol+arp+stp+lacp+lldp) [ **arp** | **stp** | **lacp** | **lldp** | **isis** | **icmp** | **ospf** | **pim** | **igmp** | **vrrp** | **snmp** | **dhcp** | **bgp** | **ldp** | **icmpv6** | **ospfv3** | **pimv6** | **mld** | **vrrpv6** | **snmpv6** | **dhcpv6** | **bgp4plus** | **ldpv6** ] [ **slot** *slot-id* ] command in the user view.
3. To clear statistics about packets received by interfaces that rank top 10 in the number of received packets, run the [**reset ip host packet statistics receive**](cmdqueryname=reset+ip+host+packet+statistics+receive) command in the user view.
4. To clear statistics about protocol packets sent by the specified interface, run the [**reset ip host packet statistics send protocol interface**](cmdqueryname=reset+ip+host+packet+statistics+send+protocol+interface) { *ifType* *ifNum* | *ifName* } command in the user view.
5. To clear statistics about protocol packets received by the specified interface, run the [**reset ip host packet statistics receive protocol interface**](cmdqueryname=reset+ip+host+packet+statistics+receive+protocol+interface) { *ifType* *ifNum* | *ifName* } command in the user view.