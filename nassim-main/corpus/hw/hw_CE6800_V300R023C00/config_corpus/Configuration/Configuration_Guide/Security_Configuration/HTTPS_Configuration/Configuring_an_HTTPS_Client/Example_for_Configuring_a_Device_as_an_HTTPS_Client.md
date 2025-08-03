Example for Configuring a Device as an HTTPS Client
===================================================

Example for Configuring a Device as an HTTPS Client

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001512680758__fig5412203812116), before configuring the HTTPS client, you need to configure an SSL policy on the device and load the corresponding digital certificate. After the SSL policy is associated with HTTP, you can log in to the HTTPS server from the HTTPS client.

**Figure 1** Network diagram for accessing files on another device using HTTPS  
![](figure/en-us_image_0000001512680766.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an SSL policy for the HTTPS client.
2. Configure an HTTPS client.

#### Procedure

1. Configure an SSL policy for the HTTPS client.
   
   
   
   # Configure a PKI realm. Import the local certificates and private key file.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] pki realm domain1
   [*HUAWEI-pki-realm-domain1] commit
   [~HUAWEI-pki-realm-domain1] quit
   [~HUAWEI] pki import-certificate local realm domain1 pem filename https_local.pem
   [~HUAWEI] pki import rsa-key-pair http-key pem restconf.pem   //Skip this step if the private key file is generated on the local device.
   ```
   
   # Import the CA certificate of the HTTP client to verify the validity of the local certificate of the HTTP client.
   
   ```
   [~HUAWEI] pki import-certificate ca realm domain1 pem filename https_ca.pem
   ```
   
   
   
   # Configure an SSL policy and bind it to the PKI realm.
   
   
   
   ```
   [~HUAWEI] ssl policy policy1
   [*HUAWEI-ssl-policy-policy1] pki-domain domain1
   [*HUAWEI-ssl-policy-policy1] commit
   [~HUAWEI-ssl-policy-policy1] quit
   ```
2. Configure an HTTPS client.
   
   
   ```
   [~HUAWEI] http
   [*HUAWEI-http] client ssl-policy policy1
   [*HUAWEI-http] client ssl-verify peer
   [*HUAWEI-http] commit
   [~HUAWEI-http] quit
   ```

#### Verifying the Configuration

Run the **display ssl policy** command to check whether the HTTPS client is configured successfully.

```
[~HUAWEI] display ssl policy
       SSL Policy Name: policy1
            PKI domain: domain_name
     Policy Applicants: HTTP-CLIENT
         Key-pair Type:
 Certificate File Type:
      Certificate Type:
  Certificate Filename:
     Key-file Filename:
              CRL File:
       Trusted-CA File:
```

#### Configuration Scripts

```
#
ssl policy policy1
 pki-domain domain1
#
http
 client ssl-policy policy1
 client ssl-verify peer
#
pki realm domain1
#
return
```