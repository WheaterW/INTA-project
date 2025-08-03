exclude interface(access-filter)
================================

exclude interface(access-filter)

Function
--------



The **exclude interface** command configures an exception interface for the iNOF host access interface whitelist.

The **undo exclude interface** command deletes an exception interface from the iNOF host access interface whitelist.



By default, no exception interface is configured for the iNOF host access interface whitelist.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**exclude interface** { *interface-name* | *interface-type* *interface-number* } [ **to** { *interface-name* | *interface-type* *interface-number* } ]

**undo exclude interface** { *interface-name* | *interface-type* *interface-number* } [ **to** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an exception interface to be configured for the iNOF host access interface whitelist. | - |
| *interface-type* | Specifies the type of an exception interface to be configured for the iNOF host access interface whitelist. | - |
| *interface-number* | Specifies the number of an exception interface to be configured for the iNOF host access interface whitelist. | - |
| **to** | Specifies an interface range that includes all interfaces between the two interfaces. | - |



Views
-----

iNOF host access interface whitelist view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to configure an exception interface for the iNOF host access interface whitelist.

* If the iNOF host access interface whitelist function is disabled, the configured whitelist and exception interfaces do not take effect.
* If you run the **access-filter enable** command to enable the iNOF host access interface whitelist function, host access to iNOF is controlled as follows:
* If an exception interface has been configured for the iNOF host access interface whitelist, a host can access the iNOF through such an interface without being restricted by the whitelist.
* If no exception interface is configured for the iNOF host access interface whitelist, whether a host can access the iNOF is determined based on the configured whitelist information.

**Precautions**

* Only physical interfaces can be configured as exception interfaces of the iNOF host access interface whitelist.
* An interface cannot be added to the iNOF host access interface whitelist while being configured as an exception interface of the iNOF host access interface whitelist.
* When a host needs to connect to two devices in the M-LAG and the iNOF host access interface whitelist function is enabled on the two M-LAG devices, you need to run the **host interface** command on both M-LAG devices to specify the IP address of the host to access the iNOF through the M-LAG member interface of the local M-LAG device; alternatively, run the **exclude interface** command on both M-LAG devices to specify the M-LAG member interface as an exception interface of the iNOF host access interface whitelist.
* When running this command, pay attention to the following points when using the keyword to:
  + The two interfaces before and after to must be of the same type and have the same attribute. For example, they are both interfaces resulting from a split. If they are interfaces resulting from a split, they must belong to the same physical interface.
  + The two interfaces before and after the keyword to must be in the same slot. If adjacent interfaces in multiple slots need to be added, you are advised to run this command multiple times or use the to keyword multiple times.
  + If the keyword to is not used, ignore the preceding points.

Example
-------

# Configure an exception interface for the iNOF host access interface whitelist.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] access-filter
[*HUAWEI-ai-service-inof-access-filter] exclude interface 100GE 1/0/1

```