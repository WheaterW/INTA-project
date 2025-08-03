Configuring a Loopback Interface as an RP
=========================================

You can configure a loopback interface as either a static Rendezvous Point (RP) or a Candidate-Rendezvous Point (C-RP). To configure a static RP, perform the configuration on all the Routers in the PIM-SM domain; to configure a C-RP, perform the configuration only on the Routers where Anycast-RP is to be configured.

#### Procedure

* Configure a static RP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The PIM view is displayed.
  3. Run [**static-rp**](cmdqueryname=static-rp) *rp-address*
     
     
     
     The loopback interface address is configured as a static RP address.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a C-RP.
  
  
  
  Before configuring a C-RP, configure a Candidate-BootStrap Router (C-BSR) and a BSR boundary. The C-BSR address must be different from the C-RP address.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The PIM view is displayed.
  3. Run [**c-rp**](cmdqueryname=c-rp) *interface-type* *interface-number*
     
     
     
     The loopback interface address is configured as a C-RP address.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.