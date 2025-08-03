Configuring the DS-Lite ALG Function
====================================

The IP packets of some protocols, such as FTP and ICMP, contain IP addresses and port numbers in the data field. To implement DS-Lite translation for these protocol packets, you need to enable the DS-Lite ALG function.

#### Usage Scenario

DS-Lite translates only the IP addresses contained in user data packets and the port information in the TCP/UDP headers of data packets. For special protocols, for example, FTP, the Data field in a packet contains IP address or port information. If the IP address or port information in the data field is not translated, inconsistency and errors occur. A good way to solve the DS-Lite translation issue for these special protocols is to use the ALG function. Functioning as a special conversion agent for application protocols, the ALG interacts with the DS-Lite device to establish states. The ALG uses DS-Lite state information to change the specific data in the Data field of IP packets and to complete other necessary work, so that application protocols can run across internal and external networks.

#### Pre-configuration Tasks

Before configuring DS-Lite ALG, complete the following tasks:

* Configure basic DS-Lite functions.
* Configure distributed or centralized DS-Lite translation function.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Enable the DS-Lite ALG function in the DS-Lite instance view or the NAT policy template view:
   1. Enable the DS-Lite ALG function in the DS-Lite instance view.
      
      
      1. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
         
         The DS-Lite instance view is displayed.
      2. Run [**ds-lite alg**](cmdqueryname=ds-lite+alg) { **all** | **ftp** [ **rate-threshold** *rate-threshold-value* ] | **pptp** | **rtsp** | **sip** [ **separate-translation** ] }
         
         The DS-Lite ALG function is enabled for one or more application layer protocols.
         
         To configure DS-Lite for the SIP control channel and data channel separately, run the [**ds-lite alg**](cmdqueryname=ds-lite+alg) **sip** **separate-translation** command.
      3. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.
   2. Enable the DS-Lite ALG function in the NAT policy template view.
      
      
      1. Run [**nat-policy template**](cmdqueryname=nat-policy+template) *template-name* A NAT policy template is configured.
      2. Run [**nat alg**](cmdqueryname=nat+alg) { **all** | **ftp** | **pptp** | **rtsp** | **sip** } The DS-Lite ALG function is enabled for one or more application layer protocols.
         
         ![](../../../../public_sys-resources/note_3.0-en-us.png) 
         
         In VS mode, this configuration process is supported only by the admin VS.
      3. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The configurations in a NAT policy template take effect only after the NAT policy template is issued by a RADIUS server. If packets of users to go online match the NAT policy template, the configuration in the template takes effect on the users.
      
      If the DS-Lite ALG function is enabled in the DS-Lite instance view and the NAT policy template view, the later configuration takes effect.

#### Verifying the Configuration

After configuring the DS-Lite ALG function, you can run the display commands to check the DS-Lite instance configuration or NAT policy template.

* Run the [**display ds-lite instance**](cmdqueryname=display+ds-lite+instance) [ *instance-name* ] command to check the ALG configuration of a DS-Lite instance.
* Run the [**display nat-policy template**](cmdqueryname=display+nat-policy+template) [ *template-name* ] command to check the ALG configuration in a NAT policy template.