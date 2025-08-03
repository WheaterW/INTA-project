Associating a Service-Location Group with a VRRP Group
======================================================

In the interface view, configure association between a service-location group and VRRP.

#### Context

Configuring association between a service-location group and VRRP allows a VRRP group to track the service-location group status in real time so that the involved device can determine whether to perform a master/slave switchover. Perform the following operations on both the master and backup devices.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* [**track**](cmdqueryname=track) **service-location** *service-location-id* [ **reduced** *value-reduced* ]
   
   
   
   The service-location group is associated with the VRRP group.
   
   
   
   The *virtual-router-id* and *service-location-id* values configured on the master and backup devices must be the same.
   
   A VRRP group is associated with a service location (multi-core CPU) on a VSU board. All NAT instances that use the service location use the associated VRRP group. Generally, only one NAT instance is configured at each service location. Therefore, the NAT instance and VRRP group are in one-to-one relationship. In special cases, however, multiple NAT instances can use the same service location and VRRP group. In this case, you need to configure a VRRP group for each service location and configure a VLAN for each VRRP group.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In distributed inter-chassis hot backup scenarios, service-location groups also need to be associated with user-side VRRP. Otherwise, if a CGN board fails, a master/backup BRAS switchover cannot be performed. As a result, new distributed uses cannot go online.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.