Configuring a Policy for Triggering Dynamic BFD for LDP LSPs
============================================================

Configure a policy for dynamically establishing a BFD session to monitor LDP LSPs and create a BFD session.

#### Context

A policy can be enforced to establish a session of dynamic BFD for LDP LSP in either of the following modes

* Host mode: applies when all host addresses can be used to establish a BFD session. You can specify **nexthop** and **outgoing-interface** to define LSPs that support a BFD session.
* FEC list mode: applies when only some host addresses can be used to establish a BFD session.

You can use the **fec-list** command to specify host addresses. Perform the following steps on the ingress of an LSP to be monitored:

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) To use the FEC list mode, perform the following operations:
   1. Run [**fec-list**](cmdqueryname=fec-list) *list-name*
      
      
      
      A FEC list is created, and the FEC list view is displayed.
   2. Run [**fec-node**](cmdqueryname=fec-node+nexthop+outgoing-interface) *fec-node-address* [ **nexthop** *nexthop-address* | **outgoing-interface** *interface-type* *interface-number* ] \*
      
      
      
      A FEC node is added to the FEC list.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
4. Run [**mpls bfd-trigger**](cmdqueryname=mpls+bfd-trigger+host+nexthop+outgoing-interface+fec-list) { **host** [ **nexthop** *next-hop-address* | **outgoing-interface** *interface-type interface-number* ] \* | **fec-list** *list-name* } [ **option-tlv** ]
   
   
   
   A policy for triggering dynamic BFD for LDP LSPs is configured.
   
   
   
   The policy for establishing a session of dynamic BFD for LDP LSP is configured.
5. (Optional) Run [**mpls bfd-option-tlv ip-prefix**](cmdqueryname=mpls+bfd-option-tlv+ip-prefix) *ip-prefix-name*
   
   
   
   An IP prefix list is configured to trigger the establishment of LDP BFD sessions working in compatible mode.
   
   
   
   If the [**mpls bfd-trigger**](cmdqueryname=mpls+bfd-trigger) command has been run to configure the BFD compatible mode globally, the [**mpls bfd-option-tlv ip-prefix**](cmdqueryname=mpls+bfd-option-tlv+ip-prefix) command does not take effect.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.