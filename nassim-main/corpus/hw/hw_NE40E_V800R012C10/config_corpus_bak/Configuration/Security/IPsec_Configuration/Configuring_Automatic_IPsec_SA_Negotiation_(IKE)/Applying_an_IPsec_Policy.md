Applying an IPsec Policy
========================

This section describes how to apply an IPsec policy to a tunnel interface to implement security protection on different data flows.

#### Context

If an IPsec policy is applied to an interface through IKE negotiation, an SA is not established immediately. IKE starts to negotiate an IPsec SA only when the data flow that matches a certain IPsec policy is sent from the interface.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**service-location**](cmdqueryname=service-location) *service-location-id* command to create a VSM HA backup group and access its view.
3. Run the [**location**](cmdqueryname=location) command to bind the VSM HA backup group to the CPU of the service board.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
6. Run the [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name* command to create a VSM HA service instance group and access its view.
7. Run the [**service-location**](cmdqueryname=service-location) *service-location-id* command to bind the VSM HA backup group to the VSM HA service instance group.
8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
9. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
10. Run the [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number* command to create a tunnel interface and enter the tunnel interface view.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    You need to create a tunnel interface first. An IPsec policy can be applied only to a tunnel interface, but not to a physical interface.
11. Run the [**tunnel-protocol**](cmdqueryname=tunnel-protocol+ipsec) **ipsec** command to configure IPsec on the tunnel interface.
12. Run either of the following commands to configure an IP address for the tunnel interface:
    * Run the [**ip address**](cmdqueryname=ip+address) *ip-address* *mask* command to configure an IP address for the tunnel interface.
    * Run the [**ip address unnumbered**](cmdqueryname=ip+address+unnumbered+interface) **interface** *interface-type* *interface-number* command to configure the tunnel interface to borrow an IP address from another interface.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If an available IP address exists on a device, run the first command to configure an IP address for the tunnel interface. The second command is run only when no available IP address exists on a device.
    
    The second command may bring the following risks:
    * If a tunnel interface that has been configured with the [**tunnel-protocol**](cmdqueryname=tunnel-protocol+ipsec) **ipsec** command borrows an IP address from a physical or logical interface, the interface cannot be bound to other services. Otherwise, other services are also diverted to the IPsec tunnel.
    * If the IP address of another physical or logical interface is borrowed and the IP address of the interface changes, IPsec negotiation fails.
    * If the IP address of a physical interface is borrowed and the physical interface alternates between up and down, IPsec negotiation may fail.
13. Run the [**ipsec policy**](cmdqueryname=ipsec+policy) *policy-name* **service-instance-group** *service-group-name* command to apply an IPsec policy to the interface.
    
    To use IPsec on a DSVPN-enabled interface, run the [**ipsec policy**](cmdqueryname=ipsec+policy+service-instance-group+share) *profile-name* **service-instance-group** *service-group-name* [ **share** ] command to bind an IPsec profile to the interface.![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    Generally, an IPsec profile can be applied to only one interface. In a scenario where multiple mGRE tunnels of a DSVPN share the same source, if you need to apply the same IPsec profile to multiple tunnel interfaces for IPsec tunnel sharing, specify the **share** parameter when running this command.
    
    The **share** parameter can be used only in this scenario. In addition, mGRE tunnels with the same source address must be configured with different keys. In addition, you need to run the [**tunnel-protocol**](cmdqueryname=tunnel-protocol+gre+p2mp) **gre** **p2mp** command and the [**source**](cmdqueryname=source) [ *source-ip-address* | { *interface-name* | *interface-type* *interface-number* } ] command on the tunnel interface.
14. (Optional) Run the [**ipsec generate-service-route**](cmdqueryname=ipsec+generate-service-route) command to enable automatic IPsec service route generation.
    
    Automatic IPsec service route generation is mainly applied to the following two scenarios:
    * When a security policy is used to establish IPsec tunnels, you may not know the IPsec service route information of the remote end (such as the IP address and interface of the remote end). Therefore, static routes cannot be configured manually. In this case, run the [**ipsec generate-service-route**](cmdqueryname=ipsec+generate-service-route) command to enable the function of automatic IPsec service route generation.
    * When IPsec tunnels are established using an IPsec policy template, IPsec service routes will be generated during the IPsec negotiation. If you want to generate IPsec service routes by configuring static routes, you can run the [**undo ipsec generate-service-route**](cmdqueryname=undo+ipsec+generate-service-route) command to disable the function of automatic IPsec service route generation first.
15. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.