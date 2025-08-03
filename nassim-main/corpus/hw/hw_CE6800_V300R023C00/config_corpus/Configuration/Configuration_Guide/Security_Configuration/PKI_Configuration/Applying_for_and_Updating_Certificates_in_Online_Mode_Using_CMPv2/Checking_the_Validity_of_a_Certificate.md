Checking the Validity of a Certificate
======================================

Checking the Validity of a Certificate

#### Prerequisites

The CA certificate and local certificate have been installed on the device.


#### Context

Each certificate installed on the local device must be authenticated to ensure validity before it is used. Certificate authentication verifies the issuing time, issuer information, and certificate validity. The main point of this is to check the CA signature on the certificate and ensure that the certificate is valid and not revoked.

To complete certificate authentication, the local device needs the following information: CA certificate, CRL, local certificate and its private key, and certificate authentication configuration.

The local device authenticates a local certificate as follows:

1. Uses the CA certificate's public key to authenticate the CA's signature.
   
   To authenticate a certificate, a PKI entity must obtain the public key of the certificate-issuing CA from the CA's certificate, allowing it to check the CA's signature on the certificate. An upper-level CA authenticates the certificates of lower-level CAs. The authentication is performed along the certificate chain, and terminated at a trustpoint (the root CA holding a self-signed certificate or a subordinate CA trusted by the PKI entity).
   
   PKI entities that share the same root or subordinate CA and possess CA certificates can authenticate certificates of each other (peer certificates).
   
   In short, certificate chain authentication starts at the target certificate (PKI entity's certificate to be authenticated) and ends at a trustpoint. Authentication of a peer certificate chain generally ends at the first trusted certificate or CA.
2. Checks whether the certificate has expired.
3. Checks whether the certificate has been revoked in CRL, OCSP, or None mode.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Check the validity of the CA or local certificate.
   
   
   ```
   [pki validate-certificate](cmdqueryname=pki+validate-certificate) { ca | local } { realm realm-name | filename file-name }
   ```
   
   
   
   The [**pki validate-certificate ca**](cmdqueryname=pki+validate-certificate+ca) command allows you to check the validity of only the root CA certificate, not subordinate CA certificates. When multiple CA certificates are imported on a device, you can use only the [**pki validate-certificate local**](cmdqueryname=pki+validate-certificate+local) command to check the validity of subordinate certificates.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```