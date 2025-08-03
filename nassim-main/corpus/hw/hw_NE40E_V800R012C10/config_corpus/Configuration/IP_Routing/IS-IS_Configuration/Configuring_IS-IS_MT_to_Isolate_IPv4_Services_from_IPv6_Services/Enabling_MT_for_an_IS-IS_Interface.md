Enabling MT for an IS-IS Interface
==================================

After IS-IS MT is enabled, associate a specified interface with MT instances.

#### Context

Various topology instances can be associated with one interface so that specified links of the interface can participate in the SPF calculation for the topology instances.

The following parameters can be configured for an interface in different topology instances:

* Cost of the interface in each topology instance
* Administrative tag of the interface in each topology instance

An interface transmitting different services needs to be associated with different topology instances. Perform the following operations:

* [Associate an interface with an IPv4 topology instance](#EN-US_TASK_0172366065__step_dc_vrp_isis_cfg_010601).
* [Associate an interface with an IPv6 topology instance](#EN-US_TASK_0172366065__step_dc_vrp_isis_cfg_010602).


#### Procedure

1. Associate an interface with an IPv4 topology instance.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**ip topology**](cmdqueryname=ip+topology) *topology-name* **enable**
      
      
      
      An IPv4 topology instance is bound to the interface.
   4. Run [**isis topology**](cmdqueryname=isis+topology) *topology-name*
      
      
      
      An IPv4 topology instance is enabled on the interface.
   5. (Optional) Run [**isis**](cmdqueryname=isis) **topology** *topology-name* **cost** *cost* [ **level-1** | **level-2** ]
      
      
      
      A cost is configured on the interface for the IS-IS IPv4 topology instance.
      
      
      
      A cost change on an interface will trigger route reselection. Therefore, change the cost during network planning.
   6. (Optional) Run [**isis**](cmdqueryname=isis) **topology** *topology-name* **tag-value** *tag* [ **level-1** | **level-2** ]
      
      
      
      An administrative tag is configured on the interface for the IS-IS IPv4 topology instance.
      
      
      
      An administrative tag is carried in routes and used by route-policies to filter routes.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Associate an interface with an IPv6 topology instance.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**ipv6 topology**](cmdqueryname=ipv6+topology) *topology-name* **enable**
      
      
      
      An IPv6 topology instance is bound to the interface.
   4. Run [**isis ipv6 topology**](cmdqueryname=isis+ipv6+topology) *topology-name*
      
      
      
      An IPv6 topology instance is enabled on the interface.
   5. (Optional) Run [**isis ipv6**](cmdqueryname=isis+ipv6) [ **topology** *topology-name* ] **cost** *cost-value* [ **level-1** | **level-2** ]
      
      
      
      A cost is configured on the interface for the IS-IS IPv6 topology instance.
      
      
      
      A cost change on an interface will trigger route reselection. Therefore, change the cost during network planning.
   6. (Optional) Run [**isis ipv6**](cmdqueryname=isis+ipv6) [ **topology** *topology-name* ] **tag-value** *tag* [ **level-1** | **level-2** ]
      
      
      
      An administrative tag is configured on the interface for the IS-IS IPv6 topology instance.
      
      
      
      An administrative tag is carried in routes and used by route-policies to filter routes.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.