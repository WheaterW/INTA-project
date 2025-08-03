Configuring Tunnel Interfaces
=============================

Before creating a DS-TE tunnel, create a tunnel interface and configure tunnel attributes in the view of the tunnel interface.

#### Context

Perform the following steps on the ingress of a TE tunnel to be established:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   A tunnel interface is created, and the tunnel interface view is displayed.
3. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   The tunnel description is configured.
4. Run either of the following commands to assign an IP address to the tunnel interface:
   
   
   * To assign an IP address to the tunnel interface, run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] command.
     
     The secondary IP address of the tunnel interface can be configured only after the primary IP address is configured.
   * To configure the tunnel interface to borrow the IP address of another interface, run [**ip address unnumbered**](cmdqueryname=ip+address+unnumbered) **interface** *interface-type* *interface-number*
   
   To forward traffic, the tunnel interface must have an IP address. An MPLS TE tunnel, however, is unidirectional, and o peer address exists. Therefore, it is unnecessary to assign an IP address to a tunnel interface. A tunnel interface usually borrows the loopback address, which functions as the LSR ID of the local node.
5. Run [**tunnel-protocol mpls te**](cmdqueryname=tunnel-protocol+mpls+te)
   
   
   
   MPLS TE is configured as the tunneling protocol.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Changing, deleting, or initially configuring the tunnel mode of a tunnel interface will delete all tunnel-related configurations on the interface, such as the MTU. Exercise caution when performing this operation.
6. Run [**destination**](cmdqueryname=destination) *ip-address*
   
   
   
   The destination address of the tunnel is configured as the LSR ID of the egress.
7. Run [**mpls te tunnel-id**](cmdqueryname=mpls+te+tunnel-id) *tunnel-id*
   
   
   
   A tunnel ID is set.
8. Run [**mpls te signal-protocol**](cmdqueryname=mpls+te+signal-protocol) { **cr-static** | **rsvp-te** }
   
   
   
   A signaling protocol is configured for a tunnel.
9. (Optional) Run [**mpls te priority**](cmdqueryname=mpls+te+priority) *setup-priority* [ *hold-priority* ]
   
   
   
   The tunnel priorities are set.
   
   A smaller value indicates a higher priority.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The holding priority must be higher than or equal to the setup priority. If no holding priority is set, its value is the same as that setup priority. If the combination of the bandwidth and priorities is not listed in the TE class mapping table, LSPs cannot be established.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
    
    
    
    Each time you change an MPLS TE parameter, run the [**commit**](cmdqueryname=commit) command to commit the configuration.