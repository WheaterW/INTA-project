Configuring an SA Cache
=======================

An SA cache is used to locally save (S, G) information carried in the Source Active (SA) messages. If a Router needs to receive multicast data, it directly obtains useful (S, G) information from the SA cache. Setting the maximum number of (S, G) entries in an SA cache can prevent Deny of Service (DoS) attacks. You are allowed to disable the SA cache function on the NE40E.

#### Context

By default, the SA cache function is enabled on the Router configured with an MSDP peer.


#### Procedure

* Set the maximum number of (S, G) entries in an SA cache.
  
  
  
  To prevent DoS attacks, performing this configuration on all MSDP peers is recommended.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The MSDP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *peer-address* **sa-cache-maximum** *sa-limit*
     
     
     
     The maximum number of (S, G) entries in the SA cache is set.
     
     
     
     + *peer-address*: specifies the IP address of a remote MSDP peer.
     + *sa-limit*: specifies the maximum number of (S, G) entries in the SA cache. If the specified maximum number is smaller than the SA cache specification, the specified value takes effect; otherwise, the SA cache specification takes effect.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Disable the SA cache function.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The MSDP view is displayed.
  3. Run [**undo cache-sa-enable**](cmdqueryname=undo+cache-sa-enable)
     
     
     
     The SA cache function is disabled.
     
     
     
     After the SA cache function is disabled, the RP directly forwards the received SA messages to other remote MSDP peers and does not save the (S, G) information carried in the SA messages locally. If the device needs to receive multicast data, it must wait for the SA message sent by the MSDP peer in the next sending period. This may result in a delay in obtaining multicast information.
     
     To enable the SA cache function, run the [**cache-sa-enable**](cmdqueryname=cache-sa-enable) command in the MSDP view.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.