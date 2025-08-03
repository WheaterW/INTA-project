Assigning an IP address to a VBDIF Interface
============================================

The IP address assigned for a VBDIF interface that performs local proxy ARP for a bridge domain (BD) must be in the same network segment as the IP addresses of the member interfaces in the BD.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   A BD is created.
3. Run [**interface vbdif**](cmdqueryname=interface+vbdif) *bd-id*
   
   
   
   A VBDIF interface is created, and the VBDIF interface view is displayed.
   
   
   
   The number of the VBDIF interface must be the same as the BD ID specified in Step 2.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A VBDIF interface of a BD goes Up only if the BD has a Layer 2 sub-interface that is in the Up state. To add a Layer 2 sub-interface to a BD, run the [**bridge-domain (Layer 2 sub-interface view)**](cmdqueryname=bridge-domain+%28Layer+2+sub-interface+view%29) command in the view of the Layer 2 sub-interface.
4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   
   
   An IP address is assigned to the VBDIF interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.