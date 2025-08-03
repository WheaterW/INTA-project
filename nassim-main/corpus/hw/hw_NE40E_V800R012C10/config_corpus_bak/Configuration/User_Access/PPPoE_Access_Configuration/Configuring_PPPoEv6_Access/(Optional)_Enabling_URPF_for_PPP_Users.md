(Optional) Enabling URPF for PPP Users
======================================

Enabling URPF for PPP users prevents source address spoofing attacks.

#### Procedure

* Enable the function in the virtual template view :
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **virtual-template** *virtual-template-number*
     
     A virtual template is created and the virtual template view is displayed.
  3. Run [**ipv6 urpf**](cmdqueryname=ipv6+urpf) **strict** **enable** [ **check subnet** ]
     
     IPv6 URPF is enabled for PPPoE users.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable the function in the VPN view :
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run **ip vpn-instance** **vpn-instance-name**
     
     A VPN instance is created, and the VPN instance view is displayed.
  3. Run **ipv6-family** [ **unicast** ]
     
     Enable the VPN instance IPv6 address family, and enter its view.
  4. Run [**access ipv6 urpf strict**](cmdqueryname=access+ipv6+urpf+strict) { **disable** | **enable** [ **check subnet** ] }
     
     IPv6 URPF is disabled or enabled for PPPoE users.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The URPF function in the VPN view takes precedence over the URPF function in the VT view.