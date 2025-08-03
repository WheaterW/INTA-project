Creating a Signature File for the Description File
==================================================

Creating a Signature File for the Description File

#### Context

To ensure image security, the image description file must be digitally signed. The OAS uses the OpenPGP digital signature standard and the free open-source tool Gnu Privacy Guard (GnuPG) to generate keys and verify digital signatures. Most Linux distributions are pre-installed with the GnuPG tool. You are advised to use a fixed environment for operation to avoid repeated key generation.


#### Procedure

1. Generate the key of User1 as prompted.
   
   
   ```
   gpg --gen-key or gpg --full-generate-key
   ```
   
   The command format may vary according to the GnuPG version. For details, run the **gpg --help** command.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * The full featured key pair generation mode must be used to generate keys.
   * Only the key algorithm RSA is supported, and the recommended key length is 3072 bits or more.
   * For hash algorithms, SHA (256-bit or longer) is recommended.
2. Output the public key file of User1.
   
   
   ```
   gpg --armor --output public-key.txt --export User1
   ```
   
   **public-key.txt** is the exported public key file, and **--export** specifies the ID of the user who exports the public key.
3. Obtain the fingerprint of the public key of User1 for installing the public key on the device.
   
   
   ```
   gpg --fingerprint User1
   ```
4. Encrypt the description file **hellodocker\_manifest.xml** to generate **hellodocker\_manifest.xml.asc**.
   
   
   ```
   gpg --armor --detach-sign hellodocker_manifest.xml
   ```
5. Rename the generated **hellodocker\_manifest.xml.asc** file as **hellodocker\_manifest.sig**.