(Optional) Creating OSPF Virtual Links
======================================

This section describes how to create logical links between backbone areas and to ensure the OSPF network connectivity.

#### Context

After OSPF areas are deployed, OSPF route updates between non-backbone areas are transmitted through the backbone area. Therefore, OSPF requires that all non-backbone areas be connected to a backbone area and backbone areas be connected as well. However, these requirements may not be met due to various limitations. OSPF virtual links can be configured to solve the problem.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**area**](cmdqueryname=area) *area-id*
   
   
   
   The OSPF area view is displayed.
4. Run [**vlink-peer**](cmdqueryname=vlink-peer) *router-id* [ **dead** *dead-interval* | **hello** *hello-interval* | **retransmit** *retransmit-interval* | **trans-delay** *trans-delay-interval* | **smart-discover** | [ **simple** [ **plain** *plain-text* | [ **cipher** ] *cipher-text* ] | { **md5** | **hmac-md5** | **hmac-sha256** } [ *key-id* { **plain** *plain-text* | [ **cipher** ] *cipher-text* } ] | **authentication-null** | **keychain** *keychain-name* ] ]  \*
   
   
   
   A virtual link is created.
   
   
   
   You also need to run this command on the other end of the virtual link.
   
   The default parameter values are recommended when a virtual link is configured. You can change the parameter values as required. Suggested parameter configurations are as follows:
   * The smaller the **hello** value, the faster the router detects network topology changes, and the more network resources are consumed.
   * If the **retransmit** parameter is set to a small value, unnecessary LSA retransmission occurs. Therefore, you are advised to set the parameter to a large value on a low-speed network.
   * The authentication mode of a virtual link must be the same as that of the backbone area.
   * It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.