Configuring a Local TDMoPSN Service
===================================

To configure the local TDMoPSN Service, you need to create
a local CCC connection and only configure the incoming and outgoing
interfaces of the CCC connection on a local PE. The local CCC connection
is bidirectional and only one such connection needs to be created.

#### Context

The local CCC connection is bidirectional, and only one
connection is required.

Perform the following steps on PEs:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view
   is displayed.
2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
   
   
   
   MPLS L2VPN is enabled.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**ccc**](cmdqueryname=ccc) *ccc-connection-name* **interface** *interface-type1* *interface-number1* **out-interface** *interface-type2* *interface-number2* [ **jitter-buffer** *depth* | **idle-code** *idle-code-value* | **rtp-header** | **tdm-encapsulation** *number* ]
   
   
   
   A local CCC connection is
   created.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

After the configuration mentioned above on the PE, a local
CCC connection is created.