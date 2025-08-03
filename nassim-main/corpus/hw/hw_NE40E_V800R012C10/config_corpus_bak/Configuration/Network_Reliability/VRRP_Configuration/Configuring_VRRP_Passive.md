Configuring VRRP Passive
========================

The VRRP passive function allows a device in a VRRP group to forcibly switch to the Master state without performing master/backup negotiation.

#### Context

In a scenario where all gateways are active, the gateways must be configured with the same IP address and MAC address. You can configure a VRRP group on the gateways to virtualize multiple gateways into one device so that they have the same virtual IP address and MAC address. This reduces manual planning and simplifies configuration. However, backup devices in a VRRP group do not have the forwarding capability. They need to forcibly switch to the Master state. After VRRP passive is configured, devices in the VRRP group do not negotiate the master/backup status. Instead, they all become the master devices and have the forwarding capability.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

After the VRRP passive function is enabled, multiple master devices exist, restricting the functions of the VRRP group. You are therefore advised to enable this function only in EVPN VPLS networking where dual active gateways are deployed. Exercise caution when enabling this function in other scenarios.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **virtual-ip** *virtual-address*
   
   
   
   A VRRP group is created, and a virtual IP address is assigned to the VRRP group.
4. Run [**vrrp passive**](cmdqueryname=vrrp+passive)
   
   
   
   The VRRP passive function is enabled so that the corresponding device is forcibly switched to the Master state when the interface goes up.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring the VRRP passive function, run the [**display vrrp**](cmdqueryname=display+vrrp) command to check the status of the VRRP group.