Configuring a Proper Reassembly Timeout Period for IPv6 Fragments
=================================================================

To improve device performance and prevent attacks, run the ipv6 reassembling timeout command to set a proper reassembly timeout period for IPv6 fragments so that IPv6 fragments that have waited for reassembly for a long time are promptly aged.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 reassembling timeout**](cmdqueryname=ipv6+reassembling+timeout) *interval*
   
   
   
   A new reassembly timeout period for IPv6 fragments is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a long reassembly timeout period is set, a large number of IPv6 fragments are stored on the device, waiting to be reassembled. This consumes resources, reduces device performance, and may cause network attacks. Therefore, you are not recommended to set a long reassembly timeout period.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.