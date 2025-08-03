Security Audit
==============

Security Audit

#### Context

Security audit covers identifying, recording, storing, and analyzing information related to security behaviors. The security audit result is used to determine which security behaviors are performed and which users are responsible for these behaviors.

Information required for security audit is saved as security logs, which must be stored separately and allocated with independent security channels. The security level of such logs must be higher than that of common logs to prevent the logs from being tampered with, deleted, or deciphered. Once the device is attacked, these logs need to be used for attack source tracing.

Security logs include operation logs involving system startup verification, account login (such as AAA logs), account management, network security event recording, and certificate key management.


#### Procedure

If a device is attacked or the system of a device is insecure, run the **display logfile cfcard:/logfile/security/security.log** command in the system view to check the corresponding log based on the log ID and determine whether unauthorized access occurs at the specified time point during system running.


Run the **display logfile cfcard:/logfile/security/security.log** command to check details about a security log, including the log generation date and time, event type, event content, and event triggering source.

```
<HUAWEI> display logfile cfcard:/logfile/security/security.log
###############################################################################
#     This logfile is generated at slot 1
#     Digest(0000029124):aea3e0df5dd7b86e5db512c1f67d950299e1f88e3b605526ddc3bcc2c50acac4                
###############################################################################
Jun 11 2019 07:41:21 HUAWEI %%01OPS/5/OPS_LOGIN(s):CID=0x80b40431;Succeeded in establishing the OPS connection.(ServiceType=embedding-script, UserName=_SYSTEM_, Ip=0.0.0.0, VpnName=_public_)
```