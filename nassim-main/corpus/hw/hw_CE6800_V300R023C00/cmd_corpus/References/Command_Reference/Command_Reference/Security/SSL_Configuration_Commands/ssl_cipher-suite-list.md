ssl cipher-suite-list
=====================

ssl cipher-suite-list

Function
--------



The **ssl cipher-suite-list** command creates an SSL cipher suite and displays the SSL cipher suite customization view.

The **undo ssl cipher-suite-list** command deletes the created SSL cipher suite.



By default, no SSL cipher suite is created.


Format
------

**ssl cipher-suite-list** *customization-policy-name*

**undo ssl cipher-suite-list** *customization-policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *customization-policy-name* | Specifies the name of an SSL cipher suite. | The value is a string of 1 to 32 case-insensitive characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

During client and server authentication, an algorithm list is provided for the client and server to perform SSL algorithm negotiation. To create an SSL cipher suite and enter the view for SSL algorithm configuration, run the ssl cipher-suite-list command.

**Follow-up Procedure**

Run the **set cipher-suite** command to specify encryption algorithms supported in an SSL cipher suite for an SSL policy.

**Precautions**

* By default, an SSL cipher suite supports no encryption algorithm. If you run the **binding cipher-suite-customization** command to bind an SSL cipher suite to an SSL policy, the system displays a message indicating that the binding fails. In this case, you must run the ssl cipher-suite command to configure an encryption algorithm for the SSL cipher suite. If the configured encryption algorithms include only the RSA algorithm and the **cipher-suit exclude key-exchange rsa** command is run to exclude the RSA key exchange algorithm from an SSL policy, no encryption algorithm is available in the SSL policy cipher suite. When the **binding cipher-suite-customization** command is run to bind an SSL policy cipher suite to an SSL policy, the system still displays a message indicating that the binding fails. That is, if the **cipher-suit exclude key-exchange rsa** command is run to exclude the RSA key exchange algorithm from an SSL policy, the SSL policy cipher suite must support at least one non-RSA encryption algorithm.
* To allow multiple algorithms to be used in an SSL cipher suite, run this command multiple times.
* To delete multiple algorithms from an SSL policy cipher suite, run the undo cipher-suite command multiple times.
* The following algorithms are insecure and are not recommended: tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha, tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha256, tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha, tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha256, tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha, tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha256, tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha, tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha256, tls12\_ck\_rsa\_aes\_128\_cbc\_sha, tls12\_ck\_rsa\_aes\_128\_cbc\_sha256, tls12\_ck\_rsa\_aes\_256\_cbc\_sha, tls12\_ck\_rsa\_aes\_256\_cbc\_sha256, tls12\_ck\_rsa\_with\_aes\_128\_gcm\_sha256, tls12\_ck\_rsa\_with\_aes\_256\_gcm\_sha384, tls1\_ck\_dhe\_dss\_with\_aes\_128\_sha, tls1\_ck\_dhe\_dss\_with\_aes\_256\_sha, tls1\_ck\_dhe\_rsa\_with\_aes\_128\_sha, tls1\_ck\_dhe\_rsa\_with\_aes\_256\_sha, tls1\_ck\_rsa\_with\_aes\_128\_sha and tls1\_ck\_rsa\_with\_aes\_256\_sha.
* The tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha, tls12\_ck\_dhe\_dss\_aes\_128\_cbc\_sha256, tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha, tls12\_ck\_dhe\_dss\_aes\_256\_cbc\_sha256, tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha, tls12\_ck\_dhe\_rsa\_aes\_128\_cbc\_sha256, tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha, tls12\_ck\_dhe\_rsa\_aes\_256\_cbc\_sha256, tls12\_ck\_rsa\_aes\_128\_cbc\_sha, tls12\_ck\_rsa\_aes\_128\_cbc\_sha256, tls12\_ck\_rsa\_aes\_256\_cbc\_sha, tls12\_ck\_rsa\_aes\_256\_cbc\_sha256, tls12\_ck\_rsa\_with\_aes\_128\_gcm\_sha256, tls12\_ck\_rsa\_with\_aes\_256\_gcm\_sha384, tls1\_ck\_dhe\_dss\_with\_aes\_128\_sha, tls1\_ck\_dhe\_dss\_with\_aes\_256\_sha, tls1\_ck\_dhe\_rsa\_with\_aes\_128\_sha, tls1\_ck\_dhe\_rsa\_with\_aes\_256\_sha, tls1\_ck\_rsa\_with\_aes\_128\_sha, and tls1\_ck\_rsa\_with\_aes\_256\_sha parameters in this command can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.
* Under the same security conditions, compared with the ECDHE key exchange algorithm, the DHE key exchange algorithm occupies more CPU resources during negotiation. You are advised to preferentially use the ECDHE key exchange algorithm in the tls12\_ck\_ecdhe\_rsa\_with\_aes\_128\_gcm\_sha256 and tls12\_ck\_ecdhe\_rsa\_with\_aes\_256\_gcm\_sha384 cipher suites. In addition, configure elliptic curve parameters for brainpool and curve in the SSL policy that uses the cipher suite list.


Example
-------

# Create an SSL cipher suite named test.
```
<HUAWEI> system-view
[~HUAWEI] ssl cipher-suite-list test

```