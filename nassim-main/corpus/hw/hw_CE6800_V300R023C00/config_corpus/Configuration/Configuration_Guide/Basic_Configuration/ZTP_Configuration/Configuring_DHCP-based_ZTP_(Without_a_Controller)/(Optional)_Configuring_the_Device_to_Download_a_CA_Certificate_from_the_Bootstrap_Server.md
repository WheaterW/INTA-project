(Optional) Configuring the Device to Download a CA Certificate from the Bootstrap Server
========================================================================================

(Optional) Configuring the Device to Download a CA Certificate from the Bootstrap Server

#### Prerequisites

The device has been deployed.


#### Context

In the scenario where no initial certificate is available on iMaster NCE-Fabric, if the device needs to be managed by the controller, you need to import the CA certificate trusted by the controller to the device.

The bootstrap server stores the CA certificate trusted by the controller. Currently, iMaster NCE-Fabric integrates the function of the bootstrap server. The device needs to download the CA certificate **NCE-bootstrap.pem** from the bootstrap server and import the certificate to the **default** domain.

A maximum of 10 bootstrap servers can be configured for the device. The bootstrap servers with the same IP address and VPN instance name are considered as one bootstrap server. The interaction process between the device and bootstrap server is as follows:

1. The device proactively establishes an HTTPS connection with a bootstrap server.
2. The device sends a request packet to the bootstrap server to download a CA certificate. The request packet carries the device ESN or the IP address of the bootstrap server.
3. The bootstrap server searches for the CA certificate based on the ESN or IP address in the request packet and sends a response packet carrying the CA certificate to the device. The response packet also carries the device ESN or the IP address of the bootstrap server.
4. After receiving the response packet from the bootstrap server, the device terminates the HTTPS connection with the bootstrap server, parses the response packet, and verifies the validity of the certificate. If the verification fails, the device cannot obtain the CA certificate. In this case, the device attempts to obtain the CA certificate from the next bootstrap server. The device will keep doing so until it successfully obtains a CA certificate.

After successfully obtaining the CA certificate **NCE-bootstrap.pem** from the bootstrap server, the device automatically imports the certificate to the default domain.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an SSL policy and bind it to the default domain.
   
   
   ```
   [ssl policy](cmdqueryname=ssl+policy) policy-name
   [pki-domain](cmdqueryname=pki-domain) default
   [quit](cmdqueryname=quit)
   ```
3. Configure the device to download a CA certificate from the bootstrap server. 
   
   
   ```
   [ztp certificate-remote](cmdqueryname=ztp+certificate-remote) { ipv4-addr | ipv6 ipv6-addr } [ vpn-instance vpnvalue ] port portvalue ssl-policy policyname [ verify-type esn ]
   ```
   
   By default, the device is not configured to download a CA certificate from the bootstrap server.
   
   When the **verify-type esn** parameter is specified, a certificate is authenticated based on the device ESN. That is, the request packet sent by the device to the bootstrap server for downloading the CA certificate carries the device ESN. When parsing the response packet from the bootstrap server, the device uses the ESN for verification.
   
   When the **verify-type esn** parameter is not specified, a certificate is authenticated based on the IP address of the bootstrap server. That is, the request packet sent by the device to the bootstrap server for downloading the CA certificate carries the IP address of the bootstrap server. When parsing the response packet from the bootstrap server, the device uses the IP address for verification.
   
   After **NCE-bootstrap.pem** is imported to the **default** domain, if another CA certificate needs to be downloaded from the bootstrap server, delete the original certificate from the **default** domain and run the [**ztp certificate-remote**](cmdqueryname=ztp+certificate-remote) command again.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```