Configuring the Support for Segmented Tunnels in an AS
======================================================

To ensure successful transmission of multicast traffic among intra-AS areas that use different types of MPLS protocols for tunnel establishment, configure the support for segmented tunnels in the AS.

#### Context

If areas in an AS use different types of MPLS protocols for tunnel establishment, configure the NG MVPN's ingress node and the nodes that connect different types of tunnels (tunnel connection nodes) to support segmented tunnels.


#### Procedure

* Configure the ingress node.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     A VPN instance is created, and its view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
  4. Run [**mvpn**](cmdqueryname=mvpn)
     
     
     
     The VPN instance IPv4 address family MVPN view is displayed.
  5. Run [**inter-area-segmented enable**](cmdqueryname=inter-area-segmented+enable)
     
     
     
     The ingress node is configured to support inter-area segmented tunnels in the AS.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the tunnel connection node.
* Run [**system-view**](cmdqueryname=system-view)
  
  
  
  The system view is displayed.
* Run [**multicast mvpn inter-area-segmented enable**](cmdqueryname=multicast+mvpn+inter-area-segmented+enable)
  
  
  
  The tunnel connection node is configured to support inter-area segmented tunnels in the AS.
* Run [**commit**](cmdqueryname=commit)
  
  
  
  The configuration is committed.