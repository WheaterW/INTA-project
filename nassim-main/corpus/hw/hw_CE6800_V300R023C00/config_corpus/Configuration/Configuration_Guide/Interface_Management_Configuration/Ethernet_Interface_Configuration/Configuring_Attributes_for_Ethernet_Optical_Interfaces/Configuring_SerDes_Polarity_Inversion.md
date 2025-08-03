Configuring SerDes Polarity Inversion
=====================================

Configuring SerDes Polarity Inversion

#### Context

When Huawei and non-Huawei 100GE ZR4 optical module (80 km) are connected, the interfaces cannot communicate because the mapping modes of the optical modules' data channels are different. In this case, you can configure SerDes polarity inversion so that the optical modules' data channels keep consistent, ensuring normal service running.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure SerDes polarity inversion.
   
   
   ```
   [optical pn-reverse enable](cmdqueryname=optical+pn-reverse+enable)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Only interfaces that have Huawei 100G ZR4 (80 km) optical modules installed support this command. If this command is run on an interface that has other media installed, the interface goes down due to SerDes P/N mismatch.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```