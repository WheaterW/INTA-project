Configuring a Dynamic Routing Protocol to Import Direct Routes
==============================================================

After you associate direct routes with a Virtual Router Redundancy Protocol (VRRP) group, configure a dynamic routing protocol to import the direct routes so that the path selection by the dynamic routing protocol can be controlled.

#### Context

After direct routes are associated with a VRRP group, VRRP-enabled devices modify the cost of each direct route to the virtual IP network segment based on the VRRP status. To control the path by a dynamic routing protocol, enable the dynamic routing protocol to import direct routes and inherit the costs from the imported direct routes.

Currently, dynamic routing protocols include the Interior Gateway Protocol (IGP) and Border Gateway Protocol (BGP). If an IGP is configured to import direct routes, routing information protocol (RIP) cannot inherit costs from the imported direct routes. This section describes how to configure Open Shortest Path First (OSPF), Intermediate System to Intermediate System (IS-IS), and BGP to import direct routes.


#### Procedure

* Configure OSPF to import direct routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     
     
     The OSPF process view is displayed.
  3. Run [**import-route**](cmdqueryname=import-route) **direct**
     
     
     
     OSPF is configured to import direct routes.
  4. Run [**default**](cmdqueryname=default) **cost** **inherit-metric**
     
     
     
     OSPF is enabled to inherit the costs from the imported direct routes.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The [**default (OSPF)**](cmdqueryname=default+%28OSPF%29) command has a lower priority than the [**apply cost**](cmdqueryname=apply+cost) command. If the [**apply cost**](cmdqueryname=apply+cost) command is run, it overrides the [**default (OSPF)**](cmdqueryname=default+%28OSPF%29) command. Therefore, before running the [**default (OSPF)**](cmdqueryname=default+%28OSPF%29) command, ensure that the [**apply cost**](cmdqueryname=apply+cost) command is not run.
     + Do not run the [**default**](cmdqueryname=default) **cost** *cost-value* command after you run the [**default**](cmdqueryname=default) **cost** **inherit-metric** command. If the [**default**](cmdqueryname=default) **cost** *cost-value* command is run after the [**default**](cmdqueryname=default) **cost** **inherit-metric** command, the [**default**](cmdqueryname=default) **cost** *cost-value* command overrides the [**default**](cmdqueryname=default) **cost** **inherit-metric** command.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure IS-IS to import direct routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS process view is displayed.
  3. Run [**import-route**](cmdqueryname=import-route) **direct** **inherit-cost**
     
     
     
     IS-IS is configured to import direct routes and to inherit the costs from the imported direct routes.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure BGP to import direct routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP process view is displayed.
  3. Run [**import-route**](cmdqueryname=import-route) **direct**
     
     
     
     BGP is configured to import direct routes.
     
     BGP automatically inherits the costs from the imported direct routes. The inherited costs are shown as the multi-exit discrimination (MED) values.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.