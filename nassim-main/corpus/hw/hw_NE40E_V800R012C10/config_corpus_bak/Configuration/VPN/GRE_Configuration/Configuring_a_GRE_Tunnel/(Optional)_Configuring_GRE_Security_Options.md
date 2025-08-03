(Optional) Configuring GRE Security Options
===========================================

Configuring GRE security options can improve GRE tunnel security.

#### Context

To enhance the security of a GRE tunnel, configure E2E check or key authentication on the endpoint devices of the tunnel. This security mechanism prevents the tunnel interfaces of both devices from incorrectly identifying and receiving packets from other devices.

Perform the following steps on the endpoint Routers of a tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   The tunnel interface view is displayed.
3. Run [**gre key**](cmdqueryname=gre+key) { **simple** *key-number-simple* | [ **cipher** ] *key-number-cipher* }
   
   
   
   The GRE key of the tunnel interface is set.
   
   
   
   If keys are set for the tunnel interfaces on the two ends of the tunnel, ensure that the keys are the same. Alternatively, you may choose not to set keys for the tunnel interfaces on both ends of the tunnel.
   * **simple** *key-number-simple*: specifies a cleartext key (an integer).
   * *key-number-cipher*: specifies a cleartext key (an integer) or a ciphertext key.
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When configuring a key, you are advised to use the ciphertext mode. The key is saved in configuration scripts in cleartext if you select the cleartext mode, which poses a high security risk. To ensure device security, change the key on a regular basis.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.