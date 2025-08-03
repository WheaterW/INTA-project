Configuring an SSL Policy (Loading a Certificate Using PKI)
===========================================================

Configuring an SSL Policy (Loading a Certificate Using PKI)

#### Prerequisites

A certificate has been loaded to the PKI realm to be bound. The loaded certificate can be an initial device certificate or a digital certificate applied by a user. For details on how to load a certificate using PKI, see Configuration Guide > PKI Configuration.


#### Context

SSL uses data encryption, identity authentication, and message integrity check mechanisms to ensure security of TCP-based application layer protocols. An SSL policy can be applied to application layer protocols to provide secure connections.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an SSL policy and enter the SSL policy view.
   
   
   ```
   [ssl policy](cmdqueryname=ssl+policy) policy-name
   ```
   
   By default, no SSL policy is configured.
3. (Optional) Set the elliptic curve parameter for the ECDHE algorithm.
   
   
   ```
   [ecdh group](cmdqueryname=ecdh+group) { nist | curve | brainpool } *
   ```
   
   By default, the elliptic curve parameters of the ECDHE algorithm are Curve and Brainpool.
4. (Optional) Configure a minimum SSL version for the SSL policy.
   
   
   ```
   [ssl minimum version](cmdqueryname=ssl+minimum+version) { tls1.1 | tls1.2 | tls1.3 }
   ```
   
   By default, the minimum version used by an SSL policy is TLS1.2.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * SSL policies support three SSL versions: TLS1.1, TLS1.2, and TLS1.3. TLS1.3 ensures the highest security, followed by TLS1.2 and TLS1.1. TLS1.2 and TLS1.3 are recommended.
   * The **tls1.1** parameter in this command can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.
5. Bind a PKI realm to the SSL policy. After a PKI realm is bound, the SSL policy uses the certificates and CRLs in the PKI realm.
   
   
   ```
   [pki-domain](cmdqueryname=pki-domain) pki-domain
   ```
6. (Optional) Bind a cipher suite to the SSL policy.
   
   
   ```
   [binding cipher-suite-customization](cmdqueryname=binding+cipher-suite-customization) customization-name
   ```
   
   By default, no cipher suite is bound to an SSL policy. In this case, all encryption algorithms can be used.
   
   The cipher suite to be bound to the SSL policy must have been configured. For details, see [(Optional) Configuring a Cipher Suite for an SSL Policy](galaxy_ssl_cfg_0010.html).
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```