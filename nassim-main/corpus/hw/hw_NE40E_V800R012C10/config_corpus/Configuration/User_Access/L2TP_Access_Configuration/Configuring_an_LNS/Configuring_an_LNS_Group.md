Configuring an LNS Group
========================

This section describes how to configure tunnel parameters on the LNS side, such as the source interface for tunnel setup, tunnel board, maximum number of L2TP tunnels, and priority re-marking after CAR.

#### Context

An interface IP address must be configured for each LNS group as the source address for communicating with a LAC. Based on the configured IP address, the NE40E can correctly determine the LNS group that processes the tunnel connection request from a LAC. In addition to the IP address, you can also configure other parameters, such as the tunnel board and the maximum number of L2TP tunnels that can be configured, so that the LNS and LAC can communicate.

Perform the following steps on the NE40E.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**lns-group**](cmdqueryname=lns-group) *group-name*
   
   
   
   An LNS group is created, and its view is displayed.
3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
   
   
   
   A description is configured for the LNS group.
4. Run [**bind slot**](cmdqueryname=bind+slot) *slot\_id*
   
   
   
   A tunnel board is bound to the LNS group.
   
   
   
   Multiple tunnel boards can be configured on the NE40E. You can specify the tunnel board for an LNS group. Multiple tunnel boards can be specified for an LNS group. Load balancing is implemented among these tunnel boards based on tunnels.
5. Run [**bind source**](cmdqueryname=bind+source) { *interface-type* *interface-num* | *i*nterface-name** }
   
   
   
   An interface is bound to the LNS group.
   
   
   
   The IP address of the source interface bound to the LNS group, that of the source interface bound to the LAC-side L2TP group, and the source IP address of the RBS tunnel in dual-device hot backup scenarios cannot be the same.
6. (Optional) Run either of the following commands to enable tunnel load balancing:
   
   
   * To enable tunnel load balancing based on the number of tunnels on tunnel boards bound to an LNS group, run the [**tunnel load-balance by-tunnel**](cmdqueryname=tunnel+load-balance+by-tunnel) command.
   * To enable tunnel load balancing based on the number of sessions on tunnel boards bound to the LNS group, run the [**tunnel load-balance by-session**](cmdqueryname=tunnel+load-balance+by-session) command.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
9. (Optional) Run [**l2tp tunnel-limit**](cmdqueryname=l2tp+tunnel-limit) *tunnel-number*
   
   
   
   The maximum number of L2TP tunnels that can be set up is configured.
   
   
   
   To prevent too many L2TP tunnels from affecting LNS performance, you can configure the maximum number of L2TP tunnels that can be set up.
10. (Optional) Run [**l2tp slot**](cmdqueryname=l2tp+slot) *slot-id* **block** **enable**
    
    
    
    A tunnel board is locked.
    
    
    
    If the number of L2TP tunnels established on a tunnel board reaches the upper limit, you can lock the tunnel board to prevent the device performance from being affected by the setup of L2TP tunnels on the tunnel board.
11. (Optional) Run [**l2tp lns fast-reply enable slot**](cmdqueryname=l2tp+lns+fast-reply+enable+slot) *slot-id*
    
    
    
    The tunnel board of an LNS is enabled to send packets to the network-side outbound interface board connected to a LAC based on hardware.
12. (Optional) Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
    
    
    
    An L2TP group is created, and its view is displayed.
13. (Optional) Run [**lns schedule after car**](cmdqueryname=lns+schedule+after+car)
    
    
    
    The LNS is configured to re-mark the priorities of service packets entering a tunnel after performing CAR.
    
    
    
    After the configuration is modified, the modification takes effect only for new tunnels.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    When an LNS is configured to re-mark the priorities of packets entering a tunnel after performing CAR, the LNS does not support last-mile QoS.
14. (Optional) Run [**tunnel retrans-queue**](cmdqueryname=tunnel+retrans-queue) *number*
    
    
    
    The maximum number of concurrent L2TP sessions allowed for an L2TP tunnel is configured. Excess session requests are denied.
15. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.