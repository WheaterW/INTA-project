(Optional) Configuring a BAS Interface to Send RIP Routes
=========================================================

(Optional) Configuring a BAS Interface to Send RIP Routes

#### Context

When users of different services belong to different VLANs and the users want to access corresponding network-side servers, the user-side device cannot determine the interfaces from which users' server access request packets are to be sent. To resolve this problem, the user-side device is configured to learn routing information of the servers through RIP to guide packet forwarding on the outbound interface. In BRAS scenarios, no IP address is configured for a BAS interface by default, and RIP packets cannot be advertised through the BAS interface. As such, the BAS interface needs to generate an interface IP address through address borrowing so that this address is used as the source IP address of RIP packets.


#### Pre-configuration Tasks

Before configuring this function, complete the following tasks:

* Ensure that RIP routes can be normally advertised between devices.
* Configure loopback addresses.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [*. subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   The BAS interface view is displayed.
4. Run [**rip over ipoe**](cmdqueryname=rip+over+ipoe)
   
   
   
   RIP is enabled for IPoE users.
   
   
   
   After this command is run on a BAS interface, if the [**ip address unnumbered**](cmdqueryname=ip+address+unnumbered) command is not run on the BAS interface to borrow an IP address, the protocol status of the BAS interface cannot go up, and IPoE users cannot go online.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the interface view.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run **[**ip pool**](cmdqueryname=ip+pool)** **ip-pool-name** ****bas********remote****
   
   
   
   The remote address pool view is displayed.
8. Run [**gateway unnumbered interface**](cmdqueryname=gateway+unnumbered+interface) **LoopBack** *ifNum* [**mask**](cmdqueryname=mask) { *mask-length* | *mask-network* }
   
   
   
   The remote address pool is configured to borrow the gateway IP address and mask of a loopback interface.
   
   
   
   The interface whose IP address is borrowed can only be a loopback interface, and the IP address of an interface can be borrowed only when its mask is 32 bits.
   
   The mask length or mask configured using this command must be the same as that configured using the [**gateway**](cmdqueryname=gateway) command. Running this command will override the configuration of the [**gateway**](cmdqueryname=gateway) command.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.