Configuring VRRP6 in Load Balancing Mode
========================================

Configuring VRRP6 in Load Balancing Mode

#### Procedure

* Create VRRP6 groups working in multi-gateway load balancing mode.
  
  
  
  If VRRP6 groups need to work in multi-gateway load balancing mode, repeat steps 1 through 6 in [Configuring VRRP6 in Master/Backup Mode](vrp_vrrp6_cfg_0010.html) to configure two or more VRRP6 groups and assign different VRIDs (specified by *virtual-router-id*) to them.
* Create VRRP6 groups working in single-gateway load balancing mode.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. (Optional) Configure an interval for the master devices in LBRG member groups to send VRRP6 Advertisement packets.
     
     
     ```
     [vrrp member-lbrg timer hello](cmdqueryname=vrrp+member-lbrg+timer+hello) hello-time
     ```
     
     
     
     To ensure that the MAC entries on downstream switches can be promptly updated, you can configure an interval for the master devices in LBRG member groups to send VRRP6 Advertisement packets to ensure service traffic reliability.
  3. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  4. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     
     
     Determine whether to perform this step based on the current interface working mode.
  5. Enable IPv6 on the interface.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
     
     By default, IPv6 is disabled.
  6. Configure an IPv6 address for the interface.
     
     
     ```
     [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length }
     ```
  7. Create a VRRP6 group and configure the first virtual IPv6 address for it.
     
     
     ```
     [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id [ virtual-ip virtual-address [ link-local ] ]
     ```
     
     
     + You must specify a virtual IPv6 address for the VRRP6 group configured as an LBRG.
     + You do not need to specify a virtual IPv6 address for the VRRP6 group configured as an LBRG member group.
  8. Configure a priority for each device in the VRRP6 group.
     
     
     ```
     [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id priority priority-value
     ```
  9. Create an LBRG.
     
     
     ```
     [vrrp6 vrid](cmdqueryname=vrrp6+vrid) vrid-value load-balance
     ```
  10. Add the VRRP6 group to the LBRG.
      
      
      ```
      [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id join load-balance-vrrp vrid lb-vrid-value
      ```
  11. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```