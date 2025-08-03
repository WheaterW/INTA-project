Setting Bandwidth Values and Weights for the Protocol Group Whose Packets Are to Be Sent to the CPU
===================================================================================================

You can specify the CIR, and weight for a protocol group of packets to be sent to the CPU according to the actual networking requirements. With the configuration, if the queues of packets to be sent to the CPU are full, the packets of the specified protocol group can be processed by the CPU in time.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Run [**protocol-group**](cmdqueryname=protocol-group+whitelist+user-defined-flow+management) { **whitelist** | **user-defined-flow** | **management** | **route-protocol** | **multicast** | **arp** | **mpls** | **access-user** | **link-layer** | **network-layer** | **system-message** | **blacklist** | **check-failed** | **fwddata-to-cp** } { **cir** *cir-value* | **weight** *weight-value* } \*
   
   
   
   The bandwidth and weight are set for a specified protocol group.
4. Set a weight for packets in a specified protocol queue of a protocol group.
   
   
   
   **Table 1** Setting weights for protocol queues
   | Operation | Command |
   | --- | --- |
   | Set a weight for packets in a protocol queue of the whitelist protocol group. | [**protocol-group**](cmdqueryname=protocol-group+whitelist+queue+whitelist-bgp+whitelist-ldp) **whitelist** **queue** { **whitelist-bgp** | **whitelist-ldp** | **whitelist-management** | **whitelist-multicast** | **whitelist-reserve** } **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of the user-defined flow protocol group. | [**protocol-group**](cmdqueryname=protocol-group+user-defined-flow+queue+user-define-flow-1) **user-defined-flow** **queue** { **user-define-flow-1** | **user-define-flow-2** | **user-define-flow-3** | **user-define-flow-4** | **user-define-flow-5** | **user-define-flow-6** | **user-define-flow-7** | **user-define-flow-8** } **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of the management protocol group. | [**protocol-group**](cmdqueryname=protocol-group+management+queue+dcn+ftp+ntp+snmp+ssh+sshv6) **management** **queue** { **dcn** | **ftp** | **ntp** | **snmp** | **ssh** | **sshv6** | **syslog** | **telnet** } **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of the routing protocol group. | [**protocol-group**](cmdqueryname=protocol-group+route-protocol+queue+bgp+bgpv6+isis+ospf+ospfv3) **route-protocol** **queue** { **bgp** | **bgpv6** | **isis** | **ospf** | **ospfv3** | **rip** } **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of multicast packets. | [**protocol-group**](cmdqueryname=protocol-group+multicast+queue+igmp+multicast-reserve+msdp+pim) **multicast** **queue** { **igmp** | **multicast-reserve** | **msdp** | **pim** } **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of the ARP protocol group. | [**protocol-group**](cmdqueryname=protocol-group+arp+queue+arp+nd+weight) **arp** **queue** { **arp** | **nd** } **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of the MPLS protocol group. | [**protocol-group**](cmdqueryname=protocol-group+mpls+queue+ldp+oam-ping+rsvp+vxlan+weight) **mpls** **queue** { **ldp** | **oam-ping** | **rsvp** | **vxlan** } **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of the user access protocol group. | [**protocol-group**](cmdqueryname=protocol-group+access-user+queue+bas-arp+bas-igmp+bas-nd) **access-user** **queue** { **bas-arp** | **bas-igmp** | **bas-nd** | **bas-trigger** | **dhcp** | **dhcpv6** | **eapol** | **l2tp** | **lldp** | **ppp** | **vbas-reserve** | **web** } **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of the link-layer protocol group. | [**protocol-group**](cmdqueryname=protocol-group+link-layer+queue+3ah+bfd+link-detect+trunk+y1731) **link-layer** **queue** { **3ah** | **bfd** | **link-detect** | **trunk** | **y1731** | **interface-rdi** | **lag-check** | **lag-ping-trace** | **mac-vlan** } **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of the network-layer protocol group. | [**protocol-group**](cmdqueryname=protocol-group+network-layer+queue+clock+default+dns+fragment) **network-layer** **queue** { **clock** | **default** | **dns** | **fragment** | **gre** | **hwtacas** | **icmp** | **icmpv6** | **ipv4-reserve** | **ipv6-option** | **nhrp** | **vrrp** | **radius-diameter** } **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of the system-message protocol group. | [**protocol-group**](cmdqueryname=protocol-group+system-message+queue+system-message+weight) **system-message** **queue** **system-message** **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of the blacklist protocol group. | [**protocol-group**](cmdqueryname=protocol-group+blacklist+queue+blacklist+weight) **blacklist** **queue** **blacklist** **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of the detection protocol group. | [**protocol-group**](cmdqueryname=protocol-group+check-failed+queue+check-failed+weight) **check-failed** **queue** **check-failed** **weight** *weight-value* |
   | Set a weight for packets in a protocol queue of the forwarded-packet protocol group. | [**protocol-group**](cmdqueryname=protocol-group+fwddata-to-cp+queue+forward-data+weight) **fwddata-to-cp** **queue** **forward-data** **weight** *weight-value* |
5. Set a weight for packets of a specified priority in a protocol queue.
   
   
   
   **Table 2** Setting weights for packets of specified priority values in protocol queues
   | Operation | Command |
   | --- | --- |
   | Set a weight for packets with a specified priority in a specified protocol queue of the whitelist protocol group. | [**protocol-group**](cmdqueryname=protocol-group+whitelist+queue+whitelist-bgp+whitelist-ldp) **whitelist** **queue** { **whitelist-bgp** | **whitelist-ldp** | **whitelist-management** | **whitelist-multicast** | **whitelist-reserve** } **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the user-defined-flow protocol group. | [**protocol-group**](cmdqueryname=protocol-group+user-defined-flow+queue+user-define-flow-1) **user-defined-flow** **queue** { **user-define-flow-1** | **user-define-flow-2** | **user-define-flow-3** | **user-define-flow-4** | **user-define-flow-5** | **user-define-flow-6** | **user-define-flow-7** | **user-define-flow-8** } **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the management protocol group. | [**protocol-group**](cmdqueryname=protocol-group+management+queue+dcn+ftp+ntp+snmp+ssh+sshv6) **management** **queue** { **dcn** | **ftp** | **ntp** | **snmp** | **ssh** | **sshv6** | **syslog** | **telnet** } **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the routing protocol group. | [**protocol-group**](cmdqueryname=protocol-group+route-protocol+queue+bgp+bgpv6+isis+ospf+ospfv3) **route-protocol** **queue** { **bgp** | **bgpv6** | **isis** | **ospf** | **ospfv3** | **rip** } **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the multicast protocol group. | [**protocol-group**](cmdqueryname=protocol-group+multicast+queue+igmp+multicast-reserve+msdp+pim) **multicast** **queue** { **igmp** | **multicast-reserve** | **msdp** | **pim** } **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the ARP protocol group. | [**protocol-group**](cmdqueryname=protocol-group+arp+queue+arp+nd+priority+be+af1+af2+af3+af4+ef) **arp** **queue** { **arp** | **nd** } **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the MPLS protocol group. | [**protocol-group**](cmdqueryname=protocol-group+mpls+queue+ldp+oam-ping+rsvp+vxlan+priority+be) **mpls** **queue** { **ldp** | **oam-ping** | **rsvp** | **vxlan** } **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the access-user protocol group. | [**protocol-group**](cmdqueryname=protocol-group+access-user+queue+bas-arp+bas-igmp+bas-nd) **access-user** **queue** { **bas-arp** | **bas-igmp** | **bas-nd** | **bas-trigger** | **dhcp** | **dhcpv6** | **eapol** | **l2tp** | **lldp** | **ppp** | **vbas-reserve** | **web** } **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the link-layer protocol group. | [**protocol-group**](cmdqueryname=protocol-group+link-layer+queue+3ah+bfd+link-detect+trunk+y1731) **link-layer** **queue** { **3ah** | **bfd** | **link-detect** | **trunk** | **y1731** | **interface-rdi** | **lag-check** | **lag-ping-trace** | **mac-vlan** } **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the network-layer protocol group. | [**protocol-group**](cmdqueryname=protocol-group+network-layer+queue+clock+default+dns+fragment) **network-layer** **queue** { **clock** | **default** | **dns** | **fragment** | **gre** | **hwtacas** | **icmp** | **icmpv6** | **ipv4-reserve** | **ipv6-option** | **nhrp** | **vrrp** | **radius-diameter** } **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the system-message protocol group. | [**protocol-group**](cmdqueryname=protocol-group+system-message+queue+system-message+priority+be) **system-message** **queue** **system-message** **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the blacklist protocol group. | [**protocol-group**](cmdqueryname=protocol-group+blacklist+queue+blacklist+priority+be+af1+af2+af3) **blacklist** **queue** **blacklist** **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the detection protocol group. | [**protocol-group**](cmdqueryname=protocol-group+check-failed+queue+check-failed+priority+be+af1) **check-failed** **queue** **check-failed** **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
   | Set a weight for packets with a specified priority in a specified protocol queue of the forwarded-packet protocol group. | [**protocol-group**](cmdqueryname=protocol-group+fwddata-to-cp+queue+forward-data+priority+be+af1) **fwddata-to-cp** **queue** **forward-data** **priority** { **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** } **weight** *weight-value* |
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.