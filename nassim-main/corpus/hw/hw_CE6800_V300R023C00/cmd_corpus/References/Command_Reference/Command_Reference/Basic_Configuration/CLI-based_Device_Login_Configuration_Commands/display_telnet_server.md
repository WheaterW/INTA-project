display telnet server
=====================

display telnet server

Function
--------

The **display telnet server** command displays the global configuration information of the Telnet server.



Format
------

**display telnet server**



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

By executing this command checks the basic Telnet server configurations.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display current connections information of the Telnet server.
```
<HUAWEI> display telnet server
Telnet server           : Enable
Telnet server port      : 23
Telnet IPv6 server      : Enable
Telnet IPv6 server port : 23
ACL name                : --
ACL number              : --
ACL6 name               : --
ACL6 number             : --

```


**Table 1** Description of the
**display telnet server** command output

| Item | Description |
| --- | --- |
| ACL name | ACL name of the Telnet server. |
| ACL number | ACL number of the Telnet server. |
| ACL6 name | ACL name of the Telnet IPv6 server. |
| ACL6 number | ACL number of the Telnet IPv6 server. |
| Telnet server | Status of the Telnet server. The options are as follows:   * Enable: enabled. * Disable: disabled. |
| Telnet server port | Port number of the Telnet server. |
| Telnet IPv6 server | Status of the Telnet IPv6 server. The options are as follows:   * Enable: enabled. * Disable: disabled. |
| Telnet IPv6 server port | Port number of the Telnet IPv6 server. |