client ssl-policy
=================

client ssl-policy

Function
--------



The **client ssl-policy** command configures an SSL policy for an HTTP client.

The **undo client ssl-policy** command deletes the SSL policy on an HTTP client.



By default, no SSL policy is configured on an HTTP client.


Format
------

**client ssl-policy** *policy-name*

**undo client ssl-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of an SSL policy. | The value is a string of 1 to 23 case-insensitive characters, without spaces. If an initial certificate is loaded to the PKI realm to which the specified SSL policy is bound, the certificate is delivered in interactive mode. |



Views
-----

HTTP view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Legacy HTTP does not have any security mechanism. It transmits data in simple text and does not verify the identities of communicating parties. Therefore, data transmitted over HTTP may be tampered with. In applications that require high security, such as e-commerce and online banking, HTTP is inapplicable. To enhance security, run the client ssl-policy command to configure an SSL policy for an HTTP client.

**Prerequisites**

* An SSL policy has been created and the SSL policy view is displayed using the **ssl policy** command in the system view.
* A digital certificate or certificate chain has been loaded using the **certificate load** command in the SSL policy view.

**Configuration Impact**

HTTP security is enhanced with the SSL security mechanisms, such as data encryption, identity verification, and message integrity check.

**Precautions**

An HTTP client can only have one SSL policy configured. If the client ssl-policy command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Configure an SSL policy named policy1 on the HTTP client and load an initial certificate to the PKI realm bound to the specified SSL policy.
```
[~HUAWEI] http
[~HUAWEI-http] client ssl-policy policy1
Warning: A preset certificate is loaded to the PKI domain bound to the specified SSL policy. The current operation has security risks. Continue? [Y/N]:Y

```

# Configure an SSL policy named policy1 for an HTTP client.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1
[*HUAWEI-ssl-policy-policy1] certificate load pem-cert a_servercertchain2_pem_dsa.pem key-pair dsa key-file a_serverkeychain2_pem_dsa.pem auth-code cipher YsHsjx_202206
[*HUAWEI-ssl-policy-policy1] quit
[*HUAWEI] http
[*HUAWEI-http] client ssl-policy policy1

```