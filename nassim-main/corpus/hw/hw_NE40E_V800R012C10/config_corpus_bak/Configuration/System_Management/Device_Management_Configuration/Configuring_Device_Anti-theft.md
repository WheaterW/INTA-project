Configuring Device Anti-theft
=============================

This section describes how to configure the device anti-theft function.

#### Context

Device anti-theft allows users to create a pair of public and private keys using an NMS for locking or unlocking devices. The public key is loaded to the device for enabling the anti-theft function, and the private key is used to generate an authorization file for unlocking the device. This pair of keys function as a lock attached to the device. The device can only be used with the correct keys. The anti-theft function effectively prevents devices from being stolen.


#### Pre-configuration Tasks

Before configuring device anti-theft, complete the following tasks:

* Load the required anti-theft license, anti-theft enabling file, and authorization file.
* Generate a public key and a private key using an NMS, and send the public key to the device.
* Configure the NMS as the destination host of trap messages using the [**snmp-agent target-host**](cmdqueryname=snmp-agent+target-host) command, and configure the device to communicate with the NMS through SNMPv2c or SNMPv3.

#### Procedure

1. Run [**anti-theft install enable file**](cmdqueryname=anti-theft+install+enable+file) *filename* in the user view
   
   
   
   Anti-theft is enabled.
2. Run [**anti-theft install authorization file**](cmdqueryname=anti-theft+install+authorization+file) *filename*
   
   
   
   A temporary anti-theft authorization file is installed.

#### Verifying the Configuration

Run the [**display anti-theft status**](cmdqueryname=display+anti-theft+status) command to check the anti-theft status.