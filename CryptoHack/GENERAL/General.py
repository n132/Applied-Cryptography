from Crypto.PublicKey import RSA


def readPrivacyKeyfromPem():
    key = open("./privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem").read()
    res = RSA.importKey(key)
    print(res.d)
def readNfromDer():
    key = open("./2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der",'rb').read()
    res = RSA.importKey(key)
    print(res.n)
def readNfromSSHPub():
    key = open("./bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub").read()
    res = RSA.importKey(key)
    print(res.n)
def readHintfronmCertPub():
    # https://www.nmmapper.com/sys/tools/subdomainfinder/
    return True
    
if __name__ == "__main__":
    readNfromSSHPub()