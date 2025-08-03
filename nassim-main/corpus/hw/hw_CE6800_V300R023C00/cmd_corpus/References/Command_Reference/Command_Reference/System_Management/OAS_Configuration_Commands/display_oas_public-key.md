display oas public-key
======================

display oas public-key

Function
--------



The **display oas public-key** command displays the installed public key files.




Format
------

**display oas public-key**


Parameters
----------

None

Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run this command to view the list of public key files installed on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the installed public key files.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] display oas public-key
Public key information:
---------------------------------------------------------------------------------------------------
public-key1.txt
public-key2.txt
---------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display oas public-key** command output
| Item | Description |
| --- | --- |
| Public key information | Public key file list information. |