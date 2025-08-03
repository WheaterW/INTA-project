(Optional) Configuring MLD
==========================

If multicast listener discovery (MLD) is enabled on a multicast device's interface connecting to a user network segment, multicast group members on the local network can be managed. According to the service plan, you can enable MLD on a user-side public network CE connected to a receiver PE or directly on a receiver PE. Perform this task for the latter case.

#### Context

In the TCP/IP protocol suite, MLD can be used to manage IPv6 multicast group members. It sets up and maintains multicast group memberships between IP hosts and their directly neighboring multicast routers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   
   
   The interface specified in *interface-type* *interface-number* must be the interface connected to a host.
3. Run [**pim ipv6 sm**](cmdqueryname=pim+ipv6+sm)
   
   
   
   IPv6 PIM-SM is enabled.
4. Run [**mld enable**](cmdqueryname=mld+enable)
   
   
   
   MLD is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.