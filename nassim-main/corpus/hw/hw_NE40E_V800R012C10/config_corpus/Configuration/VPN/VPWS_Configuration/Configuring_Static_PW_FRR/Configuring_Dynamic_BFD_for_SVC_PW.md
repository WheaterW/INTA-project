Configuring Dynamic BFD for SVC PW
==================================

Dynamic BFD for SVC PW accelerates PW fault detection, facilitating fast switching of SVC PWs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally, and the BFD global view is displayed.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .**subinterface-number** ]
   
   
   
   The AC interface view is displayed.
5. Run [**mpls l2vpn pw bfd**](cmdqueryname=mpls+l2vpn+pw+bfd) [ **detect-multiplier** *multiplier* | **min-rx-interval** *rx-interval* | **min-tx-interval** *tx-interval* ] \* [ **track** **group** *group-name* ] [ **remote-vcid** *vc-id* ] [ **track-interface** ] [ **secondary** ]
   
   
   
   Dynamic BFD for VPWS PW is configured, and BFD control packet detection parameters are set.
   
   
   
   If the PW to be detected is a secondary PW, configure **secondary**.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.