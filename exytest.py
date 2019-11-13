import unittest

# --------------------------------------
def ex(ini,fin):

    for x in range(ini,fin):
        if(x%3==0 and x%5==0): res="Linianos"
        else:
            if(x%3==0): res="Linio"
            else:
                if(x%5==0): res="IT"
                else: res=x
        print(res)
    return res


ini=1
fin=101


# --------------------------------------

class Pruebas(unittest.TestCase):

    def test_md3(self):
        self.assertEqual(ex(3,4),"Linio")

    def test_md5(self):
        self.assertEqual(ex(5,6),"IT")

    def test_mboth(self):
        self.assertEqual(ex(15,16),"Linianos")

    def test_mnone(self):
        a=1
        self.assertEqual(ex(a,2),a)

    def test_ret(self):
        self.assertIsNotNone(ex(ini,fin))

ex(1,101)
probar=raw_input(str("Correr Units Test? [Y/n]"))

if(probar=='Y' or probar=='y' or probar==""): unittest.main()
else:print("Adios")



# if __name__=='__main__':
    # unittest.main()
