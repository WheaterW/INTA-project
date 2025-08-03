(Optional) Configuring the Mode in Which a BGP Label Inherits the QoS Priority in an Outer Tunnel Label
=======================================================================================================

When data packets are transmitted from a core ASBR to an AGG ASBR, you can determine whether a BGP label inherits the QoS priority carried in an outer tunnel label.

#### Context

In the inter-AS seamless MPLS or inter-AS seamless MPLS+HVPN networking, each packet arriving at a core ASBR or AGG ASBR carries an inner private label, a BGP LSP label, and an outer MPLS tunnel label. The core ASBR and AGG ASBR remove outer MPLS tunnel labels from packets before sending the packets to each other. If a BGP LSP label in a packet carries a QoS priority different from that in the outer MPLS tunnel label in the packet, you can configure the core ASBR or AGG ASBR to determine whether the BGP LSP label inherits the QoS priority carried in the outer MPLS tunnel label to be removed.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The BGP-IPv4 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+exp-mode+pipe+uniform) { *group-name* | *ipv4-address* } **exp-mode** { **pipe** | **uniform** }
   
   
   
   The mode in which a BGP label inherits the QoS priority in the outer tunnel label is specified.
   
   You can configure either of the following parameters:
   * **uniform**: The BGP label inherits the QoS priority carried in the outer MPLS tunnel label.
   * **pipe**: The QoS priority carried in the BGP label does not change, and the BGP label does not inherit the QoS priority carried in the outer MPLS tunnel label.
   The default QoS priority inheriting mode varies according to the outer MPLS tunnel type:
   * LDP: By default, the BGP label inherits the QoS priority carried in the outer MPLS tunnel label.
   * TE: By default, the BGP label does not inherit the QoS priority carried in the outer MPLS tunnel label.