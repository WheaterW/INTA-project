display service-scheme
======================

display service-scheme

Function
--------



The **display service-scheme** command displays the configuration of service schemes.




Format
------

**display service-scheme** [ **name** *name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *name* | Specifies the name of a service scheme. | The service scheme must already exist. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The **display service-scheme** command displays the configuration of service schemes. Before applying a service scheme to a domain, run the **display service-scheme** command to check whether the service scheme meets requirements.

**Precautions**

The **display service-scheme** command displays the detailed configuration if the command is executed in the service scheme view or the name of a service scheme is specified. Otherwise, this command displays only the summary of service schemes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of the service scheme svcscheme1.
```
<HUAWEI> display service-scheme name svcscheme1
  Service-scheme-name           : svcscheme1                                                                                               
  Service-scheme-dns-name       : -                                                                                                 
  Service-scheme-primary-dns    : -                                                                                                 
  Service-scheme-secondary-dns  : -                                                                                                 
  Service-scheme-adminlevel     : 15                                                                                                 
  Service-scheme-dhcpgroup      : -                                                                                                 
  Service-scheme-ippool         : - 
  Service-scheme-priority       : 1                                                                                                
  Service-scheme-vlapool        : svcscheme1
  Access-limit-username-maxnum  : 10                                                                                                 
  Service-scheme-qosprofile     : -
  Split-tunnel-ACL              : -

```

# Display information about all service schemes.
```
<HUAWEI> display service-scheme
  Total of service scheme: 2
  -------------------------------------------------------------------
  Service-scheme-name                    scheme-index
  -------------------------------------------------------------------
  svcscheme1                               0
  svcscheme2                               1
  -------------------------------------------------------------------

```

**Table 1** Description of the **display service-scheme** command output
| Item | Description |
| --- | --- |
| Service-scheme-name | Name of a service scheme. |
| Service-scheme-dns-name | Bound DNS name. |
| Service-scheme-primary-dns | Address of the primary DNS server. |
| Service-scheme-secondary-dns | Address of the secondary DNS server. |
| Service-scheme-adminlevel | Level of an administrator. |
| Service-scheme-dhcpgroup | Bound DHCP group. |
| Service-scheme-ippool | Bound IP pool. |
| Access-limit-username-maxnum | Maximum number of users who are allowed to access the network using the same user name. |
| Scheme-index | Index of a service scheme. |