Understanding HTTPS
===================

Understanding HTTPS

#### HTTP Message Format

HTTP is a request/response protocol and therefore involves request and response messages.

**Request message**

An HTTP client sends a request message to an HTTP server. This request message consists of three parts: request line, request header, and request body, as shown in [Figure 1](#EN-US_CONCEPT_0000001513159906__fig1527916543403).**Figure 1** Request format  
![](figure/en-us_image_0000001564120001.png)

**Table 1** Request fields
| Field | Description |
| --- | --- |
| Method | HTTP method, performed on the resource identified by the request URI. It includes the following methods: GET, HEAD, PUT, POST, TRACE, OPTIONS, DELETE, and extension-method. |
| URI | URL. |
| HTTP/Version-number | HTTP version. |
| Header-Name-n:value | Header field name: value. |
| Optional request body | (Optional) Request body. |


**Response message**

After receiving and interpreting a request message from an HTTP client, an HTTP server responds with a response message, which consists of three parts: response line, response header, and response body, as shown in [Figure 2](#EN-US_CONCEPT_0000001513159906__fig20271143716416).**Figure 2** Response format  
![](figure/en-us_image_0000001512840362.png)

**Table 2** Response fields
| Field | Description |
| --- | --- |
| HTTP/Version-number | HTTP version. |
| Status code | HTTP status code.  A status code is a 3-digit integer result code of the attempt to understand and satisfy the request. Status codes 200 to 299 indicate success, 300 to 399 resource redirection, 400 to 499 client request errors, and 500 to 599 server errors. |
| Message | HTTP status message. |
| Header-Name-n:value | Header field name: value. |
| Optional response body | (Optional) Response body. |




#### HTTP Communication Process

[Figure 3](#EN-US_CONCEPT_0000001513159906__fig1157219502582) shows the HTTP-based information exchange process in a client-server model. The process consists of four steps: establishing a connection, sending a request, sending a response, and closing the connection.

**Figure 3** HTTP communication process  
![](figure/en-us_image_0000001563760265.png)

1. An HTTP client initiates a connection request to an HTTP server.
2. After the connection is established, the HTTP client sends a request message to the HTTP server.
3. After receiving the request message, the HTTP server sends a response message to the HTTP client.
4. After receiving the response message, the HTTP client sends a request for closing the connection.

#### HTTP Using SSL

HTTP does not have any security mechanism. It transmits data in clear text and does not authenticate either communication party. Therefore, data transmitted over such a protocol is vulnerable to tampering, sacrificing transmission security. The SSL protocol uses data encryption, identity authentication, and message integrity check to ensure the security of TCP-based application layer protocols. HTTPS uses SSL to ensure HTTP security and can be understood as simply HTTP plus SSL. The URL of a secure connection starts with https:// instead of http://.

When SSL is used for data transmission, the HTTP client initiates a connection to an appropriate port of the HTTP server, and sends a ClientHello message to start the SSL handshake. After the SSL handshake is complete, the HTTP client initializes the first HTTP request. All HTTP data must be sent as SSL application data.

Certificates are required for HTTPS connections. Before applying for a certificate, you need to understand the following concepts:

**Digital certificate**

A digital certificate is issued by a certificate authority (CA) to certify the ownership of a public key by the named subject of the certificate. (A certificate applicant becomes the certificate subject after obtaining the certificate.) A digital certificate includes the subject name, public key, digital signature of the CA, and the certificate's validity period; it authenticates both communication parties for more reliable communication.

The device supports certificates in PEM, ASN1, and PFX formats. Certificates have the same content regardless of format.

* The PEM (.pem) digital certificate is common. It is used for text transmission between systems.
* The ASN1 (.der) format is a universal digital certificate format. It is the default format for most browsers.
* The PFX (.pfx) format is a universal digital certificate format. It is a binary format that can be converted into PEM or ASN1 format.

**CA**

A CA is an entity that issues, manages, and revokes digital certificates. It validates the identities of digital certificate holders, issues digital certificates (that is signing digital certificates to prevent certificates from being forged or tampered with), and manages certificates and cryptographic keys. The globally trusted CA is called a root CA, and can authorize other CAs as subordinate CAs. The CA identity is described in a trusted CA file.

For example, CA1 functions as the root CA and issues a certificate for CA2. CA2 then issues a certificate for CA3 and so on, until CAn issues the final server certificate.

If CA3 issues the server certificate, then authentication on the client starts from server certificate authentication. The CA3 certificate is used to authenticate the server certificate. If authentication succeeds, the CA2 certificate is used to authenticate the CA3 certificate. Finally, the CA1 certificate is used to authenticate the CA2 certificate. Server certificate authentication succeeds only when the CA2 certificate has been authenticated by the CA1 certificate.

**Certificate revocation list (CRL)**

A CRL is a list of digital certificates that have been revoked by the issuing CA before their scheduled expiration date and should no longer be trusted.

If a CA revokes a digital certificate, the declaration on authorized key pairs is revoked before the certificate expires. After a certificate in a CRL expires, the certificate is deleted in order to shorten the CRL.