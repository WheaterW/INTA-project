Sync
====

This capability enables a device to perform full or incremental data synchronization. Through data synchronization, the NMS or controller that manages network devices can have the same configuration data with NEs in real time.

#### Full Synchronization

The <sync-full> operation requests a device to implement full data synchronization. After the NMS connects to an NE for the first time, it synchronizes all data of the NE to the NMS.

The YANG model defines the capability in the **huawei-netconf-sync.yang** file.

After the server receives an <rpc> element containing a <sync-full> element, the server performs a syntax check on the <rpc> element. If the element fails the syntax check, the server returns an <rpc-reply> element containing an <rpc-error> element to terminate processing. Otherwise, the server responds with <rpc-reply>, obtains the synchronization data, encapsulates the data in XML format, writes the data into XML files by feature, compresses the data into a .zip file, and automatically transfers the file to the specified directory through FTP or SFTP. SFTP is recommended because it is more secure than FTP.

Full synchronization supports the following functions:

* Cancels a specific full data synchronization operation.
* Uploads a full data synchronization file.
* Queries the file upload progress.

Example of full data synchronization: The server uses FTP to automatically transfer AAA module configurations in the obtained full synchronization data to the home directory of the user **root** (password: **YsHsjx\_202206**) on the server whose IP address is 10.1.1.1. The data is saved as a file named **Multi\_App\_sync\_full.zip**.

* RPC request
  
  ```
  <?xml version="1.0" encoding="utf-8"?>
  <rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="4">
    <sync-full xmlns="urn:huawei:yang:huawei-netconf-sync">
      <target>
        <user-name>root</user-name>
        <password>YsHsjx_202206</password>
        <target-addr>10.1.1.1</target-addr>
        <path>/home</path>
      </target>
      <transfer-protocol>ftp</transfer-protocol>
      <transfer-method>auto</transfer-method>
      <filename-prefix>Multi_App_sync_full</filename-prefix>
      <app-err-operation>stop-on-error</app-err-operation>
      <filter>
        <aaa xmlns="urn:huawei:yang:huawei-aaa"/>
      </filter>
    </sync-full>
  </rpc>
  
  ```
* RPC reply
  
  The RPC reply message carries a full data synchronization identifier assigned by the NETCONF server. This message is returned using the <sync-full-id> parameter.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  After full synchronization is triggered, the RPC reply message sent by the device carries the nc-ext attribute.
  
  ```
  <?xml version="1.0" encoding="utf-8"?>
  <rpc-reply xmlns:nc-ext="urn:huawei:yang:huawei-ietf-netconf-ext"
             xmlns:nc-sync="urn:huawei:yang:huawei-netconf-sync"
             xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"
             message-id="2"
             nc-ext:flow-id="32">
    <nc-sync:sync-full-id>185</nc-sync:sync-full-id>
  </rpc-reply>
  
  ```

The following is an example of using the cancel-synchronization operation to cancel full synchronization with sync-full-id being 185.

* RPC request
  
  ```
  <rpc message-id="cancel" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <cancel-synchronization xmlns="urn:huawei:yang:huawei-netconf-sync">
      <sync-full-id>185</sync-full-id>
    </cancel-synchronization>
  </rpc>
  ```
* RPC reply
  
  ```
  Success reply
  <?xml version="1.0" encoding="UTF-8"?>
  <rpc-reply message-id="cancel" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <ok/>
  </rpc-reply>
  ```

The following is an example of uploading the full synchronization file through the upload-sync-file operation.

* RPC request
  
  ```
  <rpc message-id="upload" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <upload-sync-file xmlns="urn:huawei:yang:huawei-netconf-sync"> 
      <sync-full-id>185</sync-full-id>
      <result-save-time>1</result-save-time>        
    </upload-sync-file>
  </rpc>
  ```
* RPC reply
  
  ```
  <?xml version="1.0" encoding="UTF-8"?>
  <rpc-reply message-id="upload" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <ok/>
  </rpc-reply>
  ```

The following is an example of using the <get> operation to query the file upload progress.

* RPC request
  
  ```
  <rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="query_status185">
    <get>
      <filter type="subtree">
        <synchronization xmlns="urn:huawei:yang:huawei-netconf-sync">
          <file-transfer-statuss>
            <file-transfer-status>
              <sync-full-id>185</sync-full-id>
              <status></status>
              <progress></progress>
              <error-message></error-message>
            </file-transfer-status>
          </file-transfer-statuss>
        </synchronization>
      </filter>
    </get>
  </rpc>
  ```
* RPC reply
  
  ```
  <?xml version="1.0" encoding="UTF-8"?>
  <rpc-reply message-id="query_status12" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <data>
      <synchronization xmlns="urn:huawei:yang:huawei-netconf-sync">
        <file-transfer-statuss>
          <file-transfer-status>
            <sync-full-id>12</sync-full-id>
            <status>In-Progress</status>
            <progress>50</progress>
          </file-transfer-status>
        </file-transfer-statuss>
      </synchronization>
    </data>
  </rpc-reply>
  ```


#### Incremental Synchronization

The <sync-increment> operation requests a device to synchronize incremental configuration data. When the configuration changes, the client detects the change through the configuration change identifier flow-id. Each time the configuration changes, the value of **flow-id** increases by 1. If the client needs to obtain the modified configuration, it synchronizes data incrementally.

If the <sync-increment> operation succeeds, the NETCONF server replies with an <rpc-reply> element that contains the <data> element. The <data> element contains the data that was changed between two configuration committing operations. If the operation fails, the server returns an <rpc-reply> element containing an <rpc-error> element.

<sync-increment> uses the difference attribute to identify the change operation of a configuration data instance. The YANG model defines the capability in the **huawei-netconf-metadata.yang** file.

The following is an example of an incremental data synchronization operation that synchronizes IFM module configurations between change points 6 and 7.

* RPC request
  
  ```
  <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> 
    <sync-increment xmlns="urn:huawei:yang:huawei-netconf-sync"> 
      <target> 
        <flow-id>7</flow-id> 
      </target> 
      <source> 
        <flow-id>6</flow-id> 
      </source> 
      <filter> 
        <ifm xmlns="urn:huawei:yang:huawei-ifm"/> 
      </filter> 
    </sync-increment> 
  </rpc>
  ```
* RPC reply
  
  ```
  <rpc-reply xmlns:nc-md="urn:huawei:yang:huawei-netconf-metadata"> 
    <data xmlns="urn:huawei:yang:huawei-netconf-sync"> 
      <ifm xmlns="urn:huawei:yang:huawei-ifm"> 
         <interfaceName>Vlanif 1</interfaceName> 
            <ifAm4s> 
              <ifAm4 nc-md:difference="create"> 
                <ipAddress>10.1.1.1</ipAddress> 
                <netMask>255.255.255.0</netMask> 
                <addressType/> 
              </ifAm4> 
            </ifAm4s> 
          </interface> 
        </interfaces> 
      </ifm> 
    </data> 
  </rpc-reply>
  ```