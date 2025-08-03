ssl-policy (GRPC client view)
=============================

ssl-policy (GRPC client view)

Function
--------



The **ssl-policy** command enables a client to perform SSL verification on a server.

The undo ssl-verify command disables a client from performing SSL verification on a server.



By default, no SSL policy is configured for a gRPC client.


Format
------

**ssl-policy** *ssl-policy-name* [ **verify-san** *san* ]

**undo ssl-policy** [ *ssl-policy-name* [ **verify-san** *san* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verify-san** *san* | Specifies the SAN name of the certificate on the server. | The value is a string of 1 to 255 case-sensitive characters. It cannot contain spaces. |
| **ssl-policy** *ssl-policy-name* | Specifies the name of an SSL policy. | The value is a string of 1 to 23 case-sensitive characters. It cannot contain spaces. |



Views
-----

GRPC client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When you create a gRPC-based static subscription, an insecure TCP connection is set up between the device functioning as a client and the collector functioning as a server. In this case, you can run the **ssl-policy** command to configure an SSL policy for the client to establish a secure SSL connection with the server.To ensure device information security, you are advised to load the obtained certificate to the SSL policy. It is not recommended to use the initial certificate.

**Prerequisites**

Ensure that the SSL policy has been created before you run the **ssl-policy** command.

**Precautions**

If the no-tls parameter has been configured by running the **ipv4-address port** or **ipv6-address port** command in the destination group view or **protocol** command in the subscription view and taken effect, the TLS encryption mode is not used. In this case, the client-specific SSL policy does not take effect.


Example
-------

# Configure an SSL policy named policy2 for a client during Telemetry static subscription.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy2
[*HUAWEI-ssl-policy-policy2] quit
[*HUAWEI] grpc
[*HUAWEI-grpc] grpc client
[*HUAWEI-grpc-client] ssl-policy policy2

```

# Display an alarm when the specified policy uses the default pki-domain configuration.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy2
[*HUAWEI-ssl-policy-policy2] pki-domain default
Warning: A preset certificate is loaded to the specified PKI domain. The current operation has security risks. Continue? [Y/N]:y
[*HUAWEI-ssl-policy-policy2] quit
[*HUAWEI] grpc
[*HUAWEI-grpc] grpc client
[*HUAWEI-grpc-client] ssl-policy policy2
Warning: A preset certificate is loaded to the PKI domain bound to the specified SSL policy. The current operation has security risks. Continue? [Y/N]:y
[*HUAWEI-grpc-client]

```