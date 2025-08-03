c-rp
====

c-rp

Function
--------



The **c-rp** command configures a candidate-rendezvous point (C-RP) on a Router, so that the Router can announce itself as a C-RP to the bootstrap router (BSR).

The **undo c-rp** command deletes a C-RP.



By default, no C-RP is configured.


Format
------

**c-rp** { *interface-type* *interface-number* | *port-name* } [ **group-policy** { *basic-acl-number* | **acl-name** *acl-name* } | **priority** *priority* | **holdtime** *hold-interval* | **advertisement-interval** *adv-interval* ] \*

**undo c-rp** { *interface-type* *interface-number* | *port-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type and number of an interface. The IP address of the specified interface is advertised as the C-RP address.  To avoid frequent protocol changes caused by interface flapping, using loopback interfaces is recommended. | - |
| *interface-number* | Specifies the type and number of an interface. The IP address of the specified interface is advertised as the C-RP address.  To avoid frequent protocol changes caused by interface flapping, using loopback interfaces is recommended. | - |
| *port-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **group-policy** *basic-acl-number* | Specifies the range of multicast groups served by a C-RP. The range is restricted to the multicast groups permitted by a specified ACL. basic-acl-number specifies the number of a basic ACL that defines the service range of the advertised RP. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value must start with a letter or digit, and cannot contain only digits. |
| **priority** *priority* | Specifies a priority value for a C-RP. A larger value indicates a lower C-RP priority. | The value is an integer ranging from 0 to 255. The default value is 0. |
| **holdtime** *hold-interval* | Specifies a timeout period during which the BSR waits to receive an Advertisement message from a C-RP. | The value is an integer ranging from 1 to 65535, in seconds. The default value is 150 seconds. |
| **advertisement-interval** *adv-interval* | Specifies an interval at which a C-RP sends Advertisement messages. | The value is an integer ranging from 1 to 65535, in seconds. The default value is 60 seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An RP is the core of a PIM-SM network. Therefore, a C-RP must be able to communicate with other devices. It is recommended that you configure a C-RP on the backbone network device and reserve sufficient bandwidth between the device and other devices.The rules for a C-RP to compete for an RP are as follows:

* The C-RP with the longest mask length of the served group address range matching the group address that the user joins wins.
* If the mask lengths of the multicast groups that the C-RPs serve are the same, the C-RP with the highest priority wins (the greater the priority value, the lower the priority).
* If the priorities are the same, the hash function is executed. The one with the largest calculation result wins.
* If all the preceding factors are the same, the C-RP with the largest address wins.

**Prerequisites**

PIM has been enabled and the public network PIM instance view has been displayed using the **pim** command.PIM-SM has been enabled on the interface on which a C-RP is to be configured.To use the groupPolicyValue the parameter, an ACL rule has been configured.

**Configuration Impact**

If the c-rp command is run more than once, the latest configuration overrides the previous one.NOTE:If address borrowing is configured, configuring a C-RP on interfaces that have the same addresses is not recommended. If the priorities of such interfaces are different, the BSR considers that the C-RP configuration is repeatedly modified.


Example
-------

# In the public network instance view, configure 100GE 1/0/1 as a C-RP of PIM-SM domains 225.1.0.0/16 and 226.2.0.0/16, configure a basic ACL 2069, and set the priority of the C-RP to 10.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] acl number 2069
[*HUAWEI-acl4-basic-2069] rule permit source 225.1.0.0 0.0.255.255
[*HUAWEI-acl4-basic-2069] rule permit source 226.2.0.0 0.0.255.255
[*HUAWEI-acl4-basic-2069] quit
[*HUAWEI] pim
[*HUAWEI-pim] c-rp 100GE 1/0/1 group-policy 2069 priority 10

```