display tftp client
===================

display tftp client

Function
--------



The **display tftp client** command displays the current configuration of the TFTP client.




Format
------

**display tftp client**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



You can set the source IP address by using **tftp client source** command. You can also configure the ACL by using **tftp server acl** command. After setting the source IP address and configuring the ACL of a TFTP client, you can run this command to view the configuration. By default, the source IP address of a TFTP client is set to 0.0.0.0.




Example
-------

# Display the current configuration of the TFTP client.
```
<HUAWEI> display tftp client
--------------------------------------------------------------------------------
ACL name             :
ACL number           :
IPv6 ACL name        :
IPv6 ACL number      :
Source IPv4 address  :  0.0.0.0
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display tftp client** command output
| Item | Description |
| --- | --- |
| ACL name | Indicates the ACL name for IPv4 configuration. |
| ACL number | Indicates the ACL number for IPv4 configuration. |
| IPv6 ACL name | Indicates the ACL name for IPv6 configuration. |
| IPv6 ACL number | Indicates the ACL number for IPv6 configuration. |
| Source IPv4 address | Indicates the source IPv4 address. |