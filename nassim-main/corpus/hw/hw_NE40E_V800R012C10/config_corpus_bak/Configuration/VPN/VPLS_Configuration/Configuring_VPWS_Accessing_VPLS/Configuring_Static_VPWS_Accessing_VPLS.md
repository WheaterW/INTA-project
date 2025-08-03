Configuring Static VPWS Accessing VPLS
======================================

This section describes how to configure static VPWS accessing VPLS when UPEs do not support VPLS.

#### Procedure

1. [Configure SVC VPWS.](dc_vrp_vpws_cfg_6002.html)
2. [Configure static VPLS.](dc_vrp_vpls_cfg_6001.html)
3. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
4. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   The VSI view is displayed.
5. (Optional) Enable MAC Withdraw.
   1. Run the [**pwsignal ldp**](cmdqueryname=pwsignal+ldp) command to enter the VSI-LDP view.
   2. Run the [**mac-withdraw enable**](cmdqueryname=mac-withdraw+enable) and [**interface-status-change [ up | down ] mac-withdraw enable**](cmdqueryname=interface-status-change+%5B+up+%7C+down+%5D+mac-withdraw+enable) commands to enable MAC Withdraw.
      
      
      
      If you do not enable this function, a traffic forwarding error may occur before MAC addresses age out.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the VSI view.
6. (Optional) Run the [**local-mac remove all-but-mine**](cmdqueryname=local-mac+remove+all-but-mine) command to enable the VSI to remove all MAC entries (except those learned from the PW over which the VSI receives the MAC Withdraw message with TLV type 0x404). This is the standard processing mode.
   
   
   
   If you do not perform this step, the VSI will remove all MAC entries when receiving a MAC Withdraw message with TLV type 0x404.
7. (Optional) Enable MAC Withdraw loop detection.
   1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   2. Run the [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) command to enter the MPLS L2VPN view.
   3. Run the [**vpls mac-withdraw loop-detect enable**](cmdqueryname=vpls+mac-withdraw+loop-detect+enable) command to enable MAC Withdraw loop detection.
      
      
      
      A MAC Withdraw loop detection-capable PE forwards MAC Withdraw messages with the Path TLV inserted. A MAC Withdraw loop detection-incapable device forwards MAC Withdraw messages without inserting the Path TLV.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.