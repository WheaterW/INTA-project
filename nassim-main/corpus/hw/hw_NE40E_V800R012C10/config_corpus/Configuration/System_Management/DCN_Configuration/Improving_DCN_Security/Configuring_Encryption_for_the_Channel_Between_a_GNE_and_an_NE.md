Configuring Encryption for the Channel Between a GNE and an NE
==============================================================

To prevent malicious attacks and improve security, configure encryption for the channel between the specified GNE and NE.

#### Context

If the DCN channel between a GNE and an NE is not encrypted, the channel is prone to attacks. To improve security, configure encryption for the channel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dcn**](cmdqueryname=dcn)
   
   
   
   The DCN view is displayed.
3. Run [**dcn encrypt**](cmdqueryname=dcn+encrypt) **neid** *neid* **authkey** *auth-key* [**dh-algorithm**](cmdqueryname=dh-algorithm) { **dh1024** | **dh2048** } \*
   
   
   
   Encryption is configured for the channel to the NE with a specified NEID.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   
   For security purposes, you are advised to specify the ciphertext mode. In addition, change the password periodically.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring channel encryption, check the configurations.

Run the [**display dcn encrypt channel**](cmdqueryname=display+dcn+encrypt+channel) [ **neid** *neid* ] command to check the status of the encrypted channel.