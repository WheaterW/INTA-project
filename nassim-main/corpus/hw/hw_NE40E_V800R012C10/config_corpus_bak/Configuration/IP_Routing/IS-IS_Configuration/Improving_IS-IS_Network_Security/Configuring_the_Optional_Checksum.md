Configuring the Optional Checksum
=================================

The optional checksum encapsulates optional checksum Type-Length-Values (TLVs) into SNPs and Hello packets. After an IS-IS device receives the packets, it checks whether the checksum TLVs are correct, which improves network security.

#### Context

The optional checksum encapsulates optional checksum TLVs into the Complete Sequence Numbers Protocol Data Units (CSNPs), Partial Sequence Number Protocol Data Units (PSNPs), and Hello packets sent by IS-IS devices. When the peer device receives the encapsulated packets, it checks whether TLVs carried in the packets are correct. If TLVs are not correct, the peer device discards the packets for network security.


#### Procedure

1. Run system-view
   
   
   
   The system view is displayed.
2. Run isis
   
   
   
   An IS-IS process is created, and the IS-IS view is displayed.
3. Run [**optional-checksum enable**](cmdqueryname=optional-checksum+enable)
   
   
   
   The optional checksum function is enabled for the IS-IS process.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If MD5 authentication or Keychain authentication with valid MD5 authentication is configured on an IS-IS interface or area, IS-IS devices send Hello packets and SNP packets carrying no checksum TLVs and verify the checksum of the received packets.
   
   The MD5 algorithm is not recommended if high security is required. You are advised to enable authentication and use high-security algorithms such as HMAC-SHA256 to improve security.
4. Run commit
   
   
   
   The configuration is committed.