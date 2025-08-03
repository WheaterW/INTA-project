Configuring OSPF to Import External Routes
==========================================

Importing the routes discovered by other routing protocols can enrich OSPF routing information.

#### Context

OSPF provides loop-free intra-area routes and inter-area routes; however, OSPF cannot prevent external routing loops. Therefore, you should exercise caution when configuring OSPF to import external routes.

Perform the following operations on the Router that functions as the ASBR running OSPF:


#### Procedure

* Configure OSPF to import the routes discovered by other protocols.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     
     
     An OSPF process is started, and the OSPF view is displayed.
  3. Run [**import-route**](cmdqueryname=import-route) { **bgp** [ **permit-ibgp** ] | **direct** | **rip** [ *process-id-rip* ] | **static** | **isis** [ *process-id-isis* ] | **ospf** [ *process-id-ospf* ] } [ **cost** *cost* | **route-policy** *route-policy-name* | **tag** *tag* | **type** *type* ] \*
     
     
     
     External routes are imported.
     
     
     
     + The **cost** *cost* parameter specifies the cost of a route.
     + The **type** *type* parameter specifies the type of a route. It can be 1 or 2.
     + The **tag** *tag* parameter specifies the tag in the external LSA.
     + The **route-policy** *route-policy-name* parameter specifies the name of a route-policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set parameters for OSPF to import routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     
     
     An OSPF process is started, and the OSPF view is displayed.
  3. Run [**default**](cmdqueryname=default) { **cost** { *cost* | **inherit-metric** } | **tag** *tag* | **type** *type* } \*
     
     
     
     The default parameter (cost, tag, and type) values are configured for imported routes
     
     
     
     + The **cost** *cost* parameter specifies the default cost of the external routes imported by OSPF.
     + The **inherit-metric** parameter retains the original costs of the imported routes. If the cost is not specified, the default cost set through the [**default**](cmdqueryname=default) command is used as the cost of the imported routes.
     
     When OSPF imports external routes, you can set default values for some additional parameters, such as the route cost, tag, and type. The route tag is used to identify the protocol-related information. For example, it can be used to differentiate AS numbers when OSPF imports BGP routes.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) You can run one of the following commands to set the cost of the imported routes. The following commands are listed in descending order of priority:
     + Run the [**apply cost**](cmdqueryname=apply+cost) command in a route-policy to set the cost of the imported routes.
     + Run the [**import-route**](cmdqueryname=import-route) command for OSPF to set the cost of the imported routes.
     + Run the [**default**](cmdqueryname=default) command to set the default cost of the imported routes.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.