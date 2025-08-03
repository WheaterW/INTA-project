Configuring VLAN CAR
====================

When an access device is under attack, you can configure VLAN CAR to restrict the rate at which specific packets are sent to the CPU to protect the CPU against attacks.

#### Usage Scenario

When an access device is under attack, you can configure port+VLAN-based CAR to restrict the rate at which packets are sent to the CPU to protect the CPU against attacks.


#### Prerequisites

None


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
3. Perform one of the following operations as required:
   
   
   * On an Ethernet interface, Ethernet sub-interface, GE interface, GE sub-interface, Eth-Trunk interface, or Eth-Trunk sub-interface, POS interface, IP-Trunk interface, and EVC sub-interface on which packets are encapsulated in untag or default mode, run the [**cp-rate-limit**](cmdqueryname=cp-rate-limit+port+dhcp+dhcpv6+icmp+icmpv6+ldp-hello+rsvp+ospf) { **port** | { **dhcp** | **dhcpv6** | **icmp** | **icmpv6** | **ldp-hello** | **rsvp** | **ospf** | **rip** | **pim** | **isis** | **vrrp** | **ospfv3** | **ripng** | **pimv6** | **vrrpv6** }\* } **cir** *cir-value* [ **cbs** *cbs-value* ] [ **prior** ] command to set the rate at which ICMP/DHCP/DHCPv6/ICMPv6/LDP-HELLO/RSVP/OSPF/RIP/PIM/ISIS/VRRP/OSPFv3/RIPNG/PIMv6/VRRPv6 packets are sent to the CPU.
   * On a sub-interface for dot1q VLAN tag termination, and EVC sub-interface on which packets are encapsulated in dot1q, untag or default mode, run the [**cp-rate-limit**](cmdqueryname=cp-rate-limit+port+dhcp+dhcpv6+icmp+icmpv6+ldp-hello+rsvp+ospf) { **port** | { **dhcp** | **dhcpv6** | **icmp** | **icmpv6** | **ldp-hello** | **rsvp** | **ospf** | **rip** | **pim** | **isis** | **vrrp** | **ospfv3** | **ripng** | **pimv6** | **vrrpv6** } } **vlan** *vlan-id-begin* [**to** *vlan-id-end* ] **cir** *cir-value* [ **cbs** *cbs-value* [ **prior** ] ] command to set the rate at which ICMP/DHCP/DHCPv6/ICMPv6/LDP-HELLO/RSVP/OSPF/RIP/PIM/ISIS/VRRP/OSPFv3/RIPNG/PIMv6/VRRPv6 packets are sent to the CPU.
   * On a sub-interface for QinQ VLAN tag termination, and EVC sub-interface on which packets are encapsulated in QinQ, untag or default mode, run the [**cp-rate-limit**](cmdqueryname=cp-rate-limit+port+dhcp+dhcpv6+icmp+icmpv6+ldp-hello+rsvp+ospf) { **port** | { **dhcp** | **dhcpv6** | **icmp** | **icmpv6** | **ldp-hello** | **rsvp** | **ospf** | **rip** | **pim** | **isis** | **vrrp** | **ospfv3** | **ripng** | **pimv6** | **vrrpv6** } } **pe-vid** *pe-vid* **ce-vid** *ce-vid-begin* [ **to** *ce-vid-end* ] **cir** *cir-value* [ **cbs** *cbs-value* ] [ **prior** ] command to set the rate at which ICMP/DHCP/DHCPv6/ICMPv6/LDP-HELLO/RSVP/OSPF/RIP/PIM/ISIS/VRRP/OSPFv3/RIPNG/PIMv6/VRRPv6 packets are sent to the CPU.

#### Checking the Configurations

After configuring VLAN CAR, check the configurations.

Run the [**display cp-rate-limit**](cmdqueryname=display+cp-rate-limit) command to check statistics about all protocol packets or specific protocol packets that attack an interface.