Confirmed Commit
================

This capability indicates that the device can confirm configurations. In other words, the <commit> message delivered in this instance does not directly commit the configuration and depends on the next <commit> message to trigger configuration commitment.

#### confirmed-commit:1.0

The <commit> operation can carry the <confirmed> and <confirm-timeout> parameters.

* <confirmed>: submits the configuration data in the <candidate/> configuration database and converts it into the running configuration data on a device (configuration data in the <running/> configuration database).
* <confirm-timeout>: specifies a timeout period for confirming the <commit> operation, in seconds. The default value is 600s. After the <commit> operation is performed, if the confirmation operation is not performed within the timeout period, the configuration in the <running/> configuration database is rolled back to the state before the <commit> operation is performed and the modified data in the <candidate/> configuration database is abandoned.

This capability is valid only when the device supports the candidate configuration capability. It is mainly used in service trial running and verification scenarios.

The following is an example of submitting the current configuration and setting the timeout period for confirming the <commit> operation to 120s.

* RPC request
  
  ```
  <?xml version="1.0" encoding="utf-8"?>
  <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <commit>
      <confirmed/>
      <confirm-timeout>120</confirm-timeout>
    </commit>
  </rpc>
  
  ```
* RPC reply
  
  ```
  <?xml version="1.0" encoding="utf-8"?>
  <rpc-reply xmlns:nc-ext="urn:huawei:yang:huawei-ietf-netconf-ext"
             xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"
             message-id="101"
             nc-ext:flow-id="29"
             nc-ext:flow-id-time="2022-05-11T10:19:30Z">
    <ok/>
  </rpc-reply>
  ```

#### confirmed-commit:1.1

* The <commit> operation can carry the <persist> and <persist-id> parameters.
  
  If a <confirmed-commit> message carries the <persist> parameter, the trial run operation created using <confirmed-commit> is still effective after the associated session is terminated. The device allows a message to carry the <persist-id> parameter to update an existing trial run operation.
  
  The following example shows how to carry the <persist> parameter in a message for the <commit> operation.
  
  RPC request
  
  ```
  <?xml version="1.0" encoding="utf-8"?>
  <rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="3">
    <commit>
      <confirmed/>
      <persist>123</persist>
    </commit>
  </rpc>
  ```
  
  RPC reply
  
  ```
  <?xml version="1.0" encoding="utf-8"?>
  <rpc-reply xmlns:nc-ext="urn:huawei:yang:huawei-ietf-netconf-ext"
             xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"
             message-id="3"
             nc-ext:flow-id="29"
             nc-ext:flow-id-time="2022-05-11T10:19:30Z">
    <ok/>
  </rpc-reply>
  ```
  
  The following example shows how to carry the <persist-id> parameter in a message for the <commit> operation.
  
  RPC request
  
  ```
  <?xml version="1.0" encoding="utf-8"?>
  <rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="2">
    <commit>
      <confirmed/>
      <persist-id>123</persist-id>
    </commit>
  </rpc>
  ```
  
  RPC reply
  
  ```
  <?xml version="1.0" encoding="utf-8"?>
  <rpc-reply xmlns:nc-ext="urn:huawei:yang:huawei-ietf-netconf-ext"
             xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"
             message-id="2"
             nc-ext:flow-id="29"
             nc-ext:flow-id-time="2022-05-11T10:19:30Z">
    <ok/>
  </rpc-reply>
  ```
* The <cancel-commit> operation is supported. The <persist-id> parameter can be carried to terminate the trial run operation being executed, which is created using <confirmed-commit> with the <persist> parameter.
  
  RPC request
  
  ```
  <?xml version="1.0" encoding="utf-8"?>
  <rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="2">
    <cancel-commit>
      <persist-id>IQ,d4668</persist-id>
    </cancel-commit>
  </rpc>
  ```
  
  RPC reply
  
  ```
  <?xml version="1.0" encoding="utf-8"?>
  <rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="2">
    <ok/>
  </rpc-reply>
  ```