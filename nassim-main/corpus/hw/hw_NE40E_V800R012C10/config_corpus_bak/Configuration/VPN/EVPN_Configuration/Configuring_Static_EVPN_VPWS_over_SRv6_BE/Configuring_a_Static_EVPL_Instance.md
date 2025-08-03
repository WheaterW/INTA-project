Configuring a Static EVPL Instance
==================================

This section describes how to configure a static EVPL instance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id* **static-mode**
   
   
   
   A static EVPL instance is created, and its view is displayed.
3. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The current EVPL instance is bound to the specified VPWS EVPN instance.
4. Run [**local-service-id**](cmdqueryname=local-service-id) *service-id* [**remote-service-id**](cmdqueryname=remote-service-id) *service-id*
   
   
   
   The current EVPL instance is configured to add the local and remote service IDs to packets.
5. Run [**binding sid**](cmdqueryname=binding+sid) *sid-value* [**peer**](cmdqueryname=peer) *peer-value* [ **color** *color-value* ] [ **secondary** | **bypass** ]
   
   
   
   The remote SID and remote EVPN peer are configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   **sid** *sid-value* specifies the static SRv6 SID configured on the remote end.
   
   [**peer**](cmdqueryname=peer) *peer-value* specifies the peer IPv6 address. Set this parameter to the source address encapsulated into SRv6 packets on the remote end.
   
   **bypass** indicates the bypass VPWS tunnel. If this keyword is configured, the opcode type of the configured remote static SRv6 SID is End.DX2L.
   
   An SRv6 SID is a 128-bit IPv6 address. SRv6 SIDs are expressed in the Locator:Function:Args format. The Function field is also known as the opcode, and different opcodes define different functions.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.