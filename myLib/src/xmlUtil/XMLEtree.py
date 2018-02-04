'''
Created on 2014-1-9

@author: zhangshaojun


'''
#import xml.etree.cElementTree as ET  #// GBK support question
import xml.etree.ElementTree as ET


def prt_vlist(vlist):
    '''
    '''
    for val in vlist:
        print(val)

class ETUtil(object):
    '''
    classdocs
    '''
    
    def __init__(self, xmlstr, xmlcode='UTF-8'):
        '''
        Constructor
        '''
        if xmlcode.upper() != 'UTF-8':
            str1 = xmlstr.replace(xmlcode, 'UTF-8')
            if xmlcode.upper() != 'UNICODE':
                self.xml_utf8 = str1.decode(xmlcode).encode('utf_8')
            else:
                return    
        else:
            self.xml_utf8 = xmlstr
        self.tree = ET.fromstring(self.xml_utf8)
        
        return
        
    def parse_xml(self, repeattag, taglist, batchid, fun=prt_vlist):
        '''
        '''
        reclist=[]
        vlist= []
        reccount = 0
        for element in self.uptag.iterfind(repeattag):
            del vlist[:]
            for tag in taglist:
                vlist.append(element.find(tag).text)
            vlist.append(batchid)
            reclist.append(vlist[:])    # shallow copy
            reccount = reccount + 1
            if ( len(reclist) > 1000 ):
                fun(reclist)
                del reclist[:]        
        fun(reclist)
                
        return reccount

    def generate_xml(self, root, repeat, taglist, vlist):

        roottag = self.tree.find('.//' + root)        
        repeattag = ET.SubElement(roottag, repeat)
        for i in range(0, len(taglist)):
            subtag = ET.SubElement(repeattag, taglist[i])
            subtag.text = vlist[i]
        
        #ET.ElementTree.write('d:\\result.xml', 'utf-8')
        
        return ET.ElementTree(self.tree)

    def set_uptag(self, uptag, repeat):
        
        self.uptag = self.tree.find('.//' + uptag)
        self.repeat = repeat
        
        return
    
    def append_element(self, taglist, vlist):

        for i in range(0, len(vlist)):
            repeattag = ET.SubElement(self.uptag, self.repeat)
            for j in range(0, len(taglist)):
                #print i, ')' , taglist[j], ':' , vlist[i][j]
                subtag = ET.SubElement(repeattag, taglist[j])
                if vlist[i][j] == None:
                    subtag.text = '0'
                else:
                    subtag.text = vlist[i][j]
                    subtag.text = subtag.text.rstrip()
        
        return ET.ElementTree(self.tree)

    def set_element_text(self, tagname, value):
        element = self.tree.find('.//' + tagname)
        element.text = value
        return
    
    def get_element_text(self, tagname):
        element = self.tree.find('.//' + tagname)
        return element.text

    def get_element_len(self, tagname):
        element = self.tree.find('.//' + tagname)
        return len(element)
    
    def set_element_attrib(self, tagname, key, value):
        element = self.tree.find('.//' + tagname)
        element.set(key, value)
        return

    def get_element_attrib(self, tagname, keys):
        element = self.tree.find('.//' + tagname)
        vlist = []
        for key in keys:
            vlist.append(element.get(key))
        return vlist
    
    def get_xml_tree(self):
        return ET.ElementTree(self.tree)

'''    
str1 = open('d:\\temp\\FCS12_SAICF_20140120_16180_EE9B12228161E44D0E3316EFB3022200.XML').read()
xml = ETUtil(xmlstr=str1, xmlcode='GBK')
reccount = xml.get_element_len("BODY")
print reccount
'''
'''
#str1 = open('d:\\temp\\FCS10_SAICF_20120320_132110_718A78CAD2861F1F30B3B73E1D542660.CTL').read()
#xml = ETUtil(xmlstr=str1, xmlcode='GBK')
#xml.parse_xml('BOXBIND', ('BOXID','DEALERID','STATUS','TIME'))
str1 = open('d:\\temp\\FCS09_TEMPLATE.XML').read()
xml = ETUtil(xmlstr=str1, xmlcode='GBK')
xml.generate_xml('BODY//BOXBINDS','BOXBIND', ('BOXID','DEALERID','STATUS','TIME'), ('01B9','SQ1234', '0', '2014-01-13 15:19:00'))
tree=xml.generate_xml('BODY//BOXBINDS','BOXBIND', ('BOXID','DEALERID','STATUS','TIME'), ('02B9','SQ2234', '1', '2014-02-13 15:19:00'))
xml.set_element_text('HEAD//RECORD', '2')
tree.write('d:\\result.xml', 'GBK')
'''