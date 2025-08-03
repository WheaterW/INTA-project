Digital Certificate
===================

A digital signature cannot determine whether a public key belongs to a specific owner, as any entity can generate public and private keys. Therefore, a secure and reliable carrier is required to exchange public keys. This carrier is a digital certificate.

A digital certificate is a digitally signed file issued by a CA, containing the owner's public key and identity information.

A digital certificate, which is similar to an electronic copy of a passport or an ID card, is typically used for identity verification on the network. It ensures that one public key is possessed by only one owner.

#### Digital Certificate Structure

A simplest digital certificate contains mandatory information such as public key, name, and digital signature of the CA. In most cases, the certificate also includes information such as the public key validity period, issuer name (CA), and certificate serial number. The certificate structure complies with X.509 v3. [Figure 1](#EN-US_CONCEPT_0000001512846454__fig_dc_fd_pki_000701) shows the typical structure of a digital certificate.

**Figure 1** Digital certificate structure diagram  
![](figure/en-us_image_0000001564006281.png)

The meaning of each field in the digital certificate is as follows:

* Version: version of X.509. Generally, the v3 (0x2) is used.
* Serial Number: a positive and unique integer assigned by the issuer to the certificate. Each certificate is uniquely identified by the issuer name and the serial number.
* Signature Algorithm: signature algorithm used by the issuer to sign the certificate.
* Issuer: name of the device that has issued a certificate. It must be the same as the subject name in the digital certificate. Generally, the issuer name is the CA server's name.
* Validity: time interval during which a digital certificate is valid, including the start and end dates. The expired certificates are invalid.
* Subject: name of the entity that possesses a digital certificate. In a self-signed certificate, the issuer name is the same as the subject name.
* Subject Public Key Info: public key and the algorithm with which the key is generated.
* Extensions: a sequence of optional fields such as certificate usage, CRL address (URL), and OCSP server URL.
* Signature: signature signed on a digital certificate by the issuer using the private key.

The process of generating a certificate signature is as follows: The CA first uses a cryptographic hash algorithm to generate digest information of the certificate, and then uses a public-key cryptography algorithm and a private key of the CA to encrypt the digest information and finally generate a signature. These operations are performed on the CA before the certificate is issued.


#### Digital Certificate Types

There are three types of certificates, as described in [Table 1](#EN-US_CONCEPT_0000001512846454__table_dc_fd_pki_000702).

**Table 1** Certificate types
| Type | Description | Description |
| --- | --- | --- |
| CA certificate | CA's own certificate. If a PKI system does not have a hierarchical CA structure, the CA certificate is the self-signed certificate. If a PKI system has a hierarchical CA structure, the top CA is the root CA, which owns a self-signed certificate. | An applicant trusts a CA by verifying its digital signature. Any applicant can obtain the CA's certificate (including the public key) to verify the local certificate issued by the CA. |
| Local certificate | A certificate issued by a CA to the applicant. | - |
| Self-signed certificate | * A self-signed certificate is issued by a device to itself and is signed by the initial CA on the device. That is, the certificate issuer is the same as the certificate subject. This type of certificate contains signature information, and it does not require signature application. * An unsigned certificate, as its name implies, is not signed. It is issued by a device to itself. A signature needs to be obtained from the CA, and the certificate issuer is the CA. | A device can generate a self-signed or unsigned certificate for itself, which is a simple certificate issuing function.  The device does not support lifecycle management (such as certificate update and revocation) of its self-signed certificate. To ensure security of the device and certificate, you are advised to replace the self-signed certificate with a local certificate. |



#### Certificate Formats

Three certificate formats are supported, as described in [Table 2](#EN-US_CONCEPT_0000001512846454__table_dc_fd_pki_000703).

**Table 2** Certificate formats
| Format | Description | Description |
| --- | --- | --- |
| PKCS#12 | Saves certificate files in binary format, including or excluding the private key. Commonly used file name extensions include .P12 and .PFX. | If the file name extension of a certificate is .CER or .CRT, use Notepad to open this certificate and check its content to differentiate the certificate format.   * If the certificate starts with "-----BEGIN CERTIFICATE-----" and ends with "-----END CERTIFICATE-----", the certificate format is PEM. * If the certificate content is displayed as garbled characters, the certificate format is DER. |
| DER | Saves certificate files in binary format, excluding the private key. Commonly used file name extensions include .DER, .CER, and .CRT. |
| PEM | Saves certificate files in ASCII format, including or excluding the private key. Commonly used file name extensions include .PEM, .CER, and .CRT. |