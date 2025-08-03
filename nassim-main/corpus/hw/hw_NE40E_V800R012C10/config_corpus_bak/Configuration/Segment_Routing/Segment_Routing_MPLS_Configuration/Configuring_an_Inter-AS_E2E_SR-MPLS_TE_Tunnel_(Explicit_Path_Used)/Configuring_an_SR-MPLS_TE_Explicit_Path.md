Configuring an SR-MPLS TE Explicit Path
=======================================

An explicit path over which an SR-MPLS TE tunnel is to be established is configured on the ingress. You can specify node or link labels for the explicit path.

#### Context

An explicit path is a vector path comprised of a series of nodes that are arranged in the configuration sequence. The path through which an SR-MPLS TE LSP passes can be planned by specifying next-hop labels or next-hop IP addresses on an explicit path. Generally, an IP address specified on an explicit path is the IP address of an interface. An explicit path in use can be dynamically updated.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**explicit-path**](cmdqueryname=explicit-path) *path-name*
   
   
   
   An explicit path is created and the explicit path view is displayed.
3. Configure an explicit path.
   
   
   
   In the following example, two ASs are connected. If there are multiple ASs, add configurations based on the network topology.
   
   1. Run [**next sid label**](cmdqueryname=next+sid+label) *label-value* **type** **binding-sid** [ **index** *index-value* ]
      
      A binding SID is specified for the first AS of the explicit path.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      When the first hop of an explicit path is assigned a binding SID, the explicit path supports a maximum of three hops.
   2. Run [**next sid label**](cmdqueryname=next+sid+label) *label-value* **type** **adjacency** [ **index** *index-value* ]
      
      An inter-AS adjacency label is specified.
   3. Run [**next sid label**](cmdqueryname=next+sid+label) *label-value* **type** **binding-sid** [ **index** *index-value* ]
      
      A binding SID is specified for the second AS of the explicit path.
      
      In the case of multiple ASs, this binding SID can be the binding SID of a new E2E SR-MPLS TE tunnel.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.