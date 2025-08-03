(Optional) Configuring a Bootstrap Server
=========================================

(Optional) Configuring a Bootstrap Server

#### Context

Huawei devices do not provide the bootstrap server capability. Therefore, a third-party bootstrap server needs to be deployed. For details about how to configure the third-party bootstrap server, see the operation guide of the third-party bootstrap server.

Before configuring the bootstrap server, you must obtain the ownership voucher of the device to be deployed by referring to the following process:

* Send the root certificate of the bootstrap server to Huawei technical support engineers.
* Huawei then issues the ownership voucher of the device to be deployed based on the root certificate of the bootstrap server and the ESN of the device.
* Huawei technical support engineers send the ownership voucher to you.

#### Procedure

1. Log in to Huawei [PKI website](https://hwpki.huawei.com/pki/#/home) and download the Huawei level-2 CA certificate of the device to be deployed.
2. Install the Huawei level-2 CA certificate on the bootstrap server.
3. Obtain the ownership voucher issued by Huawei for the ZTP device to be deployed.
4. Install the ownership voucher on the bootstrap server.
5. Configure the bootstrap server.
   
   
   
   For SZTP, you need to create and upload bootstrapping data on the bootstrap server. Bootstrapping data is a set of data obtained by the device from the bootstrap server during SZTP. For details, see [RFC 8572](https://datatracker.ietf.org/doc/html/rfc8572).
   
   The following is an example of the interaction process between the device to be deployed and the bootstrap server:
   
   The device to be deployed requests bootstrapping data:
   
   ```
      POST:/restconf/operations/ietf-sztp-bootstrap-server:get-bootstrapping-data
      Content-Type: application/yang.data+xml
      <input xmlns="urn:ietf:params:xml:ns:yang:ietf-sztp-bootstrap-server">
        <signed-data-preferred/>
      </input>
   ```
   
   The bootstrap server replies with bootstrapping data.
   
   ```
      Content-Type: application/yang.data+xml
      <output xmlns="urn:ietf:params:xml:ns:yang:ietf-sztp-bootstrap-server">
        <conveyed-information>base64encodedvalue==</conveyed-information>
        <owner-certificate>base64encodedvalue==</owner-certificate>
        <ownership-voucher>base64encodedvalue==</ownership-voucher>
      </output>
   ```
   
   Bootstrapping data contains the following parts:
   
   1. Conveyed information: contains the bootstrapping information required by the device to be deployed, that is, redirect information or onboarding information (only one type of the information can be carried).
      
      ietf-sztp-conveyed-info example of the YANG model:
      
      ```
             yang-data conveyed-information:
               +-- (information-type)
                  +--:(redirect-information)
                  |  +-- redirect-information
                  |     +-- bootstrap-server* [address]
                  |        +-- address         inet:host
                  |        +-- port?           inet:port-number
                  |        +-- trust-anchor?   cms
                  +--:(onboarding-information)
                     +-- onboarding-information
                        +-- boot-image
                        |  +-- os-name?              string
                        |  +-- os-version?           string
                        |  +-- download-uri*         inet:uri
                        |  +-- image-verification* [hash-algorithm]
                        |     +-- hash-algorithm    identityref
                        |     +-- hash-value        yang:hex-string
                        +-- configuration-handling?      enumeration
                        +-- pre-configuration-script?    script
                        +-- configuration?               binary
                        +-- post-configuration-script?   script
      ```
      * Redirect information: is used to redirect a device to another bootstrap server. The redirect information contains a list of bootstrap servers, as well as the host name, optional port, and optional trust anchor certificate used by the device to authenticate the bootstrap server.
        
        Example:
        
        ```
        <conveyed-information xmlns="urn:ietf:params:xml:ns:yang:ietf-sztp-conveyed-info">
            <redirect-information>
              <bootstrap-server>
                    <address>https://sztp1.example.com</address>
                    <port>90</port>
                    <trust-anchor>base64encodedvalue==</trust-anchor>
              </bootstrap-server>
              <bootstrap-server> 
                    <address>https://sztp2.example.com</address>
                    <port>90</port>
                    <trust-anchor>base64encodedvalue==</trust-anchor>
              </bootstrap-server>
              <bootstrap-server>
                    <address>https://sztp3.example.com</address>
                    <port>90</port>
                    <trust-anchor>base64encodedvalue==</trust-anchor>
                </bootstrap-server>
            </redirect-information>
        </conveyed-information>
        ```
      * Onboarding information: provides detailed information about the image, configuration file, and other deployment files of the device to be deployed.
        
        Example:
        
        ```
        <conveyed-information xmlns="urn:ietf:params:xml:ns:yang:ietf-sztp-conveyed-info">
            <onboarding-information>
                <boot-image>
                    <os-name></os-name>
                    <os-version></os-version>
                    <download-uri>https://example.com/path/to/image/cfg_file_name.cfg</download-uri>
                    <image-verification>
                        <hash-algorithm>ietf-sztp-conveyed-info:sha-256</hash-algorithm>
                        <hash-value>ee0d0a46ebb2db92762eedba2c0afd9543bf3c3a983dab2e00c559ba9e62196f</hash-value>
                    </image-verification>
                </boot-image>
                <configuration-handling>merge</configuration-handling>
                <pre-configuration-script>base64encodedvalue==</pre-configuration-script>
                <configuration>base64encodedvalue==</configuration>
                <post-configuration-script>base64encodedvalue==</post-configuration-script>
            </onboarding-information>
        </conveyed-information>
        ```
   2. Owner certificate: contains the public key certificate of the customer. The device can use this certificate to verify the signature of the conveyed information.
   3. Ownership voucher: is signed by Huawei. The customer needs to provide the pinned domain certificate and the ESN of the device to be deployed. Huawei generates and provides the ownership voucher for the customer. For details about the ownership voucher, see [RFC 8366](https://datatracker.ietf.org/doc/html/rfc8366).Example:
      ```
         {
           "ietf-voucher:voucher": {
             "created-on": "2023-05-30T19:31:42Z",
             "expires-on": "2023-09-30T19:31:42Z",
             "assertion": "verified",
             "serial-number": "BARCODETEST20200620",
             "idevid-issuer": "base64encodedvalue==",
             "pinned-domain-cert": "base64encodedvalue==",
             "domain-cert-revocation-checks": "false",
             "last-renewal-date": ""
           }
         }
      ```