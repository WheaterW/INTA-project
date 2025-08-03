(Optional) Configuring an LSR ID for a Local LDP Session
========================================================

To isolate services, configure an LSR ID for each local LDP session.

#### Context

By default, all LDP sessions of an LSR, including local LDP sessions and remote LDP sessions, use the LSR ID of the LDP instance configured on the LSR. However, if LDP LSPs carry L2VPN and L3VPN services, sharing one LSR ID may cause LDP LSPs to fail to isolate VPN services. To address this problem, you can configure an LSR ID for each LDP session.

This section describes how to configure an LSR ID for a local LDP session.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface on which an LDP session is to be established is displayed.
3. Run [**mpls ldp local-lsr-id**](cmdqueryname=mpls+ldp+local-lsr-id+interface) { *interface-type* *interface-number* | **interface** }
   
   
   
   The primary IP address of a specified interface is used as the LSR ID for the current LDP session.
   
   
   
   Here:
   
   * *interface-type* *interface-number*: sets the primary IP address of a specified interface as the LSR ID.
   * **interface**: sets the primary IP address of the current interface as the LSR ID.
   
   If multiple links directly connect an LSR pair, the LSR ID configured on the interface of each link must be the same. Otherwise, the LDP session uses the LSR ID of the link that first finds the adjacency, while other links with different LSR IDs cannot be bound to the LDP session. As a result, LDP LSPs fail to be established on these links.
   
   If both a local session and a remote LDP session are to be established between an LSR pair, LSR IDs configured for the two sessions must be the same. Otherwise, only the LDP session that finds the adjacency first can be established.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To establish an LDP session between two devices, a TCP link must be established between them. This link is called an adjacency. After the adjacency is established, the two devices can exchange LDP control messages to establish an LDP session. If there is only one adjacency in an LDP session, the LDP session is called a single-link session. If there are multiple adjacencies in an LDP session, the LDP session is called a multi-link session.
   
   Running this command causes a single-link LDP session to reset or causes the current adjacency of a multi-link LDP session to reset.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.