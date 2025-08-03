Configuring a DiffServ Mode for VPN
===================================

This section describes how to configure the DiffServ mode for VPNs so that VPN packets can be scheduled to different queues based on their service classes.

#### Usage Scenario

1. This feature can be used on the ingress PE, egress PE, or both of them.
   * If behavior aggregate (BA) classification and the Pipe mode are both configured on the user-side interface of the ingress PE, the Pipe/Short Pipe mode preferentially takes effect.
   * If the DiffServ mode is set to Pipe on the PE, BA classification is not required.
   * If the DiffServ mode is set to Uniform on the PE, the BA classification also needs to be configured.
2. The DiffServ mode takes effect only on the L3VPN that meets the following conditions:
   * When the DiffServ mode is set to Pipe/Short Pipe on the egress PE and BA classification is configured on the outbound interface in the downstream direction, you must run the [**qos phb disable**](cmdqueryname=qos+phb+disable) command on the outbound interface of the egress PE.
   * When the DiffServ mode is set to Uniform on the egress PE and BA classification is configured on the outbound interface in the downstream direction, you do not need to run the [**qos phb disable**](cmdqueryname=qos+phb+disable) command on the outbound interface of the egress PE.
3. To allow the P node to schedule packets according to their service classes, you are also advised to configure BA classification on the P node in the following situations:
   * The performance of the P node is limited, and congestion may occur.
   * LDP over TE is implemented on the P node. The TE tunnel interface resides on the P node, and the tunnel is configured with a priority.

#### Pre-configuration Tasks

Before configuring the Pipe/Short Pipe mode for VPNs, complete the following tasks:

* Configure an MPLS TE tunnel between PEs. For details, see "MPLS TE Configuration" in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - MPLS*.
* Configure L2VPN or L3VPN services as required. For details, see HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - VPN.
* Configure BA or MF classification on the user-side interface of the ingress PE. For details, see "Class-based QoS Configuration" in HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - QoS.


#### Procedure

* Configure an L3VPN DiffServ mode.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. (Optional) Run [**l3vpn diffserv-mode short-pipe enhance enable**](cmdqueryname=l3vpn+diffserv-mode+short-pipe+enhance+enable)
     
     The enhanced Short Pipe mode in L3VPN scenarios is configured.
     
     The [**l3vpn diffserv-mode short-pipe enhance enable**](cmdqueryname=l3vpn+diffserv-mode+short-pipe+enhance+enable) command takes effect only when the DiffServ mode is set to Short Pipe.
  3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     The VPN instance view is displayed.
  4. Run [**diffserv-mode**](cmdqueryname=diffserv-mode) { **pipe** *service-class* [ *color* ] | **short-pipe** *service-class* [ *color* ] [ **domain** *ds-name* ] | **uniform** } or [**diffserv-mode**](cmdqueryname=diffserv-mode) **ingress** { **uniform** | **pipe** *service-class* *color* | **short-pipe** *service-class* *color* } **egress** { **uniform** | **pipe** | **short-pipe** [ **domain** *ds-name* ] }
     
     A DiffServ mode is configured for the VPN instance.
     
     The [**diffserv-mode**](cmdqueryname=diffserv-mode) command applies to both unicast and NG MVPN scenarios.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure a VLL DiffServ mode.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*The user-side interface view is displayed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This interface is the user-side interface to which an L2VPN is bound.
  3. Run [**diffserv-mode**](cmdqueryname=diffserv-mode) { **pipe** *service-class* *color* | **short-pipe** *service-class* *color* [ **domain** *ds-name* ] | **uniform** } or [**diffserv-mode**](cmdqueryname=diffserv-mode) **ingress** { **uniform** | **pipe** *service-class* *color* | **short-pipe** *service-class* *color* } **egress** { **uniform** | **pipe** | **short-pipe** [ **trust** { **inner-vlan-8021p** | **ip-dscp** } ] [ **domain** *ds-name* ] }
     
     A VLL DiffServ mode is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure a VPLS DiffServ mode.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
     
     The VSI view is displayed.
  3. Run [**diffserv-mode**](cmdqueryname=diffserv-mode) { **pipe** *service-class* *color* | **short-pipe** *service-class* *color* [ **domain** *ds-name* ] | **uniform** } or [**diffserv-mode**](cmdqueryname=diffserv-mode) **ingress** { **uniform** | **pipe** *service-class* *color* | **short-pipe** *service-class* *color* } **egress** { **uniform** | **pipe** | **short-pipe** [ **trust** { **inner-vlan-8021p** | **ip-dscp** } ] [ **domain** *ds-name* ] }
     
     A VPLS DiffServ mode is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure an EVPN DiffServ mode.
  
  
  + Configure a DiffServ mode in the EVPN instance view and BD-EVPN instance view.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Configure an EVPN instance. For details, see [Configuring an EVPN Instance](../vrp/dc_vrp_evpn_cfg_0004.html).
    3. Run [**diffserv-mode**](cmdqueryname=diffserv-mode) { **pipe** *service-class* *color* | **short-pipe** *service-class* *color* [ **domain** *ds-name* ] | **uniform** } or [**diffserv-mode**](cmdqueryname=diffserv-mode) **ingress** { **uniform** | **pipe** *service-class* *color* | **short-pipe** *service-class* *color* } **egress** { **uniform** | **pipe** | **short-pipe** [ **trust** { **inner-vlan-8021p** | **ip-dscp** } ] [ **domain** *ds-name* ] }
       
       An EVPN DiffServ mode is configured.
    4. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Configure a DiffServ mode in the EVPL instance view.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Configure an EVPL instance. For details, see [Configuring an EVPL Instance](../vrp/dc_vrp_evpn_cfg_0021.html).
    3. Run [**diffserv-mode**](cmdqueryname=diffserv-mode) { **pipe** *service-class* *color* | **short-pipe** *service-class* *color* [ **domain** *ds-name* ] | **uniform** } or [**diffserv-mode**](cmdqueryname=diffserv-mode) **ingress** { **uniform** | **pipe** *service-class* *color* | **short-pipe** *service-class* *color* } **egress** { **uniform** | **pipe** | **short-pipe** [ **trust** { **inner-vlan-8021p** | **ip-dscp** } ] [ **domain** *ds-name* ] }
       
       An EVPN DiffServ mode is configured.
    4. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.