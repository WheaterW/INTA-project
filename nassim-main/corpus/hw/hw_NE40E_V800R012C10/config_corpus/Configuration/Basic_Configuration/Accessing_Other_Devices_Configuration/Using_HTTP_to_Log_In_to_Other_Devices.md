Using HTTP to Log In to Other Devices
=====================================

Hypertext Transfer Protocol (HTTP) is an application-layer protocol that transports hypertext from WWW servers to local browsers. It uses the client/server model in which requests and replies are exchanged.

#### Context

To download a certificate from an HTTP server, use HTTP. HTTP transfers web page information on the Internet.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

HTTP is insecure.



#### Pre-configuration Tasks

Before using HTTP to log in to a device, complete the following tasks:

* Configure an SSL policy for the HTTP server.
* Check that the terminal and device are routable to each other.


#### Procedure

* Configure an SSL policy for the HTTP client.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ssl policy**](cmdqueryname=ssl+policy) *policy-name*
     
     
     
     An SSL policy is configured, and the SSL policy view is displayed.
  3. Run [**certificate load**](cmdqueryname=certificate+load)
     
     
     
     A certificate is loaded for the SSL policy.
     
     A certificate or certificate chain needs to be loaded for the SSL policy on the HTTP client according to the format of the certificate loaded on the HTTP server.
     
     
     
     + Run the [**certificate load**](cmdqueryname=certificate+load) **pem-cert** *certFile* **key-pair** { **dsa** | **rsa** } **key-file** *keyFile* **auth-code** [ **cipher** *authCode* ] command to load a PEM certificate for the SSL policy.
     + Run the [**certificate load**](cmdqueryname=certificate+load) **pfx-cert** *certFile* **key-pair** { **dsa** | **rsa** } **mac** or [**certificate load**](cmdqueryname=certificate+load) **pfx-cert** *certFile* **key-pair** { **dsa** | **rsa** } { **mac** **cipher** *mac-code* | **key-file** *keyFile* } **auth-code** **cipher** *authCode* command to load a PFX certificate for the SSL policy.
     + Run the [**certificate load**](cmdqueryname=certificate+load) **pem-chain** *certFile* **key-pair** { **dsa** | **rsa** } **key-file** *keyFile* **auth-code** [ **cipher** *authCode* ] command to load a PEM certificate chain for the SSL policy.
  4. Run [**trusted-ca load**](cmdqueryname=trusted-ca+load)
     
     
     
     A trusted-CA file is loaded.
     
     A trusted-CA file needs to be loaded for the SSL policy on the HTTP client according to the format of the trusted-CA file loaded on the HTTP server.
     
     
     
     + Run the [**trusted-ca load**](cmdqueryname=trusted-ca+load) **pem-ca** *caFile* command to load a trusted-CA file in PEM format for the SSL policy.
     + Run the [**trusted-ca load**](cmdqueryname=trusted-ca+load) **asn1-ca** *caFile* command to load a trusted-CA file in ASN1 format for the SSL policy.
     + Run the [**trusted-ca load**](cmdqueryname=trusted-ca+load) **pfx-ca** *caFile* **auth-code** [ **cipher** *authCode* ] command to load a trusted-CA file in PFX format for the SSL policy.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
* Configure HTTP to log in to other devices.
  1. Run [**http**](cmdqueryname=http)
     
     
     
     HTTP is enabled, and the HTTP view is displayed.
  2. (Optional) Run [**client source-interface**](cmdqueryname=client+source-interface) { *interface-name* | *interface-type* *interface-number* }
     
     
     
     A source interface is bound to the HTTP client.
  3. (Optional) Run [**client ipv6 source-address**](cmdqueryname=client+ipv6+source-address) *ipv6-address* [ **vpn-instance** *ipv6-vpn-instance-name* ]
     
     
     
     A source IPv6 address and VPN instance are specified for the HTTP client.
  4. Run [**client ssl-policy**](cmdqueryname=client+ssl-policy) *policy-name*
     
     
     
     An SSL policy is configured for the HTTP client.
  5. Run [**client ssl-verify peer**](cmdqueryname=client+ssl-verify+peer)
     
     
     
     The HTTP client is configured to perform SSL verification on the HTTP server.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.