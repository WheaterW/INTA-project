(Optional) Configuring VPN Instance-based User Traffic Statistics Collection on a BAS Interface
===============================================================================================

You can configure a device to collect statistics on user traffic based on VPN instances on a BAS interface.

#### Context

If multiple users bound to VPN instances exist on a BAS interface, you can enable VPN instance-based user traffic statistics collection on the BAS interface on the device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   The BAS interface view is displayed.
4. Run [**access-type**](cmdqueryname=access-type)
   
   
   
   A type is set for the BAS interface.
5. Run [**access statistics vpn-instance enable**](cmdqueryname=access+statistics+vpn-instance+enable)
   
   
   
   VPN instance-based user traffic statistics collection is enabled on the BAS interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Result

* After user access configuration is performed and users go online, you can run the [**display access user-flow-statistics configuration**](cmdqueryname=display+access+user-flow-statistics+configuration) or [**display vlan-statistics pevlan**](cmdqueryname=display+vlan-statistics+pevlan) command to view the traffic configuration and statistics of the device.
* To clear such user traffic statistics, run the [**reset vlan-statistics pevlan**](cmdqueryname=reset+vlan-statistics+pevlan) command. Then you can run the [**display access statistics interface**](cmdqueryname=display+access+statistics+interface) command to view new statistics.