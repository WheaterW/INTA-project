(Optional) Configuring SIP Services for the DHCPv4 Client
=========================================================

You can configure SIP services for the DHCPv4 client on a DHCPv4 server to implement multimedia communication, such as multimedia conferencing, Internet calls, distance education, and distance medical treatment.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip pool**](cmdqueryname=ip+pool) *pool-name* [ **bas** **local** | **server** ]
   
   
   
   An address pool is created, and the address pool view is displayed.
3. Run [**sip-server**](cmdqueryname=sip-server) { { **ip-address** **ip-address1**[ ****ip-address**** **ip-address2**] } | { ****list*****server-name1* [ ****list**** **server-name2** ] } }
   
   
   
   The IP address or name of the SIP server is specified.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.