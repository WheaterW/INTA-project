cmp-request origin-authentication-method
========================================

cmp-request origin-authentication-method

Function
--------



The **cmp-request origin-authentication-method** command configures the authentication method used for initial request (IR) through CMPv2.

The **undo cmp-request origin-authentication-method** command restores the default authentication method used for IR through CMPv2.



By default, the authentication method used for IR through CMPv2 is MAC.


Format
------

**cmp-request origin-authentication-method** { **message-authentication-code** | **signature** }

**undo cmp-request origin-authentication-method**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **message-authentication-code** | Indicates the MAC method for the IR. | - |
| **signature** | Indicates the signature method for the IR. | - |



Views
-----

PKI CMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

During the IR using CMPv2, a security protection measure needs to be taken:

* After you select the MAC method, run the **cmp-request message-authentication-code** command to configure the reference value and secret value. The device uses the reference value and secret value to protect messages during the IR.
* After you select the signature method, run the **cmp-request authentication-cert** command to configure the external certificate. The device uses the external certificate to protect signatures during the IR.

Example
-------

# Configure the authentication method used for IR through CMPv2.
```
<HUAWEI> system-view
[~HUAWEI] pki cmp session test
[*HUAWEI-pki-cmp-session-test] cmp-request origin-authentication-method signature

```