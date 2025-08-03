Creating an OSPF Virtual Link
=============================

Creating an OSPF Virtual Link

#### Prerequisites

Before creating an OSPF virtual link, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Enter the OSPF area view.
   
   
   ```
   [area](cmdqueryname=area) area-id
   ```
4. Create and configure a virtual link.
   
   
   ```
   [vlink-peer](cmdqueryname=vlink-peer) router-id [ dead dead-interval | hello hello-interval | retransmit retransmit-interval | trans-delay trans-delay-interval | [ simple [ [ plain ] plain-text | cipher cipher-text ] | { md5 | hmac-md5 | hmac-sha256 } [ key-id { plain plain-text | [ cipher ] cipher-text } ] | authentication-null | keychain keychain-name ] | smart-discover ]  *
   ```
   
   
   
   The virtual link must also be configured on the neighbor.
   
   The default parameter values are recommended when a virtual link is configured; however, you can modify the parameter values as needed. Suggested parameter configurations are as follows:
   
   * Set a proper [**hello**](cmdqueryname=hello) *hello-interval* value based on actual network conditions. The smaller the value, the faster the device detects network topology changes, but the more network resources are consumed.
   * If [**retransmit**](cmdqueryname=retransmit) *retransmit-interval* is set to too small a value, unnecessary LSA retransmission may occur. Therefore, setting the parameter to a large value is recommended on a low-speed network.
   * The authentication modes of a virtual link and the backbone area must be the same.
   * As the MD5 algorithm is insecure, you are advised to use a more secure authentication mode.
   * It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```