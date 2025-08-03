(Optional) Requesting the DHCP Server to Release the Client IP Address
======================================================================

The DHCP relay agent can request the DHCP server for releasing the IP address assigned to the client.

#### Context

When a DHCP client does not need an IP address or a user needs to be logged out, run the [**dhcp relay release**](cmdqueryname=dhcp+relay+release) command on the DHCP relay agent to send a Release message to the DHCP server. After the DHCP server receives the Release message, the server releases the specified IP address.

Perform the following steps on the Router that functions as a DHCP relay agent:


#### Procedure

* In the system view, configure the DHCP relay agent to request all DHCP servers to release a DHCP client IP address.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**dhcp relay release**](cmdqueryname=dhcp+relay+release) *client-ip-address* *mac-address*
     
     
     
     The DHCP relay agent is configured to request DHCP servers to release the client IP address.
* In the system view, configure the DHCP relay agent to request a specified DHCP server to release a DHCP client IP address.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**dhcp relay release**](cmdqueryname=dhcp+relay+release) *client-ip-address* *mac-address* [ *server-ip-address* ]
     
     
     
     The DHCP relay agent is configured to request the specified DHCP server to release the client IP address.
* In the interface view, configure the DHCP relay agent to request a specified DHCP server to release a DHCP client IP address.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**dhcp relay release**](cmdqueryname=dhcp+relay+release) *client-ip-address* *mac-address* [ *server-ip-address* ]
     
     
     
     The DHCP relay agent is configured to request the DHCP server connected to the interface to release the client IP address.