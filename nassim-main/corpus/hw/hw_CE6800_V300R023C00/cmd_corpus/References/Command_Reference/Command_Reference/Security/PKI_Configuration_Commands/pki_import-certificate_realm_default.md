pki import-certificate realm default
====================================

pki import-certificate realm default

Function
--------



The **pki import-certificate realm default** command imports the CA or local certificate loaded before delivery to the default realm.




Format
------

**pki import-certificate** { **default\_ca** | **default\_local** } **realm** **default**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **default\_ca** | Indicate the preset CA certificate. | - |
| **default\_local** | Indicate the preset device certificate. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Before a device is delivered, the CA certificate and local certificate are loaded on the device and stored in the NVRAM. The initial certificate, which can function as the device identity, is imported to the default realm to ensure the security of the device and external communication.If you have not applied for a digital certificate, you can run this command to import the initial certificate to the default realm.




Example
-------

# Load the initial CA certificate from the NVRAM to the default realm.
```
<HUAWEI> system-view
[~HUAWEI] pki import-certificate default_ca realm default
Info: Succeeded in importing the certificate.

```

# Load the initial local certificate from the NVRAM to the default realm.
```
<HUAWEI> system-view
[~HUAWEI] pki import-certificate default_local realm default
Info: Succeeded in importing the certificate.

```