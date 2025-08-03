Configuration Precautions for PKI
=================================

Configuration Precautions for PKI

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Preset certificates are used only for SZTP deployment and initial trust of QX services. It cannot be used as service authentication credentials after system running. It is recommended that customer certificates be used for other applications. Users are liable for security risks caused by long-term use of preset certificates, such as certificate expiration and update failure. It is recommended that customers deploy the PKI system to issue certificates to devices and software on the live network and manage the certificate lifecycle. For details, see Router Security Hardening Policies > Level-1 Security Hardening Policies (Mandatory) > Management Plane > Digital Certificate Management. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If the current version is downgraded to a version earlier than V800R021C00, run the dir ca\_config.ini command in the user view to query the size of the PKI configuration file. If the file size exceeds 19 KB, the PKI certificate cannot be imported or deleted after the downgrade. Therefore, you need to delete some certificates before the downgrade to ensure that the file size is less than 19 KB. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| A PKI reserved domain cannot be bound to or modified for services. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |