display license revoke-ticket
=============================

display license revoke-ticket

Function
--------



The **display license revoke-ticket** command displays the invalidation code of an invalid license file.




Format
------

**display license revoke-ticket**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

When the existing license file that has been activated is about to expire, apply for and activate a new license file or upgrade the existing license file. Otherwise, the expiring license becomes invalid upon expiration. As a result, function modules are shut down and services are interrupted. To prevent services from being affected, apply for a new license and activate it before the license expires. The license revocation code is the evidence for license invalidation and is used to apply for a new license.To check revocation code of the invalid license file on the device, run the **display license revoke-ticket** command.

**Prerequisites**

An invalid license file exists in the current device. Otherwise, no entry is displayed in the **display license revoke-ticket** command output.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the invalidation code of the current invalid license file.
```
<HUAWEI> display license revoke-ticket
Info: The revoke ticket is: LIC20200103006100:27C1B773ED11D9F877855CDAEE74ABFE60E07***.

```

**Table 1** Description of the **display license revoke-ticket** command output
| Item | Description |
| --- | --- |
| revoke ticket | License revoke ticket. |
| Info | Prompt. |