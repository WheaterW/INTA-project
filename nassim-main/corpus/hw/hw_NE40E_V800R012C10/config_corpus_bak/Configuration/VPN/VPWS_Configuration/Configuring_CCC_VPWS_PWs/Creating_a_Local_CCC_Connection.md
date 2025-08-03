Creating a Local CCC Connection
===============================

Creating a local CCC connection enables two CEs that connect to the same PE to communicate.

#### Context

When configured with a local CCC connection, the PE functions similar to a Layer 2 switch to directly transmit the CEs' packets without using LSPs.

Perform the following steps on the PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
   
   
   
   MPLS L2VPN is enabled.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**ccc**](cmdqueryname=ccc) *ccc-connection-name* **interface** { *interface-name1* | *interface-type1* *interface-number1* } [ **access-port** ] [ *raw* ] **out-interface** { *interface-name2* | *interface-type2* *interface-number2* } [ **access-port** ] [ *outraw* ] or [**ccc**](cmdqueryname=ccc) **ip-interworking** *ccc-connection-name* **interface** { *interface-name1* | *interface-type1* *interface-number1* } [ **access-port** ] **out-interface** { *interface-name2* | *interface-type2* *interface-number2* } [ **access-port** ] [ *outraw* ]
   
   
   
   A local CCC connection is created.
   
   
   
   * Here, you only need to configure the inbound and outbound interfaces of the local CCC connection on the PE. Because a local CCC connection is bidirectional, only one connection is required.
   * If the link encapsulation types on the two CEs are inconsistent, configure **ip-interworking** in this command to enable IP heterogeneous interworking for the local CCC connection.
   * The **raw**, **tagged**, and **access-port** parameters are available in this command only for Ethernet links. In addition, the **access-port** parameter can be configured only on Ethernet main interfaces.
5. (Optional) Run [**ccc**](cmdqueryname=ccc) *cccName* **description** *text*
   
   
   
   A description is configured for the local CCC connection.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.