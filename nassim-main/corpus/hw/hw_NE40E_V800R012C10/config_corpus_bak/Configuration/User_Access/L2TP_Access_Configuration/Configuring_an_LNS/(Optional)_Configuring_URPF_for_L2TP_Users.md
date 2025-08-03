(Optional) Configuring URPF for L2TP Users
==========================================

To prevent source address spoofing attacks, enable URPF for L2TP users.

#### Procedure

* Configurations in the virtual template view:
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface virtual-template**](cmdqueryname=interface+virtual-template) *virtual-template-number*
     
     A virtual template is created and its view is displayed.
  3. Enable URPF for L2TP users.
     + Run [**ip urpf strict enable**](cmdqueryname=ip+urpf+strict+enable) [ **check subnet** ]
       
       IPv4 URPF is enabled.
     + Run [**ipv6 urpf strict enable**](cmdqueryname=ipv6+urpf+strict+enable) [ **check subnet** ]
       
       IPv6 URPF is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configurations in the VPN instance view:
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run **ip vpn-instance** *vpn-instance-name*
     
     A VPN instance is created, and its view is displayed.
  3. Configure URPF for L2TP users.
     + For IPv4 L2TP users:
       1. Run **ipv4-family** [ **unicast** ]
          
          The VPN instance IPv4 address family is enabled, and its view is displayed.
       2. Run [**access ip urpf strict**](cmdqueryname=access+ip+urpf+strict) { **disable** | **enable** [ **check subnet** ] }
          
          IPv4 URPF is disabled or enabled for L2TP users.
     + For IPv6 L2TP users:
       1. Run **ipv6-family** [ **unicast** ]
          
          The VPN instance IPv6 address family is enabled, and its view is displayed.
       2. Run [**access ipv6 urpf strict**](cmdqueryname=access+ipv6+urpf+strict) { **disable** | **enable** [ **check subnet** ] }
          
          IPv6 URPF is disabled or enabled for L2TP users.
  4. Run [**commit**](cmdqueryname=commit)The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The URPF function configured in the VPN instance view takes precedence over that configured in the virtual template view.