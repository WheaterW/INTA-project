Configuring VRRP in Load Balancing Mode
=======================================

Configuring VRRP in Load Balancing Mode

#### Procedure

* Create VRRP groups working in multi-gateway load balancing mode.
  
  
  
  If VRRP groups need to work in multi-gateway load balancing mode, repeat the steps in [Configuring VRRP in Master/Backup Mode](vrp_vrrp_cfg_0131.html) to configure two or more VRRP groups and assign different VRIDs (specified by *virtual-router-id*) to them.
* Create VRRP groups working in single-gateway load balancing mode.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. (Optional) Configure an interval for the master devices in LBRG member groups to send VRRP Advertisement packets.
     
     
     ```
     [vrrp member-lbrg timer hello](cmdqueryname=vrrp+member-lbrg+timer+hello) hello-time
     ```
     
     
     
     To ensure that the MAC entries on downstream devices can be promptly updated, you can configure an interval for the master devices in LBRG member groups to send VRRP Advertisement packets to ensure service traffic reliability.
  3. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  4. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     
     
     Determine whether to perform this step based on the current interface working mode.
  5. Create a VRRP group.
     
     
     ```
     [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id [ virtual-ip virtual-address ]
     ```
     
     
     + You must specify a virtual IP address for the VRRP group configured as an LBRG.
     + You do not need to specify a virtual IP address for the VRRP group configured as an LBRG member group.
  6. Configure a priority for each device in the VRRP group.
     
     
     ```
     [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id priority priority-value
     ```
  7. Create an LBRG.
     
     
     ```
     [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id load-balance
     ```
  8. Add the VRRP group to the LBRG.
     
     
     ```
     [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id join load-balance-vrrp vrid lb-vrid-value
     ```
  9. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```