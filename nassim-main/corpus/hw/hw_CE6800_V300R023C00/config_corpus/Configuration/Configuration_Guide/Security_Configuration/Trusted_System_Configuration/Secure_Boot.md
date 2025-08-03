Secure Boot
===========

Secure Boot

#### Context

A communication device comprises several embedded computer systems, which are susceptible to virus attacks, tampering, and exploitation of vulnerabilities by malicious actors through the use of Trojan horses.

The secure boot function prohibits system boot in case of any damage to the system software, improving system security and reliability.


#### Related Concepts

A trusted system is one in which the hardware and software are functioning as intended and designed. To ensure a system is trustworthy, it is essential that the software integrity is of the highest level, preventing any unauthorized modifications or intrusions.


#### Fundamentals

Most boards that support secure boot have it enabled by default to ensure a trusted system. However, for certain boards, manual activation of secure boot is required.

Secure boot establishes a root of trust (RoT) for the platform by utilizing device hardware capabilities, unalterable initial boot code, and signature verification keys.

As shown in [Figure 1](#EN-US_CONCEPT_0000001559855426__dc_vrp_dcn_feature_000201), during the system boot process, the trust root, BIOS, Bootloader, OS kernel, and system software package are booted in that order, with each level measuring the file trustworthiness of the next level. If the file trustworthiness of one component fails the verification, the component cannot be booted.

If the BIOS verification step or any preceding steps fail, the device must be returned to the manufacturer for resolution. If the BIOS verification passes, but any subsequent verification fails, you can enter the BootROM menu by pressing **Ctrl**+**B**. From there, you can replace the system software package and reboot the device to resolve the issue.

**Figure 1** Secure boot process  
![](figure/en-us_image_0000001559536378.png "Click to enlarge")

#### Benefits

The secure boot function brings the following security benefits:

* Trust the software system of the device that can be properly booted.
* Prohibit the boot of the device on which the software system is detected as untrustworthy.