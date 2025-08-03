Configuration Precautions for Access to Other Devices
=====================================================

Configuration Precautions for Access to Other Devices

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Create an SSL policy. The default DH modulus is 3072, and the value can be 2048, 3072, or 4096. By default, ed25519, ed448, rsa-pss-pss-sha256, rsa-pss-pss-sha384, rsa-pss-pss-sha512, rsa-pss-rsae-sha256, rsa-pss-rsae-sha384 and rsa-pss-rsae-sha512 are enabled for signature algorithms, which can be configured separately to enhance security.  After an SSL policy is created, if the SSL handshake fails because the signature algorithm does not match or the DH modulus length is too long, run the diffie-hellman modulus command to adjust the DH modulus length or run the signature algorithm-list command to adjust the signature algorithm. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The SCP cannot interwork with the WinSCP tool. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The size of the SSL certificate file (identity certificate, CA, and CRL) cannot exceed 50 KB. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When SSL certificates are used, a maximum of one certificate, four trust certificates, and two CRLs can be loaded to an SSL policy.  When certificates in a PKI domain are used, an SSL policy can use a maximum of one certificate, 64 trust certificates, and 64 CRLs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The maximum length of an HTTP request line is 8192 bytes. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The total size of HTTP request packet headers is 4096 bytes. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The SCP cannot interwork with the WinSCP tool. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |