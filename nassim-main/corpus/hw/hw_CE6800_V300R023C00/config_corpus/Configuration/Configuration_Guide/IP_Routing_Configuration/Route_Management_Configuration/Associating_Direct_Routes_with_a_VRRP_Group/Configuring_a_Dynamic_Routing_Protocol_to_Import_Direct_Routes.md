Configuring a Dynamic Routing Protocol to Import Direct Routes
==============================================================

Configuring a Dynamic Routing Protocol to Import Direct Routes

#### Context

After direct routes are associated with the VRRP group, VRRP-enabled devices modify the cost of each direct route destined for the virtual IP network segment based on the VRRP status. To control the path selected by a dynamic routing protocol, enable the dynamic routing protocol to import direct routes and inherit the costs from the imported direct routes.

Currently, an IGP or BGP can be used as a dynamic routing protocol. Among IGP protocols, RIP cannot inherit costs of the imported direct routes. This section describes how to configure OSPF, IS-IS, and BGP to import direct routes.


#### Procedure

* Configure OSPF to import direct routes.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the OSPF view.
     
     
     ```
     [ospf](cmdqueryname=ospf) [ process-id ]
     ```
  3. Configure OSPF to import direct routes.
     
     
     ```
     [import-route direct](cmdqueryname=import-route+direct)
     ```
  4. Set the cost of external routes imported by OSPF to be equal to the cost of the external routes themselves.
     
     
     ```
     [default cost inherit-metric](cmdqueryname=default+cost+inherit-metric)
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure IS-IS to import direct routes.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Configure IS-IS to import direct routes and inherit the costs of the imported direct routes.
     
     
     ```
     [import-route direct inherit-cost](cmdqueryname=import-route+direct+inherit-cost)
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure BGP to import direct routes.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Configure BGP to import direct routes.
     
     
     ```
     [import-route direct](cmdqueryname=import-route+direct)
     ```
     
     BGP automatically inherits the costs from the imported direct routes. The inherited costs are contained in the multi-exit discrimination (MED) field.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```