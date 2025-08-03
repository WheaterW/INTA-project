Configuring an Authentication Mode for a Multi-Area Adjacency Interface
=======================================================================

Configuring an authentication mode for a multi-area adjacency interface improves OSPF network security.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The OSPF interface view is displayed.
3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
   
   
   
   OSPF is enabled on the interface.
4. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
   
   
   
   OSPF is enabled on the multi-area adjacency interface.
5. Configure an interface authentication mode as required.
   
   
   * Run the [**ospf authentication-mode**](cmdqueryname=ospf+authentication-mode) **simple** [ **plain** *plain-text* | [ **cipher** ] *cipher-text* ] **multi-area** *area-id* command to configure simple authentication for the multi-area adjacency interface.
   * Run the [**ospf authentication-mode**](cmdqueryname=ospf+authentication-mode) { **md5** | **hmac-md5** | **hmac-sha256** } [ *key-id* { **plain** *plain-text* | [ **cipher** ] *cipher-text* } ] **multi-area** *area-id* command to configure ciphertext authentication for the multi-area adjacency interface.
   * Run the [**ospf authentication-mode**](cmdqueryname=ospf+authentication-mode) **keychain** *keychain-name* **multi-area** *area-id* command to configure keychain authentication for the multi-area adjacency interface.
   * Run the [**ospf authentication-mode**](cmdqueryname=ospf+authentication-mode) **null** **multi-area** *area-id* command to configure null authentication for the multi-area adjacency interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.