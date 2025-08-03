Configuring NG MVPN Extranet
============================

To enable a service provider on a VPN to provide multicast services for users on other VPNs, configure NG MVPN extranet.

#### Usage Scenario

In real-world NG MVPN application, a service provider may need to provide multicast services to users in a different VPN than its own VPN. This requires inter-VPN multicast distribution. To enable a service provider on a VPN to provide multicast services for users on other VPNs, configure NG MVPN extranet.

NG MVPN extranet can be used in local or remote cross scenarios.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The address range of multicast groups using the NG MVPN extranet service cannot overlap that of multicast groups using the intra-VPN service.
* Extranet entries of the source and receiver VPNs support only a static RP, and the static RP address must be configured on the source VPN side. The RP on the receiver VPN side must be the same as the RP configured on the source VPN. Otherwise, the same multicast routing entries cannot be created on the receiver VPN and source VPN.
* To provide an SSM service using NG MVPN extranet, the same SSM group address must be configured on the source and receiver VPN sides.
* The MVPN target extended community attribute configured in the VPN instance IPv4 address family MVPN view cannot be the same as the VPN target extended community attribute configured in the VPN instance IPv4 address family view.
* If receivers are on the public network and unicast routes are locally leaked routes, the [**multicast extranet receive-vpn-instance public enable**](cmdqueryname=multicast+extranet+receive-vpn-instance+public+enable) command needs to be run.


#### Pre-configuration Tasks

Before configuring NG MVPN extranet, complete the following tasks:

* Configure a unicast routing protocol to ensure that IP routes between nodes are reachable.
* Configure BGP/MPLS IP VPN to ensure that the unicast VPN is running properly.
* Configure basic NG MVPN functions and ensure that they are working properly.

#### Procedure

1. Configure the same unicast routing policy on the receiver and source PEs so that the receiver VPN can import the routes to the source VPN. For detailed configurations, see [Configuring a VPN Instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html).
2. Configure a private network RP to serve the NG MVPN extranet. For details about how to configure an RP, see PIM Configuration > Configuring PIM-SM. An RP is required only on a PIM-SM network.
3. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
4. Configure a multicast routing policy.
   1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      The VPN instance view is displayed.
   2. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      
      
      The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
   3. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
      
      
      
      Multicast routing is enabled for the VPN instance IPv4 address family.
   4. Run [**mvpn**](cmdqueryname=mvpn)
      
      
      
      The VPN instance IPv4 address family MVPN view is displayed.
   5. Run [**multicast extranet select-rpf**](cmdqueryname=multicast+extranet+select-rpf) { **vpn-instance** *vpn-instance-name* | **public** } **group** *group-address* { *group-mask* | *group-mask-length* }
      
      
      
      A multicast routing policy is configured, and the upstream interface of the RPF route selected by the PIM entry corresponding to a multicast group address is specified as belonging to another VPN instance or the public network instance.
   6. Run **[**quit**](cmdqueryname=quit)**
      
      
      
      Return to the VPN instance IPv4 address family view.
   7. Run **[**quit**](cmdqueryname=quit)**
      
      
      
      Return to the VPN instance view.
   8. Run **[**quit**](cmdqueryname=quit)**
      
      
      
      Return to the system view.
5. (Optional) Run [**multicast extranet traffic-forward type**](cmdqueryname=multicast+extranet+traffic-forward+type) { **vlanif** | **qinq** | **vbdif** | ****bas**** ****igmp**** }
   
   
   
   The extranet is enabled to forward multicast traffic through a VLANIF outbound interface, QinQ/dot1q VLAN tag termination outbound interface, BAS interface, or VBDIF interface.
   
   
   
   Configure the extranet to forward multicast traffic through a VLANIF outbound interface, QinQ/dot1q VLAN tag termination interface, VBDIF interface, or BAS interface if the outbound interface used by NG MVPN extranet is any of the preceding interfaces.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **extranet** { **source-vpn-instance** { **all** | **public** | *vpn-instance-name* } | **receive-vpn-instance** { **all** | *vpn-instance-name* } } | **incoming-interface** { *interface-type* *interface-number* | **register** | **mcast-extranet** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* | **register** | **none** } | **mode** { **ssm** | **sm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] command to check information about the PIM routing table.
* Run the [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask* | *group-mask-length* } ] | *source-address* [ **mask** { *source-mask* | *source-mask-length* } ] | **extranet** { **source-vpn-instance** { **all** | **public** | *vpn-instance-name* } | **receive-vpn-instance** { **all** | *vpn-instance-name* } } | **incoming-interface** { *interface-type* *interface-number* | **register** | **mcast-extranet** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* | **register** | **none** } ] \* [ **outgoing-interface-number** [ *number* ] ] command to check information about the multicast routing table.
* Run the [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **rpf-info** *source-address* [ *group-address* ] [ **rpt** | **spt** ] command to check information about source-specific or group-and-source-specific RPF routes.