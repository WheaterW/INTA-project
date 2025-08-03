Configuring SA Request Messages
===============================

Configuring SA Request Messages

#### Context

When the remote MSDP peer has a large SA cache or a new receiver joins the group, you can configure the local RP to send SA Request messages to a specified remote MSDP peer. This allows the receiver to obtain multicast source information faster.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MSDP view.
   
   
   ```
   msdp [ vpn-instance vpn-instance-name ]
   ```
3. Configure the device to send SA Request messages.
   
   
   ```
   [peer](cmdqueryname=peer) peer-address [request-sa-enable](cmdqueryname=request-sa-enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```