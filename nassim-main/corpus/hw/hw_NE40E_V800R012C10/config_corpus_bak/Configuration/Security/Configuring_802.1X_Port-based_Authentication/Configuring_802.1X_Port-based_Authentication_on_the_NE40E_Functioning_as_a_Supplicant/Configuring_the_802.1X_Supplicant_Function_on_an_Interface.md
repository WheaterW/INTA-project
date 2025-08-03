Configuring the 802.1X Supplicant Function on an Interface
==========================================================

After the 802.1X supplicant function is enabled on an interface, the interface initiates 802.1X authentication. After the authenticator passes the authentication, the 802.1X supplicant can access the network.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**dot1x supplicant enable template**](cmdqueryname=dot1x+supplicant+enable+template) *dot1x-supplicant-template-number*
   
   
   
   The 802.1X supplicant function is enabled on the interface and an 802.1X supplicant template is specified.