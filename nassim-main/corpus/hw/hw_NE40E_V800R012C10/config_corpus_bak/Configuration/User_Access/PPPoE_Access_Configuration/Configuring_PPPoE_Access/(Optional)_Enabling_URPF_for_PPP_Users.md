(Optional) Enabling URPF for PPP Users
======================================

Enabling URPF for PPP users prevents source address spoofing attacks.

#### Procedure

* Enable the function in the virtual template view :
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **virtual-template** *virtual-template-number*
     
     A virtual template is created and the virtual template view is displayed.
  3. Run [**ip urpf**](cmdqueryname=ip+urpf) **strict** **enable** [ **check subnet** ] command
     
     IPv4 URPF for PPPoE users is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable the function in the VPN view :
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run **ip vpn-instance** *vpn-instance-name*
     
     A VPN instance is created, and the VPN instance view is displayed.
  3. Run **ipv4-family** [ **unicast** ]
     
     The IPv4 unicast address family view is displayed.
  4. Run [**access ip urpf strict**](cmdqueryname=access+ip+urpf+strict)
     
     IPv4 URPF for L2TP and PPPoE users in the VPN instance view is configured to prevent source address spoofing attacks based on VPNs.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The URPF function in the VPN view takes precedence over the URPF function in the VT view.

#### Verifying the Configuration

* In the VPN view, run [**display access um urpf**](cmdqueryname=display+access+um+urpf) command to check information about the URPF status of access users in the VPN view.
* In the All views, run [**display ppp-user urpf discard statistics**](cmdqueryname=display+ppp-user+urpf+discard+statistics) command to check the number of URPF-dropped PPPoE user packets.