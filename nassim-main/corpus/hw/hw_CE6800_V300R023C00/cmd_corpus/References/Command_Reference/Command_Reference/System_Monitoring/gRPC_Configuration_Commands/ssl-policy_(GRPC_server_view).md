ssl-policy (GRPC server view)
=============================

ssl-policy (GRPC server view)

Function
--------



The **ssl-policy** command configures an SSL policy for the gRPC service.

The **undo ssl-policy** command deletes an SSL policy of the gRPC service.



By default, no SSL policy is configured for the gRPC service.


Format
------

**ssl-policy** *ssl-policy-name*

**undo ssl-policy** [ *ssl-policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ssl-policy-name* | Specifies the name of an SSL policy. The value must be the name of an existing SSL policy. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |



Views
-----

GRPC server view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a collector functioning as a client initiates a connection to a device functioning as a server, the data sampled is dynamically subscribed to. In this case, you can configure an SSL policy for the gRPC service. This ensures that a secure SSL connection can be established between the server and client.To ensure device information security, you are advised to load the obtained certificate to the SSL policy. It is not recommended to use the initial certificate.

**Prerequisites**

The SSL policy has been created.


Example
-------

# Configure the SSL policy named policy1 for the gRPC service during Telemetry dynamic subscription.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1
[*HUAWEI-ssl-policy-policy1] quit
[*HUAWEI] grpc
[*HUAWEI-grpc] grpc server
[*HUAWEI-grpc-server] ssl-policy policy1

```

# Display an alarm when the specified policy uses the default pki-domain configuration.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy2
[*HUAWEI-ssl-policy-policy2] pki-domain default
Warning: A preset certificate is loaded to the specified PKI domain. The current operation has security risks. Continue? [Y/N]:y
[*HUAWEI-ssl-policy-policy2] quit
[*HUAWEI] grpc
[*HUAWEI-grpc] grpc server
[*HUAWEI-grpc-server] ssl-policy policy2
Warning: A preset certificate is loaded to the PKI domain bound to the specified SSL policy. The current operation has security risks. Continue? [Y/N]:y
[*HUAWEI-grpc-server]

```