Enabling MT for IPv4 an IS-IS Interface
=======================================

After IS-IS MT is enabled, associate a specified interface with MT instances so that specified links can participate in the SPF calculation for the topology instances.

#### Context

Various topology instances can be associated with one interface so that specified links of the interface can participate in the SPF calculation for the topology instances.

The following parameters can be configured for an interface in different topology instances:

* Cost of the interface in each topology instance
* Administrative tag of the interface in each topology instance


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The physical interface view is displayed.
3. Run [**ip topology**](cmdqueryname=ip+topology) *topology-name* **enable**
   
   
   
   An IPv4 topology instance is enabled for the interface.
4. Run [**isis topology**](cmdqueryname=isis+topology) *topology-name*
   
   
   
   The interface is associated with the IS-IS IPv4 topology instance.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If You want to associate an interface with multiple IPv4 topology instances, repeat this step and specify different topology names.
5. (Optional) Run [**isis**](cmdqueryname=isis) **topology** *topology-name* **cost** *cost* [ **level-1** | **level-2** ]
   
   
   
   A cost is configured for the interface in the IS-IS topology instance.
   
   
   
   A cost change on an interface will trigger route reselection. Therefore, change the cost during network planning.
6. (Optional) Run [**isis**](cmdqueryname=isis) **topology** *topology-name* **tag-value** *tag* [ **level-1** | **level-2** ]
   
   
   
   An administrative tag is configured for the interface in the IS-IS topology instance.
   
   
   
   An administrative tag is carried in routes and used by route-policies to filter routes.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.