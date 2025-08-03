download
========

download

Function
--------



The **download** command downloads the version package or configuration file of a specified URL to the corresponding path of the device.




Format
------

**download** *file-url* [ **save-as** *file-path* | [ **ssl-policy** *policy-name* [ **ssl-verify** **peer** [ **verify-dns** ] ] | **verify-dns** ] | **vpn-instance** *vpn-name* | **source-ip** *ip-address* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-url* | Specifies a URL of downloading files. | The value is a string of 1 to 255 characters. |
| **save-as** *file-path* | Specifies a path to store files. | The value is a string of 1 to 255 characters. |
| **ssl-policy** *policy-name* | Specifies an SSL policy name. | The value is a string of 1 to 23 characters. If an initial certificate is loaded to the PKI realm to which the specified SSL policy is bound, the certificate is delivered in interactive mode. |
| **ssl-verify** **peer** | Specifies to perform SSL verification on the server. | - |
| **verify-dns** | Enables CN/SAN verification. | - |
| **vpn-instance** *vpn-name* | Specifies a VPN name. | The value is a string of 1 to 31 characters. |
| **source-ip** *ip-address* | Specifies the source IP address of a device. The options are as follows:  IPv4.  IPv6. | IPv4 addresses are in dotted decimal notation.  IPv6 addresses are in colon hexadecimal notation. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* When you run the **download** command to download the version package or configuration file of a specified URL to the corresponding path of the device, the file can be saved to the corresponding path with the file name extension .cc or .cfg.
* If no path is specified, the SSL policy is downloaded to the current path. If no SSL policy name is specified, the SSL policy name in the HTTP view is used.
* If verify-dns is specified, the CN/SAN field verification is enabled for the server certificate.

**Prerequisites**

A VPN instance has been created before you configure vpn-name parameter. Otherwise, the command cannot be executed.An SSL policy has been created before you configure policy-name parameter. Otherwise, the command cannot be executed.


Example
-------

# Download the version package from https://10.1.1.1:443/test.cc to flash:/test.cc.
```
<HUAWEI> download https://10.1.1.1:443/test.cc ssl-policy test save-as flash:/test.cc vpn-instance test

```

# The initial certificate is loaded to the PKI realm to which the specified SSL policy is bound. Download the version package with URL https://10.1.1.1:443/test.cc.
```
<HUAWEI> download https://10.1.1.1:443/test.cc ssl-policy a
Warning: A preset certificate is loaded to the PKI domain bound to the specified SSL policy. The current operation has security risks. Continue? [Y/N]:Y

```

# Specify the source IPv6 address and download the version package from the URL https://[2001:db8:1::1]:443/test.cc.
```
<HUAWEI> download https://[2001:db8:1::1]:443/test.cc ssl-policy test save-as cfcard:/test.cc source-ip 2001:db8:1::2 vpn-instance test

```