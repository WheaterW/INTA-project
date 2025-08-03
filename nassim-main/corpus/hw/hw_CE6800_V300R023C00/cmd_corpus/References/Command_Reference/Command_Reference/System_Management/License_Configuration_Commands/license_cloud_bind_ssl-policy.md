license cloud bind ssl-policy
=============================

license cloud bind ssl-policy

Function
--------



The **license cloud bind ssl-policy** command is used to configure the binding policy item name.

The **undo license cloud bind ssl-policy** command is used to configure the unbound policy item name.



By default, no SSL policy is bound to the system.


Format
------

**license cloud bind ssl-policy** *policy-name*

**undo license cloud bind ssl-policy** *policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Name of SSL policy. | The value is a string of 1 to 254 case-sensitive characters. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, the device uses the non-cloud license mode. To switch the device to the cloud license mode, you need to bind a policy name with a certificate and configure the IP address and port number of the cloud license server. In this way, the device can apply for license resources from the cloud license server.

**Prerequisites**

An SSL policy has been configured.

**Precautions**

Ensure that the bound policy has a cloud certificate.


Example
-------

# Bind a policy with a cloud certificate.
```
<HUAWEI> system-view
[~HUAWEI] license cloud bind ssl-policy abc

```

# Unbind a policy with a cloud certificate.
```
<HUAWEI> system-view
[~HUAWEI] undo license cloud bind ssl-policy abc

```