npcc enable
===========

npcc enable

Function
--------



The **npcc enable** command enables the NPCC function in the interface view.

The **undo npcc enable** command disables the NPCC function in the interface view.



By default, the NPCC function is disabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**npcc enable**

**undo npcc enable**


Parameters
----------

None

Views
-----

100GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the lossless queues for which the NPCC function is to be enabled are specified globally, you need to enable the NPCC function in the interface view to implement the NPCC function for IPv4 traffic.

**Precautions**

* NPCC and dynamic load balancing are mutually exclusive.
* NPCC and iQCN are mutually exclusive.
* This command can only be used to enable the NPCC function for IPv4 traffic.
* VXLAN is not supported.
* After NPCC is enabled on an interface, statistics about RoCEv2 packets passing through queues that are not enabled with NPCC are also collected in the RoCEv2 flow table maintained by NPCC.

Example
-------

# Enable the NPCC function on a specified interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] npcc enable

```