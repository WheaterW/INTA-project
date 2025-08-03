Obtaining and Saving .proto Files and Tools
===========================================

Obtaining and Saving .proto Files and Tools

#### Procedure

1. Obtain .proto files.
   
   
   
   The method of downloading .proto files is similar to that of downloading device system software packages.
   
   1. Visit Huawei enterprise technical support website ([https://support.huawei.com/enterprise](https://support.huawei.com/enterprise/en/index.html)) or Huawei carrier technical support website ([https://support.huawei.com/carrier](https://support.huawei.com/carrierindex/en/hwe/index.html)), and search for the device model of the required version.
   2. Access the software download page and obtain .proto files of the required version.
   
   The .proto files include **huawei-grpc-dialout.proto**, **huawei-ifm.proto** for interconnection adaption, and **huawei-telemetry.proto**.
2. Obtain tools.
   
   
   1. Obtain protoc v3.0.2 for .proto file processing. Use the tool to generate message objects and serialized and deserialized Java code based on the .proto files.
      
      Download this tool at <https://repo1.maven.org/maven2/com/google/protobuf/protoc/3.0.2/>.
      
      For example, download the **protoc-3.0.2-windows-x86\_64.exe** file to the local PC.
   2. Obtain the protoc-gen-grpc-java v1.0.1 plug-in, which is used to generate Java code defined by RPC.
      
      Download this plug-in at <https://repo1.maven.org/maven2/io/grpc/protoc-gen-grpc-java/1.0.1/>.
      
      For example, download the **protoc-gen-grpc-java-1.0.1-windows-x86\_64.exe** file to the local PC.
3. Save .proto files and tools.
   
   
   
   The following example describes the directories where .proto files and tools are stored.
   
   ```
   E:\telemetryJava>dir /s 
    Volume in drive E is mail 
    Volume Serial Number is FCEF-436A 
   
    Directory of E:\telemetryJava 
   
   2018/05/02  20:05    <DIR>          . 
   2018/05/02  20:05    <DIR>          .. 
   2018/05/02  20:05    <DIR>          proto 
   2017/11/23  16:34         3,988,480 protoc-3.0.2-windows-x86_64.exe 
   2017/11/23  16:35         1,906,176 protoc-gen-grpc-java-1.0.1-windows-x86_64.exe 
                  2 File(s)      5,894,656 bytes 
   
    Directory of E:\telemetryJava\proto 
   
   2018/05/02  20:05    <DIR>          . 
   2018/05/02  20:05    <DIR>          .. 
   2017/07/06  09:53               291 huawei-grpc-dialout.proto 
   2017/11/10  10:49             4,909 huawei-ifm.proto 
   2017/07/26  19:29               701 huawei-telemetry.proto 
                  3 File(s)          5,901 bytes 
   
        Total Files Listed: 
                  5 File(s)      5,900,557 bytes 
                  5 Dir(s)  25,729,437,696 bytes free 
   
   E:\telemetryJava>
   ```