Configuring an SR-MPLS TE Explicit Path
=======================================

An explicit path over which an SR-MPLS TE tunnel is to be established is configured on the ingress. You can specify node or link labels for the explicit path.

#### Context

An explicit path is a vector path comprised of a series of nodes that are arranged in the configuration sequence. The path through which an SR-MPLS TE LSP passes can be planned by specifying next-hop labels or next-hop IP addresses on an explicit path. Generally, an IP address specified on an explicit path is the IP address of an interface. An explicit path in use can be dynamically updated.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**explicit-path**](cmdqueryname=explicit-path) *path-name*
   
   
   
   An explicit path is created, and the explicit path view is displayed.
3. Select one of the following methods to configure an explicit path:
   
   
   * Run the [**next sid label**](cmdqueryname=next+sid+label) *label-value* **type** { **adjacency** | **prefix** | **binding-sid** } [ **index** *index-value* ] command to specify a next-hop label for the explicit path.
   * Specify a next-hop address for the explicit path.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In this scenario, the [**mpls te cspf**](cmdqueryname=mpls+te+cspf) command must be run on the ingress to enable CSPF.
     
     
     1. Run the [**next hop**](cmdqueryname=next+hop) *ipv4* [ **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* | **exclude** ] [ **index** *index-value* ] command to specify a next-hop node for the explicit path.
        
        The **include** parameter indicates that an LSP must pass through a specified node. The **exclude** parameter indicates that an LSP cannot pass through a specified node.
     2. (Optional) Run the [**add hop**](cmdqueryname=add+hop) *ipv4* [ **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* | **exclude** ] { **after** | **before** } *contrastIpv4* command to add a node to the explicit path.
     3. (Optional) Run the [**modify hop**](cmdqueryname=modify+hop) *ip-address1* *ip-address2* [ **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* | **exclude** ] command to change node addresses in the explicit path.
     4. (Optional) Run the [**delete hop**](cmdqueryname=delete+hop) *ipv4* command to remove a node from the explicit path.
   * Specify both the next-hop label and IP address for the explicit path.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In this scenario, the [**mpls te cspf**](cmdqueryname=mpls+te+cspf) command must be run on the ingress to enable CSPF.
     
     1. Run the [**next sid label**](cmdqueryname=next+sid+label) *label-value* **type** { **adjacency** | **prefix** | **binding-sid** } or [**next hop**](cmdqueryname=next+hop) *ip-address* [ **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* | **exclude** ] [ **index** *index-value* ] command to specify a next-hop label or the next node for the explicit path.
     2. (Optional) Run the [**add sid label**](cmdqueryname=add+sid+label) *label-value* **type** { **adjacency** | **prefix** | **binding-sid** } { **after** | **before** } { **hop** *contrastIpv4* | **index** *indexValue* | **sid label** *contrastLabel* **index** *indexValue* } or [**add hop**](cmdqueryname=add+hop) *ipv4* [ **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* | **exclude** ] { **after** | **before** } { **hop** *contrastIpv4* | **index** *indexValue* | **sid label** *contrastLabel* **index** *indexValue* } command to add a label or node to the explicit path.
     3. (Optional) Run the [**modify hop**](cmdqueryname=modify+hop) *ip-address1* **to** { **hop** *ip-address2* [ **exclude** | **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* ] | **sid label** *label-value* **type** { **adjacency** | **prefix** } }, [**modify index**](cmdqueryname=modify+index) *indexValue* **to** { **hop** *ipv4* [ **exclude** | **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* ] | **sid label** *label-value* **type** { **adjacency** | **prefix** | **binding-sid** } }, or [**modify sid label**](cmdqueryname=modify+sid+label) *contrastLabel* **index** *indexValue* **to** { **hop** *ipv4* [ **exclude** | **include** [ [ **strict** | **loose** ] | [ **incoming** | **outgoing** ] ] \* ] | **sid label** *label-value* **type** { **adjacency** | **prefix** | **binding-sid** } } command to modify a label or node of the explicit path.
     4. (Optional) Run the [**delete**](cmdqueryname=delete+sid+label) { **sid label** *labelValue* **index** *indexValue* | **index** *indexValue* } or [**delete hop**](cmdqueryname=delete+hop) *ip-address* command to delete a label or node from the explicit path.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.