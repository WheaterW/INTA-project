Configuring MVPN Extranet
=========================

To enable a service provider on a VPN to provide multicast services for users on other VPNs, configure MVPN extranet.

#### Usage Scenario

In real-world application, a service provider may need to provide multicast services to users in a different VPN than its own VPN. This requires inter-VPN multicast distribution. To enable a service provider on a VPN to provide multicast services for users on other VPNs, configure MVPN extranet.

MVPN extranet applies to two scenarios: remote route leaking and local route leaking scenarios. For details, see [Table 1](#EN-US_TASK_0000001270432597__table_dc_vrp_multicast_cfg_225901).

**Table 1** Usage scenarios of MVPN extranet
| Usage Scenario | Description | Configuration | Remarks |
| --- | --- | --- | --- |
| remote route leaking | The source and receiver VPN instances reside on different PEs. | Configure a source VPN instance on a receiver PE | - |
| Local leaking | The source and receiver VPN instances reside on the same PE, or the multicast source belongs to the public network instance. | - | In MVPN extranet scenarios where the multicast source resides on a public network and the receiver resides on a VPN, static routes to the multicast source and public network RP must be configured in the receiver VPN instance. |


![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The address range of multicast groups using the MVPN extranet service cannot overlap that of multicast groups using the intra-VPN service.
* Only a static RP can be used in an MVPN extranet scenario, the same static RP address must be configured on the source and receiver VPN sides, and the static RP address must belong to the source VPN. If different RP addresses are configured, inconsistent multicast routing entries will be created on the two instances, causing service forwarding failures.
* To provide an SSM service using MVPN extranet, the same SSM group address must be configured on the source and receiver VPN sides.


#### Pre-configuration Tasks

Before configuring MVPN extranet, complete the following tasks:

* Configure a unicast routing protocol to ensure that devices are reachable through IP routes.
* Configure a BGP/MPLS IP VPN and ensure that the unicast VPN is working properly.
* Configure basic MVPN functions and ensure that they are working properly.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) Select the following required configuration steps to configure MVPN extranet based on usage scenarios:

* Remote leaking scenario where a source VPN instance is configured on a receiver PE: Perform steps 1, 2, and 4.
* Local leaking scenario where the source and receiver VPN instances reside on the same PE: select steps 1 and 2.
* Local leaking scenario where the multicast source belongs to the public network instance: select steps 1, 2, and 5.



#### Procedure

1. Configure the same unicast routing policy on the receiver and source PEs so that the receiver VPN can import the routes to the source VPN. For detailed configurations, see [Configuring a VPN Instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html).
2. Configure a private network RP to serve the MVPN extranet. For details about how to configure an RP, see PIM Configuration > Configuring PIM-SM. An RP is required only on a PIM-SM network.
3. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
4. Configure a multicast route selection policy.
   1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      The VPN instance view is displayed.
   2. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      
      
      The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
   3. Run [**multicast extranet select-rpf**](cmdqueryname=multicast+extranet+select-rpf) { **vpn-instance** *vpn-instance-name* | **public** } **group** *group-address* { *group-mask* | *group-mask-length* }
      
      
      
      A multicast route selection policy is configured, specifying that the upstream interface of the RPF route selected by the PIM entry corresponding to a multicast group address belongs to another VPN instance or the public network instance.
   4. Run **[**quit**](cmdqueryname=quit)**
      
      
      
      Return to the VPN instance view.
   5. Run **[**quit**](cmdqueryname=quit)**
      
      
      
      Return to the system view.
5. Configure a static route to the source in the public network and public network RP. For detailed configurations, see [Configuring IPv4 Static Routes](dc_vrp_static-route_disjoin_cfg_0003.html).
6. **Optional:** (Optional) Run [**multicast extranet traffic-forward type**](cmdqueryname=multicast+extranet+traffic-forward+type) { **vlanif** | **qinq** | **vbdif** | ****bas**** ****igmp**** }
   
   
   
   A VLANIF interface, QinQ/dot1q interface, BAS interface, or VBDIF interface is selected as the outbound interface for extranet in the local leaking scenario.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The VLANIF interface, QinQ/dot1q VLAN tag termination interface, BAS interface, or VBDIF interface can be used as the outbound interface only for extranet in the local leaking scenario.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **extranet** { **source-vpn-instance** { **all** | **public** | *vpn-instance-name* } | **receive-vpn-instance** { **all** | *vpn-instance-name* } } | **incoming-interface** { *interface-type* *interface-number* | **register** | **mcast-extranet** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* | **register** | **none** } | **mode** { **ssm** | **sm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] command to check information about the PIM routing table.
* Run the [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask* | *group-mask-length* } ] | *source-address* [ **mask** { *source-mask* | *source-mask-length* } ] | **extranet** { **source-vpn-instance** { **all** | **public** | *vpn-instance-name* } | **receive-vpn-instance** { **all** | *vpn-instance-name* } } | **incoming-interface** { *interface-type* *interface-number* | **register** | **mcast-extranet** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* | **register** | **none** } ] \* [ **outgoing-interface-number** [ *number* ] ] command to check information about the multicast routing table.
* Run the [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **rpf-info** *source-address* [ *group-address* ] [ **rpt** | **spt** ] command to check information about source-specific or group-and-source-specific RPF routes.