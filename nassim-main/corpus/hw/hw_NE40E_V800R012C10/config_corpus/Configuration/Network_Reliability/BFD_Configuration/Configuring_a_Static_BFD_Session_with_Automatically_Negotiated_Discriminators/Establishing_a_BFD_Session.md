Establishing a BFD Session
==========================

You can establish a static BFD session with automatically negotiated discriminators on both ends of the link to rapidly detect link faults.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. According to whether BFD detects an IPv4 or IPv6 link, perform any of the following operations:
   
   
   * To bind the BFD for IPv4 session to a Layer 3 interface with an IP address, run any of the following commands:
     
     [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] [ **interface** { *interface-name* | *interface-type* *interface-number* } ] **source-ip** *source-ip* **auto**
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The source address must be configured by specifying **source-ip**.
     + The IP address must be an explicit IPv4 address but not a multicast one.
   
   
   * To bind the BFD session for IPv4 to a Layer 2 interface or a Layer 3 member interface without an IP address, run the [**bfd**](cmdqueryname=bfd) *session-name***bind** **peer-ip** **default-ip** **interface** *interface-type interface-number* [ **source-ip** *source-ip* ] **auto** command.
   * To bind the BFD for IPv6 session to a Layer 3 interface with an IP address, run any of the following commands:To create static BFD session for IPv6 with an automatically negotiated discriminator, run the [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-name* ] [ **interface** *interface-type* *interface-number* ] **source-ipv6** *ipv6-address* **auto** command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The source address must be configured by specifying **source-ipv6**.
     + The IP address must be an explicit IPv6 address but not a multicast one.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.