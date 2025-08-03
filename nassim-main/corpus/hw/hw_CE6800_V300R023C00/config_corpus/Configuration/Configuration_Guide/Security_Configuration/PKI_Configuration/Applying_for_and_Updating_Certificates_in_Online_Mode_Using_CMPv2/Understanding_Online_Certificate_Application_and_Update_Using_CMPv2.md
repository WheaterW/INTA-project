Understanding Online Certificate Application and Update Using CMPv2
===================================================================

If a device can access a Certificate Authority (CA) that supports the Certificate Management Protocol version 2 (CMPv2), the device can apply for and update its local certificate using CMPv2.

#### Certificate Application

Certificate application, also known as certificate enrollment, is a process in which a PKI entity introduces itself to a CA, which then issues it a certificate. You can apply for a local certificate in online mode using CMPv2. As such, the CA creates a certificate for the PKI entity based on the certificate enrollment request. After the local certificate is created, the CA automatically saves it to the **flash:/pki/public** directory of the device. You can then manually save the local certificate to the device memory.

To obtain a local certificate online, you need to configure PKI entity information, configure an RSA key pair, install the CA certificate, apply for the local certificate, and install the local certificate. [Figure 1](#EN-US_CONCEPT_0000001513046026__fig_dc_fd_pki_000901) shows the process of applying for a certificate in online mode using CMPv2.

**Figure 1** Process of applying for a certificate in online mode using CMPv2  
![](figure/en-us_image_0000001564126153.png)

1. Create a public/private key pair on DeviceA. The public key information is required during certificate application.
2. Create entity information. When applying for a certificate, DeviceA must provide the CA with information that can prove its identity. The entity information represents identity information, including the common name, fully qualified domain name (FQDN), IP address, and email address. The common name is mandatory, while others are optional.
3. Install a CA certificate. From the installed CA certificate, the PKI entity can obtain the CA's public key required to be carried in a certificate enrollment request.
4. The PKI entity sends a certificate enrollment request to the CA.
   
   Applying for a local certificate using CMPv2 covers two scenarios: initial and non-initial local certificate application. In initial local certificate application, an initialization request (IR) is used. After creating a local certificate, the CA returns the CA certificate together with the local certificate. In signature-based non-initial local certificate application, the PKI entity is authenticated based on the signature and the CA returns only the local certificate, not the CA certificate.
   
   * Initial local certificate application using an IR
     
     A CMPv2 server can use either of the following methods to authenticate a PKI entity when a local certificate is requested for the first time:
     
     + Message authentication code: The device and CMPv2 server share a reference value and secret value of the message authentication code. When applying for the local certificate for the first time, the device adds these two values to a certificate enrollment request and sends the request to the CMPv2 server. Then the CMPv2 server validates the two values to authenticate the device.
     + Signature: When the device has an external identity certificate (local certificate issued by another CA) and sends a certificate enrollment request to the CA, the device uses the private key of this external identity certificate for signature.
   * Signature-based non-initial local certificate application using a CR
     
     This method is applicable to the scenario where the device has an external identity certificate and needs to apply for a local certificate. When sending a certificate enrollment request to the CA, the device uses the private key of the external identity certificate for signature.
5. The CA creates a certificate based on the certificate enrollment request, which is **DeviceA.cer** for DeviceA.
6. The CA automatically uploads **DeviceA.cer** to the **flash:/pki/public** directory on Device A.
7. Manually import the certificate to the memory of DeviceA.

#### Certificate Update

When a PKI entity's certificate expires or the certificate key is disclosed, the PKI entity must replace the certificate. In this case, a new application is required for updating the certificate. Two methods are available for updating the local certificate using CMPv2:

* Manual certificate update using a key update request (KUR)
  
  A KUR, also called a certificate update request, is used to update the device's existing certificate that is not expired and not revoked. During the update, the device uses the existing certificate for identity authentication, and can use the new or previous public key to update the local certificate.
* Automatic certificate update
  
  To prevent service interruptions, you must apply for a new certificate before the existing certificate expires. If manually updating the certificate, the user may forget to do so. To avoid this problem, the device supports automatic certificate update. With this function enabled, the device initiates a certificate update request to the CMPv2 server when it detects that the certificate automatic update time expires. The newly obtained certificate will replace both the certificate file in the device storage and the certificate in the device memory, without interrupting services.
  
  In this mode, the local certificate requested using an IR or updated using a KUR can be automatically updated.