Configuring an Authentication Message for the Private TLV That Supports NMS Automatic NE Management in LLDP Packets
===================================================================================================================

This section describes how to configure an authentication message for the private TLV that supports NMS automatic NE management in LLDP packets.

#### Usage Scenario

When NEs use sub-interfaces numbered 4094 for DCN communication, an NE on which NMS automatic NE management is configured encapsulates an authentication message in the private TLV that supports NMS automatic NE management in an LLDP packet before sending the LLDP packet to a downstream NE. Upon receipt of the LLDP packet, the downstream NE parses the private TLV if the downstream NE supports NMS automatic NE management. If the authentication message carried in the LLDP packet is the same as the one configured locally, NMS automatic NE management takes effect on the downstream NE. If the authentication message carried in the LLDP packet is different from the one configured locally, NMS automatic NE management does not take effect on the downstream NE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**lldp enable-dcn authentication**](cmdqueryname=lldp+enable-dcn+authentication) *authentication-string*
   
   
   
   An authentication message is configured for the private TLV that supports NMS automatic NE management in LLDP packets.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   
   For security purposes, you are advised to configure a ciphertext password and change the password periodically.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.