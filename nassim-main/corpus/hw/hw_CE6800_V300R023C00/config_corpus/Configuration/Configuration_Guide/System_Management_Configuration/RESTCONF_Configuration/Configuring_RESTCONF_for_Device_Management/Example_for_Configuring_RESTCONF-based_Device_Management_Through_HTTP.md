Example for Configuring RESTCONF-based Device Management Through HTTP
=====================================================================

Example for Configuring RESTCONF-based Device Management Through HTTP

#### Networking Requirements

RESTCONF is an HTTP-based protocol that provides RESTful APIs. External applications can use HTTP to access APIs to implement remote device management and operations. [Figure 1](#EN-US_TASK_0000001871881261__fig12573125961012) shows a network where RESTCONF is used for device management. On this network, the device functions as a RESTCONF server.

**Figure 1** RESTCONF-based device management  
![](figure/en-us_image_0000001877613041.png)
#### Configuration Precautions

Note the following during the configuration:

* If the network environment is insecure, you are advised to configure the device as an HTTPS server, which is more secure.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an HTTP server as the RESTCONF server, including configuring IP addresses for interfaces, creating an AAA user, and enabling the HTTP server function.
2. Configure an HTTP client. Postman is a common HTTP client. To obtain the Postman installation package, visit <https://www.postman.com/downloads/>.


#### Procedure

1. Configure IP addresses for interfaces on the device.
   
   
   ```
   <HUAWEI> system-view
   [*HUAWEI] interface 100ge 1/0/1
   [*HUAWEI-100GE1/0/1] undo portswitch
   [*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
   [*HUAWEI-100GE1/0/1] commit
   [~HUAWEI-100GE1/0/1] quit
   ```
2. Create an AAA user on the device.
   
   
   ```
   [*HUAWEI] aaa
   [*HUAWEI-aaa] local-user huawei123 password irreversible-cipher ********
   [*HUAWEI-aaa] local-user huawei123 service-type http
   [*HUAWEI-aaa] local-user huawei123 privilege level 3 
   [*HUAWEI-aaa] quit
   [*HUAWEI] ssh authentication-type default password
   [*HUAWEI] commit
   ```
3. Enable the HTTP service.
   
   
   ```
   [*HUAWEI] http
   [*HUAWEI-http] service restconf
   [*HUAWEI-http-service-restconf] server enable 
   [*HUAWEI-http-service-restconf] server-source 100ge 1/0/1
   [*HUAWEI-http-service-restconf] commit
   [~HUAWEI-http-service-restconf] quit
   [~HUAWEI-http] quit
   ```

#### Verifying the Configuration

# Check the TCP connection status of RESTCONF communication.

```
[~HUAWEI] display tcp status
-----------------------------------------------------------------------------------                                                                             
Cid        SocketID  Local-Addr:Port       Foreign-Addr:Port     State         VPNName                                                                          
-----------------------------------------------------------------------------------                                                                             
0x80C87550       13  0.0.0.0:23            0.0.0.0:0             LISTEN        --
0x80C87550     5592  10.1.1.1:23           10.1.1.2:63252        ESTABLISHED   -- 
0x82D8045C     7713  10.1.1.1:80           10.1.1.2:52686        ESTABLISHED   -- 
-----------------------------------------------------------------------------------  
```

The command output shows that the RESTCONF connection service with port 80 has been established on the RESTCONF server.

#### Configuration Scripts

```

#
interface 100GE1/0/1
 undo portswitch
 ip address 10.1.1.1 24
#
aaa
  local-user huawei123 password irreversible-cipher $1d$vi0^!e4S`K$+$7-&aq_=QiN[@X,$$U"C_I023We~C+G}-~EVwzM$
  local-user huawei123 service-type http
  local-user huawei123 privilege level 3 
#
http
  service restconf
  server enable
  server-source 100GE1/0/1
#
return
```