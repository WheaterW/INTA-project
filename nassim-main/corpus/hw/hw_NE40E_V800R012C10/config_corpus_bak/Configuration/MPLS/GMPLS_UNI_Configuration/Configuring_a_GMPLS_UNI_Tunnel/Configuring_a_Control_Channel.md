Configuring a Control Channel
=============================

A control channel is configured on the ingress EN and egress EN of a GMPLS UNI tunnel to carry GMPLS UNI signaling packets and ensure the normal exchange of GMPLS UNI signaling packets.

#### Context

A GMPLS UNI control channel carries control packets such as RSVP-TE signaling packets. GMPLS, as an enhancement to MPLS, separates control and data channels physically and uses LMP to manage and maintain control and data channels. A fault in the control channel does not affect the data channel, which implements uninterrupted service forwarding and improves the reliability of the entire network.

The data and control channels are separated in either out-of-band or in-band mode. [Table 1](#EN-US_TASK_0172368709__tab_dc_vrp_gmpls-uni_cfg_000501) describes the comparison between the two modes.

**Table 1** Comparison between in-band and out-of-band modes
| Item | In-band Control Channel | Out-of-Band Control Channel |
| --- | --- | --- |
| Implementation requirements | Available internal communication overheads are required. | 10 Mbit/s and 100 Mbit/s out-of-band Ethernet interfaces are required. An independent control channel network must be set up based on these interfaces. |
| Implementation mode | Its implementation uses communication overheads of the data channel and depends on the EFM OAM function. | Static routes are configured to ensure the communication on the out-of-band control channel network. |
| Maintainability | Good maintainability: by sharing the same physical links with the service plane. | Common maintainability: It uses an independent network to carry the control plane data and needs special maintenance. The maintainability of the control channel is determined by the control channel network. |
| Independence | Poor independence: It is not completely separated from the service plane by sharing the same physical links with the service plane. If the physical link goes Down, data transmission on both the control and service planes are affected. | Good independence: It is completely separated from the service plane by using different physical links from the service plane. A physical link fault on the control plane does not affect services on the service plane. |


The two separation modes have advantages of their own. Select one mode as needed.

#### Procedure

* In-band mode
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In-band control channel configurations depend on the EFM OAM function. Enable EFM OAM globally before performing the following steps.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**efm enable**](cmdqueryname=efm+enable)
     
     
     
     EFM OAM is enabled globally.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of an interface is displayed.
  4. Run [**efm enable**](cmdqueryname=efm+enable)
     
     
     
     EFM OAM is enabled on the interface.
  5. (Optional) Run [**efm packet max-size**](cmdqueryname=efm+packet+max-size) *size*
     
     
     
     The maximum size of an EFM OAMPDU is configured on the interface.
  6. Run [**lmp interface enable**](cmdqueryname=lmp+interface+enable)
     
     
     
     An LMP interface is created. This interface functions as both data channel interface and control channel interface.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After the configuration is committed, the system automatically generates a virtual LMP interface. Therefore, the in-band control channel interface is also called LMP interface. The LMP interface number is the same as the corresponding physical interface number, and the LMP interface automatically borrows the address of the data channel interface. For example, after the [**lmp interface enable**](cmdqueryname=lmp+interface+enable) command is run on GE 0/3/0, LMP 0/3/0 is automatically generated and automatically borrows the IP address of GE 0/3/0.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Out-of-band mode
  
  
  
  In out-of-band mode, static routes are configured to ensure communication on the out-of-band control channel network, and ensure routes between the ingress EN and ingress CN and between the egress CN and egress EN are reachable.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the out-of-band control channel interface is displayed.
  3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     An IP address is configured for the interface.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] }
     
     
     
     A static route that destines for an edge device on the transport network is configured (the destination address of the route is the Node ID of the edge device), and the IP address of the peer interface of the control channel is specified as the next-hop address.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.