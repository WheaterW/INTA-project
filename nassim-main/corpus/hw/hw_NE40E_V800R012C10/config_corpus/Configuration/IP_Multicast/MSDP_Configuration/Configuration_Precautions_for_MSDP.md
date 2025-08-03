Configuration Precautions for MSDP
==================================

Configuration Precautions for MSDP

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Before configuring a local RP to send SA Request messages, disable the SA caching function on the local RP and ensure that the SA caching function is enabled on the MSDP peer specified by peer-address. Otherwise, the configuration fails. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The password must be at least eight characters long and contains at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters. Otherwise, the configuration fails. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MSDP MD5 authentication and MSDP keychain authentication are mutually exclusive. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MSDP is applicable only to PIM-SM and is valid only for the Any-Source Multicast (ASM) model. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |