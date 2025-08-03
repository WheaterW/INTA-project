Example for Configuring RESTCONF-based Device Management Through HTTPS
======================================================================

Example for Configuring RESTCONF-based Device Management Through HTTPS

#### Networking Requirements

RESTCONF is an HTTP-based protocol that provides RESTful APIs. External applications can use HTTP to access APIs to implement remote device management and operations. [Figure 1](#EN-US_TASK_0000001512851258__fig104623531117) shows a network where RESTCONF is used for device management. On this network, the device functions as a RESTCONF server.

**Figure 1** RESTCONF-based device management  
![](figure/en-us_image_0000001852290130.png)

#### Configuration Precautions

If the network environment is insecure, you are advised to configure the device as an HTTPS server, which is more secure.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an HTTP server as the RESTCONF server, including configuring IP addresses for interfaces to communicate with an HTTP client, creating an AAA user, configuring an SSL policy, and enabling the HTTP server function.
2. Configure an HTTP client. Postman is a common HTTP client. To obtain the Postman installation package, visit <https://www.postman.com/downloads/>.

#### Procedure

1. Configure IP addresses for interfaces on the device.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] interface 100ge 1/0/1
   [*HUAWEI-100GE1/0/1] undo portswitch
   [*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
   [*HUAWEI-100GE1/0/1] commit
   [~HUAWEI-100GE1/0/1] quit
   ```
2. Create an AAA user on the device.
   
   
   ```
   [~HUAWEI] aaa
   [~HUAWEI-aaa] local-user huawei123 password irreversible-cipher ********
   [*HUAWEI-aaa] local-user huawei123 service-type http
   [*HUAWEI-aaa] local-user huawei123 privilege level 3 
   [*HUAWEI-aaa] quit
   [*HUAWEI] ssh authentication-type default password
   [*HUAWEI] commit
   ```
3. Configure an SSL policy on the device.
   
   
   
   # Upload the obtained digital certificate to the **/pki/public** directory of the device through SFTP. For details about how to apply for a digital certificate in PKI mode, see *Configuration Guide - PKI Configuration*.
   
   # Configure a PKI domain and import the local certificate and private key file.
   
   ```
   [~HUAWEI] pki realm domain1
   [*HUAWEI-pki-realm-domain1] commit
   [~HUAWEI-pki-realm-domain1] quit
   [~HUAWEI] pki import-certificate local realm domain1 pem filename restconf_local.pem
   [~HUAWEI] pki import rsa-key-pair restconf-key pem restconf.pem  //Skip this step if the private key file is generated on the local device.
   ```
   
   # Import the CA certificate of the HTTP client to verify the local certificate of the HTTP client.
   
   ```
   [~HUAWEI] pki import-certificate ca realm domain1 pem filename restconf_ca.pem
   ```
   
   # Configure an SSL policy and bind it to the PKI domain.
   
   
   
   ```
   [~HUAWEI] ssl policy policy1
   [*HUAWEI-ssl-policy-policy1] pki-domain domain1
   [*HUAWEI-ssl-policy-policy1] commit
   [~HUAWEI-ssl-policy-policy1] quit
   ```
4. Enable the HTTP server function on the device.
   
   
   ```
   [~HUAWEI] http
   [*HUAWEI-http] service restconf
   [*HUAWEI-http-service-restconf] secure-server enable
   [*HUAWEI-http-service-restconf] server-source 100ge1/0/1
   [*HUAWEI-http-service-restconf] ssl-policy policy1
   [*HUAWEI-http-service-restconf] ssl-verify peer
   [*HUAWEI-http-service-restconf] commit
   [~HUAWEI-http-service-restconf] quit
   [~HUAWEI-http] quit
   ```

#### Verifying the Configuration

# Check the TCP connection status of RESTCONF communication.

```
[~HUAWEI] display tcp status
2020-03-09 18:17:51.519
-----------------------------------------------------------------------------------
Cid        SocketID  Local-Addr:Port       Foreign-Addr:Port     State         VPNName
-----------------------------------------------------------------------------------
0x80C82724        1  0.0.0.0:23            0.0.0.0:0             LISTEN        --
0x82D804A7        2  0.0.0.0:443           0.0.0.0:0             LISTEN        --
0x80C82724        3  10.1.1.1:23           10.1.1.2:55452        ESTABLISHED   --
0x82D804A7        4  10.1.1.1:443          10.1.1.2:54152        ESTABLISHED   --
-----------------------------------------------------------------------------------
```

The command output shows that the RESTCONF connection service with port 443 has been established on the RESTCONF server.


#### Configuration Scripts

* RESTCONF server
  ```
  #                                                                                                                                   
  pki realm domain1
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 24
  #
  ssl policy policy1
    pki-domain domain1
  #
  aaa
    local-user huawei123 password irreversible-cipher $1d$vi0^!e4S`K$+$7-&aq_=QiN[@X,$$U"C_I023We~C+G}-~EVwzM$
    local-user huawei123 service-type http
    local-user huawei123 privilege level 3 
  #
  http
   service restconf
    secure-server enable
    server-source 100ge1/0/1
    ssl-policy policy1
    ssl-verify peer
  #
  return
  ```