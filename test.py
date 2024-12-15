import unittest
from regex import EmailManager

class emailmtest(unittest.Testcase):
    def testaddemail(self):
        if os.path.exists("testemaillibrary.txt")
            os.remove("testemaillibrary.remove")
    def testinvalidemail(self):
        res=self.manager.addemail("invalidemail")
        self.assertEqual(res, "'invalidemail'")
        self.assertNotin("invalid email",self.manager.emaillib)     