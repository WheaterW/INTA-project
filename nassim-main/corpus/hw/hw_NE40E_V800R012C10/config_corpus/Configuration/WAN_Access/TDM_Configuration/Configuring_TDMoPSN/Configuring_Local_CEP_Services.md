Configuring Local CEP Services
==============================

To configure local CEP services, you only need to create a CCC connection on a PE and configure inbound and outbound interfaces for the CCC connection.

#### Context

Because a local CCC connection is bidirectional, only one connection is required.

Perform the following steps on the PE where a local CCC connection is to be configured:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view of the PE is displayed.
2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
   
   
   
   MPLS L2VPN is enabled.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
   
   
   
   The CPOS interface view is displayed.
5. Run [**using vc4**](cmdqueryname=using+vc4)
   
   
   
   The CPOS interface is configured to work in VC4 clear channel mode, and a serial interface is created.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**ccc**](cmdqueryname=ccc) *ccc-connection-name* **interface** *interface-type1* *interface-number1* **out-interface** *interface-type2* *interface-number2* [ **jitter-buffer** *depth* | **rtp-header** ]
   
   
   
   A local CCC connection is created.
8. Run [**interface**](cmdqueryname=interface) **serial**
   
   
   
   The view of the serial interface created in Step 5 is displayed.
9. (Optional) Run [**cep soh-transport enable**](cmdqueryname=cep+soh-transport+enable)
   
   
   
   Section overhead (SOH) transparent transmission is enabled for CEP services on the serial interface. The overhead bytes E1, E2, F1, K1, K2, and D1 to D12 can be transparently transmitted.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.