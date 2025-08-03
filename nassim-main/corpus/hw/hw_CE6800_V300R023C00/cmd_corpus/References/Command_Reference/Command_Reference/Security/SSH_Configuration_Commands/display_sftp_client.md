display sftp client
===================

display sftp client

Function
--------



The **display sftp client** command displays all of the currently effective configuration on the SFTP client.




Format
------

**display sftp client**


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

After the source IP address of an SFTP client is set, you can run the display sftp client command to view the configuration. Otherwise, the SFTP client source IP address will be 0.0.0.0 by default.


Example
-------

# Display the SFTP client source IP address.
```
<HUAWEI> display sftp client
The source address of the SFTP client is 1.1.1.1.

```

**Table 1** Description of the **display sftp client** command output
| Item | Description |
| --- | --- |
| The source address of the SFTP client | Display the source address of the SFTP client. |