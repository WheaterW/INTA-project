Configuring EVC VPLS Accessing L3VPN
====================================

This section describes how to create a VBDIF interface to implement EVC VPLS accessing L3VPN.

#### Usage Scenario

EVC interfaces are Layer 2 interfaces that do not support IP addresses. If EVC L2VPN accessing L3VPN is required, you must create a BD-based interface, or VBDIF interface. A VBDIF interface is a Layer 3 interface that supports IP address configuration. Through the IP address, Layer 3 communication can be implemented through EVC.

As shown in [Figure 1](#EN-US_TASK_0172363396__fig_dc_vrp_evc_cfg_003801), on the access network, the CSG provides a BD for user site access and connects to the ASG over a VPLS PW; on the bearer network, the ASG uses the VBDIF interface to terminate the VPLS PW and establishes an L3VPN with the RSG.

**Figure 1** EVC VPLS accessing L3VPN  
![](images/fig_dc_vrp_evc_cfg_003801.png)  
#### Pre-configuration Tasks

Before configuring EVC VPLS accessing L3VPN, complete the following task:

* [Establishing the EVC Model](dc_vrp_evc_cfg_0003.html)



#### Procedure

1. Configure EVC VPLS on the CSG and ASG.
2. Configure a VPN instance on the ASG and RSG and establish an MP-IBGP peer relationship between them.
3. Create a VBDIF interface on the ASG and bind the VBDIF interface to the VPN instance.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface vbdif**](cmdqueryname=interface+vbdif) *bd-id*
      
      
      
      A VBDIF interface is created, and the VBDIF interface view is displayed.
      
      The VBDIF interface number must be the ID of a BD that has been created.
   3. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
      
      
      
      The VBDIF interface is bound to a VPN instance.
   4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
      
      
      
      An IP address is assigned to the VBDIF interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.