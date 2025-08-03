ssl policy
==========

ssl policy

Function
--------



The **ssl policy** command creates an SSL policy and displays the Secure Sockets Layer (SSL) policy view. If the SSL policy to be created already exists, running this command presents you the view of the SSL policy.

The **undo ssl policy** command deletes an SSL policy.



By default, no SSL policies are created.


Format
------

**ssl policy** *policy-name*

**undo ssl policy** *policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of an SSL policy. | The value is a string of 1 to 23 case-insensitive characters, containing letters, digits, and underscores (\_), spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to enter the SSL policy view and configure SSL services.

**Configuration Impact**

An SSL policy is created when the ssl policy command is used for the first time. The SSL policy is a mechanism for SSL message transmission.

**Follow-up Procedure**

After entering the SSL policy view, you can perform the following configurations:

* Run the **certificate load** command to load a certificate or a certificate chain.
* Run the **crl load** command to load a CRL.
* Run the **trusted-ca load** command to load a trusted-CA file.

**Precautions**

A maximum of six SSL policies can be configured.


Example
-------

# Create an SSL policy named policy1 and enter the view of the SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1

```