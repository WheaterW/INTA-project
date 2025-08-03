Enabling IPv6 IS-IS Optional Checksum
=====================================

Enabling IPv6 IS-IS Optional Checksum

#### Prerequisites

Before enabling the IPv6 IS-IS optional checksum function, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

If IPv6 IS-IS routing devices are attacked with malicious packets or IPv6 IS-IS packets are tampered with, important network information may be illegally obtained, potentially leading to a great loss. To prevent this problem, enable the IPv6 IS-IS optional checksum function. This function enables IPv6 IS-IS routing devices to encapsulate the optional checksum TLV in the CSNPs, PSNPs, and IIHs to be sent and check the TLV carried in received packets. If the TLV is incorrect, the packets are discarded, ensuring network security.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) process-id
   ```
3. Enable the optional checksum function for the IS-IS process.
   
   
   ```
   [optional-checksum enable](cmdqueryname=optional-checksum+enable)
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If MD5 authentication or keychain authentication with the valid MD5 algorithm is configured for IS-IS interfaces or an area, IS-IS devices do not encapsulate the checksum TLV in the IIHs and SNPs to be sent. Instead, these devices check the TLV in received packets.
   
   The simple or MD5 algorithm is not recommended if high security is required. To prevent routing information from being tampered with, you are advised to enable authentication and use the keychain or HMAC-SHA256 algorithm to improve security.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) **verbose** command to check detailed IS-IS LSDB information.