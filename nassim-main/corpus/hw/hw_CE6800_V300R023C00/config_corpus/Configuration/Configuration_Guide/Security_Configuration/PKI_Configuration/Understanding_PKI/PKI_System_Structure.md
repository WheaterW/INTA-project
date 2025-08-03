PKI System Structure
====================

PKI System Structure

#### PKI System Composition

As shown in [Figure 1](#EN-US_CONCEPT_0000001563766365__fig_dc_fd_pki_000801), a PKI system consists of the end entity, certificate authority (CA), registration authority (RA), and certificate/certificate revocation list (CRL) database.

**Figure 1** PKI system composition  
![](figure/en-us_image_0000001563886057.png)

**End entity**

An end entity, or PKI entity, is the end user of PKI products or services. It can be an individual, an organization, a device (for example, a router or firewall), or process running on a computer.

**CA**

A CA is a trusted entity that issues and manages digital certificates. It is an authoritative, trusted, and impartial organization. Generally, a CA is a server.

[Figure 2](#EN-US_CONCEPT_0000001563766365__fig152008552462) shows a hierarchical CA. The CA on the top of the hierarchy is the root CA and the others are subordinate CAs.

**Figure 2** Hierarchical CA  
![](figure/en-us_image_0000001563766413.png)

* The root CA is the first CA (trustpoint) in the PKI system. It issues certificates to subordinate CAs, computers, users, and services. In most certificate-based applications, the root CA can be traced through the certificate chain. The root CA holds a self-signed certificate.
* A subordinate CA can only obtain a certificate from its upper-level CA. The upper-level CA can be the root CA or another subordinate CA authorized by the root CA to issue certificates. The upper-level CA is responsible for issuing and managing certificates of lower-level CAs, and the CAs at the bottom issue certificates to end entities. For example, CA2 and CA3 are subordinate CAs, holding the certificates issued by CA1; CA4, CA5, and CA6 are also subordinate CAs, holding the certificates issued by CA2.

When a PKI entity trusts a CA, the trust is extended along the certificate chain, which is a set of certificates from the end entity's certificate to the root certificate. When a PKI entity in communication receives a certificate to be authenticated, it verifies each issuer along the certificate chain.

Certificate management is the primary function of CAs, and includes issuing, revoking, querying, and archiving certificates, as well as publishing CRLs.

**RA**

An RA enrolls and approves digital certificates. It provides extended applications of certificate issuing and management. The RA processes the certification enrollment and revocation requests from users, verifies user identities, and decides whether to submit certificate issuing or revocation requests to the CA.

While an RA is combined with a CA in most cases, it can also be independent of a CA, sharing the CA's workload and enhancing CA system security.

**Certificate/CRL database**

The certificate/CRL database stores and manages information about certificates and CRLs, and enables information to be queried.

A certificate may need to be revoked for reasons such as entity name changing, private key leaking, or service interruptions. Revoking a certificate is to unbind the public key from the PKI entity identity information. The PKI system uses a CRL to revoke a certificate.

After a certificate is revoked, the CA publishes a CRL to declare that the certificate is invalid and lists the serial numbers of all revoked certificates. The CRL provides a method to verify certificate validity.


#### **Certificate-related Operations**

A PKI manages the entire lifecycle of local certificates, including applying for, issuing, storing, downloading, installing, authenticating, updating, and revoking local certificates.

**Certificate Application**

Certificate application, also known as certificate enrollment, is a process in which a PKI entity introduces itself to a CA, which then issues it a certificate. Generally, a PKI entity generates a pair of public/private keys. The public key and the identity information (included in the certificate enrollment request) of the PKI entity are sent to the CA to generate a local certificate. The private key is stored by the PKI entity and is used to generate a digital signature and decrypt the ciphertext sent by the peer entity. Currently, the device supports offline certificate application and CMPv2-based online certificate application.

**Certificate Issuing**

If an RA is available, the RA verifies the PKI entity's identity information when the PKI entity applies for a local certificate from CA. After the verification, the RA sends the request to CA. The CA generates a local certificate based on the public key and identity information of the PKI entity, and then returns the local certificate information to the RA. If no RA is available, the CA verifies the PKI entity's identity information.

A PKI entity can also issue a self-signed or unsigned certificate to itself, implementing simple certificate issuing.

**Certificate Storage**

After the CA generates a local certificate, the CA or RA distributes the certificate to the certificate/CRL database. Users can download certificates or browse the certificate directory in the database.

**Certificate Download**

A PKI entity downloads an issued certificate in LDAP or out-of-band mode. The certificate can be a local certificate of the PKI entity, a CA/RA certificate, or a local certificate of another PKI entity.

**Certificate Installation**

In order for a downloaded certificate to take effect, it must be installed on the device (specifically imported to the device memory). The certificate can be a local certificate of the PKI entity, a CA/RA certificate, or a local certificate of another PKI entity.

**Certificate Authentication**

Each certificate installed on the local device must be authenticated to ensure validity before it is used. The main point of this is to check the CA signature on the certificate and ensure that the certificate is valid and not revoked.

**Certificate Update**

When a certificate expires or if its private key is leaked, it must be replaced by the PKI entity. You can manually apply for a new certificate or configure CMPv2 to implement automatic certificate update.

**Certificate Revocation**

In scenarios involving a change of user identity, user information, or public key; or due to user service suspension, the user must revoke the digital certificate, that is, unbind the public key from the user's identity information. A CA provides the certificate revocation function. When a PKI entity revokes its certificate in out-of-band mode, the CA stores the certificate in the CRL database or OCSP server.