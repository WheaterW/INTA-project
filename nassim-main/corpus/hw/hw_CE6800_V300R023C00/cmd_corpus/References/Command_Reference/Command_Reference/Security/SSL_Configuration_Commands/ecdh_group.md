ecdh group
==========

ecdh group

Function
--------



The **ecdh group** command configures elliptic curve parameter values for the ECDHE algorithm.

The **undo ecdh group** command restores the default values of the elliptic curve parameters for the ECDHE algorithm.



By default, the default elliptic curve parameter values of the ECDHE algorithm are Curve and Brainpool.


Format
------

**ecdh group** { **nist** | **curve** | **brainpool** | **pqc-kyber** } \*

**undo ecdh group**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **nist** | Sets the elliptic curve parameter value to Nist. | - |
| **curve** | Sets the elliptic curve parameter value to Curve. | - |
| **brainpool** | Sets the elliptic curve parameter value to Brainpool. | - |
| **pqc-kyber** | Sets the key exchange algorithm to post-quantum hybrid key algorithm. Currently, the post-quantum cryptographic algorithm complies with the draft-ietf-tls-hybrid-design-05 draft. | - |



Views
-----

SSL policy view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to modify the elliptic curve parameter settings of the ECDHE algorithm.

**Precautions**

The **ecdh group** command can configure one or more elliptic curve parameter values.The configured elliptic curve parameter values take effect only after the ECDHE algorithm suite is obtained through SSL negotiation.


Example
-------

# Configure the ecdh group parameter for an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy a
[*HUAWEI-ssl-policy-a] ecdh group nist curve brainpool pqc-kyber

```