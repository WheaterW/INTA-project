pki certificate access-control-policy default
=============================================

pki certificate access-control-policy default

Function
--------



The **pki certificate access-control-policy default** command configures the default certificate access control policy.



By default, the action in the policy is permit. That is, the certificate is allowed to pass verification.


Format
------

**pki certificate access-control-policy default** { **permit** | **deny** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **permit** | Indicates that a certificate is allowed to pass verification. | - |
| **deny** | Indicates that a certificate is not allowed to pass verification. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a service has a specified certificate access control policy, the specified certificate access control policy is used. Otherwise, the default certificate access control policy is used. You can run this command to modify the default certificate access control policy.


Example
-------

# Set the action in the default certificate access policy to deny.
```
<HUAWEI> system-view
[~HUAWEI] pki certificate access-control-policy default deny

```