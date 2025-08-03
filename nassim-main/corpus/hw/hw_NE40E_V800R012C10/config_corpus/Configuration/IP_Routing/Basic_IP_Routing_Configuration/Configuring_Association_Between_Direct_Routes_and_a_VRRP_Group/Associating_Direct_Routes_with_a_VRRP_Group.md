Associating Direct Routes with a VRRP Group
===========================================

Associating direct routes with a VRRP group on a VRRP-enabled interface or a Loopback interface allows the interface to modify the cost of each direct route to the virtual IP network segment based on the VRRP status.

#### Context

If the master device in a VRRP group fails, a master/backup switchover is performed. After the master device recovers, the direct routes of the master device immediately become available. The VRRP group performs a VRRP switchback, which takes some time. To ensure that user-to-network traffic and network-to-user traffic travel along the same path in this period, associate direct routes with the VRRP group on both the master and backup devices. In this manner, the VRRP status affects the cost of the direct route to the virtual IP network segment of the VRRP group.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-name*
   
   
   
   The interface view is displayed.
   
   
   
   VRRP must have been configured on this interface.
3. Configure the association between direct routes with the VRRP group status.
   
   
   * Configure the association between IPv4 direct routes with the VRRP4 group status.
     
     + On non-loopback interfaces:
       
       Run the [**direct-route track vrrp**](cmdqueryname=direct-route+track+vrrp) **vrid** *virtual-router-id* **degrade-cost** *cost-value* command.
     + On loopback interfaces:
       
       Run the [**direct-route track vrrp interface**](cmdqueryname=direct-route+track+vrrp+interface) *interface-type* *interface-number* **vrid** *virtual-router-id* **degrade-cost** *cost-value* command.
   * To configure association between IPv6 direct routes with the VRRP6 group status, run the [**direct-route ipv6 track vrrp6**](cmdqueryname=direct-route+ipv6+track+vrrp6) **vrid** *virtual-router-id* **degrade-cost** *cost-value* command.
   
   
   
   After the command is run, the cost of direct routes is adjusted based on the VRRP group status, with details as follows:
   
   * If the VRRP group status is Master, 0 (the highest priority) is used as the cost of the direct routes.
   * If the VRRP group status is Backup or Initialize, the *cost-value* (greater than 0) specified in the command is used as the cost of the direct routes.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.