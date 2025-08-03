Configuring GTM Extranet
========================

Configuring GTM Extranet

#### Usage Scenario

In a GTM application, a service provider in a VPN needs to provide multicast services for users on a public network. In this case, GTM extranet can be configured.


#### Pre-configuration Tasks

Before configuring GTM extranet, complete the following tasks:

* Configure a unicast routing protocol to ensure that IP routes between nodes are reachable.
* Configure BGP/MPLS IP VPN to ensure that the unicast VPN is running properly.
* Configure basic GTM functions to ensure that they are working properly.

#### Procedure

1. Import multicast source VPN routes and RP routes into the public network routing table. For configuration details, see [Configuring Route Import Between VPN and Public Network Instances](dc_vrp_mpls-l3vpn-v4_cfg_2024.html).
2. Configure a VPN RP to serve the multicast groups on the GTM extranet. For details about how to configure an RP, see **PIM Configuration** > **Configuring PIM-SM**. RPs are required only on a PIM-SM network.
3. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
4. Configure a multicast route selection policy.
   1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      The VPN instance view is displayed.
   2. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      
      
      The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
   3. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) **route-distinguisher**
      
      
      
      An RD is configured for the VPN instance IPv4 address family.
   4. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
      
      
      
      Multicast routing is enabled for the VPN instance IPv4 address family.
   5. Run [**mvpn**](cmdqueryname=mvpn)
      
      
      
      The VPN instance IPv4 address family MVPN view is displayed.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the VPN instance view.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   8. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
      
      
      
      Multicast routing is enabled.
   9. Run [**multicast mvpn ipv6-underlay**](cmdqueryname=multicast+mvpn+ipv6-underlay) *mvpnid*
      
      
      
      An MVPN IPv6 ID is configured.
   10. Run [**multicast vpn-public**](cmdqueryname=multicast+vpn-public)
       
       
       
       The public network IPv4 address family MVPN view is displayed.
   11. Run [**multicast extranet select-rpf**](cmdqueryname=multicast+extranet+select-rpf) **vpn-instance** *vpn-instance-name* **group** *group-address* { *group-mask* | *group-mask-length* }
       
       
       
       A multicast route selection policy is configured, in which another VPN instance is specified for the upstream interface of the RPF route selected for the PIM entry containing a specified multicast group address.
   12. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
5. (Optional) Run [**multicast extranet traffic-forward type**](cmdqueryname=multicast+extranet+traffic-forward+type) { **vlanif** | **qinq** | **vbdif** | ****bas**** ****igmp**** }
   
   
   
   The extranet is enabled to forward multicast traffic through a VLANIF outbound interface, QinQ/dot1q VLAN tag termination outbound interface, BAS interface, or VBDIF interface.
   
   
   
   Configure the extranet to forward multicast traffic through a VLANIF outbound interface, QinQ/dot1q VLAN tag termination sub-interface, VBDIF interface, or BAS interface if the outbound interface used by NG MVPN extranet is any of the preceding interfaces.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **extranet** { **source-vpn-instance** { **all** | **public** | *vpn-instance-name* } | **receive-vpn-instance** { **all** | *vpn-instance-name* } } | **incoming-interface** { *interface-type* *interface-number* | **register** | **mcast-extranet** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* | **register** | **none** } | **mode** { **ssm** | **sm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] command to check information about the PIM routing table.
* Run the [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask* | *group-mask-length* } ] | *source-address* [ **mask** { *source-mask* | *source-mask-length* } ] | **extranet** { **source-vpn-instance** { **all** | **public** | *vpn-instance-name* } | **receive-vpn-instance** { **all** | *vpn-instance-name* } } | **incoming-interface** { *interface-type* *interface-number* | **register** | **mcast-extranet** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* | **register** | **none** } ] \* [ **outgoing-interface-number** [ *number* ] ] command to check information about the multicast routing table.
* Run the [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **rpf-info** *source-address* [ *group-address* ] [ **rpt** | **spt** ] command to check information about source-specific or group-and-source-specific RPF routes.