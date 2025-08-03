Configuring the Multicast Forwarding Boundary
=============================================

When an interface of a multicast device is configured with a forwarding boundary for a specified group, the forwarding scope of multicast packets is restricted.

#### Context

By default, no multicast forwarding boundary is configured on an interface.

Perform the following steps on the multicast Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**multicast boundary**](cmdqueryname=multicast+boundary) *group-address* { *mask* | *mask-length* }
   
   
   
   The multicast forwarding boundary is configured.

#### Checking the Configurations

Run the [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **boundary** [ *group-address* [ *mask* | *mask-length* ] ] [ **interface** *interface-type interface-number* ] command to check information about the multicast boundary configured on an interface.