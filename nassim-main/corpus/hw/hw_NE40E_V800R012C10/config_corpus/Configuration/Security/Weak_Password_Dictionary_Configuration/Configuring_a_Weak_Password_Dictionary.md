Configuring a Weak Password Dictionary
======================================

A device provides the function of weak password dictionary maintenance. With this function, you can configure a weak password dictionary containing prohibited passwords in advance and load the dictionary to the device.

#### Prerequisites

The weak password dictionary to be loaded has been generated in .txt format and uploaded to the device.


#### Procedure

1. Run [**load security weak-password-dictionary**](cmdqueryname=load+security+weak-password-dictionary) *filePath*
   
   
   
   A weak password dictionary is loaded.

#### Verifying the Configuration

After completing the configuration, verify it.

Run the [**display security weak-password-dictionary**](cmdqueryname=display+security+weak-password-dictionary) command to check the weak password dictionary.