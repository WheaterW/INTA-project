(Optional) Loading a Digital Signature Certificate Revocation List (CRL)
========================================================================

(Optional) Loading a Digital Signature Certificate Revocation List (CRL)

#### Prerequisites

Before loading a CRL, you have completed the following task:

* Upload the CRL to the flash path of the device.

#### Context

If an issued digital signature certificate needs to be revoked due to key disclosure or other reasons, a third-party tool can be used to mark the certificate invalid and add the certificate to the CRL. After you load the latest CRL to a device, the device does not verify the digital signature certificate upon the next startup.


#### Procedure

1. Load a CRL file to the system.
   
   
   ```
   [software crl load](cmdqueryname=software+crl+load) crl-name
   ```

#### Verifying the Configuration

Run the [**display software crl**](cmdqueryname=display+software+crl) command to check information about the loaded CRL file.