Configuring an IGMP over GRE Tunnel
===================================

The information system contains different services involving multicast packets. These services are isolated through GRE tunnels. Devices' GRE interfaces are required to have IGMP capabilities.

#### Usage Scenario

If the information system contains two types of services involving multicast packets, for example, both the closed-circuit monitoring system and passenger information system in the urban rail signal system involve multicast packets, these services need to be isolated through GRE tunnels and the information system needs to access devices through GRE tunnels. To meet these needs, devices' GRE interfaces must have multicast capabilities. Currently, GRE interfaces support PIM. GRE interfaces must also have IGMP capabilities.


#### Pre-configuration Tasks

Before configuring IGMP over GRE, complete the following tasks:

* Configure a unicast routing protocol to ensure that devices are reachable.
* [Configure a tunnel interface.](dc_vrp_gre_cfg_2004.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   The tunnel interface view is displayed.
3. Run [**tunnel-protocol**](cmdqueryname=tunnel-protocol) **gre**
   
   
   
   The tunnel encapsulation type is set to GRE.
4. Run [**source**](cmdqueryname=source) *ip-address*
   
   
   
   The source IP address or source interface of the tunnel interface is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Run the [**binding tunnel gre**](cmdqueryname=binding+tunnel+gre) command to bind GRE to the source interface or the interface where the source address resides. After the binding, a GRE tunnel can use the interface to forward packets encapsulated by GRE.
5. Run [**destination**](cmdqueryname=destination) [ **vpn-instance** *vpn-instance-name* ] *ip-address*
   
   
   
   A destination IP address is set for the tunnel interface.
   
   
   
   After a tunnel interface is created, specify the source address or source interface and destination address of the tunnel.
6. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Running the [**undo pim sm**](cmdqueryname=undo+pim+sm) command deletes PIM neighbor relationships on the interface and interrupt the multicast service running on the interface.
7. Run [**igmp enable**](cmdqueryname=igmp+enable)
   
   
   
   IGMP is enabled.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display igmp interface verbose**](cmdqueryname=display+igmp+interface+verbose) command.

The command output shows detailed IGMP information on the GRE tunnel interface.