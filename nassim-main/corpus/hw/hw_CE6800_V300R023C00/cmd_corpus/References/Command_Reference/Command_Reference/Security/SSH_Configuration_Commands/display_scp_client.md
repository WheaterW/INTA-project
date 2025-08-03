display scp client
==================

display scp client

Function
--------



The **display scp client** command displays all the current SCP client configurations.




Format
------

**display scp client**


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

After the source IP address of an SCP client is set, you can run the display scp client command to view the configuration. Otherwise, the SCP client's source IP address is 0.0.0.0 by default.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the SCP client's source IP address.
```
<HUAWEI> display scp client
The source address of the SCP client is 1.1.1.1.

```

**Table 1** Description of the **display scp client** command output
| Item | Description |
| --- | --- |
| The source address | Source address. |