Access Restriction
==================

Access_Restriction

#### Networking Requirements

To improve the security of a server, configure the server to receive connection requests from only the specified source interface and address.


#### Configuration Roadmap

The configuration roadmap is as follows:

* Configure a client to communicate with the source interfaces to be specified at Layer 3.
* Configure the source interface and address for each server.
* If the server accepts only the connection from the specified source interface and source address, the configuration is successful.


#### Data Preparation

None


#### Telnet Server

After the source interface of the Telnet server is configured, the client can access the Telnet server only through this interface.

```
[~HUAWEI] telnet server-source -i LoopBack 1
```
After the source IPv6 address of the Telnet server is configured, the client can access the Telnet server only through this address.
```
[~HUAWEI] telnet ipv6 server-source -a 2001:db8::1
```

A source interface is specified for the Telnet server, and the interface isolation attribute is set for the Telnet server.
```
[~HUAWEI] telnet server-source physic-isolate -i GigabitEthernet 0/1/0 -a 10.1.1.1
```

A source IPv6 interface is specified for the Telnet server, and the interface isolation attribute is set for the Telnet server.
```
[~HUAWEI] telnet ipv6 server-source physic-isolate -i GigabitEthernet 0/1/0 -a 2001:db8::1
```


#### SSH Server

After the source interface of the SSH server is configured, the client can access the SSH server only through this interface.

```
[~HUAWEI] ssh server-source -i LoopBack 1
```
After the source IPv6 address of the SSH server is configured, the client can access the SSH server only through this address.
```
[~HUAWEI] ssh ipv6 server-source -a 2001:db8::1
```

A source interface is specified for the SSH server, and the interface isolation attribute is set for the SSH server.
```
[~HUAWEI] ssh server-source physic-isolate -i GigabitEthernet 0/1/0 -a 10.1.1.1
```

A source IPv6 interface is specified for the SSH server, and the interface isolation attribute is set for the SSH server.
```
[~HUAWEI] ssh ipv6 server-source physic-isolate -i GigabitEthernet 0/1/0 -a 2001:db8::1
```


#### FTP Server

After the source address of the FTP server is configured, the client can access the FTP server only through this address.

```
[~HUAWEI] ftp server-source -a 10.1.1.1 
```
After the source IPv6 address of the FTP server is configured, the client can access the FTP server only through this address.
```
[~HUAWEI] ftp ipv6 server-source -a 2001:db8::1
```

After the source interface of the SSH server is configured, the client can access the FTP server only through this interface.

```
[~HUAWEI] ftp server-source -i LoopBack 1
```
A source interface is specified, and interface isolation is configured.
```
[~HUAWEI] ftp server-source physic-isolate -i GigabitEthernet 0/1/0 -a 10.1.1.1
```

A source IPv6 interface is specified for the FTP server, and the interface isolation attribute is set for the FTP server.
```
[~HUAWEI] ftp ipv6 server-source physic-isolate -i GigabitEthernet 0/1/0 -a 2001:db8::1
```


#### Verifying the Security Hardening Result

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration telnet** command to check the Telnet configuration.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration ssh** command to check the SSH configuration.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration ftp** command to check the FTP configuration.