set cipher-suite
================

set cipher-suite

Function
--------



The **set cipher-suite** command specifies encryption algorithms to be supported in an SSL cipher suite bound to an SSL policy.

The **undo set cipher-suite** command deletes encryption algorithms from an SSL cipher suite bound to an SSL policy.



By default, no encryption algorithms are supported in the SSL cipher suite bound to an SSL policy.


Format
------

**set cipher-suite** { **tls1\_ck\_rsa\_with\_aes\_256\_sha** | **tls1\_ck\_rsa\_with\_aes\_128\_sha** | **tls1\_ck\_dhe\_rsa\_with\_aes\_256\_sha** | **tls1\_ck\_dhe\_dss\_with\_aes\_256\_sha** | **tls1\_ck\_dhe\_rsa\_with\_aes\_128\_sha** | **tls1\_ck\_dhe\_dss\_with\_aes\_128\_sha** | **tls12\_ck\_rsa\_aes\_128\_cbc\_sha** | **tls12\_ck\_rsa\_aes\_256\_cbc\_sha** | **tls12\_ck\_rsa\_aes\_128\_cbc\_sha256** | **tls12\_ck\_rsa\_aes\_256\_cbc\_sha256** | **tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha** | **tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha** | **tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha** | **tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha** | **tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha256** | **tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha256** | **tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha256** | **tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha256** | **tls12\_ck\_rsa\_with\_aes\_128\_gcm\_sha256** | **tls12\_ck\_rsa\_with\_aes\_256\_gcm\_sha384** | **tls12\_ck\_dhe\_rsa\_with\_aes\_128\_gcm\_sha256** | **tls12\_ck\_dhe\_rsa\_with\_aes\_256\_gcm\_sha384** | **tls12\_ck\_dhe\_dss\_with\_aes\_128\_gcm\_sha256** | **tls12\_ck\_dhe\_dss\_with\_aes\_256\_gcm\_sha384** | **tls12\_ck\_ecdhe\_rsa\_with\_aes\_128\_gcm\_sha256** | **tls12\_ck\_ecdhe\_rsa\_with\_aes\_256\_gcm\_sha384** | **tls13\_aes\_128\_gcm\_sha256** | **tls13\_aes\_256\_gcm\_sha384** | **tls13\_chacha20\_poly1305\_sha256** | **tls13\_aes\_128\_ccm\_sha256** }

**undo set cipher-suite** { **tls1\_ck\_rsa\_with\_aes\_256\_sha** | **tls1\_ck\_rsa\_with\_aes\_128\_sha** | **tls1\_ck\_dhe\_rsa\_with\_aes\_256\_sha** | **tls1\_ck\_dhe\_dss\_with\_aes\_256\_sha** | **tls1\_ck\_dhe\_rsa\_with\_aes\_128\_sha** | **tls1\_ck\_dhe\_dss\_with\_aes\_128\_sha** | **tls12\_ck\_rsa\_aes\_128\_cbc\_sha** | **tls12\_ck\_rsa\_aes\_256\_cbc\_sha** | **tls12\_ck\_rsa\_aes\_128\_cbc\_sha256** | **tls12\_ck\_rsa\_aes\_256\_cbc\_sha256** | **tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha** | **tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha** | **tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha** | **tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha** | **tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha256** | **tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha256** | **tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha256** | **tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha256** | **tls12\_ck\_rsa\_with\_aes\_128\_gcm\_sha256** | **tls12\_ck\_rsa\_with\_aes\_256\_gcm\_sha384** | **tls12\_ck\_dhe\_rsa\_with\_aes\_128\_gcm\_sha256** | **tls12\_ck\_dhe\_rsa\_with\_aes\_256\_gcm\_sha384** | **tls12\_ck\_dhe\_dss\_with\_aes\_128\_gcm\_sha256** | **tls12\_ck\_dhe\_dss\_with\_aes\_256\_gcm\_sha384** | **tls12\_ck\_ecdhe\_rsa\_with\_aes\_128\_gcm\_sha256** | **tls12\_ck\_ecdhe\_rsa\_with\_aes\_256\_gcm\_sha384** | **tls13\_aes\_128\_gcm\_sha256** | **tls13\_aes\_256\_gcm\_sha384** | **tls13\_chacha20\_poly1305\_sha256** | **tls13\_aes\_128\_ccm\_sha256** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **tls1\_ck\_rsa\_with\_aes\_256\_sha** | Supports the TLS1\_CK\_RSA\_WITH\_AES\_256\_SHA algorithm. | - |
| **tls1\_ck\_rsa\_with\_aes\_128\_sha** | Supports the TLS1\_CK\_RSA\_WITH\_AES\_128\_SHA algorithm. | - |
| **tls1\_ck\_dhe\_rsa\_with\_aes\_256\_sha** | Supports the TLS1\_CK\_DHE\_RSA\_WITH\_AES\_256\_SHA algorithm. | - |
| **tls1\_ck\_dhe\_dss\_with\_aes\_256\_sha** | Supports the TLS1\_CK\_DHE\_DSS\_WITH\_AES\_256\_SHA algorithm. | - |
| **tls1\_ck\_dhe\_rsa\_with\_aes\_128\_sha** | Supports the TLS1\_CK\_DHE\_RSA\_WITH\_AES\_128\_SHA algorithm. | - |
| **tls1\_ck\_dhe\_dss\_with\_aes\_128\_sha** | Supports the TLS1\_CK\_DHE\_DSS\_WITH\_AES\_128\_SHA algorithm. | - |
| **tls12\_ck\_rsa\_aes\_128\_cbc\_sha** | Supports the TLS12\_CK\_RSA\_AES\_128\_CBC\_SHA algorithm. | - |
| **tls12\_ck\_rsa\_aes\_256\_cbc\_sha** | Supports the TLS12\_CK\_RSA\_AES\_256\_CBC\_SHA algorithm. | - |
| **tls12\_ck\_rsa\_aes\_128\_cbc\_sha256** | Supports the TLS12\_CK\_RSA\_AES\_128\_CBC\_SHA256 algorithm. | - |
| **tls12\_ck\_rsa\_aes\_256\_cbc\_sha256** | Supports the TLS12\_CK\_RSA\_AES\_256\_CBC\_SHA256 algorithm. | - |
| **tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha** | Supports the TLS12\_CK\_DHE\_DSS\_AES\_128\_CBC\_SHA algorithm. | - |
| **tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha** | Supports the TLS12\_CK\_DHE\_RSA\_AES\_128\_CBC\_SHA algorithm. | - |
| **tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha** | Supports the TLS12\_CK\_DHE\_DSS\_AES\_256\_CBC\_SHA algorithm. | - |
| **tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha** | Supports the TLS12\_CK\_DHE\_RSA\_AES\_256\_CBC\_SHA algorithm. | - |
| **tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha256** | Supports the TLS12\_CK\_DHE\_DSS\_AES\_128\_CBC\_SHA256 algorithm. | - |
| **tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha256** | Supports the TLS12\_CK\_DHE\_RSA\_AES\_128\_CBC\_SHA256 algorithm. | - |
| **tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha256** | Supports the TLS12\_CK\_DHE\_DSS\_AES\_256\_CBC\_SHA256 algorithm. | - |
| **tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha256** | Supports the TLS12\_CK\_DHE\_RSA\_AES\_256\_CBC\_SHA256 algorithm. | - |
| **tls12\_ck\_rsa\_with\_aes\_128\_gcm\_sha256** | Supports the TLS12\_CK\_RSA\_WITH\_AES\_128\_GCM\_SHA256 algorithm. | - |
| **tls12\_ck\_rsa\_with\_aes\_256\_gcm\_sha384** | Supports the TLS12\_CK\_RSA\_WITH\_AES\_256\_GCM\_SHA384 algorithm. | - |
| **tls12\_ck\_dhe\_rsa\_with\_aes\_128\_gcm\_sha256** | Supports the TLS12\_CK\_DHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256 algorithm. | - |
| **tls12\_ck\_dhe\_rsa\_with\_aes\_256\_gcm\_sha384** | Supports the TLS12\_CK\_DHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 algorithm. | - |
| **tls12\_ck\_dhe\_dss\_with\_aes\_128\_gcm\_sha256** | Supports the TLS12\_CK\_DHE\_DSS\_WITH\_AES\_128\_GCM\_SHA256 algorithm. | - |
| **tls12\_ck\_dhe\_dss\_with\_aes\_256\_gcm\_sha384** | Supports the TLS12\_CK\_DHE\_DSS\_WITH\_AES\_256\_GCM\_SHA384 algorithm. | - |
| **tls12\_ck\_ecdhe\_rsa\_with\_aes\_128\_gcm\_sha256** | Supports the TLS12\_CK\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256 algorithm. | - |
| **tls12\_ck\_ecdhe\_rsa\_with\_aes\_256\_gcm\_sha384** | Supports the TLS12\_CK\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 algorithm. | - |
| **tls13\_aes\_128\_gcm\_sha256** | Supports the TLS1\_3\_RFC\_AES\_128\_GCM\_SHA256 algorithm. | - |
| **tls13\_aes\_256\_gcm\_sha384** | Supports the TLS1\_3\_RFC\_AES\_256\_GCM\_SHA384 algorithm. | - |
| **tls13\_chacha20\_poly1305\_sha256** | Supports the TLS1\_3\_RFC\_CHACHA20\_POLY1305\_SHA256 algorithm. | - |
| **tls13\_aes\_128\_ccm\_sha256** | Supports the TLS1\_3\_RFC\_AES\_128\_CCM\_SHA256 algorithm. | - |



Views
-----

SSL cipher suite customization view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When a server authenticates a client, an SSL cipher suite is provided for SSL algorithm negotiation. To specify encryption algorithms supported in an SSL cipher suite bound to an SSL policy, run the set cipher-suite command.

**Prerequisites**

An SSL cipher suite bound to an SSL policy has been created using the **ssl cipher-suite-list** command.

**Precautions**

* By default, an SSL cipher suite supports no encryption algorithm. If you run the **binding cipher-suite-customization** command to bind an SSL cipher suite to an SSL policy, the system displays a message indicating that the binding fails. In this case, you must run the ssl cipher-suite command to configure an encryption algorithm for the SSL cipher suite. If the configured encryption algorithms include only the RSA algorithm and the **cipher-suit exclude key-exchange rsa** command is run to exclude the RSA key exchange algorithm from an SSL policy, no encryption algorithm is available in the SSL policy cipher suite. When the **binding cipher-suite-customization** command is run to bind an SSL policy cipher suite to an SSL policy, the system still displays a message indicating that the binding fails. That is, if the **cipher-suit exclude key-exchange rsa** command is run to exclude the RSA key exchange algorithm from an SSL policy, the SSL policy cipher suite must support at least one non-RSA encryption algorithm.
* To allow multiple algorithms to be used in an SSL cipher suite, run this command multiple times.
* To delete multiple algorithms from an SSL policy cipher suite, run the undo cipher-suite command multiple times.
* The tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha, tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha256, tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha, tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha256, tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha, tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha256, tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha, tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha256, tls12\_ck\_rsa\_aes\_128\_cbc\_sha, tls12\_ck\_rsa\_aes\_128\_cbc\_sha256, tls12\_ck\_rsa\_aes\_256\_cbc\_sha, tls12\_ck\_rsa\_aes\_256\_cbc\_sha256, tls12\_ck\_rsa\_with\_aes\_128\_gcm\_sha256, tls12\_ck\_rsa\_with\_aes\_256\_gcm\_sha384, tls1\_ck\_dhe\_dss\_with\_aes\_128\_sha, tls1\_ck\_dhe\_dss\_with\_aes\_256\_sha, tls1\_ck\_dhe\_rsa\_with\_aes\_128\_sha, tls1\_ck\_dhe\_rsa\_with\_aes\_256\_sha, tls1\_ck\_rsa\_with\_aes\_128\_sha and tls1\_ck\_rsa\_with\_aes\_256\_sha algorithms are not recommended because they are of weak security.
* The tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha, tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha256, tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha, tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha256, tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha, tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha256, tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha, tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha256, tls12\_ck\_rsa\_aes\_128\_cbc\_sha, tls12\_ck\_rsa\_aes\_128\_cbc\_sha256, tls12\_ck\_rsa\_aes\_256\_cbc\_sha, tls12\_ck\_rsa\_aes\_256\_cbc\_sha256, tls12\_ck\_rsa\_with\_aes\_128\_gcm\_sha256, tls12\_ck\_rsa\_with\_aes\_256\_gcm\_sha384, tls1\_ck\_dhe\_dss\_with\_aes\_128\_sha, tls1\_ck\_dhe\_dss\_with\_aes\_256\_sha, tls1\_ck\_dhe\_rsa\_with\_aes\_128\_sha, tls1\_ck\_dhe\_rsa\_with\_aes\_256\_sha, tls1\_ck\_rsa\_with\_aes\_128\_sha, and tls1\_ck\_rsa\_with\_aes\_256\_sha parameters in this command can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.
* Under the same security conditions, compared with the ECDHE key exchange algorithm, the DHE key exchange algorithm occupies more CPU resources during negotiation. You are advised to preferentially use the ECDHE key exchange algorithm in the tls12\_ck\_ecdhe\_rsa\_with\_aes\_128\_gcm\_sha256 and tls12\_ck\_ecdhe\_rsa\_with\_aes\_256\_gcm\_sha384 cipher suites. In addition, configure elliptic curve parameters for brainpool and curve in the SSL policy that uses the cipher suite list.


Example
-------

# Specify TLS12\_CK\_DHE\_DSS\_WITH\_AES\_128\_GCM\_SHA256 and TLS12\_CK\_DHE\_DSS\_WITH\_AES\_256\_GCM\_SHA384 in an SSL cipher suite named test bound to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl cipher-suite-list test
[*HUAWEI-ssl-cipher-suite-list-test] set cipher-suite tls12_ck_dhe_dss_with_aes_128_gcm_sha256
[*HUAWEI-ssl-cipher-suite-list-test] set cipher-suite tls12_ck_dhe_dss_with_aes_256_gcm_sha384

```