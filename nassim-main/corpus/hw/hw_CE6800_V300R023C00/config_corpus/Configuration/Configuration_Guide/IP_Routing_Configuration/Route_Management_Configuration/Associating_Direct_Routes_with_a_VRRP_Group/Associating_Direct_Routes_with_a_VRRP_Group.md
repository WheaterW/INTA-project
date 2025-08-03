Associating Direct Routes with a VRRP Group
===========================================

Associating Direct Routes with a VRRP Group

#### Prerequisites

Before associating direct routes with a VRRP group, complete the following task:

* Create a VRRP group.

#### Context

If the master device in a VRRP group fails, the VRRP group performs a master/backup switchover. After the master device recovers, the direct route of the master device immediately becomes available. The VRRP group performs a VRRP switchback, which takes some time. To ensure that user-to-network traffic and network-to-user traffic travel along the same path in this period, associate direct routes with the VRRP group on both the master and backup devices. The association allows the VRRP-enabled devices to modify the cost of each direct route destined for the virtual IP network segment based on the VRRP status.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Perform either of the following operations to associate a direct route with a VRRP group.
   
   
   * Associate an IPv4 direct route with a VRRP4 group.
     ```
     [direct-route track vrrp](cmdqueryname=direct-route+track+vrrp) vrid virtual-router-id degrade-cost cost-value
     ```
   * Associate an IPv6 direct route with a VRRP6 group.
     ```
     [ipv6 direct-route track vrrp6](cmdqueryname=ipv6+direct-route+track+vrrp6) vrid virtual-router-id degrade-cost cost-value
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support this command.
   
   
   
   The cost of the direct route destined for the virtual IP network segment of the VRRP group is dynamically adjusted based on the VRRP status.
   
   * If the VRRP status is Master, the cost of the direct route is set to the default value of 0 (the highest priority).
   * If the VRRP status is Backup or Initialize, *cost-value* (greater than 0) specified in the command is used as the cost of the direct route.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```