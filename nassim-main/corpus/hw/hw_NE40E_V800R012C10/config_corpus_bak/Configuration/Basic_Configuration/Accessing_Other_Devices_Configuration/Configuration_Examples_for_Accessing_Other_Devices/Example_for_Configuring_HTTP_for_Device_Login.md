Example for Configuring HTTP for Device Login
=============================================

This section provides an example for configuring HTTP for device login, so that you can log in to an HTTP server from an HTTP client to download the desired certificate.

#### Networking Requirements

An HTTP client can download a certificate from an HTTP server through HTTP. On the network shown in [Figure 1](#EN-US_TASK_0172360153__fig_dc_vrp_http_cfg_001101), the HTTP client and server are routable to each other. To download a certificate from the server to the client, log in to the server from the client.

The server supports SSL policies. To improve data transmission security, configure an SSL policy on the HTTP client.

**Figure 1** Device login using HTTP  
![](images/fig_dc_vrp_http_cfg_001101.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an SSL policy on the HTTP client.
2. Configure the HTTP client.

#### Data Preparation

To complete the configuration, you need the following data:

* SSL policy name **policy1** to be configured on the HTTP client
* Domain name **domain1**

#### Procedure

1. Configure an SSL policy on the HTTP client.
   
   
   
   # Configure a PKI domain.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] pki domain domain1
   ```
   ```
   [*HUAWEI-pki-domain-domain1] commit
   ```
   ```
   [~HUAWEI-pki-domain-domain1] quit
   ```
   ```
   [~HUAWEI] pki import-certificate ca domain domain1 filename test.crt
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The CA certificate is used as an example. During the actual configuration, you need to replace **ca** and **test.crt** with the existing certificate type and name on the device. You can directly upload the certificate to the device for installation, or apply for and download the certificate for installation. For details, see "Obtaining a Certificate" in *PKI Configuration*.
   
   # Configure an SSL policy and bind it to the PKI domain.
   
   ```
   [~HUAWEI] ssl policy policy1
   ```
   ```
   [*HUAWEI-ssl-policy-policy1] pki-domain domain1
   ```
   ```
   [*HUAWEI-ssl-policy-policy1] commit
   ```
   ```
   [~HUAWEI-ssl-policy-policy1] quit
   ```
2. Configure the HTTP client.
   
   
   ```
   [~HUAWEI] http
   ```
   ```
   [*HUAWEI-http] client ssl-policy policy1
   ```
   ```
   [*HUAWEI-http] client ssl-verify peer 
   ```
   ```
   [*HUAWEI-http] commit
   ```
   ```
   [~HUAWEI-http] quit
   ```
3. Check whether the HTTP client is successfully configured.
   
   
   ```
   [~HUAWEI] display ssl policy
   ```
   ```
          SSL Policy Name: policy1
               PKI domain: domain1
        Policy Applicants: HTTP-CLIENT
            Key-pair Type:
    Certificate File Type:
         Certificate Type:
     Certificate Filename:
        Key-file Filename:
                 CRL File:
          Trusted-CA File:
   ```

#### Configuration Files

* HTTP client configuration file
  
  ```
  #
  ssl policy policy1
   pki-domain domain1
  #
  http
   client ssl-policy policy1
   client ssl-verify peer
  #
  return
  ```