cipher-suite exclude
====================

cipher-suite exclude

Function
--------



The **cipher-suite exclude key-exchange rsa** command excludes RSA key exchange algorithms from the cipher-suite-list.

The **undo cipher-suite exclude key-exchange rsa** command includes RSA key exchange algorithms from the cipher-suite-list.

The **cipher-suite exclude cipher mode cbc** command excludes CBC encryption mode algorithms from the cipher-suite-list.

The **undo cipher-suite exclude cipher mode cbc** command includes CBC encryption mode algorithms from the cipher-suite-list.

The **cipher-suite exclude hmac sha1** command excludes HMAC-SHA1 algorithms from the cipher-suite-list.

The **undo cipher-suite exclude hmac sha1** command includes HMAC-SHA1 algorithms from the cipher-suite-list.



By default, RSA key exchange algorithm, CBC mode algorithm and HMAC-SHA1 algorithm are not supported in an SSL cipher suite bound to an SSL policy.


Format
------

**cipher-suite exclude key-exchange rsa**

**cipher-suite exclude cipher mode cbc**

**cipher-suite exclude hmac sha1**

**undo cipher-suite exclude key-exchange** [ **rsa** ]

**undo cipher-suite exclude cipher mode** [ **cbc** ]

**undo cipher-suite exclude hmac** [ **sha1** ]


Parameters
----------

None

Views
-----

SSL policy view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

During client and server authentication, an algorithm list is provided for the client and server to perform SSL algorithm negotiation. To exclude RSA/CBC/SHA1 key exchange algorithms, run the cipher-suite exclude key-exchange rsa, cipher-suite exclude cipher mode cbc or cipher-suite exclude hmac sha1 command.

**Prerequisites**

An SSL policy has been created using the **ssl policy** command.

**Precautions**

After the cipher-suite exclude key-exchange rsa, cipher-suite exclude cipher mode cbc or cipher-suite exclude hmac sha1 command is run, the RSA/CBC/SHA1 encryption algorithm configured in the SSL cipher suite of an SSL policy does not take effect.


Example
-------

# Exclude the RSA key exchange algorithm from the SSL cipher suite bound to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy abc
[*HUAWEI-ssl-policy-abc] cipher-suite exclude key-exchange rsa

```

# Exclude the CBC encryption mode algorithm from the SSL cipher suite bound to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy abc
[*HUAWEI-ssl-policy-abc] cipher-suite exclude cipher mode cbc

```

# Exclude the HMAC-SHA1 algorithms from the SSL cipher suite bound to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy abc
[*HUAWEI-ssl-policy-abc] cipher-suite exclude hmac sha1

```