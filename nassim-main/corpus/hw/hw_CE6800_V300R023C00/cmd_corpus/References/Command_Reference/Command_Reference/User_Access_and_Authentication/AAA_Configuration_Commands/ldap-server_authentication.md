ldap-server authentication
==========================

ldap-server authentication

Function
--------

The **ldap-server authentication** command configures an LDAP authentication server.

The **undo ldap-server authentication** command deletes an LDAP authentication server.

By default, no LDAP authentication server is configured.



Format
------

**ldap-server authentication** *ip-address* [ *port* ] [ **secondary** | **third** ] [ **ssl** | **no-ssl** ]

**undo ldap-server authentication** [ **secondary** | **third** ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of an LDAP authentication server. | The value is in dotted decimal notation. |
| *port* | Specifies the port number of an LDAP authentication server. | The value is an integer that ranges from 1 to 65535. The default value is 636. If the no-ssl parameter is specified, the default value is 389.  The port number must be the same as that on the LDAP server. |
| **secondary** | Indicates the secondary LDAP authentication server. | - |
| **third** | Indicates the third LDAP authentication server. | - |
| **ssl** | This parameter must be specified when the LDAP authentication between the device and LDAP server uses LDAP over SSL. The device uses a CA certificate to authenticate the LDAP server. | - |
| **no-ssl** | Disables SSL encryption. | - |




Views
-----

LDAP server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

During LDAP authentication, LDAP is used in interaction between the device and LDAP server. The LDAP data transmission is not encrypted. For security, you can use LDAP based on SSL for encrypted transmission. LDAP server certificates need to be imported into the device to authenticate the LDAP server.

**Precautions**

After the FIPS mode is enabled, the no-ssl parameter becomes unavailable.



Example
-------

# Configure the primary LDAP authentication server.
```
<HUAWEI> system-view
[~HUAWEI] ldap-server template temp1
[*HUAWEI-ldap-temp1] ldap-server authentication 10.1.1.1 2222

```