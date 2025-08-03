ssl minimum version
===================

ssl minimum version

Function
--------



The **ssl minimum version** command sets the minimum SSL version used for an SSL policy.

The **undo ssl minimum version** command restores the minimum SSL version to the default value, regardless of whether TLS1.1, TLS1.2, or TLS1.3 is specified.



By default, the minimum SSL version used for an SSL policy is TLS1.2.


Format
------

**ssl minimum version tls1.1**

**ssl minimum version tls1.2**

**ssl minimum version tls1.3**

**undo ssl minimum version tls1.1**

**undo ssl minimum version tls1.2**

**undo ssl minimum version**

**undo ssl minimum version tls1.3**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **tls1**.**1** | Specifies the minimum SSL version used for an SSL policy is TLS1.1. | - |
| **tls1**.**2** | Specifies the minimum SSL version used for an SSL policy is TLS1.2. | - |
| **tls1**.**3** | Specifies the minimum SSL version used for an SSL policy is TLS1.3. | - |



Views
-----

SSL policy view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To set a minimum SSL version for an SSL policy, run the ssl minimum version command, which meets service modules' flexible requirements on the version of an SSL policy.SSL policies support three SSL versions: TLS1.1, TLS1.2 and TLS1.3. TLS1.3 ensures the highest security, followed by TLS1.2, TLS1.1. The TLS1.1 is not secure now, and the TLS1.3 is recommended.

**Precautions**

* TLS1.3 is recommended for higher security.
* The tls1.1 parameter can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.


Example
-------

# Set the minimum SSL version used for an SSL policy to TLS1.2.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy hw
[~HUAWEI-ssl-policy-hw] ssl minimum version tls1.2

```