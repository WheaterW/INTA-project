ssl-policy
==========

ssl-policy

Function
--------



The **ssl-policy** command configures an SSL policy for an HTTP server.

The **undo ssl-policy** command deletes the SSL policy on an HTTP server.



By default, no SSL policy is configured on an HTTP server.


Format
------

**ssl-policy** *ssl-policy-name*

**undo ssl-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ssl-policy-name* | Specifies the name of an SSL policy. | The value is a string of 1 to 23 case-insensitive characters, without spaces. If an initial certificate is loaded to the PKI realm to which the specified SSL policy is bound, the certificate is delivered in interactive mode. |



Views
-----

Service-RESTCONF view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Conventional HTTP does not have any security mechanism. It transmits data in plaintext and does not verify the identities of communications parties. Therefore, data transmitted over HTTP may be tampered with. In applications that require high security, such as e-commerce and online banking, HTTP is inapplicable. To enhance security, run the ssl-policy command to specify an SSL policy for an HTTP server.

**Prerequisites**

The following configurations must have been complete before you run the ssl-policy command.

1. An SSL policy has been created and the SSL policy view is displayed using the **ssl policy policy-name** command in the system view.
2. A digital certificate or certificate chain has been loaded using the **certificate load** command in the SSL policy view.
3. The HTTPS listening function has been enabled using the **secure-server enable** command in the Service-Restconf view.

**Configuration Impact**

HTTP security is enhanced with the SSL security mechanisms, such as data encryption, identity verification, and message integrity check.

**Precautions**

An HTTP server can only have one SSL policy configured. If the ssl-policy command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Configure an SSL policy named policy1 for an HTTP server.
```
<HUAWEI> system-view
[~HUAWEI] http
[~HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] secure-server enable
[*HUAWEI-http-service-restconf] ssl-policy policy1

```

# Configure an SSL policy named policy1 on the HTTP server and load an initial certificate to the PKI realm bound to the specified SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] http
[~HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] secure-server enable
Warning: It will create the HTTP server listening socket after the source interface is configured.
[*HUAWEI-http-service-restconf] ssl-policy policy1
Warning: A preset certificate is loaded to the PKI domain bound to the specified SSL policy. The current operation has security risks. Continue? [Y/N]:Y

```