Information Exchange Between RPs in an Anycast RP Application Is Abnormal
=========================================================================

Information Exchange Between RPs in an Anycast RP Application Is Abnormal

#### Fault Symptom

RPs in an anycast RP application fail to exchange (S, G) information registered to a local device with each other.

#### Possible Causes

Note the following precautions. If the following configuration requirements are not met, anycast RP will not perform correctly:

* In an anycast RP application, the address of an MSDP peer must differ from that of an anycast RP. The C-BSR and C-RP must be configured on different devices or interfaces.
* An MSDP peer performs the RPF check on a received SA message and then discards the message if the addresses of the local RP and the remote RP are the same.


#### Procedure

1. Check whether the RPs are correctly configured in the PIM view. In an anycast RP application, configure multiple RPs with the same address in a PIM-SM domain. Configure a loopback interface on each device to be deployed with anycast RP and assign the same IP address to the loopback interfaces.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
2. Check whether the [**originating-rp**](cmdqueryname=originating-rp) command is run in the MSDP view. The [**originating-rp**](cmdqueryname=originating-rp) command must be run on the anycast RP to replace the RP address contained in the SA message with the address of a specified interface.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
3. Check the C-BSR address and the anycast RP address to ensure they are different.