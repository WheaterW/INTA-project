Configuring Interface-based CAR
===============================

When an access device is under attack, you can configure interface-based CAR to restrict the rate at which all or specific packets are sent to the CPU to protect the CPU against attacks.

#### Usage Scenario

When an access device is under attack, to protect the CPU against attacks, configure interface-based CAR to restrict the rate at which all or specific protocol packets are sent to the CPU.


#### Prerequisites

None


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**cp-rate-limit**](cmdqueryname=cp-rate-limit+enhance+port+dhcp+dhcpv6+icmp+icmpv6+cir+cbs) **enhance** { **port** | { **dhcp** | **dhcpv6** | **icmp** | **icmpv6** } } **cir** *cir-value* [ **cbs** *cbs-value* ]
   
   
   
   The rate at which all or specific protocol packets are sent to the CPU is restricted.

#### Checking the Configurations

After configuring interface-based CAR, check the configurations.

Run the [**display cp-rate-limit**](cmdqueryname=display+cp-rate-limit+enhance+port+dhcp+dhcpv6+icmp+icmpv6+slot) [ **enhance** ] { **port** | **dhcp** | **dhcpv6** | **icmp** | **icmpv6** } [ **slot** *slot-id* ] [ **verbose** ] command to check statistics about interface-based CAR on the board.